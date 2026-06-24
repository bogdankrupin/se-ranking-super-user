#!/usr/bin/env python3
"""
Refresh the auto-generated URL index inside references/doc-map.md from the live
SE Ranking API docs sidebar.

It fetches https://seranking.com/api.html, extracts every documentation link from the
left navigation (the API / Data / Project tree), and rewrites ONLY the block between
the AUTO-GENERATED markers. The curated header, disambiguation note, and the
"Quick keyword -> section router" are preserved untouched.

Answer *content* is always read live by the skill at query time; this only keeps the
URL/anchor snapshot current between runs.

Usage:
    python scripts/refresh_doc_map.py            # rewrite the block if it changed
    python scripts/refresh_doc_map.py --check    # exit 1 if out of date (for CI)

Dependencies: requests, beautifulsoup4
    pip install requests beautifulsoup4
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

INDEX_URL = "https://seranking.com/api.html"
DOC_PREFIX = "https://seranking.com/api"
MAP_PATH = Path(__file__).resolve().parent.parent / "references" / "doc-map.md"

START_MARKER = "<!-- AUTO-GENERATED:START"
END_MARKER = "<!-- AUTO-GENERATED:END -->"

DOC_PATH_RE = re.compile(r"^https://seranking\.com/api(/|\.html|$)")

# Navigation/marketing labels that point into /api paths but are not real doc entries.
JUNK_TITLES = {
    "stub", "SEO API", "Sign in", "Start free trial", "Back",
    "Request a demo", "API", "Introduction",
}


def fetch_sidebar_links(html):
    """Return ordered, de-duplicated (title, url) documentation links."""
    soup = BeautifulSoup(html, "html.parser")
    seen = set()
    links = []
    api_html_added = False
    for a in soup.find_all("a", href=True):
        url = urljoin(INDEX_URL, a["href"].strip())
        title = " ".join(a.get_text(" ", strip=True).split())
        if not title or not DOC_PATH_RE.match(url):
            continue
        # Collapse all nav links to the index page into a single clean "Introduction" row.
        if url.rstrip("/") == "https://seranking.com/api.html".rstrip("/"):
            if api_html_added:
                continue
            title = "Introduction"
            api_html_added = True
        elif title in JUNK_TITLES:
            continue
        key = (title, url)
        if key in seen:
            continue
        seen.add(key)
        links.append((title, url))
    return links


def bucket(url):
    if url.startswith(DOC_PREFIX + "/data/"):
        return "Data API"
    if url.startswith(DOC_PREFIX + "/project/"):
        return "Project API"
    return "API (general)"


def subsection(url):
    m = re.match(r"https://seranking\.com/api/(?:data|project)/([^/#]+)", url)
    if m:
        return m.group(1)
    m = re.match(r"https://seranking\.com/api/([^/#]+)", url)
    if m:
        return m.group(1)
    return "introduction"


def build_block(links):
    """Render only the auto-generated section (between the markers)."""
    order = ["API (general)", "Data API", "Project API"]
    grouped = {area: [] for area in order}
    for title, url in links:
        grouped[bucket(url)].append((title, url))

    out = [
        START_MARKER + " -- rewritten by scripts/refresh_doc_map.py on "
        + date.today().isoformat() + ". Do not edit by hand. -->",
        "",
    ]
    for i, area in enumerate(order, 1):
        rows = grouped[area]
        if not rows:
            continue
        out.append("## " + str(i) + ". " + area + "\n")
        current_sub = None
        for title, url in rows:
            sub = subsection(url)
            if sub != current_sub:
                if current_sub is not None:
                    out.append("")
                out.append("### " + sub + "\n")
                out.append("| Topic | URL |")
                out.append("|---|---|")
                current_sub = sub
            safe = title.replace("|", "\\|")
            out.append("| " + safe + " | " + url + " |")
        out.append("")
    out.append(END_MARKER)
    return "\n".join(out)


def splice(existing, new_block):
    start = existing.find(START_MARKER)
    end = existing.find(END_MARKER)
    if start == -1 or end == -1:
        raise SystemExit(
            "Could not find AUTO-GENERATED markers in doc-map.md. "
            "Add them back before running this script."
        )
    end += len(END_MARKER)
    return existing[:start] + new_block + existing[end:]


def strip_date(s):
    return re.sub(r"on \d{4}-\d{2}-\d{2}\.", "on DATE.", s)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 if the map block is out of date (for CI).")
    args = parser.parse_args()

    resp = requests.get(INDEX_URL, timeout=30, headers={
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml",
    })
    resp.raise_for_status()

    links = fetch_sidebar_links(resp.text)
    if len(links) < 50:
        print("Only " + str(len(links)) + " doc links found -- page structure may have changed. Aborting.")
        sys.exit(2)

    existing = MAP_PATH.read_text(encoding="utf-8")
    new_block = build_block(links)
    updated = splice(existing, new_block)

    changed = strip_date(updated) != strip_date(existing)

    if args.check:
        if changed:
            print("doc-map.md is out of date. Run scripts/refresh_doc_map.py.")
            sys.exit(1)
        print("doc-map.md is up to date.")
        return

    if changed:
        MAP_PATH.write_text(updated, encoding="utf-8")
        print("Updated doc-map.md (" + str(len(links)) + " links).")
    else:
        print("No structural changes -- doc-map.md already current.")


if __name__ == "__main__":
    main()
