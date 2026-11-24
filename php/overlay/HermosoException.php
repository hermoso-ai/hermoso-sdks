<?php
/** Hand-written (sdks/php/overlay); tools/sdk-generate.mjs copies it into lib/. */

namespace Hermoso;

/** An error answer from the API; getError() is the parsed body (`['error' => ['code' => …, 'message' => …]]`). */
class HermosoException extends \RuntimeException
{
    private ?int $status;
    private mixed $error;

    public function __construct(?int $status, mixed $error, ?\Throwable $previous = null)
    {
        $this->status = $status;
        $this->error = $error;
        $message = is_array($error) ? ($error['error']['message'] ?? null) : null;
        parent::__construct($message ?? ('Hermoso API error' . ($status ? " (HTTP $status)" : '')), $status ?? 0, $previous);
    }

    public static function fromApiException(ApiException $e): self
    {
        $body = $e->getResponseBody();
        $decoded = is_string($body) ? json_decode($body, true) : (is_object($body) ? json_decode(json_encode($body), true) : null);
        return new self($e->getCode() ?: null, $decoded, $e);
    }

    public function getStatus(): ?int { return $this->status; }
    public function getError(): mixed { return $this->error; }
}
