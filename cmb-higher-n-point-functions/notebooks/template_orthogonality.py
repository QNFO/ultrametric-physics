# -*- coding: utf-8 -*-
"""
template_orthogonality.py — QNFO.UMP.007 Phase 4 (G-2)
=====================================================
Compute the shape-space orthogonality between:
  (A) the p-adic log-periodic bispectrum template (radix-locked frequency
      omega_p = 2*pi/ln(p), p in {2,3,5,7}), and
  (B) the resonant-features family (Leblond-Pajer 2011) with FREE frequency
      omega over a grid.

Method: Fergusson-Liguori-Shellard style shape correlator over the
tetrahedral momentum domain k1<=k2<=k3, k3<=k1+k2, with log-uniform sampling
(the natural measure for scale-invariant shapes). Reported:
  * shape correlation C(S_p, S_res(omega)) as a function of omega
  * max |C| over the resonant grid (degeneracy measure)
  * radix frequency separations vs the achievable resolution
    Delta_omega ~ 2*pi / ln(k_max/k_min) (Rayleigh criterion)

Reproducibility: pure numpy; all parameters explicit; output JSON evidence
file written to ../artifacts/external-search/../ (evidence discipline).
"""
import json, os
import numpy as np

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Momentum-domain grid (tetrahedral, log-uniform)
# ---------------------------------------------------------------------------
# Planck 2018 k-range proxy: ell in [2, 2508] -> k in [0.001, 0.1] h/Mpc
# Use log-uniform grid spanning ~2.5 decades. For frequency resolution we
# want a large log-dynamic-range; use k in [k_min, k_max].
K_MIN = 0.001
K_MAX = 0.1
N_PER_DECADE = 12
n_decades = np.log10(K_MAX / K_MIN)
N = int(round(n_decades * N_PER_DECADE))
k = np.geomspace(K_MIN, K_MAX, N)

k1, k2, k3 = np.meshgrid(k, k, k, indexing="ij")
# Tetrahedral mask: sorted momenta, triangle inequality, fundamental domain
m = (k1 <= k2) & (k2 <= k3) & (k3 <= k1 + k2) & (k1 + k2 > k3 * 0.999)
k1m, k2m, k3m = k1[m], k2[m], k3[m]
s = k1m + k2m + k3m
print(f"grid: {N}^3 = {N**3}, tetrahedral points: {m.sum()}")

# ---------------------------------------------------------------------------
# 2. Templates (reduced bispectrum shape functions)
# ---------------------------------------------------------------------------
def padic_template(k1_, k2_, k3_, p, eps=1.0, phi=0.0, base="equilateral"):
    """p-adic log-periodic modulation around a base shape.
    omega_p = 2*pi/ln(p)  ->  period in log-scale exactly ln(p) (one radix octave)."""
    omega_p = 2.0 * np.pi / np.log(p)
    s_ = k1_ + k2_ + k3_
    # base: equilateral-normalized dimensionless shape (flat in log space)
    if base == "equilateral":
        base_shape = np.ones_like(s_)
    elif base == "local":
        base_shape = 1.0 / (k1_ * k2_ * k3_)  # local-type scaling
        base_shape /= np.median(base_shape)
    else:
        raise ValueError(base)
    mod = 1.0 + eps * np.cos(omega_p * np.log(s_) + phi)
    return base_shape * mod

def resonant_template(k1_, k2_, k3_, omega, eps=1.0, phi=0.0, base="equilateral"):
    """Leblond-Pajer resonant-feature family with FREE frequency omega."""
    s_ = k1_ + k2_ + k3_
    if base == "equilateral":
        base_shape = np.ones_like(s_)
    elif base == "local":
        base_shape = 1.0 / (k1_ * k2_ * k3_)
        base_shape /= np.median(base_shape)
    else:
        raise ValueError(base)
    mod = 1.0 + eps * np.cos(omega * np.log(s_) + phi)
    return base_shape * mod

# ---------------------------------------------------------------------------
# 3. Shape correlator (FLS-style, weight = 1/(k1 k2 k3) volume element)
# ---------------------------------------------------------------------------
def shape_corr(S1, S2, w=None):
    if w is None:
        w = 1.0 / (k1m * k2m * k3m)
    n1 = np.sqrt(np.sum(w * S1 * S1))
    n2 = np.sqrt(np.sum(w * S2 * S2))
    if n1 == 0 or n2 == 0:
        return 0.0
    return float(np.sum(w * S1 * S2) / (n1 * n2))

# ---------------------------------------------------------------------------
# 4. Main computation
# ---------------------------------------------------------------------------
PRIMES = [2, 3, 5, 7]
OMEGA_GRID = np.linspace(0.5, 12.0, 231)  # covers all radix freqs with margin
results = {}
for p in PRIMES:
    Sp = padic_template(k1m, k2m, k3m, p)
    corrs = []
    for om in OMEGA_GRID:
        Sr = resonant_template(k1m, k2m, k3m, om)
        corrs.append(shape_corr(Sp, Sr))
    corrs = np.array(corrs)
    imax = int(np.argmax(np.abs(corrs)))
    omega_p = 2.0 * np.pi / np.log(p)
    results[p] = {
        "omega_p": float(omega_p),
        "self_corr": float(shape_corr(Sp, Sp)),
        "max_abs_corr_over_resonant_grid": float(np.abs(corrs[imax])),
        "omega_at_max": float(OMEGA_GRID[imax]),
        "corr_at_omega_p": float(corrs[int(np.argmin(np.abs(OMEGA_GRID - omega_p)))]),
    }
    print(f"p={p}: omega_p={omega_p:.4f}  max|C| vs resonant grid={np.abs(corrs[imax]):.4f} "
          f"at omega={OMEGA_GRID[imax]:.2f}  C(omega_p)={corrs[int(np.argmin(np.abs(OMEGA_GRID-omega_p)))]:.4f}")

# ---------------------------------------------------------------------------
# 5. Frequency resolution (Rayleigh) + radix separability
# ---------------------------------------------------------------------------
ln_range = np.log(K_MAX / K_MIN)
delta_omega = 2.0 * np.pi / ln_range
print(f"\nlog-dynamic-range ln(k_max/k_min) = {ln_range:.3f}")
print(f"Rayleigh frequency resolution Delta_omega ~ 2*pi/ln-range = {delta_omega:.3f}")

omega_p = {p: 2.0 * np.pi / np.log(p) for p in PRIMES}
print("\nRadix frequencies:")
for p in PRIMES:
    print(f"  p={p}: omega_p={omega_p[p]:.4f}")
print("\nRadix separation matrix (|omega_a - omega_b|):")
sep = {}
for i, a in enumerate(PRIMES):
    row = []
    for j, b in enumerate(PRIMES):
        d = abs(omega_p[a] - omega_p[b])
        row.append(f"{d:.3f}")
        sep[f"{a}-{b}"] = float(d)
    print(f"  p={a}: " + "  ".join(row))

print("\nSeparability vs Planck resolution:")
for a, b in [(2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7)]:
    resolvable = sep[f"{a}-{b}"] > delta_omega
    print(f"  p={a} vs p={b}: sep={sep[f'{a}-{b}']:.3f} "
          f"(resolvable={'YES' if resolvable else 'NO'}, Delta_omega={delta_omega:.3f})")

# ---------------------------------------------------------------------------
# 6. Evidence file
# ---------------------------------------------------------------------------
evidence = {
    "phase": "QNFO.UMP.007.P4",
    "slug": "cmb-higher-n-point-functions",
    "date": "2026-08-12",
    "grid": {"k_min": K_MIN, "k_max": K_MAX, "n": N, "tetra_points": int(m.sum())},
    "delta_omega_rayleigh": float(delta_omega),
    "results": results,
    "separations": sep,
}
ev_path = os.path.join(OUT_DIR, "template-orthogonality-evidence.json")
with open(ev_path, "w", encoding="utf-8") as f:
    json.dump(evidence, f, indent=2, ensure_ascii=False)
print(f"\nevidence written: {ev_path}")
print("DONE")
