# @hermoso/sdk

The typed TypeScript client for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads,
publish and schedule posts to your own channels, read your analytics, and call any of Hermoso's tools from your own
backend.

```bash
npm install @hermoso/sdk
```

Node 18+ (it uses the built-in `fetch`), server-side only: an API key carries full account authority, so never ship
it to a browser. Create one at [app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab, under
**Terminal & API keys**, and set it as `HERMOSO_API_KEY`. New accounts start free with no card.

The client is generated from the API's OpenAPI document, so every `/v1` operation is a typed function and every
request and response a typed model. Each call returns `{ data, error, response }`.

## Generate an ad

```ts
import { createHermosoClient, runTool, waitForJob } from '@hermoso/sdk';

const hermoso = createHermosoClient(); // reads HERMOSO_API_KEY

const started = await runTool('generate_image', {
  prompt: 'Summer launch ad for our cold brew: the can on a sunlit cafe table, headline "Cold. Brewed. Yours."',
  job: 'static_ad',
  aspectRatio: '4:5',
}, { client: hermoso, wait: 0 });

const job = await waitForJob((started as { job_id: string }).job_id, { client: hermoso });
console.log(job.url); // the finished image, on your saved brand
```

`runTool` reaches every Hermoso tool, the same set an agent gets over MCP: `render_ad` for video ads, `plan_ad`,
`clone_video`, competitor research and the ad platforms. `getTool({ path: { name } })` describes each tool's
arguments. Rendering costs credits; polling a job is free.

## Schedule a post

```ts
import { createPost } from '@hermoso/sdk';

const { data: post, error } = await createPost({
  client: hermoso,
  body: {
    channels: ['instagram', 'facebook'],
    caption: 'Cold. Brewed. Yours.',
    media: [job.url!],
    scheduled_at: '2026-12-01T15:00:00Z',
  },
  headers: { 'Idempotency-Key': crypto.randomUUID() },
});
if (error) throw new Error(JSON.stringify(error));
console.log(post.id, post.status);
```

`listChannels` lists every channel and whether this brand has it connected. Omit `scheduled_at` to publish now.
Publishing is free.

## Read analytics

```ts
import { getBestTime, listPosts, paginate } from '@hermoso/sdk';

const { data: best } = await getBestTime({ client: hermoso, query: { channel: 'instagram', timezone: 'America/New_York' } });
console.log(best?.slots?.slice(0, 5));

for await (const post of paginate(listPosts, { client: hermoso, query: { status: 'published' } })) {
  console.log(post.id, post.scheduled_at);
}
```

`paginate` follows the cursor on any list operation until the last page.

## Also

- `createHermosoClient({ apiKey, brand: '<id from listBrands>' })` acts on one brand of an account that holds several.
- `waitForJob(id, { client })` polls a render until it is `done` or `error`.
- Pass `throwOnError: true` to any operation to get the data directly and a thrown error body otherwise; the helpers
  throw `HermosoError`.

Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/) · API reference:
[hermoso.ai/docs/api](https://hermoso.ai/docs/api/) · OpenAPI:
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json) · Python: [`hermoso` on PyPI](https://pypi.org/project/hermoso/)

MIT licensed. Generated with [@hey-api/openapi-ts](https://heyapi.dev).
