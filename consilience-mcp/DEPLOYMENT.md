# Consilience MCP — Cloudflare Deployment Guide

**WBS**: `QNFO.CON.002.P6` — Deployment Phase
**Status**: DRAFT — deployment blocked in authoring session (Cloudflare MCP tools unavailable). This document is the complete deployment runbook prepared in advance per cloudflare skill v3.33.

---

## 1. Deployment Decision Matrix

The FastMCP Python server (`server.py`) is a **prompt-engine + state-tracker** — it does not call an LLM itself. This maps cleanly onto Cloudflare's McpAgent pattern.

| Aspect | Python (local, current) | TypeScript McpAgent (edge, target) |
|:-------|:------------------------|:-----------------------------------|
| Transport | stdio | Streamable HTTP (`/mcp`) |
| Session state | In-memory `_sessions` dict | D1 + KV (durable) |
| Prompt templates | `prompt_templates.py` constants | Port to `templates.ts` exports |
| Tools | `@mcp.tool()` decorators | McpAgent `onCallTool` dispatch |
| Phase C semantic match | LLM-driven (calling agent) | Optional Vectorize `consilience-dynamics` index |
| Embeddings | n/a | Workers AI `@cf/baai/bge-base-en-v1.5` |

**Recommendation**: Keep the Python server as the local canonical implementation. Port to McpAgent ONLY if edge deployment is required (multi-client access, scheduled Phase A runs, webhook ingestion).

---

## 2. McpAgent Port Outline

```typescript
// src/index.ts — port of server.py to Agents SDK McpAgent
import { McpAgent } from "agents-sdk/mcp";
import { templates } from "./templates"; // ported from prompt_templates.py

interface Env {
  CONSILIENCE_DB: D1Database;
  CONSILIENCE_KV: KVNamespace;
  AI: Ai;
  CONSILIENCE_VZ: VectorizeIndex;
}

interface SessionState {
  phase: string;
  corpus: string[];
  theorems: string[];
  translations: string[];
}

export class ConsilienceMCP extends McpAgent<Env, SessionState> {
  async onStart(): Promise<SessionState> {
    return { phase: "init", corpus: [], theorems: [], translations: [] };
  }

  async onCallTool(name: string, args: any) {
    switch (name) {
      case "translate_theorem":
        // return templates.translateTheoreme(args.theorem_statement)
        break;
      case "phase_a_corpus_ingestion":
        // args.abstracts → templates.phaseA(args.abstracts)
        break;
      // ... phase_b, phase_c, phase_d, full_pipeline, get_session_state, reset_session
    }
  }
}

export default ConsilienceMCP;
```

**Durable state note**: replace the in-memory `_sessions` with D1 `sessions` table (id TEXT PRIMARY KEY, phase TEXT, corpus JSON, updated_at TEXT) + KV `phase:{id}` cursor for long pipelines. See `wrangler.toml` commented bindings.

---

## 3. Deployment Steps (EXECUTE ONLY WITH CLOUDFLARE MCP TOOLS)

Per cloudflare skill §MCP-Driven Operations — **MCP tools FIRST** (`cloudflare` main server), `npx wrangler` SECOND, REST API THIRD. NEVER PowerShell (KIF-59), NEVER Dashboard (KIF-60).

```bash
# Pre-flight (KIF-61: workers_dev must be true — already set in wrangler.toml)
npx wrangler whoami                                  # → account quniverse

# 1. Create resources
npx wrangler d1 create qnfo-consilience              # → capture database_id → uncomment binding
npx wrangler vectorize create consilience-dynamics --dimensions=768 --metric=cosine
npx wrangler kv namespace create CONSILIENCE_KV

# 2. Port templates (python → TS) then deploy
npx wrangler deploy

# 3. VERIFICATION (MANDATORY — KIF-50 gate, MCP Anti-Phantom Gate)
#    Probe ≥2 data-dependent routes, not just /health:
curl -s https://qnfo-consilience-mcp.q08.workers.dev/mcp        # POST MCP initialize → 200
curl -s https://qnfo-consilience-mcp.q08.workers.dev/health     # → bindings object
#    Verify via TWO independent MCP servers (cloudflare-builds + cloudflare-observability):
#    cloudflare-builds       → deploy succeeded, latest deployment timestamp
#    cloudflare-observability → healthy invocations, zero error rate
#    cloudflare-auditlogs    → deploy action recorded
```

---

## 4. KIF-50 Binding Gate (CRITICAL)

If deployment goes through REST API PUT (NOT recommended), bindings MUST be included in `metadata.bindings` — a bare PUT silently drops ALL bindings and the Worker 500s with `Cannot read properties of undefined (reading 'prepare')`.

**Always prefer `npx wrangler deploy` from `wrangler.toml`** (declares every binding).

---

## 5. Route Decision

| Option | Route | When |
|:-------|:------|:-----|
| workers.dev | `qnfo-consilience-mcp.q08.workers.dev/mcp` | Internal/testing (default) |
| Custom domain | `mcp.consilience.qnfo.org/mcp` | Public MCP endpoint — requires zone-level Workers route (POST `/zones/{ZONE_ID}/workers/routes`) + DNS record |

---

## 6. Resource Baselines Impact

| Resource | Current baseline | After deploy | Note |
|:---------|:----------------|:-------------|:-----|
| Workers | 9 | 10 | +qnfo-consilience-mcp — legitimate growth |
| D1 databases | 6 | 7 | +qnfo-consilience |
| Vectorize indexes | 5 | 6 | +consilience-dynamics |
| KV namespaces | 1 | 2 | +CONSILIENCE_KV |

All within warning thresholds (±1). No baseline drift.

---

## 7. Blockers (authoring session, 2026-08-04)

| Blocker | Evidence | Unblock trigger |
|:--------|:---------|:----------------|
| Cloudflare MCP tools (`workers_list`, `cloudflare` main) not exposed in this session's tool list | cloudflare skill §MCP-Driven Operations lists them; they were absent from the live function set | Session with Cloudflare MCP servers configured + OAuth tokens valid (fleet-oauth-refresh daily cron) |
| wrangler not on PATH (WRANGLER-PATH-REGRESSION-1 class) | cloudflare v3.33 documents PATH reversion; `where wrangler` failed | Re-apply npm-global PATH fix or invoke `node C:\Users\LENOVO\npm-global\node_modules\wrangler\bin\wrangler.js` directly |
| D1 write access for `QNFO.CON.002` registration | Requires Cloudflare MCP `cloudflare` server D1 query capability | Same unblock as above |

**Classification**: ALL THREE are `EXTERNAL-BLOCK` per kaizen Phase 5 Deferred-Items Gate — genuinely blocked by missing tooling in this session, documented with evidence + unblock trigger. Not silently deferred.

---

## 8. Registration Prerequisites (from WBS.TAXONOMY.md §7)

1. ✅ WBS code assigned: `QNFO.CON.002`
2. ✅ Textual entry added to `WBS.TAXONOMY.md` §3 (2026-08-04)
3. ⏳ KG node `proj-qnfo-con-002` (label=Project) — via query_graph create or gateway `/sync` (X-Sync-Token)
4. ⏳ D1 row in `portfolio-state.program_registry` — via Cloudflare MCP / d1-safe-write.js
5. ⏳ GitHub repo `QNFO/consilience-framework` (if standalone repo desired; currently lives in ultrametric-physics monorepo)

---

*Draft prepared 2026-08-04. Deployment executable in a session with Cloudflare MCP tool access.*
