---
title: "The p-Adic Observable Program: The Fine-Structure Constant as a Length Ratio at the Prime Places"
wbs: "QNFO.UMP.014"
slug: "p-adic-observable-program"
branch: "ump/paper/p-adic-observable-program"
repo: "QNFO/ultrametric-physics"
phase: "P0"
status: "active"
core_claim_locked: "2026-08-28"
author: "Rowan Brad Quni-Gudzinas"
---

# PROJECT-PLAN — QNFO.UMP.014

## 0. Phase-0 classification

- **Topic source:** 2026-08-28 DeepSeek chat synthesis (545-chat census; `_deepseek-research-synthesis-2026-08-28.md`), candidate theses #1–7, plus the same-day notes `p-adic QM` (the redundancy critique), `Partition Signatures in Physics` (§2 of RES.029), and `Ultrametric Paradigm Explained`.
- **User directive:** triage all 7 candidates against the corpus, then recommend and lock the single strongest project.
- **Classification:** NET-NEW project. Triage verdict (§7): candidates 2 and 4 are already published; candidates 5–7 are covered or infra; candidate 3 is partially covered. **Candidate 1 is the strongest genuine gap.**
- **WBS resolve (D1 program_registry, checked 2026-08-28):** `QNFO.UMP.014` unclaimed; UMP project numbering reaches UMP.013. Branch convention: `ump/paper/<slug>`, tag `v0.1-phase0-ump014`.

## 1. Core claim (LOCKED, Phase 0)

> The fine-structure constant carries a p-adic length-ratio reading: α is expressible as a ratio of length scales canonically assigned to the prime places of the electron's rational data (p-adic radius data on the Bruhat–Tits tree), and this reading
> (i) reproduces the measured α ≈ 7.2973525693 × 10⁻³ within the construction's stated tolerance;
> (ii) makes a numerically distinct prediction about α's place-structure — a p-adic evaluation of the RS-1 decomposition α⁻¹ = 137 + Δ_adelic + Δ_RG that decides whether the 137-coincidence is cosmetic or non-cosmetic (an open test recorded in durable memory on 2026-07-23 and never executed);
> (iii) yields an anisotropic α test protocol at quantum-standards precision that is computable today and falsifiable.

Scope boundary (inherited from RES.029, 10.5281/zenodo.22142794): the claims are readings of mathematical structure; no new particle physics is implied; the premises end where the identification of a physical length at the p-adic place begins.

## 2. Hypothesis cards (HYPOTHESIS-CARD-1)

- **H-ALPHA-1 (length-ratio reading exists).** Prediction: a canonical p-adic length pair (Bruhat–Tits radius data associated with the electron's rational invariants) yields a ratio within 1e-5 of measured α with at most one named input. Falsifier: no such canonical pair exists without ≥ 2 free parameters.
- **H-ALPHA-2 (non-cosmetic 137).** Prediction: the p-adic valuation pattern of the Δ_adelic / Δ_RG terms is stable under place change, i.e. the 137 near-coincidence carries non-cosmetic p-adic content. Falsifier: the pattern is indistinguishable from a random rational approximation — cosmetic.
- **H-ALPHA-3 (anisotropic signature).** Prediction: the adelic reading predicts an α anisotropy at a computable relative magnitude in a specified measurement geometry. Falsifier: standard isotropy at the stated precision. The disconfirmation criterion is pre-registered with its number (OSF) at P5.

## 3. Premise-depth disclosure (SO-WHAT-GATE)

- **L0** — α = e²/(4πε₀ħc), measured dimensionless constant: named input.
- **L1** — Ostrowski's theorem (all completions of ℚ): imported theorem.
- **L2** — The adelic product formula: imported theorem.
- **L3** — A physical length/temperature can be identified at a p-adic place: PREMISE (the boundary RES.029 flags; inherited explicitly).
- **L4** — The specific p-adic length data assigned to the electron: HYPOTHESIS (what H-ALPHA-1 tests; not a theorem).
- **L5** — Derived numerical predictions (i)–(iii): derived from L0–L4; verified in code before assertion (COMPUTATIONAL-VERIFICATION-1).

The claim is as deep as L4. L4 is the honest frontier; everything above it is imported, everything below it is computation.

## 4. Why a reader should care, and what a practitioner can do

The 2026-08-28 DeepSeek critique charges the p-adic scaffolding with redundancy: it is organizational, not dynamical, and earns its keep only if the p-adic topology produces constraints that resist Archimedean rewriting. This project answers the charge with a concrete test. If H-ALPHA-1..3 hold, the p-adic reading constrains α in a way the bare Archimedean reading does not state; if they fail, the redundancy charge is confirmed with a number and the corpus register records a certified null.

Practitioner deliverable: an anisotropic test protocol with target precision and a computable deviation, executable on existing quantum-standards hardware (atomic/optical clocks, ion/Rydberg spectroscopy). A metrologist gets a number to look for.

Crosswalk (title-visible bridge): p-adic valuation ↔ length scale · Bruhat–Tits tree ↔ hierarchical resolution ladder · place ↔ measurement basis · prime gap ↔ spectral irregularity.

## 5. Adjacent-domain scan (CROSSWALK-TRANSLATION-1)

- **UMP (primary):** valuation theory, Bruhat–Tits geometry.
- **INM:** the zitterbewegung-as-observable thread (zbw-majorana-tqc-p4, "Zitterbewegung as the Physical Realization of p-Adic Anyon Braiding").
- **Metrology (JPC-adjacent):** quantum standards, anisotropic measurement protocols; feeds the JPCub measurement discipline.

## 6. Due-diligence evidence (Phase 1 core)

- **Corpus anchors:** fine-structure-constant-cross-ratio (10.5281/zenodo.20108536, α = CR(r_e, λ_C), adelic §7.7, falsifiability §8.4) · adelic-crossratio · UMP.009 v5.0 (10.5281/zenodo.21965332) · RES.020 scalar family (10.5281/zenodo.22035210) · RES.029 (10.5281/zenodo.22142794) · RS-1 α⁻¹ = 137 + Δ_adelic + Δ_RG (rosetta artifacts) · Alpha as Bifurcation Parameter (10.5281/zenodo.21690631).
- **Gap proofs:** living-paper `LIKE '%anisotropic%'` = 0 records; no corpus record claims the p-adic length-ratio reading of α; memory records the cosmetic-vs-non-cosmetic p-adic evaluation of the 137-coincidence as never executed (2026-07-23 Ostrowski red-team).
- **External:** arXiv has no precedent for α as a p-adic length ratio with an anisotropic quantum-standards test (closest: Castro physics/0104016 + hep-th/0203086, El Naschie/Cantorian tradition — distinct; Chang–Zhu 2011.07773 spatial α variation — not p-adic). Evidence files: artifacts/external-search/ at P1.

## 7. Triage verdict table (7 candidates, 2026-08-28)

| # | Candidate | WBS | Corpus status | Verdict |
|---|---|---|---|---|
| 1 | p-adic observable program (α length ratio + zitterbewegung + anisotropic test) | UMP | Pieces exist; anisotropic test = 0 records; 137-coincidence test outstanding | **LOCKED — QNFO.UMP.014** |
| 2 | Adelic Cross-Domain Program consolidation | ADL | Published: UMP.009 v5.0 (21965332) + phase 3–4 update | DONE (synthesis stale) |
| 3 | IUH falsifiable core | INM | informational-universe ×2, infomatics-v1, qfundamental-falsifiability-protocol | Covered; residual soft |
| 4 | QLoF pure-syntax rewrite | SLB | quantum-laws-of-form + syntactic-token-calculus + RES.020 published | DONE (synthesis stale) |
| 5 | QEC-Darwinism × joules | JPC | QEC.001 (21964674) + jpcub-qec-landauer (22117282): per-family floor, nested-vs-flat 1.6–3× | Both sides published; junction thin |
| 6 | Ultrametric vs supremacy | UMP/PLT | huang audit + BQNN baseline + ultrametric-QC foundations + qudit advantage | Covered; residual = business |
| 7 | Taxonomy → KG product spec | PLT | RES.022 + terminology-silos + consilience-framework | Infra; research side covered |

## 8. UIA — Universal Ignorance Audit (ZENODO-INQUIRY-1, administered 2026-08-28 on the core claim)

- **Q1 (target):** α admits a canonical p-adic length-ratio reading with predictions (i)–(iii).
- **Q2 (falsity):** H-ALPHA-1/2/3 falsifiers in §2; a certified null is a result.
- **Q3 (truth):** H-ALPHA-1 within 1e-5 with ≤1 input; H-ALPHA-2 non-cosmetic; H-ALPHA-3 a pre-registered anisotropy number.
- **Q4 (objects unknown):** whether any canonical p-adic length data exists independent of the Archimedean lengths (L4 is precisely the unknown).
- **Q5 (methods unknown):** whether "canonical" can be defined without importing the Archimedean answer (circularity risk — the L3/L4 seam).
- **Q6 (prior falsifications):** A1 anharmonic ladder null, harmonic-paradigm retraction, CMB log-periodic null — the register's discipline applies.
- **Q7 (unstatable unknowns):** a dependence we cannot name because our vocabulary is Archimedean-first.
- **Q8 (surprise):** a p-adic prediction surviving at full CODATA precision with zero inputs.
- **Q9 (vocabulary failure):** "length at the p-adic place" may be a category error, not a quantity.
- **Q10 (smallest experiment):** the anisotropic test at quantum-standards precision (H-ALPHA-3).
- **Q11 (smallest computation):** the p-adic valuation pattern of Δ_adelic/Δ_RG (H-ALPHA-2) — pure code, no hardware.
- **Q12 (imported unanalyzed):** α's measured value, Ostrowski, the product formula, L3.
- **Q13 (avoided question):** whether the whole program is a numerology wrapper around 1/137.
- **Q14 (silence):** [held]
- **Q15 (recursive):** this audit assumes "places of ℚ" is the right decomposition to interrogate α at all; the next audit pass starts there.

## 9. Pipeline (WBS-coded)

- **[QNFO.UMP.014.P1]** Full-corpus + external due diligence; evidence files to artifacts/external-search/.
- **[QNFO.UMP.014.P2]** Computational verification pass: H-ALPHA-2 p-adic valuation pattern; H-ALPHA-1 construction numerics with golden values, edge cases, seeded tests; sim script deposited.
- **[QNFO.UMP.014.P3]** Literature triage; references.bib (reference list rendered FROM the bib); citation audit.
- **[QNFO.UMP.014.P4]** Paper draft: `<slug>.md/.html/.pdf`; rendering gates (check_rendering.py); no browser chrome.
- **[QNFO.UMP.014.P5]** OSF pre-registration of the H-ALPHA-3 disconfirmation criterion; premise-depth + crosswalk sections final.
- **[QNFO.UMP.014.P6]** Red-team review (Accuracy/Completeness/Dependency); fix all HARD findings.
- **[QNFO.UMP.014.P7]** Zenodo publish (deposit integrity gates, PUBLISH-LOCK-1); D1/KG/R2 distribution.
- **[QNFO.UMP.014.P8]** Post-publication adversarial audit; dissemination (CAMPAIGNS-OUTREACH-1).
