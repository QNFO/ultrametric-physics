# -*- coding: utf-8 -*-
"""
template_orthogonality_profiles.py — QNFO.UMP.007 Phase 4 (G-2, companion)
========================================================================
Report the FULL cross-correlation matrix between p-adic templates at each
radix: C(S_p_a, S_p_b) for all pairs, plus the correlation profile of each
p-adic template against the resonant family at the OTHER radix frequencies.
This is the discriminator table: it shows which primes are mutually
orthogonal and which (5 vs 7) are degenerate at Planck resolution.
"""
import json, os
import numpy as np

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")

K_MIN = 0.001
K_MAX = 0.1
N_PER_DECADE = 12
N = int(round(np.log10(K_MAX / K_MIN) * N_PER_DECADE))
k = np.geomspace(K_MIN, K_MAX, N)
k1, k2, k3 = np.meshgrid(k, k, k, indexing="ij")
m = (k1 <= k2) & (k2 <= k3) & (k3 <= k1 + k2) & (k1 + k2 > k3 * 0.999)
k1m, k2m, k3m = k1[m], k2[m], k3[m]
s = k1m + k2m + k3m
w = 1.0 / (k1m * k2m * k3m)

def padic(k1_, k2_, k3_, p):
    om = 2.0 * np.pi / np.log(p)
    return np.cos(om * np.log(k1_ + k2_ + k3_))

def corr(A, B):
    na = np.sqrt(np.sum(w * A * A))
    nb = np.sqrt(np.sum(w * B * B))
    return float(np.sum(w * A * B) / (na * nb))

PRIMES = [2, 3, 5, 7]
T = {p: padic(k1m, k2m, k3m, p) for p in PRIMES}
om = {p: 2.0 * np.pi / np.log(p) for p in PRIMES}
ln_range = np.log(K_MAX / K_MIN)
delta_om = 2.0 * np.pi / ln_range

print("=== Cross-correlation matrix C(S_p_a, S_p_b) (pure modulation parts) ===")
print(f"    {'':>6}" + "".join(f"{p:>10}" for p in PRIMES))
matrix = {}
for a in PRIMES:
    row = []
    for b in PRIMES:
        c = corr(T[a], T[b])
        row.append(c)
        matrix[f"{a}-{b}"] = c
    print(f"p={a}: " + "".join(f"{c:>10.4f}" for c in row))

print("\n=== Discriminator interpretation (|C|>0.7 OR sep<delta => degenerate) ===")
for a, b in [(2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7)]:
    c = matrix[f"{a}-{b}"]
    sep = abs(om[a] - om[b])
    degenerate = (abs(c) > 0.7) or (sep < delta_om)
    verdict = "DEGENERATE" if degenerate else "ORTHOGONAL"
    print(f"  p={a} vs p={b}: C={c:.4f}  |C|={abs(c):.4f}  sep={sep:.3f}  delta={delta_om:.3f}  -> {verdict}")

# Correlation vs omega profile for p=2 (width of the matched-frequency peak)
print("\n=== p=2 template vs resonant family across omega grid (peak width) ===")
om_grid = np.linspace(1.0, 12.0, 111)
profile = []
for ow in om_grid:
    Sr = np.cos(ow * np.log(s))
    profile.append(corr(T[2], Sr))
profile = np.array(profile)
for ow, c in zip(om_grid[::10], profile[::10]):
    print(f"  omega={ow:6.3f}  C={c:8.4f}")

evidence = {
    "phase": "QNFO.UMP.007.P4",
    "date": "2026-08-12",
    "cross_corr_matrix": matrix,
    "omega": om,
    "delta_omega": float(delta_om),
    "interpretation": {
        "degenerate_pairs": [f"{a}-{b}" for a, b in [(2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7)]
                             if (abs(matrix[f"{a}-{b}"]) > 0.7 or abs(om[a] - om[b]) < delta_om)],
        "orthogonal_pairs": [f"{a}-{b}" for a, b in [(2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7)]
                             if not (abs(matrix[f"{a}-{b}"]) > 0.7 or abs(om[a] - om[b]) < delta_om)],
    },
}
with open(os.path.join(OUT_DIR, "template-orthogonality-profiles.json"), "w", encoding="utf-8") as f:
    json.dump(evidence, f, indent=2, ensure_ascii=False)
print("\nevidence written: template-orthogonality-profiles.json")
print("DONE")
