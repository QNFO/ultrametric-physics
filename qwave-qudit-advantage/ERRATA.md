# ERRATA: The Qudit Advantage (QNFO.UMP.005)

**DOI:** 10.5281/zenodo.21827737 (v0.4, published 2026-08-06)
**ERRATA version:** v1.0
**Date:** 2026-08-10
**STATUS:** PUBLISHED — corrected in v0.5 (DOI 10.5281/zenodo.21878856)

---

## AI-QUALITY-GATE-1 Audit Results

This paper was audited against the AI-QUALITY-GATE-1 forensic quality gate
(research skill v2.91, 2026-08-10). The gate requires AI-generated/AI-assisted
papers to clear five markers before publication. Findings:

### Marker (i): Elementary physics/energy-budget error — FAIL

**Section 3.3, paragraph 4:**

> "For the JPCUB model, we set $P_{\text{decode}}^{\text{qudit}} \approx 0$ as a **conservative upper bound** [speculative — decoder implementation energy not yet measured]."

**Error:** Zero is a **lower bound**, not an upper bound. A conservative upper bound
would be a high (worst-case) value — e.g., 10–100 W like the classical MWPM decoder.
Setting $P_{\text{decode}} \approx 0$ and labeling it "conservative upper bound" is
an elementary error in the direction of bounds — it makes the estimate
non-conservative by construction while presenting it as safe.

**Impact:** The JPCUB estimate of $\sim 10^{-5}$ J/sol (Section 3.5) depends on
$P_{\text{decode}} \approx 0$. The 5,000× advantage claim is inflated by at least
the missing decoder power. If the decoder actually consumes even 1 W, the JPCUB
value would increase by a factor depending on $t_{\text{sol}}$.

**Correction:** Replace $P_{\text{decode}}^{\text{qudit}} \approx 0$ with an
explicit estimate or range, properly labeled. Alternatively, state:
"$P_{\text{decode}}^{\text{qudit}} = 0$ is used here as a **lower bound** on
the total system power — actual JPCUB values will be HIGHER (worse) when decoder
power is included. This estimate is therefore optimistic."

### Marker (ii): Synthetic/unresolvable citation anchors — FAIL

**Citations `[@C5_jpcub_p0]` and `[@C6_jpcub_landscape_v2]`:**

These are QNFO-internal prefixed keys that do not resolve to externally published
records. They appear 8+ times throughout the paper (Sections 1, 2.1, 3.5, 3.6,
4.2, Declarations). A reader following these citations cannot locate a resolvable
paper — the keys are LLM prompt-template artifacts.

Additionally, these violate **INTERNAL-REF-1** (research skill v2.84): published
papers must not reference internal QNFO programs or processes by name. "JPCUB P0
protocol" and "JPCUB Competitive Landscape v2.0" are QNFO-internal program artifacts
not appropriate for external publication.

**Correction:** Replace `[@C5_jpcub_p0]` and `[@C6_jpcub_landscape_v2]` with
DOI-based citations of the published JPCUB standard and landscape papers when
they have been externally published. Until then, the JPCUB framework description
should be self-contained in this paper's Section 2.1 with explicit parameter
definitions and an acknowledgment that the framework has not been externally
validated.

### Marker (iii): Scaffold overload — FAIL

The paper body contains LLM prompt-template artifacts not standard in academic
publishing:

- `[PHILOSOPHY]` meta-tags preceding prose paragraphs (Sections 1, 4.3, 6)
- `[speculative]` hedge tags embedded in prose (Sections 1.2, 3.3, 3.5, 3.7,
  5.1, 5.2)
- Rigid Calibration Register scaffolding with `[CHECK: YYYY]` / `Strength: [STRONG]`
  / `Status: [PENDING]` brackets (Section 5.3)

These tags are structure from the LLM prompt template that generated the paper,
not authorial voice. They signal AI-generation to readers and undermine the
paper's credibility.

**Correction:** Remove all `[PHILOSOPHY]`, `[speculative]`, and bracket-scaffold
tags. Replace speculative hedges with natural-language qualifiers ("This estimate
is provisional and has not been experimentally validated"). Replace Calibration
Register bracket format with standard academic language.

### Marker (iv): Over-explaining foundations / hand-waving novel integration — FAIL

The paper spends significant space on textbook-level explanations of well-known
concepts:

- Section 2.2: Explains Shannon's $\log_2 d$ factor from first principles
- Section 2.3: Explains ultrametric distance, Bruhat-Tits trees, radix tries in
  textbook style

While the novel integration — the mechanism by which ultrametric geometry produces
"passive error resilience" — receives only a single hand-waving sentence in
Section 3.3:

> "The environment naturally selects error clusters that are localized in the
> ultrametric hierarchy, and the tree structure passively separates them [speculative]."

No Hamiltonian, no error model, no mechanism is provided for the paper's central
physical claim. This is the textbook pattern of AI-generated science papers:
explain what's already known in detail, gloss over what's novel.

**Correction:** Either (a) provide a concrete physical mechanism with an explicit
Hamiltonian, error model, and scaling analysis for how the Bruhat-Tits tree geometry
produces passive error resilience, or (b) downgrade the "passive error resilience"
claim from a core factor to an open research question and remove it from the JPCUB
calculation until a mechanism exists.

### Marker (v): Self-referential metric claims without external validation — FAIL

Section 4.2 admits:

> "The JPCUB framework [@C5_jpcub_p0] has zero external citations or independent
> validations as of 2026-08-06. The reported qudit advantage inherits the framework's
> credibility."

The paper's entire quantitative claim — the $10^{-5}$ J/sol estimate, the 5,000×
advantage, the $d^* \approx 3$ crossover — depends on a metric with zero external
validation. The admission acknowledges the problem but does not resolve it; the
conclusion presents the JPCUB values as findings rather than as what they are:
internal estimates based on an unvalidated framework.

**Correction:** The paper's conclusion should be explicitly caveated: "This estimate
is based on the JPCUB framework, which has not been externally validated. Until
the JPCUB metric receives independent review and replication, the claimed qudit
advantage is a hypothesis for investigation, not a demonstrated result." The
abstract and conclusion should not present JPCUB values as findings.

---

## Additional Issues

### INTERNAL-REF-1 Violations

The paper references QNFO-internal program artifacts as if they are published standards:

- "JPCUB P0 protocol" (multiple references in Sections 1.2, 3.7, 4.2)
- "JPCUB Competitive Landscape v2.0" (Sections 1, 2.1, 3.5, 3.6)
- "QWAV" (Declarations — commercial interest disclosure is appropriate here)

**Correction:** Replace internal program references with self-contained descriptions
or citations of published records.

### P_decode Bound Direction (expanded from Marker i)

The bound-direction error is systematic: the paper presents multiple estimates as
"conservative" when they are in fact optimistic (lower-bound when upper-bound is
warranted, or vice versa). A systematic audit of all bound claims is recommended:

| Location | Claim | Error |
|:---------|:------|:------|
| §3.3 | $P_{\text{decode}} \approx 0$ as "conservative upper bound" | Zero is a lower bound |
| §3.5 | $f_{\text{OH}}(d) = (F_{\text{qubit}}/F_{\text{qudit}})^\alpha$ with $\alpha \approx 1$ | $\alpha = 1$ is the most optimistic assumption |
| §3.5 | $N_{\text{phys}}$ reduction by $\log_2 d$ without fidelity penalty cross-check | Assumes encoding benefit is realized without overhead validation |

---

## Correction Plan

1. **v0.5 newversion:** Apply all five AI-QUALITY-GATE-1 corrections above
2. **Zenodo:** Create newversion via deposit API, upload corrected `.md` + `.pdf` + `.html`
3. **KG:** Add CORRECTS edge from newversion to parent; mark parent as SUPERSEDED
4. **D1:** Update living-paper record with newversion body

---

## Pre-Registration of This ERRATA

This ERRATA.md is committed to `ump/paper/qwave-qudit-advantage` branch in
`QNFO/ultrametric-physics` before the newversion is published, per the ERRATA
ORDERING RULE (research v2.88): ERRATA writes the correction BEFORE the newversion
exists, with STATUS: PENDING. After the newversion publishes, STATUS is updated
to PUBLISHED and the newversion DOI is recorded.
