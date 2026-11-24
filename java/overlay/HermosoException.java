package ai.hermoso.sdk;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * An error answer from the API, thrown by the {@link Hermoso} helpers. {@link #getCode()} is the API's
 * {@code error.code}; {@link #getStatus()} the HTTP status. Hand-written (sdks/java/overlay).
 */
public class HermosoException extends RuntimeException {
  private static final ObjectMapper MAPPER = new ObjectMapper();
  private final int status;
  private final String code;
  private final String body;

  public HermosoException(int status, String body) {
    super(message(status, body));
    this.status = status;
    this.body = body;
    this.code = field(body, "code");
  }

  static HermosoException from(ApiException e) {
    HermosoException out = new HermosoException(e.getCode(), e.getResponseBody());
    out.initCause(e);
    return out;
  }

  private static String field(String body, String name) {
    try {
      JsonNode n = MAPPER.readTree(body == null ? "" : body).path("error").path(name);
      return n.isTextual() ? n.asText() : null;
    } catch (Exception e) {
      return null;
    }
  }

  private static String message(int status, String body) {
    String m = field(body, "message");
    return m != null ? m : "Hermoso API error" + (status > 0 ? " (HTTP " + status + ")" : "");
  }

  /** The HTTP status, or 0 when no response arrived. */
  public int getStatus() { return status; }
  /** The API's {@code error.code}, when the body carried one. */
  public String getCode() { return code; }
  /** The raw response body. */
  public String getBody() { return body; }
}
