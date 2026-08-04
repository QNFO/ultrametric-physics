"""
consilience-mcp/server.py — FastMCP Server for the Universal Consilience Framework.

Implements tools for:
- translate_theorem: Run the Universal Consilience Prompt on any theorem
- phase_a_corpus_ingestion: Extract mathematical verbs from paper abstracts
- phase_b_cross_mapping: Translate a theorem across four domains
- phase_c_pattern_matching: Cluster translations into meta-principles, identify gaps
- phase_d_generative_transfer: Generate novel cross-domain theorems
- full_pipeline: Run phases A-D automatically

Design principle: This MCP server is a PROMPT ENGINE + STATE TRACKER.
It does NOT call an LLM itself — it returns structured prompts that the
calling agent (Claude/GPT/Gemini) will execute using its own reasoning.
Results are stored in a JSON-based session state for pipeline chaining.

WBS: QNFO.CON.002.P5.T1
"""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from typing import Any

from fastmcp import FastMCP

from prompt_templates import (
    PHASE_A_SYSTEM,
    PHASE_A_USER_TEMPLATE,
    PHASE_B_SYSTEM,
    PHASE_B_USER_TEMPLATE,
    PHASE_C_SYSTEM,
    PHASE_C_USER_TEMPLATE,
    PHASE_D_SYSTEM,
    PHASE_D_USER_TEMPLATE,
    UNIVERSAL_CONSILIENCE_SYSTEM,
    UNIVERSAL_CONSILIENCE_USER_TEMPLATE,
)

# ─── Server Initialization ─────────────────────────────────────────────────

mcp = FastMCP("Consilience Framework")

# ─── Session State ─────────────────────────────────────────────────────────

# In-memory session store. Replace with D1/Vectorize for production.
_sessions: dict[str, dict[str, Any]] = {}


def _get_or_create_session(session_id: str | None = None) -> tuple[str, dict[str, Any]]:
    """Return an existing session state or create a new one."""
    if session_id and session_id in _sessions:
        return session_id, _sessions[session_id]
    sid = session_id or str(uuid.uuid4())
    _sessions[sid] = {
        "phase": "init",
        "corpus": [],
        "theorems": [],
        "translations": [],
        "meta_principles": [],
        "gaps": [],
        "generated_theorems": [],
    }
    return sid, _sessions[sid]


# ─── Tool: translate_theorem ────────────────────────────────────────────────


@mcp.tool()
def translate_theorem(
    theorem_statement: str,
    theorem_name: str = "",
    session_id: str = "",
) -> dict[str, Any]:
    """Run the Universal Consilience Prompt on a given theorem.

    Translates a mathematical theorem into four domain lexicons:
    Physics, Computer Science, Cognitive Science, and Information Theory.

    Args:
        theorem_statement: The full mathematical statement of the theorem
        theorem_name: Optional short name for the theorem
        session_id: Optional session ID for stateful pipeline tracking

    Returns:
        Structured prompt + metadata for the calling LLM to execute.
        The calling agent should use this prompt to produce the translation.
    """
    if not theorem_statement or not theorem_statement.strip():
        raise ValueError("theorem_statement must be a non-empty string")

    sid, session = _get_or_create_session(session_id)

    system_prompt = UNIVERSAL_CONSILIENCE_SYSTEM
    user_prompt = UNIVERSAL_CONSILIENCE_USER_TEMPLATE.format(
        theorem_statement=theorem_statement
    )

    result = {
        "session_id": sid,
        "tool": "translate_theorem",
        "theorem_name": theorem_name or "unnamed_theorem",
        "theorem_statement": theorem_statement,
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "instruction": (
            "Feed the system_prompt and user_prompt to an LLM. "
            "The LLM MUST return valid JSON with keys: Core_Dynamic, "
            "Domain_Translations (Physics, Computer_Science, Cognitive_Science, "
            "Information_Theory), and Synthesis_Consilience."
        ),
        "expected_keys": [
            "Core_Dynamic",
            "Domain_Translations.Physics",
            "Domain_Translations.Computer_Science",
            "Domain_Translations.Cognitive_Science",
            "Domain_Translations.Information_Theory",
            "Synthesis_Consilience",
        ],
    }

    # Track in session
    session["theorems"].append(
        {"name": theorem_name, "statement": theorem_statement, "status": "prompted"}
    )

    return result


# ─── Tool: phase_a_corpus_ingestion ─────────────────────────────────────────


@mcp.tool()
def phase_a_corpus_ingestion(
    abstracts: list[str],
    session_id: str = "",
) -> dict[str, Any]:
    """Phase A: Extract mathematical verbs from paper abstracts.

    Ingests paper abstracts and extracts the core mathematical "verbs"
    (classifies, lifts, decomposes, bounds, approximates, etc.).

    Args:
        abstracts: List of paper abstract texts (5-10 recommended)
        session_id: Optional session ID for stateful pipeline tracking

    Returns:
        Structured prompt + metadata for the calling LLM.
    """
    if not abstracts:
        raise ValueError("abstracts must be a non-empty list of strings")
    if any(not a or not a.strip() for a in abstracts):
        raise ValueError("all abstracts must be non-empty strings")

    sid, session = _get_or_create_session(session_id)

    abstracts_text = "\n\n---\n\n".join(
        f"## Abstract {i + 1}\n{a}" for i, a in enumerate(abstracts)
    )

    system_prompt = PHASE_A_SYSTEM
    user_prompt = PHASE_A_USER_TEMPLATE.format(abstracts=abstracts_text)

    result = {
        "session_id": sid,
        "tool": "phase_a_corpus_ingestion",
        "phase": "A",
        "abstract_count": len(abstracts),
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "instruction": (
            "Feed the system_prompt and user_prompt to an LLM. "
            "For each abstract, the LLM MUST return: theorem_name, "
            "core_dynamic, mathematical_objects, and verb_category."
        ),
        "verb_categories": [
            "classifies",
            "lifts",
            "decomposes",
            "bounds",
            "approximates",
            "completes",
            "embeds",
            "restricts",
            "factors",
            "dualizes",
        ],
    }

    session["corpus"] = abstracts
    session["phase"] = "A_complete"

    return result


# ─── Tool: phase_b_cross_mapping ────────────────────────────────────────────


@mcp.tool()
def phase_b_cross_mapping(
    theorem: str,
    theorem_name: str = "",
    session_id: str = "",
) -> dict[str, Any]:
    """Phase B: Translate a single theorem across four domains.

    Wraps translate_theorem for explicit pipeline phase tracking.

    Args:
        theorem: Full mathematical statement of the theorem
        theorem_name: Short name (e.g., from Phase A extraction)
        session_id: Optional session ID for stateful pipeline tracking

    Returns:
        Structured prompt output (same format as translate_theorem)
    """
    return translate_theorem(theorem, theorem_name, session_id)


# ─── Tool: phase_c_pattern_matching ────────────────────────────────────────


@mcp.tool()
def phase_c_pattern_matching(
    translations_json: str,
    session_id: str = "",
) -> dict[str, Any]:
    """Phase C: Cluster Synthesis_Consilience outputs into meta-principles.

    Identifies gaps where a principle is proven in one domain but
    absent in another — these are the NOVEL HYPOTHESIS ZONES.

    Args:
        translations_json: JSON string of all translation outputs from Phase B.
            Must be a JSON array of objects, each containing at minimum
            theorem_name and Synthesis_Consilience fields.
        session_id: Optional session ID for stateful pipeline tracking

    Returns:
        Structured prompt + parsed translations for the calling LLM.
    """
    if not translations_json or not translations_json.strip():
        raise ValueError("translations_json must be a non-empty JSON string")

    # Validate parseable
    try:
        parsed = json.loads(translations_json)
    except json.JSONDecodeError as e:
        raise ValueError(f"translations_json is not valid JSON: {e}")

    if not isinstance(parsed, list):
        raise ValueError("translations_json must be a JSON array")

    sid, session = _get_or_create_session(session_id)

    system_prompt = PHASE_C_SYSTEM
    user_prompt = PHASE_C_USER_TEMPLATE.format(translations_json=translations_json)

    result = {
        "session_id": sid,
        "tool": "phase_c_pattern_matching",
        "phase": "C",
        "translation_count": len(parsed),
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "instruction": (
            "Feed the system_prompt and user_prompt to an LLM. "
            "The LLM MUST return JSON with: meta_principles (array of "
            "{name, description, member_theorems, domains_present, "
            "domains_absent}) and gap_matrix (array of {principle, "
            "proven_in, unproven_in, transfer_hypothesis})."
        ),
        "parsed_translations": parsed,
    }

    session["translations"] = parsed
    session["phase"] = "C_complete"

    return result


# ─── Tool: phase_d_generative_transfer ──────────────────────────────────────


@mcp.tool()
def phase_d_generative_transfer(
    gap_description: str,
    proven_domain: str,
    target_domain: str,
    principle: str = "",
    session_id: str = "",
) -> dict[str, Any]:
    """Phase D: Generate a novel theorem in the target domain.

    Takes a principle proven in one domain and generates a novel
    theorem/algorithm in a target domain using only translated lexicons.

    Args:
        gap_description: Description of the gap (principle proven in source,
            unproven in target)
        proven_domain: The domain where the principle is established
        target_domain: The domain to generate a novel theorem for
        principle: Optional name/label for the principle being transferred
        session_id: Optional session ID for stateful pipeline tracking

    Returns:
        Structured prompt + metadata for the calling LLM.
    """
    valid_domains = {
        "Physics",
        "Computer_Science",
        "Cognitive_Science",
        "Information_Theory",
    }
    if proven_domain not in valid_domains:
        raise ValueError(
            f"proven_domain must be one of {valid_domains}, got '{proven_domain}'"
        )
    if target_domain not in valid_domains:
        raise ValueError(
            f"target_domain must be one of {valid_domains}, got '{target_domain}'"
        )
    if proven_domain == target_domain:
        raise ValueError("proven_domain and target_domain must be different")
    if not gap_description or not gap_description.strip():
        raise ValueError("gap_description must be a non-empty string")

    sid, session = _get_or_create_session(session_id)

    system_prompt = PHASE_D_SYSTEM
    user_prompt = PHASE_D_USER_TEMPLATE.format(
        proven_domain=proven_domain,
        target_domain=target_domain,
        principle=principle or "unnamed_principle",
        gap_description=gap_description,
    )

    result = {
        "session_id": sid,
        "tool": "phase_d_generative_transfer",
        "phase": "D",
        "proven_domain": proven_domain,
        "target_domain": target_domain,
        "principle": principle,
        "gap_description": gap_description,
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "instruction": (
            "Feed the system_prompt and user_prompt to an LLM. "
            "The LLM MUST return JSON with: source_principle, target_theorem, "
            "proof_sketch, validation_protocol, and novelty_assessment."
        ),
        "expected_keys": [
            "source_principle",
            "target_theorem",
            "proof_sketch",
            "validation_protocol",
            "novelty_assessment",
        ],
    }

    session["generated_theorems"].append(
        {
            "proven_domain": proven_domain,
            "target_domain": target_domain,
            "principle": principle,
            "status": "prompted",
        }
    )

    return result


# ─── Tool: full_pipeline ───────────────────────────────────────────────────


@mcp.tool()
def full_pipeline(
    abstracts: list[str],
    session_id: str = "",
) -> dict[str, Any]:
    """Run the complete four-phase autonomous research pipeline.

    Orchestrates Phases A-D in sequence:
    A: Corpus ingestion (extract mathematical verbs)
    B: Cross-mapping (translate each theorem across 4 domains)
    C: Pattern matching (cluster into meta-principles, find gaps)
    D: Generative transfer (create novel cross-domain theorems)

    Args:
        abstracts: List of 5-10 paper abstract texts to seed the pipeline
        session_id: Optional session ID for stateful pipeline tracking

    Returns:
        Complete pipeline plan with all phases and their prompts.
        The calling agent should execute each phase in order,
        feeding the outputs of one phase as inputs to the next.
    """
    if not abstracts:
        raise ValueError("abstracts must be a non-empty list")
    if len(abstracts) < 3:
        raise ValueError("at least 3 abstracts recommended for meaningful results")

    sid, session = _get_or_create_session(session_id)
    session["phase"] = "pipeline_started"

    # Phase A
    phase_a_result = phase_a_corpus_ingestion(abstracts, sid)

    pipeline_plan = {
        "session_id": sid,
        "tool": "full_pipeline",
        "pipeline_version": "1.0.0",
        "abstract_count": len(abstracts),
        "phases": {
            "A_corpus_ingestion": {
                "description": "Extract mathematical verbs from abstracts",
                "tool": "phase_a_corpus_ingestion",
                "input": abstracts,
                "output": phase_a_result,
                "next": "Feed phase_a_result.system_prompt + user_prompt to LLM. "
                "Use the LLM's output (theorem_name + core_dynamic for each abstract) "
                "as input to Phase B.",
            },
            "B_cross_mapping": {
                "description": "Translate each extracted theorem across 4 domains",
                "tool": "phase_b_cross_mapping",
                "instruction": (
                    "For each theorem extracted in Phase A, call phase_b_cross_mapping "
                    "with the theorem statement. Feed each resulting prompt to the LLM. "
                    "Collect all translations as a JSON array."
                ),
            },
            "C_pattern_matching": {
                "description": "Cluster translations, find gaps",
                "tool": "phase_c_pattern_matching",
                "instruction": (
                    "Collect all Phase B translation outputs into a JSON array. "
                    "Call phase_c_pattern_matching with this array. "
                    "Feed the resulting prompt to the LLM to identify meta-principles "
                    "and novelty gaps."
                ),
            },
            "D_generative_transfer": {
                "description": "Generate novel cross-domain theorems",
                "tool": "phase_d_generative_transfer",
                "instruction": (
                    "For each gap identified in Phase C, call phase_d_generative_transfer "
                    "with the gap description, proven domain, and target domain. "
                    "Feed each resulting prompt to the LLM to generate novel theorems."
                ),
            },
        },
        "execution_order": [
            "1. Run Phase A prompt → extract theorems",
            "2. For each theorem, run Phase B prompt → get cross-domain translations",
            "3. Collect all Phase B outputs, run Phase C prompt → get gaps",
            "4. For each gap, run Phase D prompt → generate novel theorems",
        ],
    }

    session["pipeline_plan"] = pipeline_plan

    return pipeline_plan


# ─── Tool: get_session_state ────────────────────────────────────────────────


@mcp.tool()
def get_session_state(session_id: str) -> dict[str, Any]:
    """Get the current state of a pipeline session.

    Args:
        session_id: The session ID to query

    Returns:
        Current session state including phase, corpus, theorems,
        translations, gaps, and generated theorems.
    """
    if session_id not in _sessions:
        raise ValueError(f"Session '{session_id}' not found")
    state = _sessions[session_id].copy()
    state["session_id"] = session_id
    return state


# ─── Tool: reset_session ───────────────────────────────────────────────────


@mcp.tool()
def reset_session(session_id: str) -> dict[str, str]:
    """Reset a pipeline session to its initial state.

    Args:
        session_id: The session ID to reset

    Returns:
        Confirmation message.
    """
    if session_id not in _sessions:
        raise ValueError(f"Session '{session_id}' not found")
    _sessions[session_id] = {
        "phase": "init",
        "corpus": [],
        "theorems": [],
        "translations": [],
        "meta_principles": [],
        "gaps": [],
        "generated_theorems": [],
    }
    return {"session_id": session_id, "status": "reset"}


# ─── Entry Point ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
