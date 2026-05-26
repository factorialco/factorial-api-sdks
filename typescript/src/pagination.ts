/**
 * Pagination utilities for the Factorial API.
 *
 * The Factorial API uses cursor-based pagination. Every list endpoint returns:
 *   { data: T[], meta: PagedMeta }
 *
 * To fetch the next page, pass `after_id` equal to the `end_cursor` from the
 * previous response's `meta`. The maximum page size is 100 (the default).
 */

/** Pagination metadata returned by every list endpoint. */
export type PagedMeta = {
  /** Cursor pointing to the first item in the current page. */
  start_cursor?: string;
  /** Cursor pointing to the last item in the current page. Pass as `after_id` to fetch the next page. */
  end_cursor?: string;
  /** Whether there is a previous page. */
  has_previous_page: boolean;
  /** Whether there is a next page. */
  has_next_page: boolean;
  /** Number of items in the current page. */
  limit: number;
  /** Total number of items across all pages. */
  total: number;
};

/** Shape of a paged API response. */
export type PagedResponse<T> = {
  data?: T[];
  meta?: PagedMeta;
};

/** Options for pagination helpers. */
export type PaginateOptions = {
  /**
   * Maximum number of items to fetch in total across all pages.
   * Useful as a safety cap when consuming large datasets.
   * Defaults to no limit.
   */
  maxItems?: number;
  /**
   * Number of items per page (max 100, Factorial default is 100).
   */
  limit?: number;
};

/** Parameters passed to the underlying fetcher on each page request. */
type FetchParams = {
  limit?: number;
  after_id?: string;
};

/**
 * Async generator that auto-paginates through all pages of a list endpoint,
 * yielding one item at a time.
 *
 * @param fetcher - A function that accepts pagination params and returns a paged response.
 * @param options - Optional limit and maxItems cap.
 *
 * @example
 * ```ts
 * // Used internally by resource classes — prefer client.employees.employees.paginate()
 * for await (const employee of client.employees.employees.paginate()) {
 *   console.log(employee.full_name);
 * }
 * ```
 */
export async function* paginate<T>(
  fetcher: (params: FetchParams) => Promise<{ data: PagedResponse<T> | undefined; error: unknown }>,
  options: PaginateOptions = {},
): AsyncGenerator<T> {
  const { maxItems, limit } = options;
  let afterId: string | undefined;
  let totalYielded = 0;

  while (true) {
    const params: FetchParams = {};
    if (limit !== undefined) params.limit = limit;
    if (afterId !== undefined) params.after_id = afterId;

    const response = await fetcher(params);

    if (response.error) {
      throw response.error;
    }

    const paged = response.data;
    if (!paged || !paged.data?.length) break;

    for (const item of paged.data) {
      yield item;
      totalYielded++;
      if (maxItems !== undefined && totalYielded >= maxItems) return;
    }

    if (!paged.meta?.has_next_page || !paged.meta?.end_cursor) break;

    afterId = paged.meta.end_cursor;
  }
}

/**
 * Collects all items from an async generator into a plain array.
 *
 * @example
 * ```ts
 * // Used internally by resource classes — prefer client.employees.employees.all()
 * const employees = await client.employees.employees.all({ maxItems: 500 });
 * ```
 */
export async function collectAll<T>(generator: AsyncGenerator<T>): Promise<T[]> {
  const results: T[] = [];
  for await (const item of generator) {
    results.push(item);
  }
  return results;
}
