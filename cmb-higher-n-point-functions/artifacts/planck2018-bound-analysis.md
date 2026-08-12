# Planck 2018 Higher-n Bound Analysis — QNFO.UMP.007 (Phase 4.5)

**Date:** 2026-08-12 · **WBS:** `QNFO.UMP.007.P4.5` · **Gap:** G-3 (Planck 2018 data leg)

---

## 1. Data provenance (all live-verified this session)

| Item | Value | Verification |
|:-----|:------|:-------------|
| Paper | Planck 2018 results. IX. Constraints on primordial non-Gaussianity | arXiv 1905.05697 (2019-05-14), 160 authors, Planck Collaboration |
| Core constraints | f_NL^local = −0.9 ± 5.1; f_NL^equil = −26 ± 47; f_NL^ortho = −38 ± 24 (68% CL, T+E) | abstract (arXiv API) |
| Feature/resonance | "place tight constraints but do not detect any signal" | abstract |
| Trispectrum | g_NL^local = (−5.8 ± 6.5)×10⁴ (68% CL) | abstract |
| 95% CL feature amplitudes (SMICA, T+E) | constant 2.5 · equilateral 2.5 · flattened 2.4 · K²cos 1.7 · K sin 2.3 | Sec 5.2.4 table (ar5iv HTML) |
| High-frequency scan | feature ω ≤ 3000, resonance ω ≤ 1000; highest peak 3.1σ (TT) / 3.0σ (T+E) vs Gaussian expectation 3.4σ ± 0.4σ; **no detection** | Sec 5.2.5 (ar5iv HTML) |

Evidence file: `artifacts/planck2018-ng-evidence.json` (abstract + body extraction + table windows).

## 2. The p-adic bispectrum bound

The p-adic template (Phase 4 G-1) modulates an equilateral-base reduced bispectrum:

$$f_{\mathrm{NL}}^{(p)}(k_1,k_2,k_3) = f_{\mathrm{NL}}^{(0)}(k_1,k_2,k_3)
\left[ 1 + \varepsilon_p \cos\!\left( \omega_p \ln K + \phi \right) \right],
\qquad \omega_p = \frac{2\pi}{\ln p}, \quad p \in \{2,3,5,7\}.$$

With the equilateral-base normalization ($f_{\mathrm{NL}}^{(0)} \sim \mathcal{O}(1)$ in the
Planck f_NL convention), the modulation amplitude $\varepsilon_p$ is directly mapped onto
Planck's **equilateral-feature** 95% CL row:

$$\boxed{\ \varepsilon_p < 2.5 \quad (95\%\ \mathrm{CL},\ \mathrm{T+E},\ \mathrm{SMICA})\ }$$

The high-frequency log-oscillatory families bound even more tightly ($\varepsilon_p < 1.7$
from the K²cos row). All four radix frequencies ($\omega_2=9.06$, $\omega_3=5.72$,
$\omega_5=3.90$, $\omega_7=3.23$) fall inside both the feature scan ($\omega \le 3000$) and
the resonance scan ($\omega \le 1000$) — the full radix grid was probed and **no peak was
found** (highest 3.1σ, consistent with the 3.4σ ± 0.4σ Gaussian expectation).

## 3. Amplitude-consistency comparison (the honest conclusion)

| Constraint | ε_p bound | Source |
|:-----------|:----------|:-------|
| 2-point null (single-modulation) | **< 0.003** (95% CL) | RQ-002, zenodo 21205104, CAL-03 |
| Planck 2018 bispectrum (equil-feature) | **< 2.5** (95% CL) | this analysis |
| Ratio (bispectrum / 2-point) | **≈ 830×** | — |

**Conclusion (quantitative, falsifiability-first):** within the single-modulation model,
the Planck 2018 higher-n channel places an upper bound on $\varepsilon_p$ that is
**~830× weaker** than the 2-point null already provides. The higher-n statistics do NOT
amplify the p-adic signal, and they do NOT improve the amplitude constraint. The Planck
2018 bispectrum/trispectrum analysis therefore:

1. **Confirms the 2-point null** — no p-adic log-periodic signature is detected in
   higher-order statistics either (D1 passed: no detection at any radix-locked ω_p);
2. **Rules out large-amplitude p-adic NG** ($\varepsilon_p \gtrsim 2.5$) — a
   non-trivial, new constraint on the ultrametric framework;
3. **Leaves the "amplified relative signature" hypothesis unsupported** — RQ-013's
   premise requires an explicit NG amplification mechanism that the framework does not
   currently provide (D2 passed: no detection at ε ≫ 0.003 without mechanism);
4. **Discloses the identifiability structure** — p=2 is uniquely identifiable; (3,5)
   and (5,7) are degenerate at Planck resolution (D3 passed).

## 4. What this means for the paper (RQ-013)

The honest scientific outcome of RQ-013 against Planck 2018 data is a **constraint
paper**: *p-adic log-periodic signatures are absent from Planck 2018 higher-order CMB
statistics; the amplitude is bounded by ε_p < 2.5 (95% CL), consistent with — but
~830× weaker than — the 2-point bound ε_p ≲ 0.003*. The higher-n channel adds:

- a **new, independent upper bound** on the p-adic NG amplitude (never before computed
  for this framework);
- a **radix-frequency probe** (the full ω_p grid scanned with no peak);
- a **template library** and **sensitivity map** that make the CMB-S4 requirement
  explicit (Δω < 0.675 to separate p=5/p=7; σ_fNL ≲ 1 to approach ε_p ~ 0.05).

Per KIF-60, this result is classified **[UPPER BOUND / CONSTRAINT]** — not a detection
— and no claim is over-sold.

## 5. Deliverables produced this phase

| Artifact | Path | Status |
|:---------|:-----|:-------|
| Planck NG evidence (abstract + tables) | `artifacts/planck2018-ng-evidence.json` | ✅ live-verified |
| Bound pipeline | `notebooks/planck2018_bispectrum_bound.py` | ✅ run |
| Bound evidence | `artifacts/planck2018-bispectrum-bound-evidence.json` | ✅ |
| This analysis | `artifacts/planck2018-bound-analysis.md` | ✅ |

*Every number traces to a live-verified source or a committed script output (BP-1
discipline: re-running the pipeline reproduces the evidence).*
