# hermoso (Go)

The typed Go client for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and
schedule posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

```bash
go get github.com/hermoso-ai/hermoso-sdks/go
```

Go 1.24+. Releases are the `go/v*` tags of this repository; there is no other registry. Create an API key at
[app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab, under **Terminal & API keys**, and set it as
`HERMOSO_API_KEY`. New accounts start free with no card.

## Quickstart: make an image ad, wait for it, schedule it

```go
client, _ := hermoso.NewHermosoClient("") // reads HERMOSO_API_KEY
started, _ := client.RunTool(ctx, "generate_image", map[string]any{
	"prompt": `Summer ad for our cold brew, headline "Cold. Brewed. Yours."`, "job": "static_ad", "aspectRatio": "4:5",
}, &hermoso.RunToolOptions{Wait: hermoso.Ptr(0)})
job, _ := client.WaitForJob(ctx, *started.Job.JobId, nil)
when := time.Date(2026, 12, 1, 15, 0, 0, 0, time.UTC)
post, _ := client.CreatePostWithResponse(ctx, &hermoso.CreatePostParams{IdempotencyKey: hermoso.Ptr(uuid.NewString())}, hermoso.PostCreate{
	Channels: []string{"instagram", "facebook"}, Caption: hermoso.Ptr("Cold. Brewed. Yours."),
	Media: &[]hermoso.PostCreate_Media_Item{hermoso.MediaURL(*job.Url)}, ScheduledAt: &when,
})
fmt.Println(*post.JSON200.Id, *post.JSON200.Status)
```

(Errors are elided above; check each one.) `RunTool` reaches every Hermoso tool (`render_ad` for video ads,
`plan_ad`, competitor research, the ad platforms); `GetToolWithResponse` describes each tool's arguments. Rendering
costs credits; polling a job and publishing are free. Omit `ScheduledAt` to publish now.

## The helpers

| Helper | What it does |
|---|---|
| `NewHermosoClient(apiKey, opts...)` | A client with your key. `WithBrand(id)` acts on one brand of an account that holds several; `WithBaseURL`, `WithHTTPClient` as usual. |
| `client.ListAllPosts(ctx, params)` | A Go 1.23 iterator over every item, following `next_cursor` (also `ListAllJobs`, `ListAllTools`, `ListAllConversionEvents`; `Paginate` for any list). |
| `client.WaitForJob(ctx, id, opts)` | Polls a render until it is `done` or `error`. |
| `client.RunTool(ctx, name, args, opts)` | Calls any tool; `Result` when it finished, `Job` when it queued a render. |

Every `/v1` operation is a method on `*ClientWithResponses` named after its operationId (`GetCreditsWithResponse`,
`ListChannelsWithResponse`, `GetBestTimeWithResponse`, …), with the typed body on `JSON200` and the API's error on
`JSON400`/`JSON401`/…. The helpers return `*hermoso.APIError` carrying `error.code` and `message`.

Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/) · OpenAPI:
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json). MIT licensed. Generated with
[oapi-codegen](https://github.com/oapi-codegen/oapi-codegen); `hermoso.gen.go` is regenerated, never edited by hand.
