// @hermoso/sdk: the typed client for the Hermoso API (https://hermoso.ai/docs/api/).
//
// Everything under ./gen is GENERATED from the /v1 OpenAPI document by tools/sdk-generate.mjs and must not be edited.
// This file is the small hand-written layer on top: a client that reads your key, a cursor paginator, a job waiter
// and a one-line tool call.
import { createClient, createConfig, type Client } from './gen/client/index.js';
import { getJob, callTool } from './gen/sdk.gen.js';
import type { Job, ToolResult, ToolJob } from './gen/types.gen.js';

export * from './gen/sdk.gen.js';
export type * from './gen/types.gen.js';
export { createClient, createConfig } from './gen/client/index.js';
export type { Client, Config, Options as RequestOptions } from './gen/client/index.js';
export { SPEC_SHA256, CONTRACT_VERSION } from './gen/spec.gen.js';

export const DEFAULT_BASE_URL = 'https://app.hermoso.ai';

/** An error body from the API (`{ error: { type, code, message, … } }`), thrown by the helpers in this file. */
export class HermosoError extends Error {
  readonly status: number | undefined;
  readonly body: unknown;
  constructor(body: unknown, status?: number) {
    const e = (body as { error?: { message?: string; code?: string } } | undefined)?.error;
    super(e?.message || `Hermoso API error${status ? ` (HTTP ${status})` : ''}`);
    this.name = 'HermosoError';
    this.status = status;
    this.body = body;
  }
}

export interface HermosoClientOptions {
  /** A Hermoso API key (`hmk_…`). Defaults to the HERMOSO_API_KEY environment variable. */
  apiKey?: string;
  /** Act on this brand (an `id` from `listBrands`) instead of the one the key is pinned to. Sent as `X-Hermoso-User`. */
  brand?: string;
  /** Defaults to https://app.hermoso.ai. */
  baseUrl?: string;
  /** A custom fetch, e.g. for proxies or tests. */
  fetch?: typeof fetch;
}

const env = (k: string): string | undefined =>
  (globalThis as { process?: { env?: Record<string, string | undefined> } }).process?.env?.[k];

/**
 * A client authenticated with your API key. Pass it as `client` to any operation:
 *
 *   const hermoso = createHermosoClient();
 *   const { data } = await listChannels({ client: hermoso });
 */
export function createHermosoClient(options: HermosoClientOptions = {}): Client {
  const apiKey = options.apiKey ?? env('HERMOSO_API_KEY');
  if (!apiKey) throw new Error('No Hermoso API key: pass { apiKey } or set HERMOSO_API_KEY. Create one at https://app.hermoso.ai on the "API, MCP & CLI" tab, under "Terminal & API keys".');
  return createClient(createConfig({
    baseUrl: options.baseUrl ?? DEFAULT_BASE_URL,
    auth: () => apiKey,
    ...(options.brand ? { headers: { 'X-Hermoso-User': options.brand } } : {}),
    ...(options.fetch ? { fetch: options.fetch } : {}),
  }));
}

type Page<T> = { data?: T[]; has_more?: boolean; next_cursor?: string | null };
type ListFn<O, T> = (options: O) => Promise<{ data?: Page<T> | undefined; error?: unknown; response?: Response }>;

/**
 * Iterate every item of a cursor-paginated list (`listPosts`, `listJobs`, `listTools`, `listConversionEvents`),
 * following `next_cursor` until `has_more` is false:
 *
 *   for await (const post of paginate(listPosts, { client: hermoso, query: { status: 'scheduled' } })) { … }
 *
 * `listConversionEvents` takes its cursor as `cursor`; every other list takes `starting_after`. That is detected.
 */
export async function* paginate<O extends { query?: object }, T>(fn: ListFn<O, T>, options: O, { cursorParam }: { cursorParam?: string } = {}): AsyncGenerator<T> {
  const param = cursorParam ?? (fn.name === 'listConversionEvents' ? 'cursor' : 'starting_after');
  let cursor: string | null | undefined;
  for (;;) {
    const opts = cursor ? { ...options, query: { ...(options.query || {}), [param]: cursor } } : options;
    const res = await fn(opts);
    if (res.error !== undefined || !res.data) throw new HermosoError(res.error, res.response?.status);
    for (const item of res.data.data || []) yield item;
    cursor = res.data.next_cursor;
    if (!cursor || res.data.has_more === false) return;
  }
}

/**
 * Poll a job (a render, a stitch, an upscale…) until it is `done` or `error`, and return it. A finished job's file is
 * `job.url`. Polling is free; re-calling the tool that started the job would start (and bill) a second one.
 */
export async function waitForJob(id: string, { client, intervalMs = 5000, timeoutMs = 20 * 60_000 }: { client?: Client; intervalMs?: number; timeoutMs?: number } = {}): Promise<Job> {
  const until = Date.now() + timeoutMs;
  for (;;) {
    const res = await getJob({ client, path: { id } });
    if (res.error !== undefined || !res.data) throw new HermosoError(res.error, res.response?.status);
    const job = res.data as Job;
    if (job.status === 'done' || job.status === 'error') return job;
    if (Date.now() > until) throw new Error(`Job ${id} is still ${job.status} after ${Math.round(timeoutMs / 1000)}s. It keeps running: call waitForJob again.`);
    await new Promise((r) => setTimeout(r, intervalMs));
  }
}

/**
 * Run any Hermoso tool through `POST /v1/tools/{name}` with its arguments, and get its result. When the tool starts
 * a render, the result is a job handle: pass `job_id` to `waitForJob`. `GET /v1/tools/{name}` describes each tool's
 * arguments.
 *
 *   const plan = await runTool('plan_ad', { product: 'our cold brew, summer offer', format: 'video' }, { client: hermoso });
 */
export async function runTool(name: string, args: Record<string, unknown> = {}, { client, wait, idempotencyKey }: { client?: Client; wait?: number; idempotencyKey?: string } = {}): Promise<ToolResult | ToolJob> {
  const res: { data?: ToolResult | ToolJob; error?: unknown; response?: Response } = await callTool({
    client,
    path: { name },
    body: args,
    ...(wait !== undefined ? { query: { wait: String(wait) } } : {}),
    ...(idempotencyKey ? { headers: { 'Idempotency-Key': idempotencyKey } } : {}),
  } as Parameters<typeof callTool>[0]) as never;
  if (res.error !== undefined || !res.data) throw new HermosoError(res.error, res.response?.status);
  return res.data as ToolResult | ToolJob;
}
