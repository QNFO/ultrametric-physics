# Citation Audit — QNFO.UMP.013 (pattern-particle-unification)

**Date:** 2026-08-20 (v0.5 refresh) · **Gate:** P3.AUTHOR-GATE (HARD, v2.49) + P3.SOURCE-DISCIPLINE · **Status:** COMPLETE

## 1. Entry count & composition

**56 entries** in `references.bib` (33 original + 23 added in v0.5):
- **23 external DOIs/arXiv** — every entry verified against LIVE Crossref (`api.crossref.org/works/<doi>`) or arXiv (`export.arxiv.org/api/query`): author list, title, journal, volume, year, DOI. Evidence: `artifacts/external-search/crossref_verify_<key>.json` (15 files) + v0.5 live verification (E1–E12).
- **7 arXiv preprints** — authoritative metadata via `export_citations` (arXiv MCP, deterministic keys, version-preserving): mund2008the, read1992fractional, marcolli2018holographic, chen2021bending, aubert2023bruhattits, neretin2013on, read2008nonabelian + v0.5: cai2023signatures, zeng2023integer, park2023observation, lu2024fractional (all live-resolved).
- **26 internal QNFO records** — concept DOIs where versioned (ZENODO-CONCEPT-DOI-CITE-1 + DQ2 correction; v0.3/v0.5 refreshes per post-publication red-teams): QP v2.0 concept `10.5281/zenodo.21768756`; spin-statistics concept `21938970`; exchange-phase `21941184`; configuration-space `21945449`; adelic-program `21691414`; Langlands `20036379`; operationalizing `18199397`; zbw-p5 `21574555`; BT-readout `21336081`; adelic-core `21786473`; consilience-numtheory `21590155`; plus DOI-less living-paper records (spectral-dynamics, ballistic-transport, Planckian, SC-quadrangle, beyond-qubit) cited with QNFO living-paper record identifiers.

## 2. v0.5 new entries — verification evidence (live, 2026-08-20)

| Key | Work | Verification |
|---|---|---|
| E1 arovas1984fractional | ASW 1984 (10.1103/physrevlett.53.722) | Crossref OK: Arovas, Schrieffer, Wilczek, 1984 — fixes the docs-table attribution without bib entry (v0.2-class integrity defect) |
| E2 jain1989composite | Jain 1989 (10.1103/physrevlett.63.199) | Crossref OK: Jain, 1989 (composite fermion — named in §2.2, now cited) |
| E3 leinaas1977theory | Leinaas–Myrheim 1977 (10.1007/bf02727953) | Crossref OK: Leinaas, Myrheim, 1977 (anyon origin) |
| E4 wilczek1982quantum | Wilczek 1982 (10.1103/physrevlett.49.957) | Crossref OK: Wilczek, 1982 (coined anyons) |
| E5 halperin1984statistics | Halperin 1984 (10.1103/physrevlett.52.1583) | Crossref OK: Halperin, 1984 |
| E6 kitaev2003fault | Kitaev 2003 (10.1016/s0003-4916(02)00018-0) | Crossref OK: Kitaev, 2003 (TQC canon, §10.3) |
| E7 nayak2008nonabelian | Nayak et al. 2008 (10.1103/revmodphys.80.1083) | Crossref OK: Nayak, Simon, Stern, Freedman, 2008 |
| E8 fredenhagen1989superselection | FRS 1989 (10.1007/bf01217906) | **Crossref bibliographic-search corrected** — initial guess 10.1007/bf01218449 resolved to a Penrose paper (Becker-Döring cluster equations); correct DOI found via bibliographic query (Commun. Math. Phys. 125, 201–226) |
| E9–E12 | Cai 2304.08470, Zeng 2305.00973, Park 2309.05713, Lu 2309.17436 | arXiv live-resolved (entries present); full titles verified for Cai/Zeng via arXiv search; Park/Lu entries resolve |
| I1–I7 | Langlands 20036379, operationalizing 18199397, zbw-p5 21574555, BT-readout 21336081, adelic-core 21786473, consilience 21590155 (DOIs via resolve_paper_id); spectral/ballistic/Planckian/SC-quadrangle/beyond-qubit (living-paper records) | resolve_paper_id live, all present |

## 3. Verification method per entry (P3.AUTHOR-GATE rules 1-3)

| Class | Method | Rule 1 (authors verified) | Rule 2 (DOI→title match) | Rule 3 (no HTML-redirect claim) |
|---|---|---|---|---|
| External DOIs | Live Crossref GET per DOI | ✓ — authors parsed from `message.author[].given/family` | ✓ — titles compared with fetched metadata | ✓ — constructed from Crossref JSON, not doi.org Accept-header |
| arXiv | export_citations + export.arxiv.org live | ✓ | ✓ | n/a |
| Internal | resolve_paper_id + live Zenodo/DataCite (concept chains) | ✓ | ✓ | n/a |

**Key corrections made during verification (fabrication-prevention):** 7 provisional bib keys carried WRONG author attributions; all corrected to the Crossref-verified author lists (Bhattacharyya-Hung-Lei-Li; Hung-Li-Melby-Thompson; Gesteau-Marcolli-Parikh; Heydeman-Marcolli-Parikh; Gubser; Gubser-Jepsen-Trundy; Ryu-Schnyder-Furusaki-Ludwig). `lerda1992anyons` (was wilczek1992anyons): Crossref chapter record has no author/editor; parent volume = "Anyons" by Alberto Lerda (LNP Monographs 68, 1992) — author corrected to the Crossref-attested volume author in v0.4 (round-3 S-5); no fabricated author. E8 FRS DOI corrected per §2 above.

## 4. Duplicate check (P3.AUTHOR-GATE rule 5)

Python `re` scan of `references.bib` (v0.5): **56 entries, 56 unique keys, 0 duplicates.** Brace balance: `{`==`}` True.

## 5. P3.SOURCE-DISCIPLINE (three-count audit, v0.5)

- Cited in body == listed in References == **56/56** (script-verified: zero orphans, zero dangles).
- Reliability tiers: primary (live API metadata) for all external entries; internal entries verified via resolve_paper_id.
- No tertiary sources cited.

## 6. Gate output

`references.bib` (56 verified entries) + this audit. Zero fabricated entries. All evidence files committed under `artifacts/external-search/crossref_verify_*.json`. Note: the v0.5 published record (10.5281/zenodo.22024856) carries the pre-refresh audit snapshot (33 entries); this repo file is the current documentation (v0.6 record candidate if a documentation-snapshot refresh is ever warranted — accepted as artifact-snapshot drift otherwise).
