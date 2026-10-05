/**
 * Error types for the Factorial API client.
 *
 * Every non-2xx HTTP response is thrown as a {@link FactorialApiError} carrying
 * the status, method, URL and parsed body. Transport failures (DNS, connection
 * reset, aborted request) are *not* wrapped — they surface as the underlying
 * error, typically a `TypeError` from `fetch`.
 */

/** Constructor payload for {@link FactorialApiError}. */
export interface FactorialApiErrorInit {
  /** HTTP status code, e.g. `401`. */
  status: number;
  /** HTTP reason phrase, e.g. `"Unauthorized"`. Empty over HTTP/2. */
  statusText: string;
  /** HTTP method of the failed request, e.g. `"GET"`. */
  method: string;
  /** Full request URL, including the query string. */
  url: string;
  /**
   * Response body: the parsed JSON when the body was valid JSON, the raw string
   * for non-JSON bodies, `undefined` when the body was empty.
   */
  body: unknown;
  /** Response headers. Rate-limit and request-id headers live here. */
  headers?: Headers;
  /** The raw `Response`, when one was produced. */
  response?: Response;
}

/**
 * Thrown for every non-2xx response from the Factorial API.
 *
 * @example
 * ```ts
 * try {
 *   await client.employees.employees.get({ path: { id: "1" } });
 * } catch (err) {
 *   if (err instanceof FactorialApiError) {
 *     console.error(err.status, err.method, err.url, err.body);
 *   } else {
 *     throw err; // transport failure (e.g. a fetch TypeError)
 *   }
 * }
 * ```
 */
export class FactorialApiError extends Error {
  /** HTTP status code, e.g. `401`. */
  readonly status: number;
  /** HTTP reason phrase, e.g. `"Unauthorized"`. Empty over HTTP/2. */
  readonly statusText: string;
  /** HTTP method of the failed request, e.g. `"GET"`. */
  readonly method: string;
  /** Full request URL, including the query string. */
  readonly url: string;
  /**
   * Response body: the parsed JSON when the body was valid JSON, the raw string
   * for non-JSON bodies, `undefined` when the body was empty.
   */
  readonly body: unknown;
  /**
   * Response headers. Rate-limit and request-id headers live here.
   *
   * Non-enumerable, so logging the error stays readable.
   */
  readonly headers!: Headers;
  /**
   * The raw `Response`. Its body stream has already been consumed to populate
   * {@link FactorialApiError.body} — read that instead.
   *
   * Non-enumerable, so logging the error stays readable.
   */
  readonly response?: Response;

  constructor(init: FactorialApiErrorInit) {
    super(formatMessage(init));
    this.name = "FactorialApiError";
    this.status = init.status;
    this.statusText = init.statusText;
    this.method = init.method;
    this.url = init.url;
    this.body = init.body;
    // `headers` and `response` are hidden from enumeration: console.error(err)
    // and JSON.stringify(err) would otherwise dump the whole Response object,
    // burying the fields that identify the failure.
    Object.defineProperty(this, "headers", {
      value: init.headers ?? new Headers(),
      enumerable: false,
      writable: false,
      configurable: true,
    });
    Object.defineProperty(this, "response", {
      value: init.response,
      enumerable: false,
      writable: false,
      configurable: true,
    });
  }
}

/**
 * `instanceof`-safe check for {@link FactorialApiError}.
 *
 * Prefer `err instanceof FactorialApiError`. Use this helper when two copies of
 * the package may be loaded at once (the ESM + CJS dual-package hazard), where
 * `instanceof` can fail across realm boundaries.
 */
export function isFactorialApiError(error: unknown): error is FactorialApiError {
  return (
    error instanceof FactorialApiError ||
    (typeof error === "object" &&
      error !== null &&
      (error as { name?: unknown }).name === "FactorialApiError")
  );
}

/**
 * Converts the raw value thrown by the underlying fetch client for a non-2xx
 * response (the parsed JSON body, the raw text, or `""`) into a
 * {@link FactorialApiError}.
 *
 * Registered as the client's error interceptor by `FactorialClient`. Values
 * that do not describe an HTTP error response are returned untouched:
 *
 * - no `Response` — a transport failure such as a `fetch` `TypeError`
 * - an ok `Response` — a failure while parsing a 2xx body
 * - an `Error` instance — already a usable error, e.g. thrown by a user
 *   interceptor
 */
export function toFactorialApiError(
  error: unknown,
  response: Response | undefined,
  request: Request | undefined,
): unknown {
  if (response === undefined || response.ok) return error;
  if (error instanceof Error) return error;
  return new FactorialApiError({
    status: response.status,
    statusText: response.statusText,
    method: request?.method ?? "UNKNOWN",
    url: request?.url ?? response.url,
    // An empty body reaches us as "" because JSON.parse("") throws upstream.
    body: error === "" ? undefined : error,
    headers: response.headers,
    response,
  });
}

/** Longest body excerpt appended to the error message. */
const EXCERPT_MAX_LENGTH = 200;

function formatMessage({
  status,
  statusText,
  method,
  url,
  body,
}: FactorialApiErrorInit): string {
  const head = `Factorial API ${status}${statusText ? ` ${statusText}` : ""}: ${method} ${url}`;
  const excerpt = bodyExcerpt(body);
  return excerpt ? `${head} — ${excerpt}` : head;
}

function bodyExcerpt(body: unknown): string | undefined {
  if (body === undefined || body === null || body === "") return undefined;

  let text: string;
  if (typeof body === "string") {
    text = body;
  } else {
    try {
      text = JSON.stringify(body) ?? String(body);
    } catch {
      // Circular structures and BigInt values make JSON.stringify throw.
      text = String(body);
    }
  }

  const oneLine = text.replace(/\s+/g, " ").trim();
  if (!oneLine) return undefined;
  return oneLine.length > EXCERPT_MAX_LENGTH
    ? `${oneLine.slice(0, EXCERPT_MAX_LENGTH)}…`
    : oneLine;
}
