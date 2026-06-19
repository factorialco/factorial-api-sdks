<!-- Vendored from https://apidoc.factorialhr.com/docs/pagination.md -->

# Pagination

This page contains information about how pagination works in Factorial's API

> 📘 Pagination default is set to 100 items
>
> It is important to note that pagination is applied by default for every request, with a set limit of 100 items per request when no pagination limit parameter is present. This limit of 100 is also the max limit per request.

## Cursor Pagination

This is the default pagination type for our API. This type of pagination moves to and from a page via the use of a cursor. The following terms are worthy of note:

* **limit**: This is the page limit or page size.  It's equivalent to saying "Fetch me only \{\{limit}} items". It is of type `Integer`. If it is above the max limit or absent, we would default to using the max limit.
* **after\_id**: This is the id that serves as the pointer for a request. Only items after this `id` would be fetched.
* **before\_id**: This is also an id that serves as the pointer for a request. Only items before this `id` would be fetched.

The sorting is by **ID in ascending** order.

A typical cursor pagination request would look something like this

```
GET `.../users?limit=10&after_id=MTY=
```

The query result would have meta information required to make subsequent requests:

```
{
  "meta": {
        "has_next_page": true,
        "has_previous_page": false,
        "start_cursor":"MTc=",
        "end_cursor":"Mjc="
        "total": 85,
        "limit": 10
    },
  "data": [...]
}

```

You can choose to go either forward or backward on a page, by indicating an `after_id` or  a `before_id`. The first request, however, just requires the`limit` (ie. how many items you intend to fetch).

<br />
