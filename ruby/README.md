# hermoso (Ruby)

The typed Ruby client for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and
schedule posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

```bash
gem install hermoso
```

or `gem 'hermoso'` in your Gemfile.

Ruby 3.1+. Create an API key at [app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab, under
**Terminal & API keys**, and set it as `HERMOSO_API_KEY`. New accounts start free with no card.

## Quickstart: make an image ad, wait for it, schedule it

```ruby
require 'hermoso'
require 'securerandom'

client = Hermoso.client # reads HERMOSO_API_KEY
started = Hermoso.run_tool('generate_image', { prompt: 'Summer ad for our cold brew, headline "Cold. Brewed. Yours."',
                                               job: 'static_ad', aspectRatio: '4:5' }, client: client, wait: 0)
job = Hermoso.wait_for_job(started.job_id, client: client)
post = Hermoso::PostsApi.new(client).create_post(
  Hermoso::PostCreate.build_from_hash(channels: %w[instagram facebook], caption: 'Cold. Brewed. Yours.',
                                      media: [job.url], scheduled_at: '2026-12-01T15:00:00Z'),
  idempotency_key: SecureRandom.uuid
)
puts post.id, post.status
```

`run_tool` reaches every Hermoso tool (`render_ad` for video ads, `plan_ad`, competitor research, the ad platforms);
`Hermoso::ToolsApi.new(client).get_tool(name)` describes each tool's arguments. Rendering costs credits; polling a job
and publishing are free. Omit `scheduled_at` to publish now.

## The helpers

| Helper | What it does |
|---|---|
| `Hermoso.client(api_key:, brand:, base_url:)` | An `ApiClient` with your key; `brand:` acts on one brand of an account that holds several. |
| `Hermoso.paginate(api, :list_posts, status: 'published')` | An `Enumerator` over every item of a list, following `next_cursor`. |
| `Hermoso.wait_for_job(id, client:)` | Polls a render until it is `done` or `error`. |
| `Hermoso.run_tool(name, args, client:, wait:)` | Calls any tool; returns a `ToolResult`, or a `ToolJob` when it queued a render. |

Every `/v1` operation is a method on a generated API class (`Hermoso::CreditsApi`, `PostsApi`, `AnalyticsApi`, …),
with typed models in `Hermoso::`. Generated operations raise `Hermoso::ApiError`; the helpers raise
`Hermoso::HermosoError` with the API's `error.code` and `message`.

Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/) · OpenAPI:
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json). MIT licensed. Generated with
[OpenAPI Generator](https://openapi-generator.tech); `lib/` is regenerated, never edited by hand.
