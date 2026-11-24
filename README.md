# Hermoso SDKs

Typed clients for the [Hermoso API](https://hermoso.ai/docs/api/): generate image and video ads, publish and schedule
posts to your own channels, read your analytics, and call any of Hermoso's tools from your own backend.

| Language | Package | Install |
|---|---|---|
| TypeScript / Node 18+ | [`@hermoso/sdk`](https://www.npmjs.com/package/@hermoso/sdk) | `npm install @hermoso/sdk` |
| Python 3.11+ | [`hermoso`](https://pypi.org/project/hermoso/) | `pip install hermoso` |
| Go 1.24+ | [`github.com/hermoso-ai/hermoso-sdks/go`](go/) | `go get github.com/hermoso-ai/hermoso-sdks/go` |
| Ruby 3.1+ | [`hermoso`](https://rubygems.org/gems/hermoso) | `gem install hermoso` |
| PHP 8.1+ | [`hermoso/sdk`](https://packagist.org/packages/hermoso/sdk) | `composer require hermoso/sdk` |
| Java 11+ | [`ai.hermoso:hermoso-sdk`](java/) | from source: `mvn install` in [`java/`](java/) |
| .NET 8+ | [`Hermoso.Sdk`](https://www.nuget.org/packages/Hermoso.Sdk) | `dotnet add package Hermoso.Sdk` |
| Rust 1.85+ | [`hermoso`](rust/) | from source: `hermoso = { git = "https://github.com/hermoso-ai/hermoso-sdks" }` |

Java and Rust install from this repository until their registry packages (Maven Central, crates.io) are published;
the code is the same.

Every SDK is generated from the API's OpenAPI document ([`openapi.json`](openapi.json), live copy at
[app.hermoso.ai/openapi.json](https://app.hermoso.ai/openapi.json)), with a small hand-written layer for the same four
things in every language: a client that reads your key, pagination, waiting on render jobs, and calling any tool. They
are regenerated and released together whenever the API gains something, and share one version number.

- [TypeScript](typescript/README.md) · [Python](python/README.md) · [Go](go/README.md) · [Ruby](ruby/README.md) ·
  [PHP](php/README.md) · [Java](java/README.md) · [.NET](dotnet/README.md) · [Rust](rust/README.md)
- Docs: [hermoso.ai/docs/sdks](https://hermoso.ai/docs/sdks/)

Create an API key at [app.hermoso.ai](https://app.hermoso.ai) on the **API, MCP & CLI** tab. New accounts start free.

This repository is published from Hermoso's main codebase; the generated code (`typescript/src/gen`,
`python/hermoso`, `go/hermoso.gen.go`, `ruby/lib`, `php/lib`, `java/src`, `dotnet/Generated`, `rust/src`) is not
edited by hand. Issues are welcome here.

MIT licensed.
