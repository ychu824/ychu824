#!/usr/bin/env python3
"""Regenerate the categorized SGLang-Omni / vLLM-Omni PR list in README.md.

Run daily by .github/workflows/sync-prs.yml; needs GH_TOKEN for the search API.
"""
import json, os, re, sys, urllib.parse, urllib.request

USER = "ychu824"
SGL, VLLM = "sgl-project/sglang-omni", "vllm-project/vllm-omni"
REPOS = {SGL: "SGLang-Omni", VLLM: "vLLM-Omni"}
TOKEN = os.environ.get("GH_TOKEN", "")

# Category from a title's leading [Tag]s (first match wins); unmatched -> OTHER.
CATEGORIES = [
    ("Performance", {"perf"}),
    ("Serving & realtime", {"realtime", "serving", "scheduler"}),
    ("Correctness", {"bugfix", "fix", "bug"}),
    ("Benchmarks & CI", {"benchmark", "ci/build", "ci", "test"}),
]
OTHER = "Other"
# Tags that are neither a category nor a model name.
IGNORE_TAGS = {"docs", "doc", "feature", "feat", "misc", "model", "frontend", "wip", "rfc", "refactor", "core"}
# Display names for model tags.
MODEL_ALIASES = {"fun-cosyvoice3": "CosyVoice3"}

# Per-PR tweaks, keyed by (repo, number).
EXCLUDE = {(SGL, 2261)}
OVERRIDES = {
    (SGL, 2626): "Correctness",   # restores repetition-aware sampling on CUDA
    (SGL, 2299): "Correctness",   # generation-length contract in the adapter
    (VLLM, 9632): "Performance",  # removes duplicate reference conditioning
}
TITLE_OVERRIDES = {
    (SGL, 3038): "Retry in-session admission rejections in the duplex recorder",
}
ORDER = [c for c, _ in CATEGORIES] + [OTHER]
assert all(v in ORDER for v in OVERRIDES.values()), "unknown category in OVERRIDES"


def search(q):
    items, page = [], 1
    while True:
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
            {"q": q, "sort": "created", "order": "desc", "per_page": 100, "page": page})
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        if data.get("incomplete_results"):
            sys.exit("search returned incomplete results; leaving README unchanged")
        items += data["items"]
        if len(items) >= min(data["total_count"], 1000) or not data["items"]:
            return items
        page += 1


def key(i):
    return i["repository_url"].split("/repos/", 1)[1], i["number"]


def split_title(title):
    m = re.match(r"\s*((?:\[[^\[\]]*\]\s*)+)", title)
    if not m:
        return [], title.strip()
    tags = re.findall(r"\[([^\[\]]*)\]", m.group(1))
    return tags, title[m.end():].strip() or title.strip()


def esc(text):
    return re.sub(r"([\\`*_\[\]<>|])", r"\\\1", text)


known = set().union(*(k for _, k in CATEGORIES))
q = f"author:{USER} type:pr is:merged " + " ".join(f"repo:{r}" for r in REPOS)
merged = [i for i in search(q) if key(i) not in EXCLUDE]
if not merged:
    sys.exit("no PRs found; leaving README unchanged")
merged.sort(key=lambda i: i["pull_request"]["merged_at"] or "", reverse=True)

groups = {}
for i in merged:
    k = key(i)
    tags, rest = split_title(i["title"])
    low = {t.lower() for t in tags}
    cat = OVERRIDES.get(k) or next((c for c, keys in CATEGORIES if low & keys), OTHER)
    models = [MODEL_ALIASES.get(t.lower(), t) for t in tags if t.lower() not in known | IGNORE_TAGS]
    meta = " · ".join([REPOS[k[0]]] + models)
    title = TITLE_OVERRIDES.get(k, rest)
    groups.setdefault(cat, []).append(f"- [{esc(title)}]({i['html_url']}) <sub>{esc(meta)}</sub>")

parts = [f"**{c}**\n\n" + "\n".join(groups[c]) for c in ORDER if c in groups]
new = "<!-- PRS:START -->\n" + "\n\n".join(parts) + "\n<!-- PRS:END -->"

readme = open("README.md", encoding="utf-8").read()
readme, n = re.subn(r"<!-- PRS:START -->.*?<!-- PRS:END -->", lambda _: new, readme, flags=re.S)
if n != 1:
    sys.exit("PRS marker not found")
readme, n = re.subn(r"<sub>\d+ merged PRs</sub>", f"<sub>{len(merged)} merged PRs</sub>", readme, count=1)
if n != 1:
    sys.exit("counter not found")
open("README.md", "w", encoding="utf-8").write(readme)
print(f"merged={len(merged)} " + " ".join(f"{c}={len(groups[c])}" for c in ORDER if c in groups))
