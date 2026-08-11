# Core Claim Lock — QNFO.UMP.007 (CMB Higher n-Point Functions)

**Status:** LOCKED (Phase 0, P6) — pre-registered at commit time (git hash below is
filled at the Phase 0 commit; the commit timestamp is the immutability anchor).

---

## 1. The Core Claim

**C1 (primary):** If ultrametric (p-adic) log-periodic structure is physically
realized in the primordial fluctuation field, then the CMB *bispectrum* (and
higher-n correlators) must exhibit a log-periodically modulated non-Gaussian shape:
the reduced bispectrum $f_{\mathrm{NL}}(k_1,k_2,k_3)$ carries multiplicative
oscillations in $\log_p$ of the scale ratios, with a characteristic period
$\Delta \log_p = 1$ (one octave in the relevant radix) that is *not* present in
standard local/equilateral/orthogonal templates.

**C2 (null companion):** The published 2-point null (RQ-002, amplitude < 0.3% at 95%
CL) does NOT rule out C1: higher-order statistics are independent observable channels
with different noise propagation, and a sub-threshold 2-point oscillation can imprint
an *amplified* relative signature in the bispectrum shape where the 2-point signal is
suppressed by a different power of the coupling.

**C3 (testable form):** The bispectrum signature is parameterized by an amplitude
$\varepsilon_{p}$ (analogous to $A_{\mathrm{LPO}}$ for the 2-point case) and a radix
$p$. The prediction is falsifiable for each $(p, \varepsilon_p)$ pair against the
Planck 2018 bispectrum estimator results and the public temperature maps.

---

## 2. Falsifiability Condition (disconfirmation)

The framework is **disconfirmed** for a given radix $p$ if:

> **D1:** The Planck 2018 bispectrum (from the public COM_CompMap products and the
> published estimator results, e.g. Planck 2018 non-Gaussianity papers) shows NO
> evidence of log-periodic modulation in $f_{\mathrm{NL}}(k_1,k_2,k_3)$ with period
> $\Delta\log_p = 1$, at a sensitivity that bounds the p-adic bispectrum amplitude
> $\varepsilon_p$ below the value required by the 2-point null consistency relation,
> computed with a look-elsewhere-corrected significance (BP-3 gate).

**D2 (consistency):** The framework is also disconfirmed if the detected higher-n
signature is inconsistent with the 2-point bound: a bispectrum detection at
$\varepsilon_p \gg$ the 2-point-implied amplitude, without a mechanism explanation,
counts as a contradiction of the single-field ultrametric model (not of the data).

**D3 (degeneracy):** If the best-fit p-adic shape is statistically indistinguishable
from a standard template (local/equilateral/orthogonal) at $\Delta \log\text{-odds}
\le 0$ under KIF-60, the claim is capped at **[RETRODICTION — not evidence]** and the
paper reports the constraint, not a detection.

---

## 3. Pre-registration Discipline (KIF-60)

- **A. Pre-registration:** this file IS the timestamped prediction. The git commit of
  this file (hash + timestamp) is the immutable anchor. No analysis results were used
  to write C1-C3; the formalism and the prediction are fixed BEFORE the Planck data is
  analyzed in this project (analysis happens in P4).
- **B. Falsifiability gradient:** D1/D2/D3 are concrete disconfirmation conditions.
- **C. Surprise accounting:** P(match | random structure) will be estimated in the
  P4 analysis per the BP-3 density gate: if the p-adic shape is dense in the space of
  allowed bispectrum shapes, the look-elsewhere penalty is applied and reported.
- **D. Confirmation-seeking test:** the alternative that a detection would falsify is
  "standard single-field slow-roll ΛCDM with no p-adic structure," which predicts NO
  log-periodic modulation in the reduced bispectrum shape. A non-detection does NOT
  confirm ΛCDM — it only constrains $\varepsilon_p$.

---

## 4. Scope Boundaries (what this claim is NOT)

1. This is NOT a claim that p-adic structure exists — it is a falsifiable test with a
   specified disconfirmation condition.
2. This is NOT a re-analysis of the 2-point null (RQ-002 result is assumed).
3. This is NOT a claim about any specific physical mechanism (string/M-theory, adelic
   QFT, etc.) — only about the observable signature in CMB higher-n statistics.
4. Every numerical claim in the paper will pass BP-1 (independent recompute), BP-7
   (sigma provenance), and BP-3 (density/look-elsewhere) before publication.

---

*Locked by: research agent (CMD RESEARCH protocol, Phase 0 P6). Commit anchor:
filled at Phase 0 commit.*
