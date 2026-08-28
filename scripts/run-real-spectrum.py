#!/usr/bin/env python3
"""QNFO.UMP.014 P3-exec — real-data arm: ExoMol NaH Rivlin rovibrational level spectrum.
Parses the .states file, unfolds by rank (non-parametric), computes R2(s), Sigma^2(L),
Delta_3(L). Report-only: molecular spectra are expected near-Poisson/intermediate, not GUE;
this run validates the pipeline on real data. Writes artifacts/verification/nah-output.json.
Usage: python scripts/run-real-spectrum.py <path-to-states.bz2>"""
import json, sys, hashlib, bz2
import numpy as np
from math import pi, log


def load_states(path):
    energies = []
    with bz2.open(path, "rt") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    energies.append(float(parts[1]))
                except ValueError:
                    continue
    return np.array(sorted(energies))


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


def number_variance(xi, L):
    lo = xi[0] + 0.2 * (xi[-1] - xi[0])
    hi = xi[0] + 0.8 * (xi[-1] - xi[0])
    counts = []
    x = lo
    while x + L <= hi:
        counts.append(np.searchsorted(xi, x + L) - np.searchsorted(xi, x))
        x += L
    return float(np.var(counts)) if len(counts) >= 20 else float("nan")


def rigidity_delta3(xi, L):
    lo = xi[0] + 0.2 * (xi[-1] - xi[0])
    hi = xi[0] + 0.8 * (xi[-1] - xi[0])
    vals = []
    x = lo
    while x + L <= hi:
        m = np.searchsorted(xi, x)
        n = np.searchsorted(xi, x + L)
        if n - m >= 5:
            xw = xi[m:n]
            cnt = np.arange(m, n, dtype=float) - m
            b, a = np.polyfit(xw, cnt, 1)
            vals.append(float(np.mean((cnt - (a + b * xw)) ** 2)))
        x += L
    return float(np.mean(vals)) if vals else float("nan")


def unfold_smoothed(e, deg=5):
    """Smoothed-staircase unfolding: xi = poly-fit of the empirical cumulative count,
    rescaled to unit mean spacing. Captures the trend, preserves local fluctuations."""
    n = len(e)
    staircase = np.arange(1, n + 1, dtype=float)
    e0, e1 = e[0], e[-1]
    u = (e - e0) / (e1 - e0)
    coeff = np.polyfit(u, staircase, deg)
    smooth = np.polyval(coeff, u)
    smooth *= (n - 1) / (smooth[-1] - smooth[0])
    return smooth


def main():
    path = sys.argv[1]
    e = load_states(path)
    xi = unfold_smoothed(e)
    centers, r2, edges = pair_correlation_r2(xi)
    nv = {str(L): number_variance(xi, L) for L in (1.0, 2.0, 5.0, 10.0, 20.0)}
    d3 = {str(L): rigidity_delta3(xi, L) for L in (5.0, 10.0, 20.0)}
    strict = bool(np.all(np.diff(e) > 0))
    ok = len(e) >= 1000 and strict and np.all(np.isfinite(r2))
    results = {
        "dataset": "ExoMol NaH 23Na-1H Rivlin states",
        "n_levels": int(len(e)),
        "energy_range_cm": [float(e[0]), float(e[-1])],
        "strictly_increasing": strict,
        "unfolding": "smoothed staircase (poly deg 5), unit mean spacing",
        "r2_s": centers.tolist(),
        "r2": r2.tolist(),
        "r2_first_bin": float(r2[0]),
        "r2_mean_s_0.15_1.5": float(np.mean(r2[(centers >= 0.15) & (centers <= 1.5)])),
        "number_variance": nv,
        "rigidity_delta3": d3,
        "sanity_pass": bool(ok),
        "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
    }
    with open("artifacts/verification/nah-output.json", "w") as f:
        json.dump(results, f, indent=2)
    print("=== QNFO.UMP.014 P3-exec real-data arm (NaH Rivlin) ===")
    print("[PASS] sanity (>=1000 levels, strictly increasing, finite R2)" if ok
          else "[FAIL] sanity", "n_levels=%d" % len(e))
    print("R2 first bin =", float(r2[0]), " mean R2 over s in [0.15,1.5] =",
          results["r2_mean_s_0.15_1.5"])
    print("Sigma^2:", nv)
    print("Delta_3:", d3)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
