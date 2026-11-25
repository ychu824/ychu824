#!/usr/bin/env python3
"""Regenerate the merged/open upstream PR lists in README.md from the GitHub search API.

Upstream = PRs authored by USER in repositories USER doesn't own.
Run by .github/workflows/sync-prs.yml; needs GH_TOKEN for the search API.
"""
import json, os, re, sys, urllib.parse, urllib.request

USER = os.environ.get("PROFILE_USER", "ychu824")
TOKEN = os.environ.get("GH_TOKEN", "")


def search(q):
    items, page = [], 1
    while True:
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
            {"q": q, "sort": "created", "order": "desc", "per_page": 100, "page": page})
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
        with urllib.request.urlopen(req) as r:
            data = json.load(r)
        items += data["items"]
        if len(items) >= data["total_count"] or not data["items"]:
            return items
        page += 1


def repo(i):
    return i["repository_url"].split("/repos/", 1)[1]


def esc(t):
    return t.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def block(name, summary, rows, header):
    body = "\n".join([header, header_sep(header)] + rows) if rows else "_None right now._"
    return (f"<!-- {name}:START -->\n<details>\n<summary>{summary}</summary>\n\n"
            f"{body}\n\n</details>\n<!-- {name}:END -->")


def header_sep(header):
    return "|" + "---|" * (header.count("|") - 1)


merged = search(f"author:{USER} type:pr is:merged -user:{USER}")
merged.sort(key=lambda i: i["pull_request"]["merged_at"] or "", reverse=True)
open_ = search(f"author:{USER} type:pr is:open -user:{USER}")

m_rows = [f"| `{repo(i)}` | [{esc(i['title'])}]({i['html_url']}) | {i['pull_request']['merged_at'][:10]} |" for i in merged]
o_rows = [f"| `{repo(i)}` | [{esc(i['title'])}]({i['html_url']}) | {'draft' if i.get('draft') else 'in review'} |" for i in open_]

readme = open("README.md", encoding="utf-8").read()
for name, summary, rows, header in [
    ("MERGED", f"All merged upstream PRs ({len(merged)})", m_rows, "| Repo | PR | Merged |"),
    ("OPEN", f"Open PRs · in review and work in progress ({len(open_)})", o_rows, "| Repo | PR | Status |"),
]:
    new = block(name, summary, rows, header)
    readme, n = re.subn(rf"<!-- {name}:START -->.*?<!-- {name}:END -->", lambda _: new, readme, flags=re.S)
    if n != 1:
        sys.exit(f"marker {name} not found")

open("README.md", "w", encoding="utf-8").write(readme)
print(f"merged={len(merged)} open={len(open_)}")
