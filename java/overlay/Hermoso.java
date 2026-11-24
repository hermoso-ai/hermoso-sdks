package ai.hermoso.sdk;

import ai.hermoso.sdk.api.JobsApi;
import ai.hermoso.sdk.model.Job;
import ai.hermoso.sdk.model.ToolJob;
import ai.hermoso.sdk.model.ToolResult;

import java.io.IOException;
import java.lang.reflect.Method;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.function.Consumer;

/**
 * The small hand-written layer over the generated client: a client that reads your key, a cursor paginator, a job
 * waiter and a one-line tool call. Not generated; tools/sdk-generate.mjs copies it in from sdks/java/overlay.
 *
 * <pre>{@code
 * ApiClient client = Hermoso.client();                       // reads HERMOSO_API_KEY
 * Credits credits = new CreditsApi(client).getCredits(CreditsApi.APIGetCreditsRequest.newBuilder().build());
 * }</pre>
 */
public final class Hermoso {
  /** The Hermoso API. */
  public static final String DEFAULT_BASE_URL = "https://app.hermoso.ai";

  private Hermoso() {}

  /** Options for {@link #client(Options)}. */
  public static final class Options {
    private String apiKey;
    private String brand;
    private String baseUrl = DEFAULT_BASE_URL;
    private Duration timeout = Duration.ofSeconds(90);

    /** A Hermoso API key ({@code hmk_…}). Defaults to the HERMOSO_API_KEY environment variable. */
    public Options apiKey(String apiKey) { this.apiKey = apiKey; return this; }
    /** Act on this brand (an id from listBrands) instead of the one the key is pinned to. Sent as X-Hermoso-User. */
    public Options brand(String brand) { this.brand = brand; return this; }
    /** Defaults to https://app.hermoso.ai. */
    public Options baseUrl(String baseUrl) { this.baseUrl = baseUrl; return this; }
    /** Read timeout per request; defaults to 90 seconds. */
    public Options timeout(Duration timeout) { this.timeout = timeout; return this; }
  }

  /** Start building {@link Options}. */
  public static Options options() { return new Options(); }

  /** A client authenticated with HERMOSO_API_KEY. */
  public static ApiClient client() { return client(new Options()); }

  /** A client authenticated with your API key. Pass it to any generated API: {@code new PostsApi(client)}. */
  public static ApiClient client(Options options) {
    String key = options.apiKey != null ? options.apiKey : System.getenv("HERMOSO_API_KEY");
    if (key == null || key.isEmpty()) {
      throw new IllegalArgumentException("No Hermoso API key: pass Options.apiKey or set HERMOSO_API_KEY. Create one at https://app.hermoso.ai on the \"API, MCP & CLI\" tab, under \"Terminal & API keys\".");
    }
    ApiClient client = new ApiClient();
    client.updateBaseUri(options.baseUrl.replaceAll("/+$", ""));
    client.setReadTimeout(options.timeout);
    final String brand = options.brand;
    Consumer<HttpRequest.Builder> auth = b -> {
      b.setHeader("Authorization", "Bearer " + key);
      if (brand != null && !alreadySet(b, "X-Hermoso-User")) b.setHeader("X-Hermoso-User", brand);
    };
    client.setRequestInterceptor(auth);
    return client;
  }

  private static boolean alreadySet(HttpRequest.Builder b, String header) {
    try {
      return b.copy().build().headers().firstValue(header).isPresent();
    } catch (RuntimeException e) {
      return false;
    }
  }

  /** One page of a list: anything with getData(), getNextCursor() and, usually, getHasMore(). */
  @FunctionalInterface
  public interface PageFetcher {
    /** Fetch the page after {@code cursor} (null for the first page). */
    Object fetch(String cursor) throws ApiException;
  }

  /**
   * Every item of a cursor-paginated list, following {@code next_cursor} until {@code has_more} is false. Pass the
   * cursor through as the list's {@code startingAfter} (or {@code cursor}, for listConversionEvents):
   *
   * <pre>{@code
   * PostsApi posts = new PostsApi(client);
   * for (Post post : Hermoso.paginate(Post.class,
   *     cursor -> posts.listPosts(PostsApi.APIListPostsRequest.newBuilder().status("published").startingAfter(cursor).build()))) { … }
   * }</pre>
   */
  public static <T> Iterable<T> paginate(Class<T> itemType, PageFetcher fetch) {
    return () -> new Iterator<T>() {
      private List<?> items = Collections.emptyList();
      private int index = 0;
      private String cursor = null;
      private boolean last = false;

      @Override
      public boolean hasNext() {
        while (index >= items.size()) {
          if (last) return false;
          Object page;
          try {
            page = fetch.fetch(cursor);
          } catch (ApiException e) {
            throw HermosoException.from(e);
          }
          List<?> data = (List<?>) call(page, "getData");
          items = data == null ? Collections.emptyList() : new ArrayList<>(data);
          index = 0;
          cursor = (String) call(page, "getNextCursor");
          Object hasMore = callIfPresent(page, "getHasMore");
          last = cursor == null || cursor.isEmpty() || Boolean.FALSE.equals(hasMore);
        }
        return true;
      }

      @Override
      public T next() {
        if (!hasNext()) throw new NoSuchElementException();
        return itemType.cast(items.get(index++));
      }
    };
  }

  private static Object call(Object target, String method) {
    try {
      return target.getClass().getMethod(method).invoke(target);
    } catch (ReflectiveOperationException e) {
      throw new IllegalArgumentException(target.getClass().getSimpleName() + " is not a paginated list (no " + method + "())", e);
    }
  }

  private static Object callIfPresent(Object target, String method) {
    for (Method m : target.getClass().getMethods()) if (m.getName().equals(method) && m.getParameterCount() == 0) return call(target, method);
    return null;
  }

  /** Polls a job every 5 seconds for up to 20 minutes; see {@link #waitForJob(ApiClient, String, Duration, Duration)}. */
  public static Job waitForJob(ApiClient client, String id) throws InterruptedException {
    return waitForJob(client, id, Duration.ofSeconds(5), Duration.ofMinutes(20));
  }

  /**
   * Polls a job (a render, a stitch, an upscale…) until it is {@code done} or {@code error} and returns it; the file is
   * {@code job.getUrl()}. Polling is free; calling the tool again would start (and bill) a second render.
   */
  public static Job waitForJob(ApiClient client, String id, Duration interval, Duration timeout) throws InterruptedException {
    JobsApi jobs = new JobsApi(client);
    Instant deadline = Instant.now().plus(timeout);
    while (true) {
      Job job;
      try {
        job = jobs.getJob(id, null);
      } catch (ApiException e) {
        throw HermosoException.from(e);
      }
      if ("done".equals(job.getStatus()) || "error".equals(job.getStatus())) return job;
      if (Instant.now().isAfter(deadline)) {
        throw new IllegalStateException("Job " + id + " is still " + job.getStatus() + "; it keeps running, call waitForJob again.");
      }
      Thread.sleep(interval.toMillis());
    }
  }

  /** Options for {@link #runTool(ApiClient, String, Map, RunToolOptions)}. */
  public static final class RunToolOptions {
    private Integer wait;
    private String idempotencyKey;

    /** Seconds to hold the request while a render finishes; 0 answers at once with a job handle. Unset: up to 45s. */
    public RunToolOptions wait(int seconds) { this.wait = seconds; return this; }
    /** Makes the call safe to retry: a replay returns the original answer (or the job it queued). */
    public RunToolOptions idempotencyKey(String key) { this.idempotencyKey = key; return this; }
  }

  /** Start building {@link RunToolOptions}. */
  public static RunToolOptions runOptions() { return new RunToolOptions(); }

  /** What a tool call answered: {@link #result()} when the tool finished, {@link #job()} when it queued a render. */
  public static final class ToolCallResult {
    private final ToolResult result;
    private final ToolJob job;

    ToolCallResult(ToolResult result, ToolJob job) { this.result = result; this.job = job; }
    /** The tool's answer, or null when it queued a render. */
    public ToolResult result() { return result; }
    /** The queued render (pass {@code getJobId()} to waitForJob), or null when the tool finished. */
    public ToolJob job() { return job; }
    /** True when the tool queued a render. */
    public boolean isJob() { return job != null; }
  }

  /** Runs a tool with the server's default wait. */
  public static ToolCallResult runTool(ApiClient client, String name, Map<String, Object> args) throws IOException, InterruptedException {
    return runTool(client, name, args, new RunToolOptions());
  }

  /**
   * Runs any Hermoso tool through {@code POST /v1/tools/{name}} with its arguments. ToolsApi.getTool describes each
   * tool's arguments.
   *
   * <pre>{@code
   * ToolCallResult plan = Hermoso.runTool(client, "plan_ad", Map.of("product", "our cold brew, summer offer"));
   * }</pre>
   */
  public static ToolCallResult runTool(ApiClient client, String name, Map<String, Object> args, RunToolOptions options) throws IOException, InterruptedException {
    String path = "/v1/tools/" + URLEncoder.encode(name, StandardCharsets.UTF_8).replace("+", "%20")
        + (options.wait != null ? "?wait=" + options.wait : "");
    HttpRequest.Builder b = HttpRequest.newBuilder()
        .uri(URI.create(client.getBaseUri() + path))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .POST(HttpRequest.BodyPublishers.ofByteArray(client.getObjectMapper().writeValueAsBytes(args == null ? Map.of() : args)));
    if (options.idempotencyKey != null) b.header("Idempotency-Key", options.idempotencyKey);
    if (client.getReadTimeout() != null) b.timeout(client.getReadTimeout());
    if (client.getRequestInterceptor() != null) client.getRequestInterceptor().accept(b);
    HttpResponse<byte[]> res = client.getHttpClient().send(b.build(), HttpResponse.BodyHandlers.ofByteArray());
    if (res.statusCode() == 202) return new ToolCallResult(null, client.getObjectMapper().readValue(res.body(), ToolJob.class));
    if (res.statusCode() == 200) return new ToolCallResult(client.getObjectMapper().readValue(res.body(), ToolResult.class), null);
    throw new HermosoException(res.statusCode(), new String(res.body(), StandardCharsets.UTF_8));
  }
}
