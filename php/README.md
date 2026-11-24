# hermoso/sdk (PHP)

The typed PHP client for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and
schedule posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

```bash
composer require hermoso/sdk
```

PHP 8.1+ with `curl`, `json` and `mbstring`. Create an API key at [app.hermoso.ai](https://app.hermoso.ai) on the
**API, MCP & CLI** tab, under **Terminal & API keys**, and set it as `HERMOSO_API_KEY`. New accounts start free.

## Quickstart: make an image ad, wait for it, schedule it

```php
use Hermoso\HermosoClient;
use Hermoso\Api\PostsApi;
use Hermoso\Model\PostCreate;

$hermoso = HermosoClient::create(); // reads HERMOSO_API_KEY
$started = $hermoso->runTool('generate_image', ['prompt' => 'Summer ad for our cold brew, headline "Cold. Brewed. Yours."',
    'job' => 'static_ad', 'aspectRatio' => '4:5'], wait: 0);
$job = $hermoso->waitForJob($started->getJobId());
$post = $hermoso->api(PostsApi::class)->createPost(new PostCreate([
    'channels' => ['instagram', 'facebook'], 'caption' => 'Cold. Brewed. Yours.',
    'media' => [$job->getUrl()], 'scheduled_at' => new DateTime('2026-12-01T15:00:00Z'),
]), idempotency_key: bin2hex(random_bytes(16)));
echo $post->getId(), ' ', $post->getStatus(), PHP_EOL;
```

`runTool` reaches every Hermoso tool (`render_ad` for video ads, `plan_ad`, competitor research, the ad platforms);
`ToolsApi::getTool` describes each tool's arguments. Rendering costs credits; polling a job and publishing are free.
Omit `scheduled_at` to publish now.

## The helpers

| Helper | What it does |
|---|---|
| `HermosoClient::create(apiKey:, brand:, baseUrl:)` | A client with your key; `brand` acts on one brand of an account that holds several. |
| `$hermoso->api(Api\PostsApi::class)` | Any generated API class, sharing the key and connection. |
| `$hermoso->paginate([$posts, 'listPosts'], ['status' => 'published'])` | A generator over every item of a list, following `next_cursor`. |
| `$hermoso->waitForJob($id)` | Polls a render until it is `done` or `error`. |
| `$hermoso->runTool($name, $args, wait: 0)` | Calls any tool; a `ToolResult`, or a `ToolJob` when it queued a render. |

Every `/v1` operation is a method on a generated API class in `Hermoso\Api`, with typed models in `Hermoso\Model`.
Pass optional parameters by name (`listPosts(status: 'published')`) so a parameter the API adds later never shifts your
call. Generated operations throw `Hermoso\ApiException`; the helpers throw `Hermoso\HermosoException` with the API's
`error.code`.

Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/) · OpenAPI:
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json). MIT licensed. Generated with
[OpenAPI Generator](https://openapi-generator.tech) (Guzzle 7); `lib/` is regenerated, never edited by hand.
