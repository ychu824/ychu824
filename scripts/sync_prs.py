#!/usr/bin/env python3
"""Regenerate the categorized SGLang-Omni / vLLM-Omni PR list in README.md.

Run daily by .github/workflows/sync-prs.yml; needs GH_TOKEN for the search API.
"""
import json, os, re, sys, urllib.parse, urllib.request

USER = "ychu824"
REPOS = ["sgl-project/sglang-omni", "vllm-project/vllm-omni"]
TOKEN = os.environ.get("GH_TOKEN", "")

# Category, matched against the leading [Tag]s of a PR title (first match wins).
CATEGORIES = [
    ("Performance", {"perf"}),
    ("Serving & realtime", {"realtime", "serving", "scheduler"}),
    ("Correctness", {"bugfix", "fix"}),
    ("Benchmarks & CI", {"benchmark", "ci/build", "ci", "test"}),
]
OTHER = "Models & sampling"
# Per-PR overrides when the title tag doesn't tell the story: {number: category}
OVERRIDES = {}
# PRs left off the profile.
EXCLUDE = {2261}


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


def split_title(title):
    tags = re.findall(r"^\s*((?:\[[^\]]+\]\s*)+)", title)
    tags = re.findall(r"\[([^\]]+)\]", tags[0]) if tags else []
    rest = re.sub(r"^\s*(?:\[[^\]]+\]\s*)+", "", title).strip()
    return tags, rest


def category(i, tags):
    if i["number"] in OVERRIDES:
        return OVERRIDES[i["number"]]
    low = {t.lower() for t in tags}
    for name, keys in CATEGORIES:
        if low & keys:
            return name
    return OTHER


def line(i, tags):
    _, rest = split_title(i["title"])
    known = set().union(*(k for _, k in CATEGORIES))
    models = [t for t in tags if t.lower() not in known]
    repo = "SGLang-Omni" if "sglang" in i["repository_url"] else "vLLM-Omni"
    model = f" · {', '.join(models)}" if models else ""
    rest = rest.replace("|", "\\|")
    return f"- [{rest}]({i['html_url']}) <sub>{repo}{model}</sub>"


q = f"author:{USER} type:pr is:merged " + " ".join(f"repo:{r}" for r in REPOS)
merged = sorted((i for i in search(q) if i["number"] not in EXCLUDE), key=lambda i: i["pull_request"]["merged_at"] or "", reverse=True)

groups = {}
for i in merged:
    tags, _ = split_title(i["title"])
    groups.setdefault(category(i, tags), []).append(line(i, tags))

order = [c for c, _ in CATEGORIES] + [OTHER]
parts = [f"**{c}**\n\n" + "\n".join(groups[c]) for c in order if c in groups]
new = "<!-- PRS:START -->\n" + "\n\n".join(parts) + "\n<!-- PRS:END -->"

readme = open("README.md", encoding="utf-8").read()
readme, n = re.subn(r"<!-- PRS:START -->.*?<!-- PRS:END -->", lambda _: new, readme, flags=re.S)
if n != 1:
    sys.exit("PRS marker not found")
readme = re.sub(r"merged PRs: \d+", f"merged PRs: {len(merged)}", readme)
open("README.md", "w", encoding="utf-8").write(readme)
print(f"merged={len(merged)} " + " ".join(f"{c}={len(v)}" for c, v in groups.items()))
