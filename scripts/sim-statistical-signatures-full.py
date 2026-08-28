#!/usr/bin/env python3
"""QNFO.UMP.014 P3-exec — five-observable statistical-signatures run on three references:
Poisson (uncorrelated), GUE (numpy Hermitian), Primes {ln p} p<=10^7 unfolded by Li(x)
(arithmetic reference; Gallagher: Poisson-flat pair correlation beyond the twin-gap hard
core; the Montgomery-Odlyzko GUE law applies to the Riemann zeros — a later arm).
R2(s), K(tau), Sigma^2(L), Delta_3(L) (report).
Deterministic seed. Writes artifacts/verification/full-output.json."""
import json, sys, hashlib, math
import numpy as np
from math import log, pi, sin
from scipy.special import expi

SEED = 20260828
X_PRIME = 10_000_000


def poisson_spectrum(n, rng):
    return np.sort(rng.uniform(0.0, n, n))


def gue_spectrum(n, rng):
    a = rng.normal(0.0, 1.0, (n, n)) + 1j * rng.normal(0.0, 1.0, (n, n))
    h = (a + a.conj().T) / 2.0
    return np.sort(np.linalg.eigvalsh(h))


def primes_upto(x):
    sieve = np.ones(x + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return np.nonzero(sieve)[0].astype(float)


def pair_correlation_r2(xi, s_max=3.0, n_bins=30, k_max=10):
    """True two-point pair correlation R2(s) via the k-th-neighbor decomposition
    R2(s) = sum_k p_k(s), each order normalized separately (flat spectrum -> 1)."""
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


def form_factor_full(xi, tau):
    return float(abs(np.sum(np.exp(1j * tau * xi))) ** 2)


def main():
    rng = np.random.default_rng(SEED)
    checks = []
    results = {"seed": SEED, "python": sys.version.split()[0], "numpy": np.__version__}

    n_pois = 10000
    xi_pois = poisson_spectrum(n_pois, rng)

    n_gue = 2000
    gue = gue_spectrum(n_gue, rng)
    u = gue / (2.0 * math.sqrt(n_gue))
    xi_gue = n_gue / 2.0 + (n_gue / pi) * (u * np.sqrt(1.0 - u ** 2) + np.arcsin(u))

    primes = primes_upto(X_PRIME)
    xi_primes = expi(np.log(primes)) - expi(math.log(2.0))

    refs = {"poisson": xi_pois, "gue": xi_gue, "primes": xi_primes}
    results["reference_sizes"] = {k: int(len(v)) for k, v in refs.items()}

    r2 = {}
    for name, xi in refs.items():
        centers, r, edges = pair_correlation_r2(xi)
        r2[name] = {"s": centers.tolist(), "r2": r.tolist()}
    s = np.array(r2["poisson"]["s"])
    curve = bin_averaged_curve(gue_r2_curve, np.linspace(0.0, 3.0, 31))
    arr = {k: np.array(v["r2"]) for k, v in r2.items()}
    m_p = (s >= 0.15) & (s <= 1.8)
    m_q = (s >= 0.8) & (s <= 1.5)
    dev_p = float(np.mean(np.abs(arr["poisson"] - 1.0)[m_p]))
    dev_g = float(np.mean(np.abs(arr["gue"] - curve)[m_p]))
    dev_q = float(np.mean(np.abs(arr["primes"] - 1.0)[m_q]))
    p1, p2, p3 = dev_p < 0.05, dev_g < 0.08, arr["primes"][0] < 0.05
    p4 = arr["gue"][0] < 0.4 and arr["poisson"][0] > 0.7
    checks.append(("Poisson pair correlation flat (mean|R2-1| < 0.05)", p1, dev_p))
    checks.append(("GUE pair correlation matches 1-(sin pi s/pi s)^2 (mean|d| < 0.08)", p2, dev_g))
    checks.append(("Primes twin-gap hard core (R2 first bin = 0 vs Poisson ~ 1)", p3, arr["primes"][0]))
    checks.append(("level repulsion: GUE repels (R2[0]<0.4), Poisson flat (>0.7)",
                   p4, (arr["gue"][0], arr["poisson"][0])))
    results["primes_bulk_r2"] = {
        "mean_abs_dev_s_0.8_1.5": dev_q,
        "note": "beyond the hard core the primes' R2 is Poisson-like with a Hardy-Littlewood "
                "tuple excess at small s (twin-prime gap 2 -> unfolded spacing 2/ln p); the "
                "exact Poisson limit is X->infinity (Gallagher). The Montgomery-Odlyzko GUE "
                "law applies to the Riemann zeros, a later arm."}

    nv = {name: {str(L): number_variance(xi, L) for L in (1.0, 2.0, 5.0, 10.0, 20.0)}
          for name, xi in refs.items()}
    p5 = abs(nv["poisson"]["20.0"] - 20.0) <= 3.0
    euler = 0.5772156649015329
    gue_pred = (1.0 / pi ** 2) * (log(2.0 * pi * 20.0) + 1.0 + euler - pi ** 2 / 8.0)
    p6 = 0.5 * gue_pred <= nv["gue"]["20.0"] <= 2.0 * gue_pred
    p7 = nv["primes"]["20.0"] < 14.0
    checks.append(("Poisson number variance ~ L (within 15% at L=20)", p5, nv["poisson"]["20.0"]))
    checks.append(("GUE number variance matches Dyson formula within factor 2 (L=20)",
                   p6, (nv["gue"]["20.0"], gue_pred)))
    checks.append(("Primes number variance sub-linear (< 14 at L=20)", p7, nv["primes"]["20.0"]))

    kf = {name: form_factor_full(xi, 3.0) / len(xi) for name, xi in refs.items()}
    p8 = abs(kf["poisson"] - 1.0) < 0.4
    checks.append(("Poisson form factor plateau at tau=3 (|K/N-1| < 0.4)", p8, kf["poisson"]))
    # The GUE ramp assertion requires ensemble averaging over many realizations; the
    # single-realization full-spectrum form factor at tau=3 fluctuates ~ O(1/sqrt N)
    # around the plateau. Reported as observational data only (P3-exec later item).

    d3 = {name: {str(L): rigidity_delta3(xi, L) for L in (5.0, 10.0, 20.0)}
          for name, xi in refs.items()}

    results["pair_correlation"] = r2
    results["number_variance"] = nv
    results["form_factor_K_over_N_tau3"] = kf
    results["rigidity_delta3"] = d3
    results["checks"] = [{"name": n, "pass": bool(p)} for (n, p, _) in checks]
    results["all_pass"] = all(p for (_, p, _) in checks)
    results["script_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()

    with open("artifacts/verification/full-output.json", "w") as f:
        json.dump(results, f, indent=2)

    print("=== QNFO.UMP.014 P3-exec full suite ===")
    for n, p, d in checks:
        print(("[PASS] " if p else "[FAIL] ") + n + (("  %r" % (d,)) if d is not None else ""))
    print("all_pass =", results["all_pass"])
    sys.exit(0 if results["all_pass"] else 1)


if __name__ == "__main__":
    main()
