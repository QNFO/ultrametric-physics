# Citation Audit — QNFO.UMP.013 (pattern-particle-unification)

**Date:** 2026-08-19 · **Gate:** P3.AUTHOR-GATE (HARD, v2.49) + P3.SOURCE-DISCIPLINE · **Status:** COMPLETE

## 1. Entry count & composition

**33 entries** in `references.bib`:
- **15 external DOIs** — every entry verified against LIVE Crossref `api.crossref.org/works/<doi>` (author list, title, journal, volume, year, DOI). Evidence: `artifacts/external-search/crossref_verify_<key>.json` (15 files).
- **7 arXiv preprints** — authoritative metadata via `export_citations` (arXiv MCP, deterministic keys, version-preserving): mund2008the, read1992fractional, marcolli2018holographic, chen2021bending, aubert2023bruhattits, neretin2013on, read2008nonabelian.
- **11 internal QNFO records** — concept DOIs where versioned (ZENODO-CONCEPT-DOI-CITE-1 + DQ2 correction; v0.3 refresh per post-publication red-team): QP v2.0 cited by live-verified concept `10.5281/zenodo.21768756`; spin-statistics by concept `21938970` (record 21964598); exchange-phase by concept `21941184`; configuration-space by concept `21945449` (record 21962450); adelic-program by concept `21691414`.

## 2. Verification method per entry (P3.AUTHOR-GATE rules 1-3)

| Class | Method | Rule 1 (authors verified) | Rule 2 (DOI→title match) | Rule 3 (no HTML-redirect claim) |
|---|---|---|---|---|
| External DOIs | Live Crossref GET per DOI | ✓ — authors parsed from `message.author[].given/family` | ✓ — titles compared with fetched metadata | ✓ — constructed from Crossref JSON, not doi.org Accept-header |
| arXiv | export_citations (authoritative arXiv API) | ✓ | ✓ | n/a |
| Internal | Phase 1 `resolve_paper_id` + live Zenodo GET (21784490 → concept 21768756) | ✓ | ✓ | n/a |

**Key corrections made during verification (fabrication-prevention):** 7 provisional bib keys carried WRONG author attributions; all corrected to the Crossref-verified author lists:
- 10.1007/jhep01(2018)139 → Bhattacharyya, Hung, Lei, Li (NOT Heydeman)
- 10.1007/jhep04(2019)170 → Hung, Li, Melby-Thompson (NOT Gubser)
- 10.1007/jhep10(2022)169 → Gesteau, Marcolli, Parikh (NOT Gubser)
- 10.4310/atmp.2021.v25.n3.a2 → Heydeman, Marcolli, Parikh (NOT Melnikov)
- 10.4310/atmp.2017.v21.n7.a3 → Gubser (NOT Denef)
- 10.1088/1751-8121/ab0757 → Gubser, Jepsen, Trundy (key fixed)
- 10.1088/1367-2630/12/6/065010 → Ryu, Schnyder, Furusaki et al. (NOT Chiu)
- lerda1992anyons (was wilczek1992anyons): Crossref chapter record (10.1007/978-3-540-47466-1_8) has no author/editor; parent volume 10.1007/978-3-540-47466-1 = "Anyons" by Alberto Lerda (LNP Monographs 68, 1992) — author corrected to the Crossref-attested volume author in v0.4 (round-3 red-team finding S-5); no fabricated author.

## 3. Duplicate check (P3.AUTHOR-GATE rule 5)

Python `re` scan of `references.bib`: **33 entries, 33 unique keys, 0 duplicates.** Brace balance: `{`==`}` True.

## 4. P3.SOURCE-DISCIPLINE (three-count audit)

- Queries sent this session: 24 (12 corpus formulations + 6 OpenAlex + 4 Crossref + Zenodo ×2 + EuropePMC + arXiv MCP ×3)
- Sources received: 33 verified records
- Sources cited: 33 — **cited == received**, no fabrication window.
- Reliability tiers: primary (live API metadata) for all 33; no tertiary sources cited.

## 5. Gate output

`references.bib` (33 verified entries) + this audit. Zero fabricated entries. All evidence files committed under `artifacts/external-search/crossref_verify_*.json`.
