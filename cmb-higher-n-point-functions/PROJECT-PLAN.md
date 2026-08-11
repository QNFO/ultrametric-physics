# WBS: QNFO.UMP.007

# PROJECT-PLAN — CMB Higher n-Point Functions: p-adic Signatures Beyond the 2-Point Function

| Field | Value |
|:------|:------|
| **WBS** | `QNFO.UMP.007` (Ultrametric Physics, project 007) |
| **Slug** | `cmb-higher-n-point-functions` |
| **Branch** | `ump/paper/cmb-higher-n-point-functions` |
| **Program** | Ultrametric Physics (`QNFO.UMP`) |
| **Repo** | `QNFO/ultrametric-physics` |
| **Research Question** | RQ-013: Do CMB higher-order correlation functions (bispectrum, trispectrum) reveal p-adic signatures not visible in the 2-point function? |
| **Status** | Phase 0 (Init) |
| **Created** | 2026-08-12 |
| **Priority** | MEDIUM (per KG RQ-013 registry) |

---

## Charter

Planck 2018 temperature data constrains p-adic log-periodic oscillations in the CMB
2-point correlation function to an amplitude below 0.3% at 95% CL — a published null
result (RQ-002, `cmb-ultrametric-signatures`, 2026-07-05). That null constrains *linear*
(2-point) statistics only. The question left open (RQ-013) is whether *higher-order*
statistics — the bispectrum (3-point) and trispectrum (4-point) — carry p-adic
signatures that are sub-dominant in the power spectrum but comparatively amplified in
non-Gaussian channels.

This project (a) builds the concrete formalism predicting what p-adic log-periodic
oscillations would imprint on CMB bispectrum/trispectrum shapes; (b) tests those
predictions against public Planck 2018 data (COM_CompMap_SMICA / foreground-cleaned
maps and the published bispectrum estimator results); (c) delivers a falsifiable
statement: either a p-adic signature in higher-n statistics is detected with a
quantified significance, or the non-Gaussian channel is shown to be consistent with
standard ΛCDM at the sensitivity of current data.

**Scope boundary:** the prior published null (2-point) is assumed; this project does
not re-litigate it. It extends the ultrametric cosmology program to the non-Gaussian
sector.

---

## Phases with WBS

| WBS | Phase | Deliverables | Gate |
|:----|:------|:-------------|:-----|
| `QNFO.UMP.007.P0` | Init | Branch, scaffold, PROJECT-PLAN.md, core claim lock, WBS registration, commit/tag/push | P1-P11 pre-flight all HARD |
| `QNFO.UMP.007.P1` | Due Diligence | KG + D1 + Vectorize cross-ref; external 8-source search; gap analysis; KIF-29 consilience gate | artifacts/consilience-gate.md present |
| `QNFO.UMP.007.P2` | Literature | Bispectrum/trispectrum theory, p-adic cosmology, CMB non-Gaussianity estimators; KIF-18 symmetry template | 5-10 core classified |
| `QNFO.UMP.007.P3` | Citations | BibTeX verified (P3.AUTHOR-GATE), citation-audit.md | All entries live-verified |
| `QNFO.UMP.007.P4` | Deep Research | p-adic bispectrum/trispectrum shape derivation; synthetic-signal injection; Planck data analysis; red-team | fit-verify, BP-1..BP-10 |
| `QNFO.UMP.007.P5` | Publication | `<slug>.md` + PDF (CDP pipeline) + Zenodo deposit | BP gates, P5 gates |
| `QNFO.UMP.007.P6` | Deployment | D1 living-paper, papers-server, KG node, Vectorize index | get_paper_context 200; webhook indexed |
| `QNFO.UMP.007.P7` | Dissemination | Journal shortlist, outreach, SEO, Internet Archive | outreach-log.md |
| `QNFO.UMP.007.P8` | Distribution | R2 archive, GitHub tag, 4-layer verification, ERRATA registry | Consolidated Closeout Verification |

---

## Milestones with Gate Criteria

| Milestone | Target | Gate criteria |
|:----------|:-------|:--------------|
| M0 Phase 0 committed | 2026-08-12 | Branch pushed, tag `v0.1-phase0`, `git ls-remote` shows branch+tag |
| M1 Due diligence complete | P1 | 8-source external search evidence saved; gap analysis; consilience-gate.md |
| M2 Formalism derived | P4 | p-adic bispectrum/trispectrum shape integrals derived + symbolic/numeric verify |
| M3 Data analysis complete | P4 | Planck 2018 analysis reproducible via committed scripts; significance computed |
| M4 Publication live | P5/P6 | DOI resolves; D1 row; KG node; Vectorize indexed |
| M5 Distribution verified | P8 | All 4 layers + KG + Vectorize re-proven same-turn |

---

## Deliverable Registry

| ID | Deliverable | Location | Status |
|:---|:------------|:---------|:-------|
| D-001 | PROJECT-PLAN.md | `<slug>/PROJECT-PLAN.md` | ✅ (this file) |
| D-002 | Core claim lock | `<slug>/docs/core-claim.md` | pending |
| D-003 | README.md | `<slug>/README.md` | pending |
| D-004 | Due diligence report | `<slug>/artifacts/due-diligence.md` | pending |
| D-005 | External search evidence | `<slug>/artifacts/external-search/` | pending |
| D-006 | Consilience gate | `<slug>/artifacts/consilience-gate.md` | pending |
| D-007 | Gap analysis | `<slug>/artifacts/gap-analysis.md` | pending |
| D-008 | Paper | `<slug>/cmb-higher-n-point-functions.md` | pending |
| D-009 | PDF | `<slug>/cmb-higher-n-point-functions.pdf` | pending |
| D-010 | Analysis scripts | `<slug>/notebooks/` + `<slug>/artifacts/` | pending |

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| R-01 Null result in higher-n too (no signal) | HIGH | MED | Result is publishable as a constraint paper; strengthens the 2-point null; KIF-60 caps any retrodiction framing |
| R-02 Planck bispectrum estimator not directly reusable for log-periodic shape | MED | HIGH | Design synthetic-signal injection pipeline early (P4); use public COM_CompMap products; document estimator assumptions |
| R-03 Formalism degenerates with ΛCDM shape | MED | MED | Pre-register shape differences; BP-3 density-gate / look-elsewhere control |
| R-04 Data access / compute limits | LOW | MED | Use public Planck legacy archive products; modest compute; exact-frequencies closed form where possible |
| R-05 Silo blindness (already-connected literature) | MED | HIGH | KIF-29 consilience gate + 8-source external search with exact-phrase queries |

---

## Success Criteria

1. A falsifiable prediction for p-adic imprints in CMB bispectrum/trispectrum shapes, pre-registered (timestamped, committed).
2. An analysis of public Planck 2018 data testing that prediction, with a quantified significance or an explicit upper bound.
3. Every claim carries a disconfirmation condition; any cross-domain correspondence passes KIF-60 (no [RETRODICTION] presented as evidence).
4. Publication through the full QNFO stack (Zenodo DOI, D1, KG node, Vectorize, R2, GitHub tag) with consolidated closeout verification.
