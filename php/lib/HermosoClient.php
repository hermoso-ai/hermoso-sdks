<?php
/**
 * The small hand-written layer over the generated client: a client that reads your key, a cursor paginator, a job
 * waiter and a one-line tool call. Not generated; tools/sdk-generate.mjs copies it in from sdks/php/overlay.
 */

namespace Hermoso;

use GuzzleHttp\Client;
use Hermoso\Api\JobsApi;
use Hermoso\Api\ToolsApi;
use Hermoso\Model\Job;
use Hermoso\Model\ToolJob;
use Hermoso\Model\ToolResult;

/**
 * A client authenticated with your API key. Build any generated API from it:
 *
 *   $hermoso = HermosoClient::create();                       // reads HERMOSO_API_KEY
 *   $credits = $hermoso->api(Api\CreditsApi::class)->getCredits();
 */
final class HermosoClient
{
    public const DEFAULT_BASE_URL = 'https://app.hermoso.ai';

    public function __construct(public readonly Configuration $config, public readonly Client $http)
    {
    }

    /** `$brand` acts on that brand (an id from listBrands) instead of the one the key is pinned to. */
    public static function create(?string $apiKey = null, ?string $brand = null, string $baseUrl = self::DEFAULT_BASE_URL, float $timeout = 90.0): self
    {
        $key = $apiKey ?? (getenv('HERMOSO_API_KEY') ?: null);
        if (!$key) {
            throw new \InvalidArgumentException('No Hermoso API key: pass $apiKey or set HERMOSO_API_KEY. Create one at https://app.hermoso.ai on the "API, MCP & CLI" tab, under "Terminal & API keys".');
        }
        $config = (new Configuration())->setAccessToken($key)->setHost(rtrim($baseUrl, '/'));
        $http = new Client(['timeout' => $timeout, 'headers' => $brand ? ['X-Hermoso-User' => $brand] : []]);
        return new self($config, $http);
    }

    /**
     * An instance of any generated API class, sharing this client's key and connection.
     *
     * @template T
     * @param class-string<T> $class e.g. Api\PostsApi::class
     * @return T
     */
    public function api(string $class): object
    {
        return new $class($this->http, $this->config);
    }

    /**
     * Every item of a cursor-paginated list, following `next_cursor` until `has_more` is false. `$params` are the list
     * method's arguments by name:
     *
     *   foreach ($hermoso->paginate([$hermoso->api(Api\PostsApi::class), 'listPosts'], ['status' => 'published']) as $post) { … }
     *
     * listConversionEvents takes its cursor as `cursor`; every other list takes `starting_after`. That is detected.
     */
    public function paginate(callable $operation, array $params = []): \Generator
    {
        $name = is_array($operation) ? (string) $operation[1] : '';
        $cursorParam = $name === 'listConversionEvents' ? 'cursor' : 'starting_after';
        $cursor = null;
        while (true) {
            $args = $cursor !== null ? array_merge($params, [$cursorParam => $cursor]) : $params;
            try {
                $page = $operation(...$args);
            } catch (ApiException $e) {
                throw HermosoException::fromApiException($e);
            }
            if ($page instanceof Model\Error) {
                throw new HermosoException(null, json_decode((string) $page, true));
            }
            foreach ($page->getData() ?? [] as $item) {
                yield $item;
            }
            $cursor = $page->getNextCursor();
            $hasMore = method_exists($page, 'getHasMore') ? $page->getHasMore() : null;
            if ($cursor === null || $cursor === '' || $hasMore === false) {
                return;
            }
        }
    }

    /**
     * Polls a job (a render, a stitch, an upscale…) until it is `done` or `error` and returns it; the file is
     * `$job->getUrl()`. Polling is free; calling the tool again would start (and bill) a second render.
     */
    public function waitForJob(string $id, float $interval = 5.0, float $timeout = 1200.0): Job
    {
        $jobs = $this->api(JobsApi::class);
        $deadline = microtime(true) + $timeout;
        while (true) {
            try {
                $job = $jobs->getJob($id);
            } catch (ApiException $e) {
                throw HermosoException::fromApiException($e);
            }
            if (!$job instanceof Job) {
                throw new HermosoException(null, json_decode((string) $job, true));
            }
            if (in_array($job->getStatus(), ['done', 'error'], true)) {
                return $job;
            }
            if (microtime(true) > $deadline) {
                throw new \RuntimeException("Job $id is still {$job->getStatus()}; it keeps running, call waitForJob again.");
            }
            usleep((int) ($interval * 1_000_000));
        }
    }

    /**
     * Runs any Hermoso tool through POST /v1/tools/{name} and returns its result: a ToolResult, or a ToolJob handle when
     * it queued a render (pass getJobId() to waitForJob). ToolsApi::getTool describes each tool's arguments.
     *
     *   $plan = $hermoso->runTool('plan_ad', ['product' => 'our cold brew, summer offer', 'format' => 'video']);
     */
    public function runTool(string $name, array $args = [], ?int $wait = null, ?string $idempotencyKey = null): ToolResult|ToolJob
    {
        try {
            [$out] = $this->api(ToolsApi::class)->callToolWithHttpInfo($name, $args ?: new \stdClass(), wait: $wait === null ? null : (string) $wait, idempotency_key: $idempotencyKey);
        } catch (ApiException $e) {
            throw HermosoException::fromApiException($e);
        }
        if ($out instanceof ToolResult || $out instanceof ToolJob) {
            return $out;
        }
        throw new HermosoException(null, json_decode((string) $out, true));
    }
}
