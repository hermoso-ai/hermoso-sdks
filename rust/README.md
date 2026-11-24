# hermoso (Rust)

The typed Rust client for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and
schedule posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

```bash
cargo add hermoso
cargo add tokio --features macros,rt-multi-thread
```

Rust 1.85+, async (reqwest + rustls; `default-features = false, features = ["native-tls", "bon"]` for the platform
TLS). Create an API key at [app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab, under **Terminal &
API keys**, and set it as `HERMOSO_API_KEY`. New accounts start free with no card.

## Quickstart: make an image ad, wait for it, schedule it

```rust
use hermoso::{Api, ToolOutcome, apis::posts_api::CreatePostParams, models::{PostCreate, PostCreateMediaInner}};

let client = hermoso::client()?; // reads HERMOSO_API_KEY
let prompt = r#"Summer ad for our cold brew, headline "Cold. Brewed. Yours.""#;
let started = client.run_tool("generate_image", serde_json::json!({ "prompt": prompt, "job": "static_ad", "aspectRatio": "4:5" }),
    hermoso::RunToolOptions { wait: Some(0), ..Default::default() }).await?;
let ToolOutcome::Job(handle) = started else { unreachable!("wait=0 answers with a job") };
let job = client.wait_for_job(handle.job_id.as_deref().unwrap(), Default::default()).await?;
let mut post = PostCreate::new(vec!["instagram".into(), "facebook".into()]);
post.caption = Some("Cold. Brewed. Yours.".into());
post.media = Some(vec![PostCreateMediaInner::String(job.url.unwrap())]);
post.scheduled_at = Some(chrono::DateTime::parse_from_rfc3339("2026-12-01T15:00:00Z")?);
let post = client.api.posts_api().create_post(CreatePostParams::builder().post_create(post).idempotency_key("cold-brew-launch-2026-12-01".into()).build()).await?;
```

`run_tool` reaches every Hermoso tool (`render_ad` for video ads, `plan_ad`, competitor research, the ad platforms);
`tools_api().get_tool` describes each tool's arguments. Rendering costs credits; polling a job and publishing are free.
Leave `scheduled_at` unset to publish now.

## The helpers

| Helper | What it does |
|---|---|
| `hermoso::client()` / `client_with(ClientOptions { brand, .. })` | A client with your key; `brand` acts on one brand of an account that holds several. |
| `client.api.posts_api()…` | The generated client for every `/v1` operation (bring `hermoso::Api` into scope). |
| `hermoso::paginate(\|cursor\| …)` | A `Stream` over every item of a list, following `next_cursor`. |
| `client.wait_for_job(id, WaitOptions)` | Polls a render until it is `done` or `error`. |
| `client.run_tool(name, args, RunToolOptions)` | Calls any tool; `ToolOutcome::Result` when it finished, `ToolOutcome::Job` when it queued a render. |

Every operation takes one parameter struct with a builder (`ListPostsParams::builder().status(…).build()`), so a
parameter the API adds later never breaks a call site. Helpers return `HermosoError`, whose `Api` variant carries the
API's `error.code` and `message`; generated errors convert into it with `?`.

Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/) · OpenAPI:
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json). MIT licensed. Generated with
[OpenAPI Generator](https://openapi-generator.tech); `src/apis` and `src/models` are regenerated, never edited by hand.
