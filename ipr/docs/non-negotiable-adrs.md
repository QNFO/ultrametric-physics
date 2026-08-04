
# NON-NEGOTIABLE IMMUTABLE ADRs — QNFO/QWAV Governance Foundation

**Compiled:** 2026-08-04 | **Session:** 1tz85-vMiqh2TyFySznBA  
**Authority:** qnfo-core v1.12 §N-1, git-github v2.14 §Protected Repositories, governance_policies D1  
**Status:** Consolidated cross-reference register — all 9 ADRs identified with enforcement per skill.

---

## ADR Register

### ADR-2026-007 — WBS Code Convention (2026-08-04)
**Rule:** Every plan step, branch, tag, D1 row, and KG edge carries `{PORTFOLIO}.{PROG}.{NNN}.P{N}.T{N}.S{N}`.
**Enforced by:** qnfo-core §N-1 (canonical table), research §Phase 0.1 (branch naming), git-github §Branch Discipline, kaizen §Kaizen Pipeline, WBS-AGENT-PROTOCOL.md §2.
**Severity:** HARD — un-auditable without WBS codes.
**Anti-pattern:** WBS-NO-CODE (git-github v2.10), WBS-INVENT-CODE, WBS-STD-1/WBS-STD-2 (research v2.62).

### ADR-026 — Skills Repository Protection (2026-07-18; amended 2026-08-04)
**Rule:** `QNFO/qnfo-skills` contains ONLY skill definitions. NEVER place project data, publications, research artifacts, governance documents, tags, or GitHub Releases there.
**Enforced by:** git-github §Protected Repositories (REPO-TARGET GATE), qnfo-core §N-1 (routing table).
**Severity:** HARD — violation = fabrication-level offense (qnfo-core Rule 14).
**Incidents:** (1) research-project tags + Zenodo-DOI Release committed; (2) 6 stale project tags pre-dating remediation; (3) post-remediation tags/residual refs.

### ADR-010 — QNFO Not an Acronym (2026-07-30)
**Rule:** QNFO, ODR, QWAV, and similar project identifiers are proper names, NOT acronyms. Never expand them. Any expansion without explicit user confirmation is a fabrication.
**Enforced by:** qnfo-core §0.0 Proprietary Nomenclature Integrity (v1.7).
**Severity:** HARD — same class as fabricated authors/DOIs.
**Incidents:** QNFO → "Quantum Number Field Ontology" (2026-07-30); ODR → "Ontological Distribution of Reality" (2026-08-03).

### ADR-021 — Thin-Client Mandate (2026-07-18)
**Rule:** No local project files outside `C:\Users\LENOVO\.deepchat\skills\` and `%TEMP%`. Code lives in git repos; data lives in R2/D1/Vectorize.
**Enforced by:** system skill (file-hygiene mandate), git-github §TEMP Volatility (KIF-32 HARD GATE).
**Severity:** HARD — thin-client architecture, bloat-cleanup enforcement.

### ADR-025 — Thin-Client Cleanup (2026-07-18)
**Rule:** All temp clones deleted same-turn. Never assume temp files persist across turns.
**Enforced by:** git-github §TEMP Volatility (SAME-TURN-COMMIT mandate), research TEMP-VOLATILITY-2.
**Severity:** HARD — data loss risk (KIF-32 incident).

### Python-First Execution Mandate (2026-07-31)
**Rule:** Python is the ONLY execution environment. PowerShell is permanently deleted. Zero tolerance.
**Enforced by:** qnfo-core §0.6, windows-command-patterns S0.0/S1.0.
**Severity:** HARD — PowerShell caused 25+ documented failures (PSFAIL.md).

### Ostrowski Dimensionless Mandate (2026-08-01)
**Rule:** ALL physics formulas in dimensionless Planck units. Dimensional formulas must include dimensionless equivalent + Ostrowski rationale.
**Enforced by:** qnfo-core §0.7 (v1.4, 4 traps), research §Phase 5 BP-1 fit-verify gate.
**Severity:** HARD — dimensional formulas without rationales are style violations equivalent to banned words.

### Research Integrity Mandate (2026-07-30)
**Rule:** ALL content factual, not promotional. Evidence over enthusiasm. Certainty calibration on every non-textbook claim. Falsifiability conditions required.
**Enforced by:** qnfo-core §0.0 (v1.7), research BP-1 through BP-10 gates, kaizen Phase R (retrospective audit).
**Severity:** HARD — foundation of QNFO publishing.

### UTF-8 Source Encoding Mandate (2026-07-31)
**Rule:** ALL text must pass mojibake scan before commit/publish/insert. Zero BOM, zero U+FFFD, zero U+FFFF.
**Enforced by:** qnfo-core §0.2 (HARD GATE), research §Phase 5 Publication Language Gate, kaizen Phase 4 Verification Gate.
**Severity:** HARD — mojibake poisons every downstream system (D1, Zenodo, GitHub, search).

---

## Cross-Reference: Skill Enforcement Coverage

| ADR | qnfo-core | research | git-github | wcp | kaizen | system | cloudflare |
|:----|:---------|:---------|:-----------|:----|:------|:------|:-----------|
| 007 (WBS) | §N-1 | §P0.1 | §Branch | — | §Pipeline | — | — |
| 026 (Skills) | §N-1 | — | §Protected | — | — | — | — |
| 010 (Acronym) | §0.0 | — | — | — | — | — | — |
| 021 (Thin) | — | — | §TEMP | — | — | §Hygiene | — |
| 025 (Cleanup) | — | TEMP-2 | §TEMP | — | — | — | — |
| Python-First | §0.6 | — | — | S0.0/S1.0 | — | — | — |
| Ostrowski | §0.7 | §P5-BP | — | — | — | — | — |
| Research Integrity | §0.0 | BP-1..10 | — | — | Phase R | — | — |
| UTF-8 | §0.2 | §P5-Lang | — | — | Phase 4 | — | — |

**Coverage:** 9/9 ADRs have primary enforcement in at least one skill. No orphan ADRs.
**Gaps:** None identified. All ADRs are enforced by the skill that owns the domain.
**Last audit:** 2026-08-04 (this compilation).

---

## Governance

This register is the consolidated source of truth for QNFO/QWAV non-negotiable ADRs.
Updates occur when:
- A new ADR is ratified (numbered, dated, with incident record)
- An existing ADR is amended or retired
- A new enforcement skill is added
- Annual audit (next: 2027-08-04)

All ADRs are immutable — they can be amended but never silently retired.
Amendment requires: (a) go-back revision to the original ADR text, or (b) a superseding ADR with cross-reference.
