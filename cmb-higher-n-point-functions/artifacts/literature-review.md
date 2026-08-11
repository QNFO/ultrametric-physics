# Literature Review + KIF-18 Mandatory Symmetry Template — QNFO.UMP.007

**Date:** 2026-08-12 · **Phase:** P2 · **Gate:** KIF-18 (HARD — both sections mandatory)

---

## 1. Summary of the literature landscape

The direct search space for p-adic log-periodic signatures in CMB higher-n correlators is
**genuinely open**: OpenAlex (exact conjunction), Crossref, Zenodo, Europe PMC, and arXiv
all return zero direct hits for the specific claim. The literature splits cleanly into
two established bodies: (a) p-adic/ultrametric cosmology and mathematics (Djordjević,
Dragović, Manin, Ebert; Avetisov, Khrennikov) and (b) resonant-feature non-Gaussianity in
standard inflation (Chen–Easther–Lim lineage: Barnaby, Barnaby–Cline, Leblond–Pajer). The
**junction between the two — p-adic structure tested via higher-n CMB statistics — is the
unoccupied niche this project occupies.**

---

## 2. Mandatory Symmetry Template (KIF-18, HARD)

### 2.1 Where External Literature Supports [Claim: p-adic log-periodic signatures may appear in CMB higher-n correlators]

1. **p-adic cosmology is an established external program.** Djordjević–Dragović–Nešić (2002,
   DOI 10.1016/s0920-5632(01)01613-9) and Dragović (2022, DOI 10.3390/sym14010073) construct
   p-adic matter and quantum-cosmology models with concrete observable programs. The claim
   builds on a live, non-isolated formalism. [primary]
2. **Ultrametric/tree structure has independently emerged in cosmology.** Harlow–Shenker–Stanford
   (2012, DOI 10.1103/physrevd.85.063516) derive an ultrametric tree from eternal inflation —
   a *different* mechanism, same structural signature, supporting the plausibility that
   hierarchical (log-periodic) structure can arise in cosmological observables without being
   pathological. [primary — methodologically independent line]
3. **Native ultrametricity is generic in complex systems.** Avetisov–Krapivsky–Nechaev (2015,
   DOI 10.1088/1751-8113/49/3/035101) show ultrametric structure emerges in sparse random
   ensembles — supporting the prior that "hierarchical correlation" is a natural observable
   class, not an exotic one. [primary]
4. **p-adic CFT provides a concrete correlator formalism.** Ebert–Sun–Zhang (2019,
   DOI 10.48550/arxiv.1911.06313) compute N-point functions in p-adic CFT; the higher-n
   correlator machinery exists to be translated to cosmology. [primary]
5. **Log-periodic spectral features are a studied, physical phenomenon** (the log-periodic
   literature generally — Sornette line, DSI in geophysics/complex systems), supporting the
   spectral-analysis methodology the project inherits from the QNFO 2-point protocol. [secondary]

### 2.2 Where External Literature Constrains or Contradicts [Claim: a detected p-adic bispectrum signature would be a p-adic detection]

> **MUST NOT be empty.** This section names the specific constraining evidence. It is not hedging;
> it defines the falsifiability boundary of the project.

1. **Resonant-feature inflation already predicts log-periodic non-Gaussian shapes.**
   Leblond–Pajer (2011, DOI 10.1088/1475-7516/2011/01/035) derive the *resonant trispectrum and a
   dozen more primordial N-point functions* from a standard single-field inflaton with an
   oscillating feature. The p-adic template is *not unique* as a log-periodic N-point shape:
   **without an orthogonality computation, a detected log-periodic bispectrum is degenerate with
   the resonant-features family and CANNOT be claimed as p-adic.** [primary — direct constraint]
2. **Non-local and particle-production inflation also produce large oscillatory NG.**
   Barnaby–Cline (2007, 2008; DOIs 10.1088/1475-7516/2007/07/017, 10.1088/1475-7516/2008/06/030)
   and Barnaby (2010, DOI 10.1103/physrevd.82.106009) show mechanisms in standard physics that
   generate exactly the class of signature the project would search for. The prior probability
   that a log-periodic bispectrum is of p-adic origin is therefore *low* unless the shape is
   radix-locked (Δlog_p = 1) AND amplitude-consistent with the 2-point null. [primary — direct constraint]
3. **The 2-point null is an internal constraint that bounds the amplitude.** QNFO's own
   published analysis (10.5281/zenodo.21205104) and CAL-03 bound A_LPO < 0.003 (95% CL) with log
   Bayes −5.14..−6.54. Any bispectrum detection whose implied amplitude is inconsistent with this
   bound contradicts the single-field ultrametric model (D2 in core-claim.md). External literature
   does not contradict this bound — it is the project's own disconfirmation condition. [internal — constraint]
4. **Look-elsewhere / trials factor is mandatory.** The search spans multiple primes p ∈ {2,3,5,7}
   and multiple shape families; without a BP-3 density gate, a marginal peak is
   [CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT]. External feature-search papers (e.g., the Planck
   resonant-features constraints) enforce the same discipline; the project must match it. [methodological constraint]
5. **Explicit no-constraining-evidence statement (partial):** No external publication directly
   addresses p-adic log-periodic CMB bispectrum signatures, so there is no external contradiction
   of the *specific* p-adic template — only the general degeneracy constraints above. [stated per
   KIF-18 "explicitly state no constraining evidence found" rule, for the narrow claim only]

**Symmetric-audit note (KIF-29):** the incumbents are graded with the same standard. ΛCDM +
resonant features explains log-periodic N-point shapes only by *adding* feature parameters (Δlog-odds
computed per template in P4); the p-adic template is likewise parameterized (ε_p, p, phase). Both
are graded on: pre-registration (✓ this project's OSF 2ndsz + core-claim.md), falsifiability gradient
(✓ D1/D2/D3), surprise accounting (P4, BP-3). No pro-incumbent bias: the resonant-feature family
absorbs the same observational space via added degrees of freedom that this project must count.

---

## 3. Gap-to-paper mapping (what P4 must resolve)

| Gap (from gap-analysis.md) | Literature that frames it | P4 action |
|:---------------------------|:--------------------------|:----------|
| G-1 p-adic bispectrum/trispectrum shape | C5-C8 (p-adic formalism), C8 (p-adic CFT correlators) | Derive template; closed form where possible |
| G-2 Orthogonality vs resonant features | C1-C4 (resonant family) | Shape-overlap projection onto Leblond–Pajer basis; Δlog-odds |
| G-3 Planck 2018 higher-n data | Planck 2018 NG papers (B8 + public products) | Build estimator pipeline |
| G-4 Quantitative amplitude prediction | C5-C6 (p-adic cosmology amplitudes) | Derive ε_p from framework — resolves CAL-03 blocker |
| G-5 Synthetic-signal injection | C1-C4 template library | Inject p-adic + resonant templates; recovery/sensitivity |
| G-6 Internal claim hygiene | due-diligence §1.3 | Publish null-based framing only |

---

## 4. Classification gate status

- Core: 9 (within 5-10) ✅
- Supporting: 12 (within 10-20) ✅
- Background: 8 (within 5-15) ✅
- Reject: 8 archived with reasons ✅
- KIF-18 template: BOTH sections populated ✅
- Phase 2 gate: **PASS**
