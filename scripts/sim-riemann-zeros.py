#!/usr/bin/env python3
"""QNFO.UMP.014 P3-exec — Riemann-zeros arm of the Montgomery-Odlyzko law.

Per SPECTRAL-ESTIMATOR-CONSTRUCTION-1 item 5: the arithmetic object whose unfolded
pair correlation matches the GUE prediction is the RIEMANN ZEROS, not the primes
(primes obey Gallagher Poisson statistics with the twin-gap hard core). This script
computes the first N zeta zeros (mpmath), unfolds by the Riemann-von Mangoldt smooth
count N(t) = (t/2pi)(log(t/2pi)-1) + 7/8, computes R2(s) via the k-th-neighbor
decomposition, and asserts agreement with the GUE curve 1-(sin pi s / pi s)^2.

Deterministic. Writes artifacts/verification/zeros-output.json.
"""
import json, sys, hashlib
import numpy as np
from math import pi, log
import mpmath
mpmath.mp.dps = 10

N_ZEROS = 500


def zeta_zeros(n):
    t = []
    for k in range(1, n + 1):
        t.append(float(mpmath.zetazero(k).imag))
    return np.array(sorted(t))


def unfold_zeros(t):
    return t / (2.0 * pi) * (np.log(t / (2.0 * pi)) - 1.0) + 7.0 / 8.0


def pair_correlation_r2(xi, s_max=3.0, n_bins=30, k_max=10):
    n = len(xi)
    edges = np.linspace(0.0, s_max, n_bins + 1)
    width = s_max / n_bins
    r2 = np.zeros(n_bins)
    for k in range(1, k_max + 1):
        sp = xi[k:] - xi[:-k]
        h, _ = np.histogram(sp, bins=edges)
        r2 += h / ((n - k) * width)
    centers = (edges[:-1] + edges[1:]) / 2.0
    return centers, r2, edges


def bin_averaged_curve(fn, edges, sub=20):
    out = []
    with np.errstate(divide="ignore", invalid="ignore"):
        for a, b in zip(edges[:-1], edges[1:]):
            t = np.linspace(a, b, sub + 1)
            out.append(float(np.nanmean(fn(t))))
    return np.array(out)


def gue_r2_curve(s):
    return 1.0 - (np.sin(pi * s) / (pi * s)) ** 2


def number_variance(xi, L):
    lo = xi[0] + 0.2 * (xi[-1] - xi[0])
    hi = xi[0] + 0.8 * (xi[-1] - xi[0])
    counts = []
    x = lo
    while x + L <= hi:
        counts.append(np.searchsorted(xi, x + L) - np.searchsorted(xi, x))
        x += L
    return float(np.var(counts)) if len(counts) >= 20 else float("nan")


def main():
    checks = []
    results = {"n_zeros": N_ZEROS, "mpmath": mpmath.__version__,
               "python": sys.version.split()[0]}

    zeros = zeta_zeros(N_ZEROS)
    results["last_zero"] = float(zeros[-1])
    xi = unfold_zeros(zeros)
    centers, r2, edges = pair_correlation_r2(xi)
    curve = bin_averaged_curve(gue_r2_curve, np.linspace(0.0, 3.0, 31))
    s = centers
    mask = (s >= 0.15) & (s <= 1.8)
    dev_gue = float(np.mean(np.abs(r2 - curve)[mask]))
    dev_pois = float(np.mean(np.abs(r2 - 1.0)[mask]))
    p_mo = dev_gue < 0.10
    p_rep = r2[0] < 0.4
    p_contrast = dev_pois > 0.25
    checks.append(("Montgomery-Odlyzko: zeros R2 matches GUE curve (mean|d| < 0.10, s in [0.15,1.8])",
                   p_mo, dev_gue))
    checks.append(("zeros level repulsion at small s (R2[0] < 0.4)", p_rep, r2[0]))
    checks.append(("zeros clearly deviate from Poisson flat (mean|R2-1| > 0.25)",
                   p_contrast, dev_pois))
    results["r2_s"] = centers.tolist()
    results["r2"] = r2.tolist()
    results["dev_vs_gue"] = dev_gue
    results["dev_vs_poisson"] = dev_pois

    nv = {str(L): number_variance(xi, L) for L in (1.0, 2.0, 5.0, 10.0, 20.0)}
    results["number_variance"] = nv
    euler = 0.5772156649015329
    dyson20 = (1.0 / pi ** 2) * (log(2.0 * pi * 20.0) + 1.0 + euler - pi ** 2 / 8.0)
    p_dyson = 0.5 * dyson20 <= nv["20.0"] <= 2.0 * dyson20
    checks.append(("zeros number variance matches Dyson formula within factor 2 (L=20)",
                   p_dyson, (nv["20.0"], dyson20)))

    results["checks"] = [{"name": n, "pass": bool(p)} for (n, p, _) in checks]
    results["all_pass"] = all(bool(p) for (_, p, _) in checks)
    results["script_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()

    with open("artifacts/verification/zeros-output.json", "w") as f:
        json.dump(results, f, indent=2)

    print("=== QNFO.UMP.014 P3-exec Riemann-zeros arm ===")
    for n, p, d in checks:
        print(("[PASS] " if p else "[FAIL] ") + n + (("  %r" % (d,)) if d is not None else ""))
    print("all_pass =", results["all_pass"])
    sys.exit(0 if results["all_pass"] else 1)


if __name__ == "__main__":
    main()
