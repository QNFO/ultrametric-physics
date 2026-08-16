# Citation Audit — Non-Archimedean Projective Perspective v0.1

**Date:** 2026-08-16 · **Method:** field-level live verification per P3.AUTHOR-GATE — Zenodo records API (refs 1–5, author + title + concept ID) and arXiv export API (refs 6–11, full author list + title), same session as the deposit.

| # | Source | Identifier | HTTP | Author match | Title match | ID kind | Verdict |
|:--|:-------|:-----------|:-----|:-------------|:------------|:--------|:--------|
| 1 | Zenodo | 10.5281/zenodo.19040000 | 200 | PASS | PASS | record | PASS |
| 2 | Zenodo | 10.5281/zenodo.19925320 | 200 | PASS | PASS | record | PASS |
| 3 | Zenodo | 10.5281/zenodo.19884971 | 200 | PASS | PASS | record | PASS |
| 4 | Zenodo | 10.5281/zenodo.21473899 | 200 | PASS | PASS | record | PASS |
| 5 | Zenodo | 10.5281/zenodo.19438889 | 200 | PASS | PASS | record | PASS |
| 6 | arXiv | hep-th/0312046 | 200 | PASS | PASS | n/a | PASS |
| 7 | arXiv | 2312.02744 | 200 | PASS | PASS | n/a | PASS |
| 8 | arXiv | 2410.13048 | 200 | PASS | PASS | n/a | PASS |
| 9 | arXiv | 2406.13255 | 200 | PASS | PASS | n/a | PASS |
| 10 | arXiv | hep-th/9410058 | 200 | PASS | PASS | n/a | PASS |
| 11 | arXiv | hep-th/9506097 | 200 | PASS | PASS | n/a | PASS |

**Totals:** 11/11 PASS field-level · 0 FAIL · 0 fabricated entries · 0 duplicate keys.

**Concept-DOI discipline (ZENODO-CONCEPT-DOI-CITE-1 + red-team 2026-08-16):** a Zenodo entry cites the concept DOI when the API reports conceptrecid == requested id (refs 1–5 checked individually).

**P3.SOURCE-DISCIPLINE:** every external source was returned by this session's arXiv tool calls (evidence: artifacts/external-search/arxiv-evidence.json); no training-recalled citation appears without a live check.
