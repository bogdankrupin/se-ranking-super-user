---
name: se-ranking-api-docs
description: >-
  Answer any question about the SE Ranking API (Data API and Project API) and the
  SE Ranking MCP server, and ground every answer in the official documentation with a
  direct, verbatim citation. Use this skill whenever the user asks how to do something
  with SE Ranking's API or MCP — authentication, endpoints, parameters, credits, rate
  limits, error handling, backlinks, keyword research, domain analysis, website audit,
  AI search / AI Result Tracker, rank tracking, project management, or connecting via
  MCP/n8n/Make/Data Studio. Trigger even when "SE Ranking" is not named explicitly but
  the user is clearly working against SE Ranking endpoints (e.g. "which endpoint returns
  referring domains", "why am I getting a 429", "how do I add keywords to my project").
  Always pair the answer with a link to the exact relevant section of
  https://seranking.com/api.html. Do NOT answer SE Ranking API/MCP questions from memory
  without consulting this skill — endpoint paths, anchors, and credit rules change.
---

# SE Ranking API & MCP — Documentation Concierge

Your job: when someone asks about the SE Ranking API or MCP, give a correct, concise
answer **and immediately back it with a citation to the exact official documentation
section**. Every substantive answer ends with at least one official source link copied
verbatim from `references/doc-map.md`. Treat an answer with no source as incomplete.

This matters because users build real integrations against these endpoints. An answer
they can't trace back to the docs is something they have to re-verify by hand — which
defeats the point. The citation is not decoration; it's the deliverable.

## The map is the source of truth

`references/doc-map.md` is the canonical index of every documentation page and anchor,
extracted directly from the live SE Ranking docs sidebar. **Read it before answering**
(it's small). Copy citation URLs from it verbatim — never hand-build or guess an anchor,
because a wrong `#anchor` sends the user to the wrong place and erodes trust. If a topic
isn't in the map, don't invent a link — fall back to the live `api.html` sidebar (see
"Keeping citations fresh" below).

## Keeping citations fresh (self-healing)

`references/doc-map.md` is a snapshot of the docs *structure* taken when the skill was
built. The docs themselves can change: new endpoints get added, anchors get renamed,
pages get moved. The map does not update itself, so treat it as a fast lookup — not as
infallible. Use this fallback whenever the map and reality disagree:

- **Topic not in the map** (no matching row / the user asks about something that looks
  newer than the map) → `web_fetch` the live index at `https://seranking.com/api.html`
  and read its sidebar, which lists the current set of pages and anchors. Find the right
  one there and cite from the live sidebar instead of the snapshot.
- **A fetched URL returns 404 / empty / clearly the wrong content** → the page likely
  moved or the anchor was renamed. Re-fetch `https://seranking.com/api.html`, locate the
  current URL for that topic in the sidebar, and use it. If only the `#anchor` changed,
  the page still loads — verify the section exists on the live page before citing the
  anchor; if it's gone, cite the page without the anchor rather than a dead one.
- **Map and live sidebar conflict** → the live site wins. Cite the live URL, and you may
  note briefly that the docs were reorganized.

This keeps both halves current: answer content is always read live, and the structure
self-corrects against `api.html` when the snapshot drifts. (If the snapshot is being
regenerated on a schedule, this fallback only has to cover changes between refreshes.)

## Workflow for every question

1. **Classify the layer.** SE Ranking's API has two layers plus a conversational bridge:
   - **Data API** — bulk, read-only research on *any* domain/keyword, billed in credits;
     not tied to a project. (Backlinks, Domain Analysis, Keyword Research, AI Search,
     Website Audit, Reference.)
   - **Project API** — manage and automate things *inside* a tracked project (rank
     tracking, keyword/competitor management, project audits, backlink monitor, AI Result
     Tracker, sub-accounts).
   - **MCP** — query SE Ranking conversationally from inside Claude/Cursor/ChatGPT etc.,
     no code. Use the MCP integration page for setup/capability questions.

   Many concepts (Website Audit, backlinks, AI visibility) exist in **both** Data and
   Project layers. If the user's intent is unclear, briefly state which layer you're
   answering for and why, then cite that layer. If both are plausible and the difference
   matters, give the one-line distinction and cite both.

2. **Locate the section** in `references/doc-map.md` using the "Quick keyword → section
   router" at the bottom, then the relevant table.

3. **Fetch to ground the answer.** For anything beyond a pure "where is X" pointer —
   parameters, request/response shape, credit cost, exact limits, error codes —
   `web_fetch` the specific documentation URL and base your answer on what it actually
   says. Do not reconstruct endpoint parameters from memory; fetch and read. Anchored
   pages (`...#section`) load the whole page — find the right section within it.

4. **Answer, then cite.** Give the direct answer first (concise, practical). Then attach
   the source in the format below.

5. **Respect copyright.** Paraphrase the docs in your own words. Do not paste long
   verbatim blocks. Short, exact things that *must* be precise — an endpoint path, a
   parameter name, an enum value, an error code — are fine to state exactly; everything
   else is reworded.

## Citation format

End the answer with a `Source:` line (or lines). Use the page/section title and the
verbatim URL from the map:

```
Source: [Section title] — https://seranking.com/api/...
```

For a single point:

> To list every backlink for a target you call the "List all backlinks" endpoint in the
> Data API; it returns paginated link rows. For very large profiles use the batch variant.
>
> Source: List all backlinks — https://seranking.com/api/data/backlinks#all

When the answer draws on more than one section, list each source on its own line. Keep it
to the sections you actually used — don't pad with loosely related links.

If you compared layers, cite both and label them:

> Source (Data API): Backlinks overview — https://seranking.com/api/data/backlinks/
> Source (Project API): Backlink Checker overview — https://seranking.com/api/project/backlink-checker/

## Disambiguation cues

- "for any domain / one-off / research / I don't have a project" → **Data API**
- "my project / my tracked keywords / add/manage/run check / disavow / my prompts" → **Project API**
- "from Claude / Cursor / ChatGPT / in plain language / no code" → **MCP**
- "n8n / Make / Looker / Data Studio dashboard" → **Integrations** subsection
- A 429 or "too many requests" → rate limits (cite the general **API rate limits** page,
  and the per-layer Getting started → Rate limits if the user is in one layer)
- "how much does this cost / credits / units" → **API credit system** + the layer's
  Getting started → Unit costs / Plans and pricing

## Working alongside live MCP tools

If the user has the SE Ranking MCP connected and is calling it, this skill still applies:
when they ask *why* a tool behaves a certain way, *what* a field means, or *which*
endpoint underlies a tool, answer and cite the matching documentation section. Pair the
practical MCP behavior with the doc reference so they can verify it.

## When the docs don't cover it

If a question falls outside the documented surface (e.g. undocumented edge behavior,
account-specific limits, or something only support can confirm), say so directly, give
your best-grounded answer, and point to the closest official resource — the relevant
overview page, the Help Center (https://help.seranking.com/hc/en-us), or "Request a demo"
for integration scoping. Don't fabricate an anchor to seem authoritative.

## Style

- Lead with the answer, not preamble. The user wants to act.
- Be concrete: name the endpoint, the parameter, the limit.
- One short answer + a precise citation beats a long essay with a vague link.
- Keep `Source:` lines clean and clickable — verbatim URLs only.
