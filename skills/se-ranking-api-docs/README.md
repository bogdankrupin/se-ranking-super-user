# se-ranking-api-docs — Claude Skill

A Claude Agent Skill that answers questions about the **SE Ranking API** (Data API and
Project API) and the **SE Ranking MCP server**, and grounds every answer in the official
documentation with a direct, verbatim citation to the relevant section of
[seranking.com/api.html](https://seranking.com/api.html).

Ask Claude something like *"which endpoint returns referring domains?"* or *"why am I
getting a 429?"* and it replies with a concise answer plus a `Source:` link to the exact
docs section.

## How it works

1. **Classify** the question → Data API / Project API / MCP (with disambiguation, since
   several concepts exist in both layers).
2. **Locate** the section in `references/doc-map.md` (the citation index).
3. **Fetch** the live documentation page so the answer reflects the current docs, not
   stale memory.
4. **Answer, then cite** the exact official URL verbatim.

Content is always read live. The structure (URLs + anchors) is a snapshot that
self-heals: if a topic is missing or a URL 404s, the skill falls back to the live
`api.html` sidebar.

## Layout

```
se-ranking-api-docs/
├── SKILL.md                       # behavior: answer-and-cite workflow
├── references/
│   └── doc-map.md                 # citation index (auto-block + curated router)
├── scripts/
│   ├── refresh_doc_map.py         # regenerate the URL index from the live sidebar
│   └── requirements.txt
└── .github/workflows/
    └── refresh-doc-map.yml         # weekly auto-refresh + commit
```

## Keeping the map current

The block between the `AUTO-GENERATED` markers in `references/doc-map.md` is rebuilt from
the live sidebar; the curated disambiguation note and keyword router are preserved.

```bash
pip install -r scripts/requirements.txt
python scripts/refresh_doc_map.py          # update if structure changed
python scripts/refresh_doc_map.py --check  # CI: exit 1 if out of date
```

The included GitHub Action runs this weekly (and on demand) and commits any changes.
Enable **Settings → Actions → General → Workflow permissions → Read and write** so the
bot can push.

## Install as a skill

Upload the folder (or the packaged `.skill` file) wherever you load Claude skills.
