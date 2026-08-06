# Journal Submission Strategy — QNFO.UMP.005 (qwave-qudit-advantage)

**Replaces arXiv as the peer-review leg** — author has NO arXiv endorsement and targets journals directly (standing preference).
**Canonical preprint:** DOI 10.5281/zenodo.21827737 (v0.4) — already live on Zenodo, OpenAlex-indexed, papers.qnfo.org.
**Date:** 2026-08-06

---

## Why this works without arXiv

- Zenodo → DataCite → **OpenAlex auto-indexing** (your author `A5133504808` exists) gives the paper scholarly-index presence equivalent to an arXiv listing for discovery purposes.
- **Google Scholar** and **Semantic Scholar** pick up the DOI through CrossRef/OpenAlex.
- **PhilPapers** indexing enabled (keywords added 2026-08-06) for the philosophy-of-physics framing.
- Journal submission does NOT require arXiv presence — most quantum journals accept direct submission.

## Journal Shortlist (independent-researcher friendly)

| Journal | OA / APC | Fit | Notes |
|:--------|:---------|:----|:------|
| **Frontiers in Physics** (Quantum Computing section) | OA, APC | ★★★★★ | The qudit review you cite (Wang et al. 2020) was published here — same venue is a strong fit. Accepts speculative-but-rigorous theory. |
| **EPJ Quantum Technology** | OA, APC | ★★★★☆ | SpringerOpen — explicitly welcomes theory + benchmarking work. |
| **Quantum** (quantum-journal.org) | Diamond OA (free) | ★★★★☆ | High-status open-access venue; editorial board is the field's core. Rigorous review. |
| **Quantum Science and Technology** (IOP) | Hybrid | ★★★☆☆ | Good fit for benchmarking; APC waiver possible. |
| **AVS Quantum Science** | OA | ★★★☆☆ | Interdisciplinary — energy efficiency angle fits. |
| **Entropy** (MDPI) | OA, APC | ★★★☆☆ | Information-theoretic framing (Shannon, Landauer) fits well; fast review. |

**Recommendation:** submit to **Frontiers in Physics** first (same venue as the review you build on — reviewer pool likely to include the field's qudit researchers). Fallback: **EPJ Quantum Technology**. Highest-prestige option: **Quantum**.

## Submission Checklist (before sending)

1. **Author identity**: "Rowan Brad Quni-Gudzinas, Independent Researcher — QNFO", ORCID `0009-0002-4317-5604` (canonicalized name — same in Zenodo, ORCID, OpenAlex).
2. **Manuscript**: the v0.4 PDF is journal-formatted (A4, title page, abstract, numbered sections, declarations, 22 references) — ready for submission as-is.
3. **Falsifiability framing**: lead with the pre-registered disconfirmation condition in the cover letter — "the model invites adversarial validation; any d ≥ 3 qudit platform measuring JPCUB > 0.05 J/sol falsifies the claim." This is the paper's strongest peer-review asset.
4. **[speculative] labels**: keep them — they signal calibration, not weakness; reviewers respect explicit uncertainty.
5. **Preprint linkage**: state in the cover letter that a preprint exists at the Zenodo DOI (journal policies vary on preprint simultaneous posting; Zenodo is generally accepted).

## What to write in the cover letter

- One paragraph: what the paper does (JPCUB energy benchmark for qudit architectures vs 17 qubit platforms).
- One paragraph: why it matters (first joules-per-solution estimate for any qudit platform; energy efficiency is the unexplored axis of the qudit-vs-qubit debate).
- One paragraph: what you want from review (adversarial validation of the model assumptions; the pre-registered falsification condition is the invitation).
- One line: independence + ORCID + previous work (JPCUB P0, Landscape v2.0 — both DOI-linked).

## Anti-goal (do not do)

- Do NOT submit to venues requiring institutional affiliation or invited-only review (e.g., PRX Quantum's invited track) as the first attempt.
- Do NOT present the work as "validated" — it is a pre-registered, falsifiable model inviting validation.
- Do NOT list arXiv in the manuscript's citation/preprint fields — it is not there.

## Next actions

- [ ] User selects journal (recommendation: Frontiers in Physics)
- [ ] Draft cover letter (I can draft this on request)
- [ ] Submit via journal portal (needs user account)
- [ ] On acceptance: newversion v0.5 with journal cross-reference in metadata (`related_identifiers: isPublishedIn`)
