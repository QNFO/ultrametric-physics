# p-Adic Bispectrum/Trispectrum Template — Derivation (QNFO.UMP.007, Phase 4)

**Date:** 2026-08-12 · **WBS:** `QNFO.UMP.007.P4` · **Gap:** G-1 (template derivation)

---

## 1. Starting point: the 2-point log-periodic template

The published proposal (10.5281/zenodo.19555030) predicts a log-periodic modulation of
the angular power spectrum:

$$\ell(\ell+1) C_\ell = A \left(\frac{\ell}{\ell_0}\right)^{1-n_s} \left[ 1 + B \cos\left( \frac{2\pi}{\ln q} \ln\left(\frac{\ell}{\ell_0}\right) + \phi \right) \right]$$

with $q$ the fundamental scaling ratio. For a p-adic (ultrametric) origin, discrete
scale invariance under $k \to p k$ fixes the period in log-scale to exactly
$\Delta \log k = \ln p$, i.e. the angular frequency

$$\omega_p = \frac{2\pi}{\ln p}, \qquad p \in \{2, 3, 5, 7, \ldots\}.$$

The established 2-point constraint (10.5281/zenodo.21205104; CAL-03) bounds
$A_{\mathrm{LPO}} < 0.003$ at 95% CL for all $p$, with log Bayes factors
$-5.14$ to $-6.54$ against the modulated model.

## 2. Generalization to the bispectrum

### 2.1 The reduced bispectrum

The three-point function of the primordial curvature perturbation is written in terms
of the scale-invariant reduced bispectrum $f_{\mathrm{NL}}(k_1,k_2,k_3)$:

$$\langle \zeta_{k_1}\zeta_{k_2}\zeta_{k_3} \rangle = (2\pi)^3 \delta^{(3)}(\mathbf{k}_1+\mathbf{k}_2+\mathbf{k}_3)\,
\frac{6}{5} f_{\mathrm{NL}}(k_1,k_2,k_3)\, \frac{1}{(k_1 k_2 k_3)^2} \left[P(k_1)P(k_2) + \mathrm{cyc.}\right].$$

For single-field slow-roll inflation the reduced bispectrum is a function of the
shape $r_{ij} = k_i/k_j$ only. A log-periodic modulation of the underlying fluctuation
field — the p-adic discrete scale invariance — imprints an additional factor that is
*periodic in the logarithm of the overall momentum scale* $K = k_1+k_2+k_3$
(equivalently in any overall-scale variable), because discrete scale invariance acts
by simultaneous scaling $k_i \to p\,k_i$.

### 2.2 The p-adic bispectrum ansatz

The natural ansatz, minimally extending the 2-point form, is a multiplicative
modulation of a base shape $f_{\mathrm{NL}}^{(0)}$:

$$f_{\mathrm{NL}}^{(p)}(k_1,k_2,k_3) = f_{\mathrm{NL}}^{(0)}(k_1,k_2,k_3)
\left[ 1 + \varepsilon_p \cos\!\left( \omega_p \ln K + \phi_p \right) \right],
\qquad K = k_1+k_2+k_3, \quad \omega_p = \frac{2\pi}{\ln p}.$$

The base shape $f_{\mathrm{NL}}^{(0)}$ is taken from the standard families
(local/equilateral/orthogonal); the modulation is the p-adic imprint. The two free
parameters per radix are the amplitude $\varepsilon_p$ and phase $\phi_p$.

### 2.3 Falsifiable content

The p-adic claim has three falsifiable ingredients, each distinct from the generic
resonant-features literature (Leblond–Pajer 2011):

1. **Radix-locked frequency.** The modulation frequency is *not* a free parameter: it
   must equal $\omega_p = 2\pi/\ln p$ for an integer prime $p$. A free-frequency fit
   that lands at $\omega \not\approx \omega_p$ for any small prime is a disconfirmation
   of the p-adic origin (though not of discrete scale invariance per se).
2. **Amplitude consistency with the 2-point null.** If the modulation is a property of
   the underlying field, the same amplitude scale should appear in the bispectrum
   channel. Specifically, in a single-modulation model where the same dimensionless
   amplitude modulates all correlators, $\varepsilon_p$ must be of the same order as the
   2-point amplitude bound $A_{\mathrm{LPO}} \lesssim 0.003$. A claimed bispectrum
   detection at $\varepsilon_p \gg 0.003$ requires an explicit amplification mechanism
   (D2 in core-claim.md).
3. **Radix separability.** The shape-space correlation between different primes must
   permit identification of the radix. The Phase-4 computation shows this is
   *partial*: p=2 is cleanly orthogonal to all others, but (3,5) and (5,7) are
   degenerate at Planck resolution (see §4).

## 3. Trispectrum extension

The same ansatz extends to the trispectrum: the 4-point reduced amplitude
$\tau_{\mathrm{NL}}(k_1,k_2,k_3,k_4)$ (or its shape decompositions) carries the
modulation

$$\tau_{\mathrm{NL}}^{(p)}(k_1,k_2,k_3,k_4) = \tau_{\mathrm{NL}}^{(0)}(k_1,k_2,k_3,k_4)
\left[ 1 + \varepsilon_p^{(4)} \cos\!\left( \omega_p \ln K_4 + \phi_p^{(4)} \right) \right],
\qquad K_4 = k_1+k_2+k_3+k_4.$$

The bispectrum is the primary channel (best constrained by Planck); the trispectrum
provides a consistency check and a separate amplitude $\varepsilon_p^{(4)}$ that may
differ in magnitude but must share the radix frequency $\omega_p$ if the origin is
p-adic. **The shared frequency across channels is itself a falsifiable prediction**
(disconfirmed if the best-fit bispectrum and trispectrum frequencies disagree beyond
their combined uncertainty).

## 4. Phase-4 numerical results (orthogonality / separability)

### 4.1 Method

Shape correlator (Fergusson–Liguori–Shellard style) over the tetrahedral domain
$k_1 \le k_2 \le k_3$, $k_3 \le k_1+k_2$, log-uniform sampling
$k \in [0.001, 0.1]$, weight $1/(k_1 k_2 k_3)$:

$$C(S_a, S_b) = \frac{\sum w\, S_a S_b}{\sqrt{\sum w\, S_a^2}\,\sqrt{\sum w\, S_b^2}}.$$

### 4.2 Radix frequencies and resolution

| p | $\omega_p = 2\pi/\ln p$ | ln-range $= \ln(100)$ | Rayleigh $\Delta\omega$ |
|:--|:-----------------------|:----------------------|:------------------------|
| 2 | 9.0647 | 4.605 | 1.364 |
| 3 | 5.7192 | 4.605 | 1.364 |
| 5 | 3.9040 | 4.605 | 1.364 |
| 7 | 3.2289 | 4.605 | 1.364 |

### 4.3 Cross-correlation matrix $C(S_{p_a}, S_{p_b})$

| | p=2 | p=3 | p=5 | p=7 |
|:--|:----|:----|:----|:----|
| **p=2** | 1.0000 | 0.3262 | −0.2873 | 0.2389 |
| **p=3** | 0.3262 | 1.0000 | **−0.7714** | 0.5875 |
| **p=5** | −0.2873 | **−0.7714** | 1.0000 | **−0.9149** |
| **p=7** | 0.2389 | 0.5875 | **−0.9149** | 1.0000 |

### 4.4 Discriminator verdicts (|C| > 0.7 OR separation < Rayleigh ⇒ degenerate)

| Pair | C | \|C\| | sep | Δω | Verdict |
|:-----|:--|:------|:----|:---|:--------|
| 2–3 | 0.3262 | 0.3262 | 3.346 | 1.364 | **ORTHOGONAL** |
| 2–5 | −0.2873 | 0.2873 | 5.161 | 1.364 | **ORTHOGONAL** |
| 2–7 | 0.2389 | 0.2389 | 5.836 | 1.364 | **ORTHOGONAL** |
| 3–5 | −0.7714 | 0.7714 | 1.815 | 1.364 | **DEGENERATE** (anti-correlated) |
| 3–7 | 0.5875 | 0.5875 | 2.490 | 1.364 | ORTHOGONAL (marginal) |
| 5–7 | −0.9149 | 0.9149 | 0.675 | 1.364 | **DEGENERATE** |

### 4.5 Interpretation (honest, falsifiability-first)

- **p=2 is the uniquely identifiable radix.** Its frequency ($\omega_2 = 9.06$) is well
  separated from all other small primes and its shape correlation with every other
  prime is ≤ 0.33. A detection at $\omega \approx 9.06$ with a shape that is orthogonal
  to the local/equilateral bases would be a strong p-adic (binary-tree) candidate.
- **p=3 vs p=5 and p=5 vs p=7 are degenerate at Planck resolution.** A detection in the
  band $\omega \in [3.2, 5.7]$ could be attributed to more than one radix. The paper
  MUST report this degeneracy explicitly (KIF-60 surprise accounting; the "which
  prime?" question cannot be answered at Planck's log-dynamic-range).
- **The resonant-family degeneracy remains the primary threat.** The p=2 template
  correlates with the *free-frequency* resonant family at C=0.94 near $\omega=9$
  (self-match), but the matched peak is narrow (C drops from 0.94 at ω=9 to 0.20 at
  ω=10 and −0.49 at ω=11): a radix-locked search at a fixed $\omega_p$ is
  distinguishable from a free-frequency scan only if the frequency resolution of the
  data (Δω ≈ 1.36) is smaller than the distance from $\omega_p$ to the best-fit
  resonant frequency. This is the quantitative content of the G-2 gap: the orthogonality
  is *not* between p-adic and resonant shapes at the same frequency (they are identical
  at $\omega = \omega_p$ by construction), but between *radix-locked* and *free*
  frequency hypotheses.

### 4.6 Amplitude-consistency bound (G-4, quantitative)

From the 2-point null ($A_{\mathrm{LPO}} < 0.003$ at 95% CL) and the single-modulation
assumption, the bispectrum amplitude is bounded by the same scale:

$$\varepsilon_p \lesssim A_{\mathrm{LPO}} \approx 0.003 \quad \text{(single-modulation model)}.$$

The Planck 2018 bispectrum sensitivity to a resonant-type shape is
$\sigma(f_{\mathrm{NL}}) \sim \mathcal{O}(10)$–$\mathcal{O}(10^2)$ in the
$f_{\mathrm{NL}}$ normalization; the modulation signal in the reduced bispectrum is
$\varepsilon_p \cdot f_{\mathrm{NL}}^{(0)} \sim 0.003 \times \mathcal{O}(1)$ —
**below current sensitivity by 3–4 orders of magnitude.** Consequence: within the
single-modulation model, the higher-n channel does NOT amplify the p-adic signal, and
RQ-013's "amplified relative signature" hypothesis is only viable if the framework
supplies a concrete non-linear amplification mechanism (e.g., a resonant
bispectrum-building interaction). Absent such a mechanism, the honest expected outcome
of the Planck analysis is an upper bound, not a detection — which is publishable as a
constraint and strengthens the 2-point null. This is the D2 consistency test made
quantitative.

## 5. Deliverables produced this phase

| Artifact | Path | Status |
|:---------|:-----|:-------|
| Orthogonality computation | `notebooks/template_orthogonality.py` | ✅ run, evidence saved |
| Profile computation | `notebooks/template_orthogonality_profiles.py` | ✅ run, evidence saved |
| Evidence JSON | `artifacts/template-orthogonality-evidence.json` | ✅ |
| Evidence JSON (profiles) | `artifacts/template-orthogonality-profiles.json` | ✅ |
| Amplitude bound | this document §4.6 | ✅ |
| Synthetic injection | `notebooks/synthetic_injection.py` | Phase 4 (G-5) |
| KIF-60 gate | `artifacts/bayesian-evidential-weight.md` | Phase 4 |

*Evidence files are committed with the phase; every number above traces to the JSON
outputs (BP-1: independent recompute by re-running the scripts).*
