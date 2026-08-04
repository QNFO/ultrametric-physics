# Consilience MCP Server

**WBS**: `QNFO.CON.002.P5.T1` — Cross-Pillar Consilience, Publication Phase, MCP Tool

A FastMCP server implementing the **Universal Consilience Prompt** and **four-phase autonomous LLM research workflow** derived from the QNFO valuation theory conversations (2026-08-04).

## Architecture

This MCP server is a **prompt template engine + state tracker** — it does NOT call an LLM itself. Each tool returns structured prompts that the calling agent (Claude, GPT, Gemini) executes using its own reasoning. Results are stored in an in-memory JSON session store for pipeline chaining.

## Tools

| Tool | Phase | Description |
|:-----|:------|:------------|
| `translate_theorem` | — | Translate any theorem into 4 domain lexicons (Physics, CS, Cognition, Info Theory) |
| `phase_a_corpus_ingestion` | A | Extract mathematical "verbs" from paper abstracts |
| `phase_b_cross_mapping` | B | Translate a theorem across 4 domains |
| `phase_c_pattern_matching` | C | Cluster translations into meta-principles, find gaps |
| `phase_d_generative_transfer` | D | Generate novel cross-domain theorems/algorithms |
| `full_pipeline` | A-D | Orchestrate the complete four-phase research loop |
| `get_session_state` | — | Inspect pipeline session state |
| `reset_session` | — | Reset a session to initial state |

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Add to your MCP client configuration (e.g., `mcp.json`):

```json
{
  "mcpServers": {
    "consilience": {
      "command": "python",
      "args": ["path/to/consilience-mcp/server.py"]
    }
  }
}
```

## Usage

### Quick Start: Translate a Theorem

```
Tool: translate_theorem
Args: {
  "theorem_statement": "If a polynomial has a simple root modulo p, it lifts uniquely to a p-adic root.",
  "theorem_name": "Hensel's Lemma"
}
```

Feed the returned `system_prompt` + `user_prompt` to an LLM. It will return JSON with translations into all four domains.

### Full Pipeline

```
Tool: full_pipeline
Args: {
  "abstracts": [
    "We classify all finite simple groups...",
    "Using p-adic methods, we prove bounds on...",
    "Quantum error correction via topological codes...",
    ...
  ]
}
```

The pipeline plan will guide you through all four phases.

## Session State

All tools accept an optional `session_id`. If omitted, a UUID is generated. The session tracks:
- Current phase
- Ingested corpus
- Extracted theorems
- Cross-domain translations
- Meta-principles and gaps
- Generated novel theorems

## Companion Documents

- `../consilience-framework/paper.md` — The Consilience Framework synthesis paper
- `../consilience-framework/foundational-chain.md` — Void → Distinction → Valuation three-path extension
- `../consilience-mcp/prompt_templates.py` — All prompt template constants

## WBS Integration

| Code | Description |
|:-----|:-----------|
| `QNFO.CON` | Cross-Pillar Consilience program |
| `QNFO.CON.002` | consilience-framework project |
| `QNFO.CON.002.P5` | Publication Phase |
| `QNFO.CON.002.P5.T1` | MCP Tool Implementation |

## License

QNFO Unified License Agreement (QNFO-ULA)
