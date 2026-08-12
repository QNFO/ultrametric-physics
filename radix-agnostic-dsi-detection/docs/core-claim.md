# Core Claim — QNFO.UMP.008 (locked 2026-08-12)

**Project:** Radix-Agnostic Detection of Discrete Scale Invariance
**WBS:** QNFO.UMP.008
**Lock status:** P6 — HARD, committed at Phase 0

---

## C1 — The core reduction (mathematical)

DSI under rescaling $x \to \lambda x$ becomes, in the coordinate $u = \ln x$,
**periodicity with angular frequency**

$$\omega_0 = \frac{2\pi}{\ln \lambda}$$

The radix λ is the inverse logarithm of a measured log-frequency:
$\hat\lambda = e^{2\pi/\omega_0}$. Radix-agnostic detection = continuous ω
estimation; radix-locked detection = fixing ω_p = 2π/ln p for primes p.

*Evidence: methodology note `_26224105300.md` §1. Verified in this session's synthetic runs.*

## C2 — The three-stage protocol recovers a non-prime radix (empirical)

Stage 1 (detrend + FFT/Lomb-Scargle peak) → Stage 2 (bounded sinusoid on
detrended residuals) → Stage 3 (candidate-radix hypothesis test).

- Synthetic λ=1.62 (intentionally NOT an integer prime): FFT peak err 1.2%,
  Lomb-Scargle (uneven grid) err 1.8%, **bounded sinusoid refinement err ≤0.02%**
  (verified across seeds 42, 12345, 7).
- σ_λ = 0.0002 (0.01% relative) via Stage-2 covariance propagation.
- Full joint LPPL fit FAILS for discovery (λ→10⁹ even at true-peak init) —
  stage separation is required.

*Evidence: `dsi-radix-detector.py` self-test + extension verification (2026-08-12).*

## C3 — Certification is mandatory (statistical integrity)

A DSI claim is certified only when ALL hold:
- **Bootstrap null** (max-statistic p: observed max peak vs shuffled max peaks) —
  p < 0.05; this p is ALREADY multiplicity-corrected (Sidak would double-count).
- **ΔBIC** (pure baseline vs +log-periodic) > 10.
- **Integrity gates** pass == 3: G1 ω ≥ 2π/u_span (resolvability), G2 SNR ≥ 1,
  G3 σ_λ/λ < 10% (radix precision).

*Evidence: red-team fix cycle 2026-08-12 (double-counting bug found+fixed).*

## D1 — Definitive null on real data (Planck 2018 TT)

Application to the Planck 2018 unbinned TT spectrum (ℓ≥30, N=2446):
**no certified DSI at any resolvable radix**, including p-adic λ∈{2,3,5,7}
(probed at 0.078 rad resolution, power_frac 0.0002–0.0005). Consistent with
radix-locked nulls: CAL-03 (DOI 10.5281/zenodo.21534747) global p=0.38,
P5 p-adic ln2/ln3/ln5 global p=0.38.

*Evidence: real-data deployment + direct self-audit (resolvability arithmetic,
p-adic probing, G4 critique) 2026-08-12.*

## D2 — G4 model subtraction is mandatory for non-power-law data

Raw-spectrum scanning produces a self-refuting artifact (λ≈10⁴–10⁵,
σ_λ/λ=985%, SNR=0.15, ω below resolvable minimum) that the gates correctly
reject. Correct protocol: scan log(y) − log(y_model) residuals against a
physical model (e.g., best-fit ΛCDM) — the shuffle-null is then valid.
Planck binned TT vs BestFit residuals: bootstrap p=0.888, ΔBIC=−7.3,
gates 0/3, detected=false.

*Evidence: G4 model-residual mode + LCDM-residual scan (2026-08-12).*

## D3 — LPPL joint fit is not a discovery scanner

Documented + reproduced: 6-parameter LPPL fit with free ω collapses to
λ≈10⁹ even initialized at the true FFT peak (exponential trend and rapid
modulation compete in the optimizer). Confirms Geraskin & Fantazzini (2011)
over-parameterization warning with live evidence. Use stage separation.

*Evidence: `dsi_twostage.py` FAIL output (2026-08-12).*

---

## Falsifiability conditions

- C2 is disconfirmed if a fresh synthetic single-radix dataset with λ∈[1.2,3.0],
  C=0.3, SNR≥10 yields Stage-2 radix error > 2%.
- C3 is disconfirmed if a pure-noise dataset (no DSI) is certified as DSI
  (false-positive rate > 5% over 100 null realizations).
- D1 is disconfirmed if any resolvable ω∈[1.42, 65] rad in the LCDM-subtracted
  Planck residuals yields bootstrap p<0.05 AND gates_pass==3.

## Success criteria

1. Certified methodology published with reproducibility evidence.
2. Planck null strengthens the p-adic program's honest-negative record.
3. `dsi-radix-detector.py` production-hardened (certification enforced by default).
