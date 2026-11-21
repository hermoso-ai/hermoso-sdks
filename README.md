# Hermoso SDKs

Typed clients for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and schedule
posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

| Language | Package | Install |
|---|---|---|
| TypeScript / Node 18+ | [`@hermoso/sdk`](https://www.npmjs.com/package/@hermoso/sdk) | `npm install @hermoso/sdk` |
| Python 3.11+ | [`hermoso`](python/) | `pip install "git+https://github.com/hermoso-ai/hermoso-sdks#subdirectory=python"` |

Both are generated from the API's OpenAPI document ([`openapi.json`](openapi.json), live copy at
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json)), with a small hand-written layer for the API key,
pagination, waiting on render jobs and calling tools. They are regenerated and released together whenever the API
gains something, and share one version number.

- [TypeScript README](typescript/README.md)
- [Python README](python/README.md)
- Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/)

Create an API key at [app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab. New accounts start free.

This repository is published from Hermoso's main codebase; the generated code under `typescript/src/gen` and
`python/hermoso` is not edited by hand. Issues are welcome here.

MIT licensed.
