use std::error;
use std::fmt;

#[derive(Debug, Clone)]
pub struct ResponseContent<T> {
    pub status: reqwest::StatusCode,
    pub content: String,
    pub entity: Option<T>,
}

#[derive(Debug)]
pub enum Error<T> {
    Reqwest(reqwest::Error),
    Serde(serde_json::Error),
    Io(std::io::Error),
    ResponseError(ResponseContent<T>),
}

impl <T> fmt::Display for Error<T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let (module, e) = match self {
            Error::Reqwest(e) => ("reqwest", e.to_string()),
            Error::Serde(e) => ("serde", e.to_string()),
            Error::Io(e) => ("IO", e.to_string()),
            Error::ResponseError(e) => ("response", format!("status code {}", e.status)),
        };
        write!(f, "error in {}: {}", module, e)
    }
}

impl <T: fmt::Debug> error::Error for Error<T> {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        Some(match self {
            Error::Reqwest(e) => e,
            Error::Serde(e) => e,
            Error::Io(e) => e,
            Error::ResponseError(_) => return None,
        })
    }
}

impl <T> From<reqwest::Error> for Error<T> {
    fn from(e: reqwest::Error) -> Self {
        Error::Reqwest(e)
    }
}

impl <T> From<serde_json::Error> for Error<T> {
    fn from(e: serde_json::Error) -> Self {
        Error::Serde(e)
    }
}

impl <T> From<std::io::Error> for Error<T> {
    fn from(e: std::io::Error) -> Self {
        Error::Io(e)
    }
}

pub fn urlencode<T: AsRef<str>>(s: T) -> String {
    ::url::form_urlencoded::byte_serialize(s.as_ref().as_bytes()).collect()
}

pub fn parse_deep_object(prefix: &str, value: &serde_json::Value) -> Vec<(String, String)> {
    if let serde_json::Value::Object(object) = value {
        let mut params = vec![];

        for (key, value) in object {
            match value {
                serde_json::Value::Object(_) => params.append(&mut parse_deep_object(
                    &format!("{}[{}]", prefix, key),
                    value,
                )),
                serde_json::Value::Array(array) => {
                    for (i, value) in array.iter().enumerate() {
                        params.append(&mut parse_deep_object(
                            &format!("{}[{}][{}]", prefix, key, i),
                            value,
                        ));
                    }
                },
                serde_json::Value::String(s) => params.push((format!("{}[{}]", prefix, key), s.clone())),
                _ => params.push((format!("{}[{}]", prefix, key), value.to_string())),
            }
        }

        return params;
    }

    unimplemented!("Only objects are supported with style=deepObject")
}

/// Internal use only
/// A content type supported by this client.
#[allow(dead_code)]
enum ContentType {
    Json,
    Text,
    Unsupported(String)
}

impl From<&str> for ContentType {
    fn from(content_type: &str) -> Self {
        if content_type.starts_with("application") && content_type.contains("json") {
            return Self::Json;
        } else if content_type.starts_with("text/plain") {
            return Self::Text;
        } else {
            return Self::Unsupported(content_type.to_string());
        }
    }
}

pub mod account_api;
pub mod analytics_api;
pub mod brands_api;
pub mod campaign_profit_api;
pub mod campaign_results_api;
pub mod channels_api;
pub mod clones_api;
pub mod connect_links_api;
pub mod connect_redirects_api;
pub mod connections_api;
pub mod credits_api;
pub mod edits_api;
pub mod events_api;
pub mod generations_api;
pub mod jobs_api;
pub mod library_api;
pub mod media_api;
pub mod models_api;
pub mod posts_api;
pub mod recasts_api;
pub mod signup_api;
pub mod tag_api;
pub mod tools_api;

pub mod configuration;

use std::sync::Arc;

pub trait Api {
    fn account_api(&self) -> &dyn account_api::AccountApi;
    fn analytics_api(&self) -> &dyn analytics_api::AnalyticsApi;
    fn brands_api(&self) -> &dyn brands_api::BrandsApi;
    fn campaign_profit_api(&self) -> &dyn campaign_profit_api::CampaignProfitApi;
    fn campaign_results_api(&self) -> &dyn campaign_results_api::CampaignResultsApi;
    fn channels_api(&self) -> &dyn channels_api::ChannelsApi;
    fn clones_api(&self) -> &dyn clones_api::ClonesApi;
    fn connect_links_api(&self) -> &dyn connect_links_api::ConnectLinksApi;
    fn connect_redirects_api(&self) -> &dyn connect_redirects_api::ConnectRedirectsApi;
    fn connections_api(&self) -> &dyn connections_api::ConnectionsApi;
    fn credits_api(&self) -> &dyn credits_api::CreditsApi;
    fn edits_api(&self) -> &dyn edits_api::EditsApi;
    fn events_api(&self) -> &dyn events_api::EventsApi;
    fn generations_api(&self) -> &dyn generations_api::GenerationsApi;
    fn jobs_api(&self) -> &dyn jobs_api::JobsApi;
    fn library_api(&self) -> &dyn library_api::LibraryApi;
    fn media_api(&self) -> &dyn media_api::MediaApi;
    fn models_api(&self) -> &dyn models_api::ModelsApi;
    fn posts_api(&self) -> &dyn posts_api::PostsApi;
    fn recasts_api(&self) -> &dyn recasts_api::RecastsApi;
    fn signup_api(&self) -> &dyn signup_api::SignupApi;
    fn tag_api(&self) -> &dyn tag_api::TagApi;
    fn tools_api(&self) -> &dyn tools_api::ToolsApi;
}

pub struct ApiClient {
    account_api: Box<dyn account_api::AccountApi>,
    analytics_api: Box<dyn analytics_api::AnalyticsApi>,
    brands_api: Box<dyn brands_api::BrandsApi>,
    campaign_profit_api: Box<dyn campaign_profit_api::CampaignProfitApi>,
    campaign_results_api: Box<dyn campaign_results_api::CampaignResultsApi>,
    channels_api: Box<dyn channels_api::ChannelsApi>,
    clones_api: Box<dyn clones_api::ClonesApi>,
    connect_links_api: Box<dyn connect_links_api::ConnectLinksApi>,
    connect_redirects_api: Box<dyn connect_redirects_api::ConnectRedirectsApi>,
    connections_api: Box<dyn connections_api::ConnectionsApi>,
    credits_api: Box<dyn credits_api::CreditsApi>,
    edits_api: Box<dyn edits_api::EditsApi>,
    events_api: Box<dyn events_api::EventsApi>,
    generations_api: Box<dyn generations_api::GenerationsApi>,
    jobs_api: Box<dyn jobs_api::JobsApi>,
    library_api: Box<dyn library_api::LibraryApi>,
    media_api: Box<dyn media_api::MediaApi>,
    models_api: Box<dyn models_api::ModelsApi>,
    posts_api: Box<dyn posts_api::PostsApi>,
    recasts_api: Box<dyn recasts_api::RecastsApi>,
    signup_api: Box<dyn signup_api::SignupApi>,
    tag_api: Box<dyn tag_api::TagApi>,
    tools_api: Box<dyn tools_api::ToolsApi>,
}

impl ApiClient {
    pub fn new(configuration: Arc<configuration::Configuration>) -> Self {
        Self {
            account_api: Box::new(account_api::AccountApiClient::new(configuration.clone())),
            analytics_api: Box::new(analytics_api::AnalyticsApiClient::new(configuration.clone())),
            brands_api: Box::new(brands_api::BrandsApiClient::new(configuration.clone())),
            campaign_profit_api: Box::new(campaign_profit_api::CampaignProfitApiClient::new(configuration.clone())),
            campaign_results_api: Box::new(campaign_results_api::CampaignResultsApiClient::new(configuration.clone())),
            channels_api: Box::new(channels_api::ChannelsApiClient::new(configuration.clone())),
            clones_api: Box::new(clones_api::ClonesApiClient::new(configuration.clone())),
            connect_links_api: Box::new(connect_links_api::ConnectLinksApiClient::new(configuration.clone())),
            connect_redirects_api: Box::new(connect_redirects_api::ConnectRedirectsApiClient::new(configuration.clone())),
            connections_api: Box::new(connections_api::ConnectionsApiClient::new(configuration.clone())),
            credits_api: Box::new(credits_api::CreditsApiClient::new(configuration.clone())),
            edits_api: Box::new(edits_api::EditsApiClient::new(configuration.clone())),
            events_api: Box::new(events_api::EventsApiClient::new(configuration.clone())),
            generations_api: Box::new(generations_api::GenerationsApiClient::new(configuration.clone())),
            jobs_api: Box::new(jobs_api::JobsApiClient::new(configuration.clone())),
            library_api: Box::new(library_api::LibraryApiClient::new(configuration.clone())),
            media_api: Box::new(media_api::MediaApiClient::new(configuration.clone())),
            models_api: Box::new(models_api::ModelsApiClient::new(configuration.clone())),
            posts_api: Box::new(posts_api::PostsApiClient::new(configuration.clone())),
            recasts_api: Box::new(recasts_api::RecastsApiClient::new(configuration.clone())),
            signup_api: Box::new(signup_api::SignupApiClient::new(configuration.clone())),
            tag_api: Box::new(tag_api::TagApiClient::new(configuration.clone())),
            tools_api: Box::new(tools_api::ToolsApiClient::new(configuration.clone())),
        }
    }
}

impl Api for ApiClient {
    fn account_api(&self) -> &dyn account_api::AccountApi {
        self.account_api.as_ref()
    }
    fn analytics_api(&self) -> &dyn analytics_api::AnalyticsApi {
        self.analytics_api.as_ref()
    }
    fn brands_api(&self) -> &dyn brands_api::BrandsApi {
        self.brands_api.as_ref()
    }
    fn campaign_profit_api(&self) -> &dyn campaign_profit_api::CampaignProfitApi {
        self.campaign_profit_api.as_ref()
    }
    fn campaign_results_api(&self) -> &dyn campaign_results_api::CampaignResultsApi {
        self.campaign_results_api.as_ref()
    }
    fn channels_api(&self) -> &dyn channels_api::ChannelsApi {
        self.channels_api.as_ref()
    }
    fn clones_api(&self) -> &dyn clones_api::ClonesApi {
        self.clones_api.as_ref()
    }
    fn connect_links_api(&self) -> &dyn connect_links_api::ConnectLinksApi {
        self.connect_links_api.as_ref()
    }
    fn connect_redirects_api(&self) -> &dyn connect_redirects_api::ConnectRedirectsApi {
        self.connect_redirects_api.as_ref()
    }
    fn connections_api(&self) -> &dyn connections_api::ConnectionsApi {
        self.connections_api.as_ref()
    }
    fn credits_api(&self) -> &dyn credits_api::CreditsApi {
        self.credits_api.as_ref()
    }
    fn edits_api(&self) -> &dyn edits_api::EditsApi {
        self.edits_api.as_ref()
    }
    fn events_api(&self) -> &dyn events_api::EventsApi {
        self.events_api.as_ref()
    }
    fn generations_api(&self) -> &dyn generations_api::GenerationsApi {
        self.generations_api.as_ref()
    }
    fn jobs_api(&self) -> &dyn jobs_api::JobsApi {
        self.jobs_api.as_ref()
    }
    fn library_api(&self) -> &dyn library_api::LibraryApi {
        self.library_api.as_ref()
    }
    fn media_api(&self) -> &dyn media_api::MediaApi {
        self.media_api.as_ref()
    }
    fn models_api(&self) -> &dyn models_api::ModelsApi {
        self.models_api.as_ref()
    }
    fn posts_api(&self) -> &dyn posts_api::PostsApi {
        self.posts_api.as_ref()
    }
    fn recasts_api(&self) -> &dyn recasts_api::RecastsApi {
        self.recasts_api.as_ref()
    }
    fn signup_api(&self) -> &dyn signup_api::SignupApi {
        self.signup_api.as_ref()
    }
    fn tag_api(&self) -> &dyn tag_api::TagApi {
        self.tag_api.as_ref()
    }
    fn tools_api(&self) -> &dyn tools_api::ToolsApi {
        self.tools_api.as_ref()
    }
}


