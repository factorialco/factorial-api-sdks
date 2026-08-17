#!/usr/bin/env python3
"""
Stage-2 generator for factorial_api_client/client.py (the FactorialClient wrapper).

Structure is derived from the REST URL of each generated endpoint
(`/api/<ver>/resources/<namespace>/<resource>/[<id>|<action>]`), which is the
single source of truth shared with the TypeScript generator — so both SDKs
expose the same namespaces, resources and methods, differing only in case
convention (snake_case here, camelCase in TS).

Method naming:
  - collection            GET → list, POST → create
  - by-id (/<id>)         GET → get, PUT → update, DELETE → delete
  - custom action (/foo)  → the action verb, snake_case (e.g. approve_resource,
                            clock_in, bulk_create_update)

Run manually after regenerating factorial_api_client/generated/:
    python python/scripts/generate_python_sdk.py

Also called by scripts/release.py after regenerating the generated/ layer. The
output is fully overwritten — never edit client.py by hand. release.py then
post-patches it for env-var support and raise_on_unexpected_status; this
generator emits the pre-patch form those patches expect.
"""
from __future__ import annotations

import keyword
import re
from pathlib import Path

PYTHON_DIR = Path(__file__).resolve().parent.parent
PKG = "factorial_api_client"
GENERATED_API = PYTHON_DIR / PKG / "generated" / "api"
OUT = PYTHON_DIR / PKG / "client.py"

URL_RE = re.compile(r'"url":\s*"(/api/[^"]+)"')
METHOD_RE = re.compile(r'"method":\s*"(get|post|put|delete)"')

COLLECTION_NAME = {"get": "list", "post": "create", "put": "update", "delete": "delete"}
BY_ID_NAME = {"get": "get", "put": "update", "delete": "delete", "post": "create"}


# ── helpers ────────────────────────────────────────────────────────────────

def pascal(snake: str) -> str:
    return "".join(p[:1].upper() + p[1:] for p in snake.split("_") if p != "")


def parse_url(url: str) -> tuple[str, str, list[str]]:
    """`/api/<ver>/resources/<ns>/<resource>/<rest...>` → (ns, resource, rest)."""
    parts = url.split("/api/", 1)[1].split("/")
    # parts = [version, "resources", ns, resource, *rest]
    ns, resource = parts[2], parts[3]
    return ns, resource, parts[4:]


def parse_sync_params(src: str) -> tuple[list[str], list[str]]:
    """Return (positional_params, keyword_params) of the module's sync()."""
    m = re.search(r"\ndef sync\((.*?)\)\s*->", src, re.S)
    if not m:
        return [], []
    before, sep, after = m.group(1).partition("*,")
    if not sep:
        before, after = m.group(1), ""

    def names(chunk: str) -> list[str]:
        out: list[str] = []
        for raw in chunk.split("\n"):
            line = raw.strip()
            if not line:
                continue
            nm = re.match(r"([A-Za-z_]\w*)\s*[:=,]", line)
            if nm:
                out.append(nm.group(1))
        return out

    return [n for n in names(before) if n != "client"], [n for n in names(after) if n != "client"]


# ── model ──────────────────────────────────────────────────────────────────

class Endpoint:
    def __init__(self, module, verb, rest, positional, keyword):
        self.module = module          # e.g. get_api_2026_04_01_resources_ats_applications
        self.verb = verb              # get | post | put | delete
        self.rest = rest              # url segments after <ns>/<resource>
        self.positional = positional  # path params, passed positionally
        self.keyword = keyword        # query/body params, passed as keywords
        self.method = ""              # assigned later


def collect_resources():
    """(namespace, resource_dir) → {dir, endpoints} grouped by REST namespace/resource."""
    resources: dict[tuple[str, str], dict] = {}
    for d in sorted(p for p in GENERATED_API.iterdir() if p.is_dir() and p.name != "__pycache__"):
        for f in sorted(d.glob("*.py")):
            if f.name == "__init__.py":
                continue
            src = f.read_text()
            url_m = URL_RE.search(src)
            verb_m = METHOD_RE.search(src)
            if not url_m or not verb_m:
                continue
            ns, resource, rest = parse_url(url_m.group(1))
            positional, kw = parse_sync_params(src)
            entry = resources.setdefault((ns, resource), {"dir": d.name, "endpoints": []})
            entry["endpoints"].append(Endpoint(f.stem, verb_m.group(1), rest, positional, kw))
    return resources


def assign_methods(endpoints):
    """Classify each endpoint into a snake_case method name. Returns the list endpoint."""
    list_ep = None
    used: dict[str, int] = {}

    def dedup(name: str) -> str:
        if keyword.iskeyword(name):
            name += "_"
        if name in used:
            used[name] += 1
            return f"{name}_{used[name]}"
        used[name] = 0
        return name

    for e in sorted(endpoints, key=lambda x: x.module):
        if not e.rest:
            name = COLLECTION_NAME[e.verb]
            is_list = e.verb == "get"
        elif e.rest[0].startswith("{"):
            name = BY_ID_NAME[e.verb]
            is_list = False
        else:
            name = e.rest[0]  # action segment, already snake_case
            is_list = False
        e.method = dedup(name)
        if is_list:
            list_ep = e
    return list_ep


# ── code emission ────────────────────────────────────────────────────────────

def call_args(e):
    parts = list(e.positional)
    parts.append("client=self._client")
    parts.extend(f"{k}={k}" for k in e.keyword)
    return ", ".join(parts)


def emit_method(e):
    pos = [f"{p}: Any" for p in e.positional]
    # Default optional (query/body) params to UNSET, not None: the generated
    # endpoints expect the UNSET sentinel for "omitted" and dereference enum
    # values unconditionally (`field_type.value`), so forwarding None crashes
    # before the request is sent. See issue #33.
    kw = [f"{p}: Any = UNSET" for p in e.keyword]
    params = "self, " + ", ".join(pos + kw)
    return [
        f"    def {e.method}({params}) -> Any:",
        f'        """Calls {e.module}."""',
        f"        return {e.module}.sync({call_args(e)})",
        "",
        f"    async def {e.method}_async({params}) -> Any:",
        f'        """Async version of {e.method}."""',
        f"        return await {e.module}.asyncio({call_args(e)})",
        "",
    ]


def emit_pagination(list_ep, taken):
    # See emit_method: optional filters default to UNSET so omitting them does
    # not forward None into the generated endpoint's serializer (issue #33).
    kw = [f"{p}: Any = UNSET" for p in list_ep.keyword]
    sig = (
        "self, *, max_items: int | None = None, limit: int | None = None"
        + "".join(f", {k}" for k in kw)
    )
    kwline = "".join(f", {k}={k}" for k in list_ep.keyword)
    all_name = "collect_all" if "all" in taken else "all"

    def fetcher_call(awaited):
        prefix = "await " if awaited else ""
        fn = "fetch_page_async" if awaited else "fetch_page"
        if list_ep.keyword:
            return [
                f"            return {prefix}{fn}(",
                f"                {list_ep.module},",
                "                self._client,",
                f"                after_id, limit=limit{kwline},",
                "            )",
            ]
        call = f"{fn}({list_ep.module}, self._client, after_id, limit=limit)"
        return [f"            return {prefix}{call}"]

    lines = []
    lines.append(f"    def paginate({sig}) -> Any:")
    lines.append('        """Cursor-paginated iterator over all items."""')
    lines.append("        def fetcher(after_id: str | None) -> Any:")
    lines.extend(fetcher_call(False))
    lines.append("        return paginate(fetcher, max_items=max_items)")
    lines.append("")
    lines.append(f"    def {all_name}({sig}) -> List[Any]:")
    lines.append('        """Collect all pages into a list."""')
    lines.append("        def fetcher(after_id: str | None) -> Any:")
    lines.extend(fetcher_call(False))
    lines.append("        return collect_all(fetcher, max_items=max_items)")
    lines.append("")
    lines.append(f"    async def paginate_async({sig}) -> Any:")
    lines.append('        """Async cursor-paginated iterator."""')
    lines.append("        async def fetcher(after_id: str | None) -> Any:")
    lines.extend(fetcher_call(True))
    lines.append("        return paginate_async(fetcher, max_items=max_items)")
    lines.append("")
    return lines


def class_name(ns, resource):
    return f"{pascal(ns)}{pascal(resource)}Resource"


def main():
    resources = collect_resources()

    # namespace -> { resource -> (dir, endpoints) }, all keyed off the REST URL.
    namespaces: dict[str, dict[str, dict]] = {}
    for (ns, resource), entry in resources.items():
        namespaces.setdefault(ns, {})[resource] = entry

    out = []
    out.append('"""')
    out.append("FactorialClient — high-level wrapper around the auto-generated API client.")
    out.append("")
    out.append(
        "This file is generated by python/scripts/generate_python_sdk.py — do not edit by hand."
    )
    out.append('"""')
    out.append("from __future__ import annotations")
    out.append("")
    out.append("from typing import Any, List")
    out.append("")
    out.append(f"from {PKG}.generated.client import AuthenticatedClient")
    out.append(f"from {PKG}.generated.types import UNSET")
    out.append(
        f"from {PKG}.pagination import ("
        "paginate, paginate_async, collect_all, fetch_page, fetch_page_async)"
    )
    out.append("")

    # Imports, grouped by the generated dir each resource lives in.
    for (ns, resource) in sorted(resources):
        entry = resources[(ns, resource)]
        out.append(f"from {PKG}.generated.api.{entry['dir']} import (")
        for mod in sorted(e.module for e in entry["endpoints"]):
            out.append(f"    {mod},")
        out.append(")")
    out.append("")
    out.append("")

    # Resource classes.
    for (ns, resource) in sorted(resources):
        endpoints = resources[(ns, resource)]["endpoints"]
        list_ep = assign_methods(endpoints)
        out.append(f"class {class_name(ns, resource)}:")
        out.append(f'    """Methods for the {ns} > {resource} resource."""')
        out.append("")
        out.append("    def __init__(self, client: AuthenticatedClient) -> None:")
        out.append("        self._client = client")
        out.append("")
        for e in sorted(endpoints, key=lambda x: x.module):
            out.extend(emit_method(e))
        if list_ep is not None:
            out.extend(emit_pagination(list_ep, {e.method for e in endpoints}))
        out.append("")

    # Namespace classes.
    for ns in sorted(namespaces):
        out.append(f"class {pascal(ns)}Namespace:")
        out.append(f'    """Domain namespace for {ns}."""')
        out.append("")
        out.append("    def __init__(self, client: AuthenticatedClient) -> None:")
        out.append("        self._client = client")
        for resource in sorted(namespaces[ns]):
            out.append(f"        self.{resource} = {class_name(ns, resource)}(client)")
        out.append("")

    # FactorialClient.
    out.append("")
    out.append("class FactorialClient:")
    out.append('    """')
    out.append("    High-level Factorial API client.")
    out.append("")
    out.append("    Usage:")
    out.append('        client = FactorialClient(api_key="YOUR_KEY")')
    out.append("        employees = client.employees.employees.list()")
    out.append("        for emp in client.employees.employees.paginate(max_items=50):")
    out.append("            print(emp)")
    out.append('    """')
    out.append("")
    out.append("    def __init__(")
    out.append("        self,")
    out.append("        *,")
    out.append("        api_key: str | None = None,")
    out.append("        token: str | None = None,")
    out.append('        base_url: str = "https://api.factorialhr.com",')
    out.append("    ) -> None:")
    out.append("        auth_token = api_key or token")
    out.append("        if not auth_token:")
    out.append('            raise ValueError("Provide api_key or token")')
    out.append("        # An api_key travels in x-api-key; a token is an OAuth2 bearer credential.")
    out.append("        auth_header_name, prefix = (")
    out.append('            ("x-api-key", "") if api_key else ("Authorization", "Bearer")')
    out.append("        )")
    out.append("        self._client = AuthenticatedClient(")
    out.append("            base_url=base_url,")
    out.append("            token=auth_token,")
    out.append("            prefix=prefix,")
    out.append("            auth_header_name=auth_header_name,")
    out.append("        )")
    for ns in sorted(namespaces):
        out.append(f"        self.{ns} = {pascal(ns)}Namespace(self._client)")
    out.append("")
    out.append("")

    OUT.write_text("\n".join(out))
    print(f"Wrote {OUT} ({len(out)} lines)")


if __name__ == "__main__":
    main()
