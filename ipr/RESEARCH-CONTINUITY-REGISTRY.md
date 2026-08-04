# RESEARCH-CONTINUITY-REGISTRY — IPR (Invariant Patterns Reframing)

**WBS: QNFO.UMP.003** | **DOI: 10.5281/zenodo.21785893**  
**Branch: ump/paper/ipr** | **Created: 2026-08-04**  
**Source Note: D:\Obsidian\notes\v1\2026\08\04\_26216024446.md (136,710 chars)**  
**Living document — must be maintained, updated, and followed up on quarterly.**

---

## 1. PAPER METADATA

| Field | Value |
|:------|:------|
| Title | Invariant Patterns and the Adelic Refactoring of Fundamental Physics |
| Author | Rowan Brad Quni-Gudzinas |
| Date | 2026-08-04 |
| DOI | 10.5281/zenodo.21785893 |
| Status | published |
| WBS | QNFO.UMP.003 |
| Repo | QNFO/ultrametric-physics |
| Branch | ump/paper/ipr |
| Deliverables | paper.md (42 KB), paper.pdf (544 KB), summary-analysis.md (29 KB), ecosystem-mapping.md (27 KB), redteam-audit-v2.md (43 KB), dialogue-continuation.md (13 KB) |

---

## 2. FALSIFIABLE PREDICTIONS

### P1 — Modified Photon Dispersion (Lorentz Violation)

**Claim:** Photon dispersion relation modified by adelic defect parameter ξ at Planck scale:

$$\omega^2 = k^2 \pm \xi \frac{k^3}{M_P}$$

where ξ = Σ_{p ≤ P} p^{-1} for some cutoff P (exact form TBD).

**Falsification condition:** If Fermi-LAT, CTA, or future gamma-ray observatories constrain Lorentz violation parameter η < ξ at 5σ confidence, P1 is falsified.

**Timescale:** CTA first light ~2026–2027; competitive constraints within 3–5 years.

**Status:** [NOT TESTED]

---

### P2 — Log-Periodic DM Power Spectrum Oscillations (FULCRUM PREDICTION)

**Claim:** Dark matter P(k) carries log-periodic modulations at prime frequencies:

$$P(k) = P_{\Lambda\text{CDM}}(k) \times \left[1 + \sum_{p \in \{2,3,5,7\}} a_p \cos\left(\frac{2\pi \ln k}{\ln p} + \phi_p\right)\right]$$

with amplitudes a_2 ≈ 0.02, a_3 ≈ 0.01, a_5 ≈ 0.005, a_7 ≈ 0.002.

**Falsification condition:** If Euclid or DESI P(k) measurements at 0.001 ≤ k ≤ 1 h/Mpc rule out a_p at the predicted amplitudes with 3σ confidence, P2 is falsified. Absence of ANY log-periodic signal at ANY prime frequency at 5σ confidence also falsifies P2.

**Timescale:** Euclid DR1 ~2026–2027; DESI Y5 ~2028.

**Status:** [NOT TESTED] — designated FULCRUM PREDICTION (P2 is the single most discriminating test)

---

### P3 — Black Hole Echoes

**Claim:** p-adic structure near BH horizon produces echoes at time delays:

$$\Delta t \sim 4M \ln p$$

for low primes p, with specific relative amplitudes.

**Falsification condition:** If LIGO-Virgo-KAGRA O4/O5 data, analysed with the predicted echo template, yield Bayes factor < 1/100 favouring echo model over no-echo null model, P3 is falsified.

**Timescale:** O4 ongoing; O5 ~2027–2029.

**Status:** [NOT TESTED]

---

## 3. FRONTIER RESEARCH QUESTIONS

### FQ1 — Distinction Path Integral (Paper §9, RQ1)
Formulate the distinction path integral rigorously: define measure on adelic graph configurations, compute partition function in simplest non-trivial case.
- **Disconfirmation:** If no well-defined measure exists for any non-trivial graph after rigorous mathematical analysis.

### FQ2 — Lorentzian Signature Emergence (Paper §9, RQ2)
Derive Lorentzian signature from analytic properties of adelic path integral saddle points.
- **Disconfirmation:** If saddle-point analysis of the simplest adelic action yields only Euclidean or degenerate signatures.

### FQ3 — Cosmological Constant (Paper §9, RQ3)
Compute cosmological constant from the adelic action; show it yields small positive vacuum energy.
- **Disconfirmation:** If computed CC is zero, negative, or 120 orders of magnitude too large.

### FQ4 — P(k) Template (Paper §9, RQ4)
Derive the log-periodic oscillation template from the adelic action for direct comparison with survey data.
- **Disconfirmation:** If the template contains more than 2 free parameters per prime or cannot be distinguished from ΛCDM.

### FQ5 — BH Echo Search (Paper §9, RQ5)
Implement the predicted echo pattern and search public LIGO data. Place upper limits or find evidence.
- **Disconfirmation:** See P3 above.

### FQ6 — Adelic Standard Model (Paper §9, RQ6)
Choose a reductive group G based on distinction graph topology; compute its automorphic spectrum.
- **Disconfirmation:** If no choice of G reproduces chiral fermion content and gauge group of SM.

### FQ7 — Primes from Distinction (Paper §9, RQ7)
Prove rigorously that the standard primes emerge from iterative distinction calculus.
- **Disconfirmation:** If distinction calculus generates a non-isomorphic 'prime' set, or fails to generate primes at all.

### FQ8 — Prime-to-Gauge Group Mapping (Dialogue Turn 13)
Conjecture: SM gauge group emerges from Galois group of maximal abelian extension of Q, filtered by ramification at {2,3,5}, with 2→SU(2)L, 3→SU(3)c, 5→U(1)Y.
- **Disconfirmation:** If coupling unification pattern contradicts this assignment.

### FQ9 — Distinction Hamiltonian de Sitter (Dialogue Turn 14, Open Q3)
Does the toy distinction Hamiltonian H = Σ_v (1 - Π_e |w_e|_v)^2 + λ·Re(Holonomy) support de Sitter solutions?
- **Disconfirmation:** If numeric simulation of finite Bruhat-Tits tree yields only AdS or Minkowski solutions.

### FQ10 — Standard Primes from LoF (Dialogue Turn 17, Open Q1)
Derive standard primes from Laws of Form re-entry graph. This is the PILLAR-2→PILLAR-1 bridge.
- **Disconfirmation:** If LoF re-entry generates a non-isomorphic arithmetic.

### FQ11 — Fermion Generations Bound (Dialogue Open Q5)
Is there a computable bound on number of fermion generations from the adelic action?
- **Disconfirmation:** If bound > 3 or unbounded, or if no bound can be derived.

### FQ12 — α Period Computation (Dialogue Turn 18)
Compute α^{-1} = ∮_C ω as a period of a canonical differential on the idele class group.
- **Disconfirmation:** If no such computation possible within 5 years (2029 deadline). Key calibration: if α^{-1} cannot be computed to within 1% of 137.036 by 2029, the framework's dimensionless-constant claim is empty.

---

## 4. PRE-REGISTRATION SCAFFOLDS

### REG-IPR-001: Euclid/DESI Log-Periodic Search

**Pre-registration date:** 2026-08-04  
**Hypothesis:** Dark matter P(k) contains log-periodic oscillations at frequencies ln p for p ∈ {2,3,5,7}, with amplitudes a_p ∝ p^{-s} (s ≈ 1).

**Null hypothesis:** No log-periodic structure beyond ΛCDM expectations.

**Measurement protocol:**
1. Obtain Euclid DR1 or DESI Y5 P(k) data
2. Fit ΛCDM + oscillatory template with fixed frequencies at p ∈ {2,3,5,7}
3. Compute Bayes factor BF = P(data|H1)/P(data|H0)
4. BF > 10 → evidence for prediction; BF < 0.1 → falsification

**Falsification condition:** BF < 0.1 for the full template OR individual a_p amplitudes excluded at 3σ.

**Status:** AWAITING DATA (Euclid DR1 ~2026–2027; DESI Y5 ~2028)

---

### REG-IPR-002: LIGO O4/O5 Black Hole Echo Search

**Pre-registration date:** 2026-08-04  
**Hypothesis:** Black hole ringdown contains secondary echoes at Δt ∼ 4M ln p for low primes.

**Null hypothesis:** No echoes beyond instrumental noise and standard ringdown.

**Measurement protocol:**
1. Download public LIGO-Virgo-KAGRA O4 strain data
2. Apply matched-filter search with echo template (delays at p=2,3,5,7)
3. Compute Bayes factor vs. no-echo null model
4. Report combined BF across all O4 events

**Falsification condition:** BF < 0.01 for echo model across combined O4 event set.

**Status:** AWAITING DATA (O4 ongoing; O5 ~2027–2029)

---

### REG-IPR-003: Quasiparticle Criterion — Mass Valuation Test

**Pre-registration date:** 2026-08-04  
**Hypothesis:** Compton number ν = m_P/m for fundamental particles has v_p(ν) ≠ 0 for all primes p ≤ p_max; quasiparticles have v_p(ν) = 0 for most primes.

**Null hypothesis:** p-adic valuations of Compton numbers are random/uniform with no structural distinction.

**Measurement protocol:**
1. Compile measured masses of all SM particles and known quasiparticles (phonons, magnons, etc.)
2. Compute ν = m_P/m for each to experimental precision
3. Compute v_p(ν) for first 20 primes
4. Apply KS test: are fundamental particle valuations drawn from different distribution than quasiparticle valuations?

**Falsification condition:** KS test p > 0.05 (no significant difference between distributions).

**Status:** EXECUTED 2026-08-04 — NULL RESULT. Criterion does not discriminate (see Section 4.1 RESULT).

---

## 5. CALIBRATION PREDICTIONS (time-bounded)

| ID | Prediction | Deadline | Status |
|:---|:-----------|:---------|:-------|
| CAL-IPR-01 | Euclid/DESI data confirms or rules out a_2 ≥ 0.02 at 3σ | 2028-12-31 | PENDING |
| CAL-IPR-02 | LIGO O4/O5 combined echo search yields definitive Bayes factor | 2029-12-31 | PENDING |
| CAL-IPR-03 | α^{-1} computation reaches within 1% of 137.036 from adelic period | 2029-08-04 | PENDING |
| CAL-IPR-04 | arXiv/INSPIRE records ≥1 external citation of IPR paper by non-QNFO author | 2028-08-04 | PENDING |
| CAL-IPR-05 | Primes-from-LoF derivation published in peer-reviewed mathematics journal | 2030-12-31 | PENDING |

---

## 6. PRIORITIZED NEXT ACTIONS

| # | Action | Priority | Effort | Depends On |
|:--|:-------|:---------|:-------|:-----------|
| 1 | **REG-IPR-003: Compute v_p(masses) for SM particles** | HIGH | Low (1 day) | PDG mass table |
| 2 | **Implement Bruhat-Tits distinction simulation** (toy Hamiltonian, Toy Turn 14) | HIGH | Medium (1 week) | Python, NumPy |
| 3 | **Fit DM P(k) template to Euclid mocks** (validate analysis pipeline before real data) | HIGH | Medium (1 week) | Euclid mock catalogs |
| 4 | **Resolve ξ cutoff P** (determine exact form of Lorentz violation parameter) | MEDIUM | Medium | Toy simulation results |
| 5 | **D1 living-paper insert** (paper body_md + metadata into papers table) | MEDIUM | Low (1 hour) | D1 access |
| 6 | **KG node creation** (create Paper node, link to UMP/SLB/INM program nodes) | MEDIUM | Low (1 hour) | KG access |
| 7 | **Update paper.md YAML in Zenodo** (if any corrections found) | LOW | Low | Newversion if needed |
| 8 | **LIGO O4 echo search** (requires access to strain data + template construction) | MEDIUM | High (2 weeks) | Template, GWpy |
| 9 | **α period computation attempt** (requires rigorous definition of moduli space) | LOW | High (months) | FQ1, FQ7 resolution |

---


### REG-IPR-003 RESULT (COMPUTED 2026-08-04) — NULL / DISCRIMINATION-FAILURE

**Status:** EXECUTED. Verdict: the pre-registered criterion does NOT discriminate
fundamental particles from quasiparticles using real-world measured masses.

**Computation:** PDG 2024 central masses (MeV/c^2); nu = m_P/m as exact Fraction
from decimal string; v_p for first 30 primes. m_P = 1.22091e22 MeV.

| particle | nu = mP/m | v2 | v3 | v5 | v7 | v11 | v13 | #nonzero/30 | fully 5-smooth |
|:---------|:----------|:---|:---|:---|:---|:----|:----|:-----------:|:--------------|
| W | 6.1e22 | 17 | 1 | 18 | 0 | 0 | 0 | 3 | NO |
| Z | 3.05e22 | 16 | 1 | 18 | -1 | 0 | 0 | 5 | NO |
| Higgs | 1.6e22/167 | 16 | 0 | 14 | 0 | 0 | 0 | 2 | NO |
| electron | 2.44e22 | 25 | 1 | 24 | -2 | -1 | 0 | 6 | NO |
| muon | 8.14e22 | 24 | -1 | 23 | 0 | 0 | 0 | 3 | NO |
| tau | 6.1e22 | 18 | 1 | 19 | 0 | 0 | 0 | 3 | NO |
| up | 5.09e22 | 16 | -2 | 19 | 0 | 0 | 0 | 3 | NO |
| down | 1.22e22 | 19 | 1 | 19 | 0 | 0 | 0 | 3 | NO |
| strange | 6.1e22 | 17 | 1 | 18 | 0 | 0 | 0 | 3 | NO |
| charm | 1.22e21 | 16 | 1 | 16 | 0 | 0 | 0 | 3 | NO |
| bottom | 6.1e20/2 | 15 | 1 | 16 | 0 | -1 | 0 | 5 | NO |
| top | 1.22e21 | 16 | 1 | 16 | -1 | 0 | 0 | 4 | NO |
| proton | 2.54e22 | 21 | -2 | 25 | 0 | -1 | 0 | 5 | NO |
| neutron | 8.14e22 | 24 | 0 | 23 | -2 | 0 | 0 | 3 | NO |

**Fully 5-smooth: 0/14. Denominator 5-smooth: 1/14.**

**Methodology findings (3):**
1. **[DECIMAL-ARTIFACT]** v2/v5 valuations are inflated by base-10 decimal
   representation: m_P = 122091 x 10^17 and measured masses are decimal strings,
   so denominators carry 2^k 5^k from 10^k. The {2,3,5}-dominance is inherited
   from base 10, NOT from any physical prime structure. Removing base-10
   factors leaves representation-residual valuations (electron den: {7:2, 11:1, 67:1})
   that depend on the DIGIT STRING, not the particle.
2. **[IMPOSSIBLE-CRITERION]** The dialogue-continuation criterion "v_p(nu) != 0
   for ALL primes up to p_max" is mathematically IMPOSSIBLE for any rational:
   a rational has v_p = 0 for all but finitely many primes (finite support).
   As stated, it would disqualify every rational — including all SM particles.
   The criterion is self-refuting as written.
3. **[NO-DISCRIMINATION]** With real measured masses (real-valued, not exact
   rationals), nu is not an exact rational; valuations are representation-dependent.
   Particle vs quasiparticle discrimination cannot be performed on PDG data.

**Revised criterion (proposal for registry):** A meaningful test requires a
theory that predicts the EXACT rational nu (e.g., from the adelic action), then
checks whether measured masses match the rational to within experimental error.
Valuations computed from measured decimals carry no physical content.

**BP-3 numerlogy gate:** The apparent 5-smooth dominance is CONSISTENT WITH
LOOK-ELSEWHERE ARTIFACT (base-10), not evidence for the Pythagorean semigroup.

**CAL-IPR-03 linkage:** This null result does NOT affect the alpha period
computation (different claim), but strengthens the requirement that any
dimensionless-constant claim must produce exact rational predictions.

**Status update:** REG-IPR-003 = EXECUTED, NULL RESULT (criterion failure).
Registry next action #1 (mass valuation test) marked COMPLETE-WITH-NULL.

## 7. CROSS-REFERENCE TO OTHER PROJECTS

| Project | WBS | Relationship |
|:--------|:----|:------------|
| ODR Thesis | QNFO.UMP.001 | IPR extends ODR's Compton-BT synthesis with full paper treatment; shares RQs 1-7 |
| Consilient Gap Synthesis | QNFO.CON.001 | IPR's Silo Cost table is a direct application of the Consilience Gate (KIF-29); 5-domain, 40-110yr gaps |
| Quasiparticle Extension | QNFO.UMP.002 | IPR's particle-vs-quasiparticle criterion (FQ8) intersects QP extension's frequency valuation theory |
| Non-Anthropocentric Natural Units | QNFO.UMP.xxx | IPR's Ostrowski Dimensionless Mandate cites this as canonical reference [8] |
| Laws of Form — SLB | QNFO.SLB.001 | FQ10 (primes from distinction) is the critical bridge between Pillars 1 and 2 |

---

## 8. SESSION CLOSEOUT CHECKLIST

- [x] Paper published (Zenodo DOI 10.5281/zenodo.21785893)
- [x] PDF built (544 KB, 238 math elements, puppeteer-core CDP)
- [x] Git branch created (ump/paper/ipr on QNFO/ultrametric-physics)
- [x] All 5 deliverables committed and pushed
- [x] Certainty labels added (6 [speculative] + 5 [established])
- [x] 'Fundamental' operationally defined (footnote in paper)
- [x] Mojibake scan passed (0 hits across all files)
- [x] P5.FRESH gate passed (Zenodo YAML verified correct)
- [x] RESEARCH-CONTINUITY-REGISTRY.md created (this file)
- [ ] D1 living-paper entry inserted and verified
- [ ] KG Paper node created and linked
- [ ] Papers-server verification (curl papers.qnfo.org)
- [ ] REG-IPR-001, 002, 003 scaffolds registered in central registry
- [ ] Update QNFO.RES master registry with IPR entry

**Session ID for audit trail:** 1tz85-vMiqh2TyFySznBA  
**Next review date:** 2026-11-04 (quarterly follow-up)

---

*End of registry. Update with each completed action, new prediction, or disconfirmation.*
