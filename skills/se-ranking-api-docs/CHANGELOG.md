# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-06-19

First public release of the SE Ranking API & MCP documentation skill for Claude.

Ask Claude anything about the SE Ranking API or MCP and get a concise answer grounded in
a verbatim citation to the exact official documentation section.

### Added
- Answers questions across the **Data API**, **Project API**, and **MCP server**, with
  built-in disambiguation between layers that share concepts (Website Audit, backlinks,
  AI visibility).
- Every answer ends with a `Source:` link copied verbatim from the documentation map.
- Reads documentation **content live** at query time, so answers reflect the current docs.
- **Self-healing citations:** if a topic is missing from the map or a URL 404s, the skill
  falls back to the live `api.html` sidebar.
- `references/doc-map.md` — curated citation index covering the full API/Data/Project
  documentation tree, with a keyword → section router and layer disambiguation note.
- `scripts/refresh_doc_map.py` — regenerates the URL/anchor index from the live sidebar,
  rewriting only the block between the `AUTO-GENERATED` markers and preserving the
  curated router. Includes a `--check` mode for CI.
- `.github/workflows/refresh-doc-map.yml` — GitHub Action that refreshes the map weekly
  (and on demand) and commits any changes.

[Unreleased]: https://github.com/bogdankrupin/se-ranking-api-docs/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/bogdankrupin/se-ranking-api-docs/releases/tag/v1.0.0
