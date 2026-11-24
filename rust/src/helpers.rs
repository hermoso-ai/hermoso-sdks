//! The hand-written layer over the generated client (sdks/rust/overlay; tools/sdk-generate.mjs copies it into src/).
use std::fmt;
use std::future::Future;
use std::sync::Arc;
use std::time::{Duration, Instant};

use futures_util::stream::{self, Stream};
use reqwest::header::{HeaderMap, HeaderValue};

use crate::apis::configuration::Configuration;
use crate::apis::jobs_api::GetJobParams;
use crate::apis::{Api, ApiClient};
use crate::models;

/// The Hermoso API.
pub const DEFAULT_BASE_URL: &str = "https://app.hermoso.ai";

/// What the helpers return when something goes wrong.
#[derive(Debug)]
pub enum HermosoError {
    /// No API key was passed and HERMOSO_API_KEY is not set.
    NoApiKey,
    /// An error answer from the API: `code` and `message` are its `error.code` and `error.message`.
    Api { status: u16, code: Option<String>, message: Option<String>, body: String },
    /// The request never got an answer.
    Http(reqwest::Error),
    /// The answer was not the JSON the API documents.
    Json(serde_json::Error),
    /// A job was still running when the wait gave up; it keeps running.
    Timeout(String),
    /// Any other error from a generated operation.
    Other(String),
}

impl fmt::Display for HermosoError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            HermosoError::NoApiKey => write!(f, "No Hermoso API key: pass one or set HERMOSO_API_KEY. Create one at https://app.hermoso.ai on the \"API, MCP & CLI\" tab, under \"Terminal & API keys\"."),
            HermosoError::Api { status, message, .. } => write!(f, "{} (HTTP {})", message.as_deref().unwrap_or("Hermoso API error"), status),
            HermosoError::Http(e) => write!(f, "{e}"),
            HermosoError::Json(e) => write!(f, "{e}"),
            HermosoError::Timeout(m) | HermosoError::Other(m) => write!(f, "{m}"),
        }
    }
}

impl std::error::Error for HermosoError {}

impl HermosoError {
    fn api(status: u16, body: String) -> Self {
        let parsed: Option<serde_json::Value> = serde_json::from_str(&body).ok();
        let field = |name: &str| parsed.as_ref().and_then(|v| v["error"][name].as_str()).map(str::to_owned);
        HermosoError::Api { status, code: field("code"), message: field("message"), body }
    }
}

impl<T: fmt::Debug> From<crate::apis::Error<T>> for HermosoError {
    fn from(e: crate::apis::Error<T>) -> Self {
        match e {
            crate::apis::Error::ResponseError(r) => HermosoError::api(r.status.as_u16(), r.content),
            crate::apis::Error::Reqwest(e) => HermosoError::Http(e),
            crate::apis::Error::Serde(e) => HermosoError::Json(e),
            other => HermosoError::Other(other.to_string()),
        }
    }
}

/// Options for [`client_with`]. `..Default::default()` the ones you do not set.
#[derive(Clone, Debug, Default)]
pub struct ClientOptions {
    /// A Hermoso API key (`hmk_…`). Defaults to the HERMOSO_API_KEY environment variable.
    pub api_key: Option<String>,
    /// Act on this brand (an `id` from list_brands) instead of the one the key is pinned to. Sent as X-Hermoso-User.
    pub brand: Option<String>,
    /// Defaults to https://app.hermoso.ai.
    pub base_url: Option<String>,
    /// Per-request timeout; defaults to 90 seconds.
    pub timeout: Option<Duration>,
}

/// The Hermoso client: `api` is the generated client for every /v1 operation (bring the [`Api`] trait into scope),
/// `config` is what each generated operation sends with.
#[derive(Clone)]
pub struct Hermoso {
    pub api: Arc<ApiClient>,
    pub config: Arc<Configuration>,
}

/// A client authenticated with HERMOSO_API_KEY.
pub fn client() -> Result<Hermoso, HermosoError> {
    client_with(ClientOptions::default())
}

/// A client authenticated with your API key.
pub fn client_with(options: ClientOptions) -> Result<Hermoso, HermosoError> {
    let key = options.api_key.or_else(|| std::env::var("HERMOSO_API_KEY").ok()).filter(|k| !k.is_empty()).ok_or(HermosoError::NoApiKey)?;
    let mut headers = HeaderMap::new();
    if let Some(brand) = options.brand.filter(|b| !b.is_empty()) {
        headers.insert("X-Hermoso-User", HeaderValue::from_str(&brand).map_err(|e| HermosoError::Other(e.to_string()))?);
    }
    let http = reqwest::Client::builder()
        .default_headers(headers)
        .timeout(options.timeout.unwrap_or(Duration::from_secs(90)))
        .build()
        .map_err(HermosoError::Http)?;
    let config = Arc::new(Configuration {
        base_path: options.base_url.unwrap_or_else(|| DEFAULT_BASE_URL.to_owned()).trim_end_matches('/').to_owned(),
        user_agent: Some(format!("hermoso-rust/{}", crate::spec::VERSION)),
        client: http,
        bearer_access_token: Some(key),
        ..Configuration::default()
    });
    Ok(Hermoso { api: Arc::new(ApiClient::new(config.clone())), config })
}

/// One page of a cursor-paginated list. Implemented for every list the API pages.
pub trait Page {
    type Item;
    /// The items, the next cursor, and `has_more` when the list reports it.
    fn into_parts(self) -> (Vec<Self::Item>, Option<String>, Option<bool>);
}

macro_rules! page {
    ($list:ty, $item:ty, has_more) => {
        impl Page for $list {
            type Item = $item;
            fn into_parts(self) -> (Vec<$item>, Option<String>, Option<bool>) { (self.data.unwrap_or_default(), self.next_cursor, self.has_more) }
        }
    };
    ($list:ty, $item:ty) => {
        impl Page for $list {
            type Item = $item;
            fn into_parts(self) -> (Vec<$item>, Option<String>, Option<bool>) { (self.data.unwrap_or_default(), self.next_cursor, None) }
        }
    };
}
page!(models::PostList, models::Post, has_more);
page!(models::JobList, models::Job, has_more);
page!(models::ToolList, models::Tool, has_more);
page!(models::ConversionEventList, std::collections::HashMap<String, serde_json::Value>);

/// Every item of a cursor-paginated list, as a stream: `fetch` gets the previous page's cursor (`None` first) and
/// passes it as the list's `starting_after` (or `cursor`, for list_conversion_events).
///
/// ```no_run
/// # use futures_util::StreamExt; use hermoso::Api;
/// # async fn run(client: hermoso::Hermoso) -> Result<(), hermoso::HermosoError> {
/// use hermoso::apis::posts_api::ListPostsParams;
/// let posts = hermoso::paginate(|cursor| {
///     let api = client.api.clone();
///     async move { api.posts_api().list_posts(ListPostsParams::builder().status("published".into()).maybe_starting_after(cursor).build()).await }
/// });
/// futures_util::pin_mut!(posts);
/// while let Some(post) = posts.next().await { println!("{:?}", post?.id); }
/// # Ok(()) }
/// ```
pub fn paginate<P, E, F, Fut>(fetch: F) -> impl Stream<Item = Result<P::Item, HermosoError>>
where
    P: Page,
    HermosoError: From<E>,
    F: FnMut(Option<String>) -> Fut,
    Fut: Future<Output = Result<P, E>>,
{
    struct State<F, I> { fetch: F, cursor: Option<String>, buffer: std::vec::IntoIter<I>, done: bool }
    let start = State { fetch, cursor: None, buffer: Vec::new().into_iter(), done: false };
    stream::unfold(start, |mut st| async move {
        loop {
            if let Some(item) = st.buffer.next() {
                return Some((Ok(item), st));
            }
            if st.done {
                return None;
            }
            match (st.fetch)(st.cursor.take()).await {
                Err(e) => { st.done = true; return Some((Err(HermosoError::from(e)), st)); }
                Ok(page) => {
                    let (items, next, has_more) = page.into_parts();
                    st.done = next.as_deref().map_or(true, str::is_empty) || has_more == Some(false);
                    st.cursor = next;
                    st.buffer = items.into_iter();
                }
            }
        }
    })
}

/// Options for [`Hermoso::wait_for_job`]: defaults poll every 5 seconds for up to 20 minutes.
#[derive(Clone, Debug)]
pub struct WaitOptions {
    pub interval: Duration,
    pub timeout: Duration,
}

impl Default for WaitOptions {
    fn default() -> Self { WaitOptions { interval: Duration::from_secs(5), timeout: Duration::from_secs(20 * 60) } }
}

/// Options for [`Hermoso::run_tool`]. `wait: Some(0)` answers at once with a job handle; `None` leaves the server
/// default (a render is held up to 45 seconds).
#[derive(Clone, Debug, Default)]
pub struct RunToolOptions {
    pub wait: Option<u32>,
    pub idempotency_key: Option<String>,
}

/// What a tool call answered.
#[derive(Clone, Debug)]
pub enum ToolOutcome {
    /// The tool finished.
    Result(models::ToolResult),
    /// The tool queued a render: pass `job_id` to [`Hermoso::wait_for_job`].
    Job(models::ToolJob),
}

impl Hermoso {
    /// Polls a job (a render, a stitch, an upscale…) until it is `done` or `error` and returns it; the file is
    /// `job.url`. Polling is free; calling the tool again would start (and bill) a second render.
    pub async fn wait_for_job(&self, id: &str, options: WaitOptions) -> Result<models::Job, HermosoError> {
        let deadline = Instant::now() + options.timeout;
        loop {
            let job = self.api.jobs_api().get_job(GetJobParams { id: id.to_owned(), x_hermoso_user: None }).await?;
            let status = job.status.clone().unwrap_or_default();
            if status == "done" || status == "error" {
                return Ok(job);
            }
            if Instant::now() > deadline {
                return Err(HermosoError::Timeout(format!("Job {id} is still {status}; it keeps running, call wait_for_job again.")));
            }
            tokio::time::sleep(options.interval).await;
        }
    }

    /// Runs any Hermoso tool through `POST /v1/tools/{name}` with its arguments. `tools_api().get_tool` describes each
    /// tool's arguments.
    ///
    /// ```no_run
    /// # async fn run(client: hermoso::Hermoso) -> Result<(), hermoso::HermosoError> {
    /// let plan = client.run_tool("plan_ad", serde_json::json!({ "product": "our cold brew, summer offer" }), Default::default()).await?;
    /// # Ok(()) }
    /// ```
    pub async fn run_tool(&self, name: &str, args: serde_json::Value, options: RunToolOptions) -> Result<ToolOutcome, HermosoError> {
        let mut url = url::Url::parse(&format!("{}/v1/tools/", self.config.base_path)).map_err(|e| HermosoError::Other(e.to_string()))?;
        url.path_segments_mut().map_err(|_| HermosoError::Other("base URL cannot carry a path".into()))?.pop_if_empty().push(name);
        let mut req = self.config.client.post(url).json(&if args.is_null() { serde_json::json!({}) } else { args });
        if let Some(w) = options.wait {
            req = req.query(&[("wait", w.to_string())]);
        }
        if let Some(k) = options.idempotency_key {
            req = req.header("Idempotency-Key", k);
        }
        if let Some(token) = &self.config.bearer_access_token {
            req = req.bearer_auth(token);
        }
        if let Some(ua) = &self.config.user_agent {
            req = req.header(reqwest::header::USER_AGENT, ua);
        }
        let res = req.send().await.map_err(HermosoError::Http)?;
        let status = res.status().as_u16();
        let body = res.text().await.map_err(HermosoError::Http)?;
        match status {
            202 => Ok(ToolOutcome::Job(serde_json::from_str(&body).map_err(HermosoError::Json)?)),
            200 => Ok(ToolOutcome::Result(serde_json::from_str(&body).map_err(HermosoError::Json)?)),
            _ => Err(HermosoError::api(status, body)),
        }
    }
}
