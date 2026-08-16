# Citation Audit — Non-Archimedean Projective Perspective v0.2

**Date:** 2026-08-16 · **Method:** field-level live verification per P3.AUTHOR-GATE — Zenodo records API (refs 1–5, author + title + concept ID), arXiv export API (refs 6–11, full author list + title), Crossref (ref 12, Monna 1952). This script (`citation-field-verify.py`) is deposited and re-runnable.

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
| 12 | Crossref | 10.1016/s1385-7258(52)50001-5 | 200 | PASS | PASS | n/a | PASS |

**Totals:** 12/12 PASS field-level · 0 FAIL · 0 fabricated entries · 0 duplicate keys.

**Concept-DOI discipline (ZENODO-CONCEPT-DOI-CITE-1):** a Zenodo entry cites the concept DOI when the API reports conceptrecid == requested id.

**P3.SOURCE-DISCIPLINE:** every external source was returned by this session's arXiv/Crossref tool calls (evidence: artifacts/external-search/); no training-recalled citation appears without a live check.

**v0.2:** ref 12 (Monna 1952, DESIGN-1 precedence) added and field-verified; inline refs 1–5 authors corrected to match live records (SOFT-3).
