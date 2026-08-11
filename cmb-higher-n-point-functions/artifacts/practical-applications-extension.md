# Practical Applications Extension (Stage 9) — QNFO.UMP.007

**Date:** 2026-08-12 · **Phase:** P4 · **Gate:** MANDATORY (research v2.99 Stage 9)

---

## 1. Candidate → Application mapping

| # | Forecast candidate | Application domain | Operational signature | Falsifiable claim |
|:--|:-------------------|:-------------------|:----------------------|:------------------|
| A1 | p-adic log-periodic bispectrum template | CMB cosmology (Planck, CMB-S4, LiteBIRD) | log-periodic modulation of reduced bispectrum at ω_p = 2π/ln p | Detection at ω≈9.06 (p=2) with shape orthogonal to local/equilateral = binary-tree candidate; null below ε=0.003 strengthens ΛCDM |
| A2 | Radix-identifiability structure | Statistical shape analysis / template-fitting pipelines | Cross-correlation matrix between candidate shapes; degeneracy map | The (3,5)/(5,7) degeneracy is an identifiability bound ANY template search must report; a claim that resolves them at Planck resolution is falsifiable (it will fail) |
| A3 | Amplitude-consistency relation | Multi-tracer cosmological constraints | ε_p (bispectrum) ≲ A_LPO (2-point) in single-modulation models | A bispectrum detection at ε≫0.003 without mechanism contradicts the single-field ultrametric model |
| A4 | Radix-locked frequency search | General DSI/feature searches in time series (not just CMB) | Lomb–Scargle/periodogram at fixed frequencies {9.06, 5.72, 3.90, 3.23} | Any claim of "log-periodic structure" that does not report which frequency family it belongs to is under-specified; the locked-frequency test is transferable |
| A5 | Higher-n consistency (shared ω_p across channels) | Cross-channel correlator analysis | Bispectrum and trispectrum best-fit frequencies must agree | Disconfirmed if bispectrum/trispectrum frequencies disagree beyond combined uncertainty |

## 2. Sensitivity requirements for a discriminating CMB-S4 search

| Requirement | Value (this phase) | Rationale |
|:------------|:-------------------|:----------|
| Frequency resolution Δω | < 1.36 (Planck) → < 0.7 for CMB-S4 | To separate p=5 vs p=7 (sep=0.675) need Δω < 0.675 → ln-range > 9.3 decades or multi-probe combination |
| σ(f_NL) per shape family | < 1.0 (vs Planck ~30) | To reach ε=0.05 sensitivity; ε=0.003 requires σ ~ 0.01 — likely beyond CMB-S4 unless NG amplification exists |
| k-range coverage | maximize ln(k_max/k_min) | Rayleigh resolution scales as 2π/ln-range; combining CMB + LSS (galaxy bispectrum) extends the range |

## 3. Calibration register additions

```
[CHECK: 2030] CMB-S4 bispectrum constrains eps_2 < 0.05 (95% CL) or detects the p=2 template.
Strength: [STRONG] | Status: [PENDING]

[CHECK: 2032] A galaxy-bispectrum (DESI/Euclid) search extends the log-dynamic range,
resolving or ruling out the p=5 vs p=7 degeneracy.
Strength: [STRONG] | Status: [PENDING]

[CHECK: 2028] No Planck-2018 higher-n p-adic detection is claimed at >3 sigma without
look-elsewhere control. (Self-check on the analysis being built.)
Strength: [STRONG] | Status: [IN-PROGRESS]
```

## 4. Near-term fork recommendations (→ Future Work)

1. **P4.5 Planck data leg** — run the radix-locked matched filter on public Planck 2018
   bispectrum products (COM_CompMap / Planck 2018 NG papers) to convert the synthetic
   sensitivity into a published upper bound on ε_p.
2. **Mechanism search** — the single-modulation model gives ε_p ≲ 0.003; if a concrete
   non-linear amplification mechanism can be derived from the ultrametric framework
   (raising the bispectrum channel), RQ-013's "amplified relative signature" hypothesis
   becomes viable. Without it, the honest result is a constraint.
3. **Cross-probe log-range extension** — combine CMB + LSS bispectra to push Δω below
   the p=5/p=7 separation (0.675).
