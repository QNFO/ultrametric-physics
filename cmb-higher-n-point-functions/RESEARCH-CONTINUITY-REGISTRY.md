# RESEARCH-CONTINUITY-REGISTRY — QNFO.UMP.007 (CMB Higher n-Point Functions)

**WBS:** `QNFO.UMP.007` · **DOI:** 10.5281/zenodo.21900192 · **Created:** 2026-08-12 (v0.2 post-audit, research v2.64 HARD gate)
**Registry type:** LIVING DOCUMENT — maintained with version bumps. Companion to the published paper and its supporting artifacts.

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | Does a map-level Planck 2018 COM_CompMap bispectrum analysis reach the pre-registered sensitivity (ε_p ≲ 3×10⁻³) that the published-table mapping could not? | OPEN — pre-registered D1 target; delivered bound ε_p<0.096 is ~32× above it | P0: acquire COM_CompMap products + run radix-locked matched filter (research pipeline P4.5 full leg) | YES (extend OSF 2ndsz or new registration) |
| FQ2 | Can the ultrametric framework produce a concrete non-linear amplification mechanism that raises the bispectrum channel above the single-modulation bound? | OPEN — the "amplified relative signature" hypothesis (RQ-013 premise) is unsupported without it | P0: derive mechanism from ultrametric tree structure / resonant interaction | YES |
| FQ3 | Does combining CMB + large-scale-structure bispectra extend the log-dynamic range enough to separate p=5 from p=7 (needs Δω<0.68, i.e. ln-range>9.3 decades)? | OPEN | P1: DESI/Euclid galaxy bispectrum search | YES |
| FQ4 | Does the p-adic log-periodic template correlate with the resonant-feature family (Leblond–Pajer) at the radix-locked frequencies when a full shape-space fit is performed on real data? | OPEN — degenerate by construction at matched frequency; orthogonality only at off-peak ω | P2: shape-overlap projection on real estimator outputs | YES |
| FQ5 | What is the actual high-frequency resonant-model row for the log-periodic template family in Planck 2018 §5.2.5 (never transcribed in this work)? | OPEN — identified as evidence gap in v0.2 audit | P0: re-extract the resonance-model row from ar5iv 1905.05697 and re-map the bound | YES |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| P1 | ε_p < 0.096 (95% CL, data normalization) for all p∈{2,3,5,7} from the published Planck 2018 feature constraints | 2026 (delivered) | Planck 2018 IX feature tables (SMICA T+E) | Any published constraint row implying ε_p ≥ 0.096 at 95% CL with an equivalent normalization |
| P2 | No p-adic log-periodic bispectrum peak at any radix-locked ω_p in Planck 2018 high-frequency scans | 2026 (delivered) | Planck 2018 §5.2.5 (ω≤3000 feature, ω≤1000 resonance) | A peak > 3.4σ±0.4σ Gaussian expectation at a radix-locked frequency |
| P3 | A map-level COM_CompMap analysis will bound ε_p below 0.096 (i.e., improve on the table mapping) or confirm the table bound | 2026–2028 | COM_CompMap + radix-locked matched filter | Map-level bound ≥ table bound with no improvement (indicates estimator/foreground limitation, not p-adic signal) |
| P4 | If an NG amplification mechanism exists in the ultrametric framework, the bispectrum bound will be ≥ 32× above the 2-point-implied amplitude; if not, it will stay near the single-modulation ratio | 2026–2030 | framework derivation + CMB-S4 | Mechanism derived but bispectrum bound unchanged (mechanism inert) OR mechanism absent but bound far above ratio (unexplained) |
| P5 | p=5 vs p=7 remain degenerate at Planck resolution (|C|=−0.91, sep=0.675<Δω) | 2026 (delivered) | shape-correlation computation | Any published analysis resolving p=5 vs p=7 at Planck log-dynamic-range |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

| Research Question | Disconfirmed if |
|:------------------|:----------------|
| RQ-013 (CMB higher n-point p-adic signature search) | (D1 weak) no modulation found at radix-locked ω_p at achieved sensitivity; OR (D2) detection at ε_p≫0.003 without mechanism; OR (D3) best-fit shape degenerate with standard template at Δlog-odds≤0 |

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|:---|:-----------|:--------------|:-----|:---------|
| REG-UMP007-001 | Map-level COM_CompMap analysis reaches ε_p sensitivity ≤ 0.096 (improves on table mapping) | Map-level bound ≥ 0.096 at 95% CL with the same template | COM_CompMap, Planck 2018 | 2028-Q4 |
| REG-UMP007-002 | A derived NG amplification mechanism raises the predicted bispectrum ε_p above 0.003 | Mechanism derivation yields ε_p ≤ 0.003 (no amplification) | framework derivation | 2027-Q4 |

## 5. CALIBRATION REGISTER

```
[CHECK: 2027] QNFO.UMP.007 higher-n constraint published with BP-3 look-elsewhere control (v0.2 satisfies: synthetic MC over 4-radix grid; table mapping inherits Planck trials handling).
Strength: [STRONG] | Status: [IN-PROGRESS]

[CHECK: 2028] Map-level COM_CompMap leg completed (FQ1/P3).
Strength: [STRONG] | Status: [PENDING]

[CHECK: 2030] CMB-S4 tests the p-adic higher-n template at >5σ sensitivity or rules it out (FQ3, P4).
Strength: [STRONG] | Status: [PENDING]

[CHECK: 2032] Galaxy-bispectrum (DESI/Euclid) resolves or rules out p=5 vs p=7 degeneracy (FQ3).
Strength: [STRONG] | Status: [PENDING]
```

## 6. NEXT ACTIONS (PRIORITIZED)

| Priority | Action | Dependencies | Target |
|:---------|:-------|:-------------|:-------|
| P0 | Re-extract the Planck 2018 §5.2.5 resonant-model row and re-map the bound (FQ5) | ar5iv 1905.05697 HTML | next research session |
| P0 | Run the map-level COM_CompMap leg (FQ1, P3, REG-UMP007-001) | COM_CompMap products; matched-filter pipeline (already built) | 2026–2028 |
| P0 | Derive/rule out the NG amplification mechanism (FQ2, P4, REG-UMP007-002) | ultrametric framework | 2026–2027 |
| P1 | Cross-probe log-range extension CMB+LSS (FQ3) | DESI/Euclid bispectrum products | 2028+ |

## 7. SESSION LOG

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-12 | CMD EXECUTE (v0.2 remediation) | Registry created per research v2.64 HARD gate (post-audit H-5 finding). Paper v0.2 scope note cross-references this registry. |
| 2026-08-12 | CMD RED TEAM SUB | Audit identified registry absence as HARD-5; FQ5 (resonant row) surfaced as evidence gap. |

**MAINTENANCE PROTOCOL:** update this registry at every phase boundary and every publication version. Never let a published frontier question or falsifiable prediction go untracked.
