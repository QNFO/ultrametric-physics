# Consilience Gate (KIF-29) — QNFO.UMP.007 (CMB Higher n-Point Functions)

**Date:** 2026-08-12 · **Phase:** P1b · **Gate:** HARD (mandatory before P2)

---

## 1. Cross-Domain Lexicon (dynamic domain selection)

Domains selected from Phase 1 evidence (not a fixed template):

| # | Domain | Selected because | Evidence |
|:--|:-------|:-----------------|:---------|
| 1 | Cosmology / CMB statistics | The observable channel: Planck 2018 higher-n correlators are the data | due-diligence §1.2-1.3 |
| 2 | Number theory (p-adic / ultrametric) | The formalism: log-periodic modulation derives from valuation structure | proposal DOI 10.5281/zenodo.19555030 |
| 3 | Inflationary phenomenology / features | The degeneracy channel: resonant non-Gaussian shapes already exist | Leblond–Pajer 2011 (10.1088/1475-7516/2011/01/035) |
| 4 | Signal processing / spectral analysis | The method: log-resample + Lomb–Scargle + bispectrum estimation | proposal §3; Planck NG estimator papers |
| 5 | Information theory | Interpretive frame: D=4 ultrametric embedding, hierarchical structure | cmb-ultrametric-signatures §1.2 |

**Domain-selection rationale:** each domain appears in the evidence base with a concrete
role (data, formalism, degeneracy, method, interpretation). No domain was added purely
to fill a template.

## 2. Minimum-Viable-Finding (one non-trivial structural isomorphism per domain)

| Domain | Structural isomorphism | Verifiable reasoning |
|:-------|:-----------------------|:---------------------|
| Cosmology/CMB | The reduced bispectrum $f_{\mathrm{NL}}(k_1,k_2,k_3)$ is a function on a 3-scale space; log-periodic modulation in $\log_p$ of scale ratios is the ultrametric analogue of the 2-point LPO modulation | Directly testable against Planck 2018 estimator results; the 2-point analogue was already bounded (A_LPO < 0.003) |
| Number theory | The oscillation period $\Delta \log_p = 1$ is the valuation-theoretic statement that $|p^n x|_p$ returns after one digit shift — a non-trivial number-theoretic constraint translated into a spectral signature | Only $p$-adic valuations produce exact one-octave periodicity; generic features produce other periodicities (Leblond–Pajer shape is not octave-locked) |
| Inflation features | Resonant bispectrum shapes from particle production are log-periodic in $k$; the p-adic template is a *constrained subset* with period fixed by the radix | Overlap computable: projection of p-adic template onto resonant template basis; BP-3 density gate |
| Signal processing | Log-resampling turns multiplicative scale invariance into additive periodicity — the same transform used for the 2-point search applies to higher-n statistics with a generalized kernel | Methodological continuity from the published proposal protocol |
| Information theory | The D=4 ultrametric embedding maps to 4 CMB angular-scale depths; higher-n correlators probe deeper tree levels | Consistent with cmb-ultrametric-signatures §1.3 scale-depth table |

**Explicit reasoned denial for absent isomorphisms:** No non-trivial isomorphism was
found between the p-adic CMB signature and *biology* or *sociology* domains — the
evidence base (Planck data, inflationary features, p-adic analysis, spectral methods,
information theory) contains no methodological-independence link to those domains, and
forcing one would violate the independent-consilience definition.

## 3. Silo Cost Table (Silo-Failure Detection Protocol)

| Domain | Structure Name | Earliest | Connected | Silo Cost | Key Paper |
|:-------|:---------------|:---------|:----------|:----------|:----------|
| Number Theory | p-adic valuations / Ostrowski completions | 1916 | 2026 (this program's 2-point test) | **110 yr** | Ostrowski, Acta Math 1916 |
| Cosmology/CMB | Log-periodic LPO in C_l | 2004 (log-periodic DSI literature; Sornette) | 2026-04 (QNFO proposal) | ~22 yr | Sornette's DSI line; QNFO proposal 19555030 |
| Inflation features | Resonant N-point functions | 2005 (Chen, Easther, Lim) | 2011 (Leblond–Pajer library) | ~6 yr | Chen–Easther–Lim 2005; Leblond–Pajer 2011 |
| Signal processing | Log-spectral periodicity | 1960s (cepstrum/log-frequency analysis) | 2026-04 (QNFO protocol) | ~60 yr | Bogert–Healy–Tukey cepstrum 1963 |

**Silo flag:** Number Theory → Cosmology carries `[SILO-FAILURE: >50yr gap]` — the
p-adic formalism existed for a century before any cosmological test; the current
project's higher-n extension continues the rectification. Inflation-features and
signal-processing domains were connected within a decade — those silos were NOT
pathological; this audit grades them symmetrically (they did not fail).

**Symmetric audit of incumbents (2026-08-04 user injunction):** ΛCDM + single-field
slow-roll is graded by the same falsifiability standard: it predicts ZERO log-periodic
modulation in higher-n shapes. Its auxiliary structure (feature models, non-local
inflation, oscillating dark energy) absorbs anomalies via added parameters — the same
goalpost-moving risk this paper audits in the p-adic framework. No pro-incumbent bias.

## 4. Synthesis Consilience

**Meta-principle (invariant across all translations):** *Log-periodic modulation in the
logarithm of scale is the observable fingerprint of discrete scale invariance; the
radix-fixed octave period distinguishes a p-adic origin from generic feature models.*

**Frontier Question:** *If the higher-n channel is constrained to the 2-point-implied
amplitude, is there any remaining observable — beyond CMB-S4 sensitivity — in which a
p-adic (rather than merely discrete-scale-invariant) structure could be distinguished
from resonant-feature inflation?*

---

## 5. KIF-60 Bayesian Evidential Weight Gate (sub-gate — 2026-08-04)

### 5.1 Pre-Registration Record (Three Concrete Tests)

| Test | Status | Evidence |
|:-----|:-------|:---------|
| A. Pre-registration | ✅ EXISTING | OSF `2ndsz` (2026-07-20, DOI 10.17605/osf.io/2ndsz) + this repo's `docs/core-claim.md` (committed 2026-08-12, sha 9eeed5e) |
| B. Falsifiability gradient | ✅ | D1/D2/D3 in `docs/core-claim.md` — concrete disconfirmation conditions |
| C. Surprise accounting | PENDING | P4 analysis: estimate P(match | random bispectrum shape); BP-3 density/look-elsewhere |

### 5.2 Confirmation-Seeking Test

**Alternative the test would falsify:** standard single-field slow-roll ΛCDM + resonant-feature
inflation (Leblond–Pajer family), which predicts log-periodic shapes NOT octave-locked to a
specific radix and with different amplitude-scaling relations. A p-adic detection must
discriminate from this alternative by the radix-locked period and the ε_p-vs-2-point amplitude
consistency relation. If the alternative predicts a nearly identical observable (tuned
resonant model), the test is a parameter measurement — graded accordingly, capped per KIF-60.

### 5.3 Tautology Trap Audit

| Trap | Check | Status |
|:-----|:------|:-------|
| Overfitting | Template free parameters (ε_p, p, phase) vs independent shape degrees of freedom | MONITOR in P4 — count dof vs matches |
| Cherry-picking | Full search space: all primes p ∈ {2,3,5,7}, all higher-n channels, all binnings reported | MANDATED: report hit/miss denominator |
| Absorption | No new dualities declared post-hoc; disconfirmation conditions fixed at pre-registration | PRE-DECLARED in core-claim.md D1-D3 |

### 5.4 Δlog-odds summary (expected)

| Claim | P(O\|T) | P(O\|¬T) | Δlog-odds | Classification |
|:------|:--------|:---------|:----------|:---------------|
| 2-point null (established) | — | — | — | ASSUMED constraint (not a claim of this paper) |
| Higher-n detection (if found) | depends on ε_p | resonant-feature degenerate — NOT small | ≤ 0 unless orthogonality proven | [NOT YET EVIDENCE] until shape-orthogonality + look-elsewhere pass |
| Higher-n upper bound (if null) | — | — | — | Reports constraint; KIF-60 cap applies to any "agreement" framing |

**Gate output:** this file satisfies the HARD requirement (Silo Cost table present +
domain isomorphisms + meta-principle + frontier question + KIF-60 record). Phase 1b
COMPLETE. P2 (literature) may proceed.

---

## Gate Calibration Register

```
[CHECK: 2027] QNFO.UMP.007 higher-n constraint published with BP-3 look-elsewhere control.
Strength: [STRONG] | Status: [PENDING]

[CHECK: 2030] CMB-S4 tests the p-adic higher-n template at >5σ sensitivity or rules it out.
Strength: [STRONG] | Status: [PENDING]
```
