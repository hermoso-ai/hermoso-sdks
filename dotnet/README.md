# Hermoso.Sdk (.NET)

The typed .NET client for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and
schedule posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

```bash
dotnet add package Hermoso.Sdk
```

.NET 8+. Create an API key at [app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab, under
**Terminal & API keys**, and set it as `HERMOSO_API_KEY`. New accounts start free with no card.

## Quickstart: make an image ad, wait for it, schedule it

```csharp
using Hermoso.Sdk;
using Hermoso.Sdk.Generated.Models;

var hermoso = HermosoClient.Create(); // reads HERMOSO_API_KEY
var started = await hermoso.RunToolAsync("generate_image", new() {
    ["prompt"] = "Summer ad for our cold brew, headline \"Cold. Brewed. Yours.\"", ["job"] = "static_ad", ["aspectRatio"] = "4:5" }, wait: 0);
var job = await hermoso.WaitForJobAsync(started.Job!.JobId!);
var post = await hermoso.Api.V1.Posts.PostAsync(new PostCreate {
    Channels = ["instagram", "facebook"], Caption = "Cold. Brewed. Yours.",
    Media = [job.Url!], ScheduledAt = DateTimeOffset.Parse("2026-12-01T15:00:00Z"),
}, c => c.Headers.Add("Idempotency-Key", Guid.NewGuid().ToString()));
Console.WriteLine($"{post!.Id} {post.Status}");
```

`RunToolAsync` reaches every Hermoso tool (`render_ad` for video ads, `plan_ad`, competitor research, the ad
platforms); `hermoso.Api.V1.Tools[name].GetAsync()` describes each tool's arguments. Rendering costs credits; polling a
job and publishing are free. Omit `ScheduledAt` to publish now.

## The helpers

| Helper | What it does |
|---|---|
| `HermosoClient.Create(apiKey, brand, baseUrl)` | A client with your key; `brand` acts on one brand of an account that holds several. |
| `hermoso.Api` | The generated, fluent client: `Api.V1.Credits.GetAsync()`, `Api.V1.Jobs[id].GetAsync()`, `Api.V1.Analytics.BestTime.GetAsync(…)`. |
| `hermoso.PaginateAsync<PostList, Post>(cursor => …)` | An `IAsyncEnumerable` over every item of a list, following `next_cursor`. |
| `hermoso.WaitForJobAsync(id)` | Polls a render until it is `done` or `error`. |
| `hermoso.RunToolAsync(name, args, wait: 0)` | Calls any tool; `Result` when it finished, `Job` when it queued a render. |

Generated operations throw the API's typed `Error` (an `ApiException`); the helpers throw `HermosoException` with
`Code` and `Status`. Query parameters are properties (`c.QueryParameters.Status = "published"`), so a parameter the API
adds later never breaks a call site.

Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/) · OpenAPI:
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json). MIT licensed. Generated with
[Kiota](https://learn.microsoft.com/openapi/kiota/); `Generated/` is regenerated, never edited by hand.
