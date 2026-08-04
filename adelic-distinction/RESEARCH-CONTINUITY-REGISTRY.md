# RESEARCH-CONTINUITY-REGISTRY.md
## QNFO.UMP.004 — Adelic Distinction: Physics as Automorphic Representation Theory on the Idele Class Group
### Created: 2026-08-04 | DOI: 10.5281/zenodo.21786603 | Concept DOI: 10.5281/zenodo.21786602

---

## FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| **FQ1** | Can the numerical values of the Standard Model's 19 dimensionless parameters be computed as periods of automorphic forms on the idele class group, i.e., as coordinates of the universal attractor in the moduli space of adelic distinction networks? | OPEN | Phase 4 deep research: attempt computation of at least one mass ratio or coupling from the idele class group's periods | YES — computational claim, pre-register method before running |

---

## FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| **P1** | Gravitational wave echoes from black hole mergers will show prime-number periodicity: time delays Δt_n = 4M ln n for integers n products of small primes, with amplitudes proportional to μ(n)/n | 2030-2040 | LIGO/Virgo/KAGRA (O4+), Einstein Telescope | Echo comb consistent with noise-only model across ≥100 high-SNR merger events with no statistically significant prime-number structure |
| **P2** | CMB polarization will show a small, parity-violating component (C_l^EB ≠ 0) with l-dependence related to prime harmonic sums | 2030-2040 | Simons Observatory, CMB-S4 | C_l^EB measurements improve by ≥1 order of magnitude and remain consistent with zero across all ℓ; any residual consistent with known foregrounds (dust, synchrotron) |

---

## PER-RQ FALSIFIABILITY CONDITIONS

| RQ | Disconfirmed If |
|:---|:---------------|
| **FQ1** | Three independent computational attempts using different automorphic form bases all fail to reproduce any Standard Model parameter to within reported experimental uncertainty; or any one parameter is shown to be structurally incompatible with any idele-class period |

---

## PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data Source | Deadline |
|:---|:-----------|:--------------|:------------|:---------|
| **REG-UMP004-001** | The Möbius function μ(n) amplitude modulation appears in GW echo stacks with p < 0.01 significance (pre-registered test) | μ(n) amplitude structure absent at p < 0.01 in ≥100 high-SNR events | LIGO/Virgo public data releases | 2037-12-31 |
| **REG-UMP004-002** | C_l^EB spectrum shows prime-harmonic structure distinguishable from foregrounds at >3σ | C_l^EB consistent with foreground-only model within measurement uncertainty | Simons Observatory / CMB-S4 public releases | 2037-12-31 |

---

## CALIBRATION REGISTER

| Prediction | Strength | Status |
|:-----------|:---------|:-------|
| `[CHECK: 2037]` Einstein Telescope or next-gen GW detector will have sufficient sensitivity to test P1 with ≥100 high-SNR merger events | WEAK | PENDING |
| `[CHECK: 2038]` Simons Observatory or CMB-S4 will have published C_l^EB measurements with uncertainty ≤1 order of magnitude better than Planck 2018 | MODERATE | PENDING |
| `[CHECK: 2039]` At least one independent research group (non-QNFO) will have investigated prime-number structure in GW echoes, triggered by P1 pre-registration | WEAK | PENDING |
| `[CHECK: 2040]` At least one computational physics group will have attempted FQ1 (Standard Model parameters as automorphic periods) | WEAK | PENDING |
| `[CHECK: 2040]` FQ1 will have yielded at least one positive result (a Standard Model parameter successfully reproduced from idele-class periods) OR one definitive negative result (proof of structural incompatibility) | WEAK | PENDING |

---

## NEXT ACTIONS (Prioritized)

| Priority | Action | Dependency | Target |
|:---------|:-------|:-----------|:-------|
| **P0** | D1/KG seeding for DOI 10.5281/zenodo.21786603 | Zenodo live | 2026-08-04 |
| **P0** | Buffer social media post | D1/KG seeded | 2026-08-04 |
| **P0** | papers.qnfo.org deployment | D1 body_md + R2 sync | 2026-08-04 |
| **P1** | Quantitative GW echo amplitude estimate relative to LIGO noise floor | P1 registered | Next session |
| **P1** | Bruhat-Tits tree diagram (p=2) for paper v0.2 | Design resource | Next session |
| **P2** | FQ1 computational attempt: one mass ratio as automorphic period | Numerical methods scoped | 2026-Q4 |
| **P3** | Paper v0.2: expand experimental section, add diagram, address red-team SOFT findings | P1 + P1 quantitative | 2026-08 |

---

## SESSION LOG

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-04 | 7gJ25ecLca3VNUeaFCZKB | Created registry; extracted FQ1 + P1-P2 + 5 calibration predictions from paper v0.1; committed to ump/paper/adelic-distinction |

---

## MAINTENANCE PROTOCOL

- **Update triggers:** (a) any new Zenodo version of the paper; (b) any external paper citing an FQ/P from this registry; (c) any prediction reaching its CHECK date; (d) any new session that advances the paper beyond v0.1
- **Minimum review cadence:** Every 90 days or every session touching the paper, whichever comes first
- **Living document:** This registry is NOT a paper artifact — it is maintained and updated across sessions. Status changes, new predictions, and verification results are appended here
