// The small hand-written layer over the generated client (Generated/, Kiota): a client that reads your key, a cursor
// paginator, a job waiter and a one-line tool call. Not generated, never touched by tools/sdk-generate.mjs.
using System.Net;
using System.Net.Http.Headers;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using Hermoso.Sdk.Generated;
using Hermoso.Sdk.Generated.Models;
using Microsoft.Kiota.Abstractions;
using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Abstractions.Serialization;
using Microsoft.Kiota.Http.HttpClientLibrary;

namespace Hermoso.Sdk;

/// <summary>An error answer from the API, thrown by the <see cref="HermosoClient"/> helpers.</summary>
public sealed class HermosoException : Exception
{
    /// <summary>The HTTP status.</summary>
    public int Status { get; }
    /// <summary>The API's <c>error.code</c>, when the body carried one.</summary>
    public string? Code { get; }
    /// <summary>The raw response body.</summary>
    public string? Body { get; }

    internal HermosoException(int status, string? body) : base(MessageOf(status, body))
    {
        Status = status;
        Body = body;
        Code = Field(body, "code");
    }

    private static string? Field(string? body, string name)
    {
        try
        {
            using var doc = JsonDocument.Parse(body ?? "");
            return doc.RootElement.TryGetProperty("error", out var e) && e.TryGetProperty(name, out var v) && v.ValueKind == JsonValueKind.String ? v.GetString() : null;
        }
        catch (JsonException) { return null; }
    }

    private static string MessageOf(int status, string? body) => Field(body, "message") ?? $"Hermoso API error (HTTP {status})";
}

/// <summary>A render a tool queued (HTTP 202): pass <see cref="JobId"/> to <see cref="HermosoClient.WaitForJobAsync"/>.</summary>
public sealed class ToolJob
{
    [JsonPropertyName("tool")] public string? Tool { get; set; }
    [JsonPropertyName("job_id")] public string? JobId { get; set; }
    [JsonPropertyName("status")] public string? Status { get; set; }
    [JsonPropertyName("poll")] public string? Poll { get; set; }
    [JsonPropertyName("poll_url")] public string? PollUrl { get; set; }
    [JsonPropertyName("retry_after_seconds")] public int? RetryAfterSeconds { get; set; }
    [JsonPropertyName("text")] public string? Text { get; set; }
}

/// <summary>What a tool call answered: <see cref="Result"/> when the tool finished, <see cref="Job"/> when it queued a render.</summary>
public sealed record ToolCallResult(ToolResult? Result, ToolJob? Job)
{
    /// <summary>True when the tool queued a render.</summary>
    public bool IsJob => Job is not null;
}

/// <summary>
/// The Hermoso API client. <see cref="Api"/> is the generated, fluent client for every <c>/v1</c> operation; the methods
/// here are the helpers on top.
/// <code>
/// var hermoso = HermosoClient.Create();                 // reads HERMOSO_API_KEY
/// var credits = await hermoso.Api.V1.Credits.GetAsync();
/// </code>
/// </summary>
public sealed class HermosoClient
{
    /// <summary>The Hermoso API.</summary>
    public const string DefaultBaseUrl = "https://app.hermoso.ai";

    private readonly HttpClient _http;
    private readonly string _baseUrl;
    private readonly string _apiKey;
    private readonly string? _brand;

    /// <summary>The generated client: <c>Api.V1.Posts.PostAsync(…)</c>, <c>Api.V1.Jobs[id].GetAsync()</c>, and so on.</summary>
    public HermosoApiClient Api { get; }

    private HermosoClient(HermosoApiClient api, HttpClient http, string baseUrl, string apiKey, string? brand)
    {
        Api = api;
        _http = http;
        _baseUrl = baseUrl;
        _apiKey = apiKey;
        _brand = brand;
    }

    /// <summary>
    /// A client authenticated with your API key (default: the HERMOSO_API_KEY environment variable). <paramref name="brand"/>
    /// acts on that brand (an id from <c>Api.V1.Brands.GetAsync()</c>) instead of the one the key is pinned to.
    /// </summary>
    public static HermosoClient Create(string? apiKey = null, string? brand = null, string baseUrl = DefaultBaseUrl, HttpClient? httpClient = null)
    {
        var key = apiKey ?? Environment.GetEnvironmentVariable("HERMOSO_API_KEY");
        if (string.IsNullOrEmpty(key))
            throw new ArgumentException("No Hermoso API key: pass apiKey or set HERMOSO_API_KEY. Create one at https://app.hermoso.ai on the \"API, MCP & CLI\" tab, under \"Terminal & API keys\".");
        var root = baseUrl.TrimEnd('/');
        var http = httpClient ?? KiotaClientFactory.Create();
        var adapter = new HttpClientRequestAdapter(new KeyAuthentication(key, brand), httpClient: http) { BaseUrl = root };
        return new HermosoClient(new HermosoApiClient(adapter), http, root, key, brand);
    }

    private sealed class KeyAuthentication(string key, string? brand) : IAuthenticationProvider
    {
        public Task AuthenticateRequestAsync(RequestInformation request, Dictionary<string, object>? additionalAuthenticationContext = null, CancellationToken cancellationToken = default)
        {
            request.Headers.TryAdd("Authorization", "Bearer " + key);
            if (brand is not null && !request.Headers.ContainsKey("X-Hermoso-User")) request.Headers.TryAdd("X-Hermoso-User", brand);
            return Task.CompletedTask;
        }
    }

    /// <summary>
    /// Every item of a cursor-paginated list, following <c>next_cursor</c> until <c>has_more</c> is false. Pass the cursor
    /// through as the list's <c>StartingAfter</c> (or <c>Cursor</c>, for the conversion-events list):
    /// <code>
    /// await foreach (var post in hermoso.PaginateAsync&lt;Post&gt;(cursor => hermoso.Api.V1.Posts.GetAsync(c =>
    ///     { c.QueryParameters.Status = "published"; c.QueryParameters.StartingAfter = cursor; })))
    /// </code>
    /// </summary>
    public async IAsyncEnumerable<T> PaginateAsync<T>(Func<string?, Task<object?>> fetchPage, [EnumeratorCancellation] CancellationToken cancellationToken = default)
    {
        string? cursor = null;
        while (true)
        {
            cancellationToken.ThrowIfCancellationRequested();
            var page = await fetchPage(cursor).ConfigureAwait(false) ?? throw new HermosoException(0, null);
            var type = page.GetType();
            if (type.GetProperty("Data")?.GetValue(page) is System.Collections.IEnumerable items)
                foreach (var item in items) yield return (T)item;
            cursor = type.GetProperty("NextCursor")?.GetValue(page) as string;
            var hasMore = type.GetProperty("HasMore")?.GetValue(page) as bool?;
            if (string.IsNullOrEmpty(cursor) || hasMore == false) yield break;
        }
    }

    /// <summary>Wraps a typed page fetch for <see cref="PaginateAsync{T}"/>.</summary>
    public async IAsyncEnumerable<T> PaginateAsync<TPage, T>(Func<string?, Task<TPage?>> fetchPage, [EnumeratorCancellation] CancellationToken cancellationToken = default) where TPage : class
    {
        await foreach (var item in PaginateAsync<T>(async c => await fetchPage(c).ConfigureAwait(false), cancellationToken)) yield return item;
    }

    /// <summary>
    /// Polls a job (a render, a stitch, an upscale…) until it is <c>done</c> or <c>error</c> and returns it; the file is
    /// <c>job.Url</c>. Polling is free; calling the tool again would start (and bill) a second render. Cancelling stops
    /// the wait, never the job.
    /// </summary>
    public async Task<Job> WaitForJobAsync(string id, TimeSpan? interval = null, TimeSpan? timeout = null, CancellationToken cancellationToken = default)
    {
        var deadline = DateTimeOffset.UtcNow + (timeout ?? TimeSpan.FromMinutes(20));
        while (true)
        {
            var job = await Api.V1.Jobs[id].GetAsync(cancellationToken: cancellationToken).ConfigureAwait(false)
                ?? throw new HermosoException(0, null);
            if (job.Status is "done" or "error") return job;
            if (DateTimeOffset.UtcNow > deadline)
                throw new TimeoutException($"Job {id} is still {job.Status}; it keeps running, call WaitForJobAsync again.");
            await Task.Delay(interval ?? TimeSpan.FromSeconds(5), cancellationToken).ConfigureAwait(false);
        }
    }

    /// <summary>
    /// Runs any Hermoso tool through <c>POST /v1/tools/{name}</c> with its arguments. <paramref name="wait"/> 0 answers at
    /// once with a job handle; omitted, a render is held up to 45 seconds. <c>Api.V1.Tools[name].GetAsync()</c> describes
    /// each tool's arguments.
    /// <code>
    /// var plan = await hermoso.RunToolAsync("plan_ad", new() { ["product"] = "our cold brew, summer offer" });
    /// </code>
    /// </summary>
    public async Task<ToolCallResult> RunToolAsync(string name, Dictionary<string, object?>? args = null, int? wait = null, string? idempotencyKey = null, CancellationToken cancellationToken = default)
    {
        var url = $"{_baseUrl}/v1/tools/{Uri.EscapeDataString(name)}" + (wait is int w ? $"?wait={w}" : "");
        using var req = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(JsonSerializer.Serialize(args ?? new Dictionary<string, object?>()), Encoding.UTF8, "application/json"),
        };
        req.Headers.Authorization = new AuthenticationHeaderValue("Bearer", _apiKey);
        req.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
        if (_brand is not null) req.Headers.Add("X-Hermoso-User", _brand);
        if (idempotencyKey is not null) req.Headers.Add("Idempotency-Key", idempotencyKey);
        using var res = await _http.SendAsync(req, cancellationToken).ConfigureAwait(false);
        var body = await res.Content.ReadAsStringAsync(cancellationToken).ConfigureAwait(false);
        if (res.StatusCode == HttpStatusCode.Accepted) return new ToolCallResult(null, JsonSerializer.Deserialize<ToolJob>(body));
        if (res.StatusCode == HttpStatusCode.OK)
            return new ToolCallResult(await KiotaJsonSerializer.DeserializeAsync(body, ToolResult.CreateFromDiscriminatorValue, cancellationToken).ConfigureAwait(false), null);
        throw new HermosoException((int)res.StatusCode, body);
    }
}
