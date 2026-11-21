# hermoso

The typed Python client for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and
schedule posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

```bash
pip install hermoso
```

Python 3.11+. Create an API key at [app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab, under
**Terminal & API keys**, and set it as `HERMOSO_API_KEY`. New accounts start free with no card.

The client is generated from the API's OpenAPI document, so every `/v1` operation has a typed function and every
request and response a typed model. Each operation lives in `hermoso.api.<group>.<operation>` with `sync`,
`sync_detailed`, `asyncio` and `asyncio_detailed`.

## Generate an ad

```python
from hermoso import create_client, run_tool, wait_for_job

client = create_client()  # reads HERMOSO_API_KEY

started = run_tool("generate_image", {
    "prompt": 'Summer launch ad for our cold brew: the can on a sunlit cafe table, headline "Cold. Brewed. Yours."',
    "job": "static_ad",
    "aspectRatio": "4:5",
}, client=client, wait=0)
job = wait_for_job(started.job_id, client=client)
print(job.url)  # the finished image, on your saved brand
```

`run_tool` reaches every Hermoso tool, the same set an agent gets over MCP: `render_ad` for video ads, `plan_ad`,
`clone_video`, competitor research and the ad platforms. `GET /v1/tools/{name}` (or `hermoso.api.tools.get_tool`)
describes each tool's arguments. Rendering costs credits; polling a job is free.

## Schedule a post

```python
import uuid
from hermoso.api.posts import create_post
from hermoso.models import PostCreate

post = create_post.sync(client=client, body=PostCreate.from_dict({
    "channels": ["instagram", "facebook"],
    "caption": "Cold. Brewed. Yours.",
    "media": [job.url],
    "scheduled_at": "2026-12-01T15:00:00Z",
}), idempotency_key=str(uuid.uuid4()))
print(post.id, post.status)
```

`hermoso.api.channels.list_channels` lists every channel and whether this brand has it connected. Omit
`scheduled_at` to publish now. Publishing is free.

## Read analytics

```python
from hermoso import paginate
from hermoso.api.analytics import get_best_time
from hermoso.api.posts import list_posts

best = get_best_time.sync(client=client, channel="instagram", timezone="America/New_York")
for slot in best.slots[:5]:
    print(slot.day_of_week, slot.hour, slot.avg_engagement)

for post in paginate(list_posts, client=client, status="published"):
    print(post.id, post.scheduled_at)
```

`paginate` follows the cursor on any list operation until the last page.

## Also

- `create_client(api_key=..., brand="<id from list_brands>")` acts on one brand of an account that holds several.
- `wait_for_job(job_id, client=client)` polls a render until it is `done` or `error`.
- Errors come back as the typed `Error` model; the helpers raise `HermosoError`.
- Async: every operation has `asyncio(...)`.

Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/) · API reference:
[hermoso.ai/docs/api](https://hermoso.ai/docs/api/) · OpenAPI:
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json) · TypeScript:
[`@hermoso/sdk`](https://www.npmjs.com/package/@hermoso/sdk)

MIT licensed. Generated with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
