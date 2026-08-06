# ERRATA — qwave-qudit-advantage (QNFO.UMP.005)

**BP-4 Correction-on-Discovery record.**
**Canonical DOI:** 10.5281/zenodo.21827347 (v0.3) → **corrected in v0.4 (DOI 10.5281/zenodo.21827737, published 2026-08-06)**
**Date:** 2026-08-06

---

## Correction C1: Citation key mislabel (bibliographic metadata hygiene)

| Field | Before | After |
|:------|:-------|:------|
| Citation key (internal) | `S3_gokhale2023` | `S3_fischer2023` |
| Rendered author list | Laurin E. Fischer, Alessandro Chiesa, Francesco Tacchino, Daniel J. Egger, Stefano Carretta, Ivano Tavernelli (CORRECT — Crossref-verified at publish) | unchanged (correct) |
| DOI | 10.1103/prxquantum.4.030327 | unchanged (correct) |

**Severity:** SOFT-to-HARD boundary. The *rendered* bibliography was always correct (authors + DOI verified live against Crossref at publish time, per P3.AUTHOR-GATE). The defect is the internal citation key, which named a non-author (Gokhale) and could mislead any agent or citation harvester reading the source `.md`/`.bib` files. Discovered 2026-08-06 during outreach-letter author verification (the outreach letter had likewise addressed the wrong person — corrected before any send).

**Root cause:** the citation key was assigned from a Phase 2 literature-review memory (where "gokhale2023" was a recall error) rather than from the Crossref author list fetched in Phase 3. The P3.AUTHOR-GATE verified authors *inside* the bib entry but the *key* was never reconciled to the verified author.

**Correction applied:**
1. `references.bib`: key renamed `S3_gokhale2023` → `S3_fischer2023` (entry content unchanged — already correct)
2. `qwave-qudit-advantage.md`: in-text `[@S3_gokhale2023]` → `[@S3_fischer2023]` (Section 3.6)
3. `artifacts/citation-audit.md`, `literature-review.md`, `due-diligence.md`: key references updated
4. `artifacts/outreach-letters.md`: Letter 3 rewritten for Ivano Tavernelli (IBM Research Zurich, senior author) — the original draft addressed Prakash Gokhale (not an author of this paper)
5. Newversion v0.4 published with corrected source files (this ERRATA is the audit trail)

**Process lesson (kaizen candidate):** Phase 3 citation verification must also reconcile the *key* to the verified author list — a key naming a non-author is a bibliographic-hygiene defect even when the rendered entry is correct. Reference: research skill P3.AUTHOR-GATE / BP-4 correction-on-discovery.
