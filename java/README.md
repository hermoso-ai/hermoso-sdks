# hermoso-sdk (Java)

The typed Java client for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and
schedule posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

Not on Maven Central yet. Install from source, then depend on `ai.hermoso:hermoso-sdk`:

```bash
git clone https://github.com/hermoso-ai/hermoso-sdks && cd hermoso-sdks/java && mvn -q install -DskipTests
```

Java 11+. Create an API key at [app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab, under
**Terminal & API keys**, and set it as `HERMOSO_API_KEY`. New accounts start free with no card.

## Quickstart: make an image ad, wait for it, schedule it

```java
ApiClient client = Hermoso.client(); // reads HERMOSO_API_KEY
Hermoso.ToolCallResult started = Hermoso.runTool(client, "generate_image", Map.of(
    "prompt", "Summer ad for our cold brew, headline \"Cold. Brewed. Yours.\"", "job", "static_ad", "aspectRatio", "4:5"),
    Hermoso.runOptions().wait(0));
Job job = Hermoso.waitForJob(client, started.job().getJobId());
Post post = new PostsApi(client).createPost(new PostCreate()
    .channels(List.of("instagram", "facebook")).caption("Cold. Brewed. Yours.")
    .media(List.of(new PostCreateMediaInner(job.getUrl())))
    .scheduledAt(OffsetDateTime.parse("2026-12-01T15:00:00Z")), UUID.randomUUID().toString(), null);
System.out.println(post.getId() + " " + post.getStatus());
```

`runTool` reaches every Hermoso tool (`render_ad` for video ads, `plan_ad`, competitor research, the ad platforms);
`new ToolsApi(client).getTool(name, null)` describes each tool's arguments. Rendering costs credits; polling a job and
publishing are free. Omit `scheduledAt` to publish now.

## The helpers

| Helper | What it does |
|---|---|
| `Hermoso.client(Hermoso.options().apiKey(…).brand(…))` | An `ApiClient` with your key; `brand` acts on one brand of an account that holds several. |
| `Hermoso.paginate(Post.class, cursor -> …)` | An `Iterable` over every item of a list, following `next_cursor`. |
| `Hermoso.waitForJob(client, id)` | Polls a render until it is `done` or `error`. |
| `Hermoso.runTool(client, name, args, options)` | Calls any tool; `result()` when it finished, `job()` when it queued a render. |

Every `/v1` operation is a method on a generated API class (`CreditsApi`, `PostsApi`, `AnalyticsApi`, …) in
`ai.hermoso.sdk.api`, with typed models in `ai.hermoso.sdk.model`. Each operation also takes a request builder
(`PostsApi.APIListPostsRequest.newBuilder().status("published").build()`), which keeps compiling when the API adds an
optional parameter. Generated operations throw `ApiException`; the helpers throw `HermosoException` with the API's
`error.code`.

Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/) · OpenAPI:
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json). MIT licensed. Generated with
[OpenAPI Generator](https://openapi-generator.tech) (`native` library: `java.net.http` and Jackson); `src/` is
regenerated, never edited by hand.
