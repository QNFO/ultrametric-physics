# Consilience Framework — Directory Index

**WBS**: `QNFO.CON.002` — Cross-Pillar Consilience, Project 002

This directory contains the synthesis of two deep-dive research conversations on valuation theory and foundational mathematics (2026-08-04), plus supporting bridge documents and deployment artifacts.

## Files

| File | Size | Description | WBS Code |
|:-----|-----:|:------------|:---------|
| `paper.md` | 32K | **The Consilience Framework: From Valuation Theory to the Void** — 10-section synthesis paper. Covers valuation theory (Ostrowski), cross-domain Rosetta Stone, foundational ladder (void → distinction → valuation), Universal Consilience Prompt, 4-phase autonomous LLM workflow, and WBS integration. | `CON.002.P4.T1` |
| `foundational-chain.md` | 20K | **Void → Distinction → Valuation: Three Extension Paths** — Path 1 (category theory formalization), Path 2 (quantum vacuum/spacetime emergence), Path 3 (minimum entropy for booting a universe). Converges on the adele ring as the complete object. | `CON.002.P4.T2` |
| `bridge-adelic-qft.md` | 10K | Integration bridge to `../adelic-qft/` — shared mathematical kernel, dependency map, joint next steps. | `CON.002.P4.T5` |
| `bridge-hensel-code.md` | 12K | Integration bridge to `../hensel-code-system/` — Ostrowski gap formalization, Hensel lifting as distinction depth, joint next steps. | `CON.002.P4.T6` |
| `bridge-wbs-6-synthesis.md` | 5K | Integration bridge to `wbs-6-synthesis/docs/` (CON.001 / Five Pillars paper) — pillar mapping, conceptual lineage, joint next steps. | `CON.002.P3` |
| `.zenodo_metadata.json` | 3K | Zenodo deposition metadata draft (DOI pending). | `CON.002.P3` |
| `consilience_framework.pdf` | 514K | Built PDF of paper.md — via `pandoc --mathml` → Edge headless `--print-to-pdf` (no TeX engine on this machine; see Quick Start). | `CON.002.P5.T2` |
| `README.md` | — | This file. | — |

## Companion Directory

| Path | Contents |
|:-----|:---------|
| `../consilience-mcp/` | FastMCP server implementing Universal Consilience Prompt + 4-phase workflow (7 tools, `CON.002.P5.T1`) |

## Cross-Referenced Projects

| Project | Location | WBS |
|:--------|:---------|:----|
| Five Pillars, One Framework | `wbs-6-synthesis/docs/` | `QNFO.CON.001` |
| Adelic QFT | `../adelic-qft/` | `QNFO.ADL.001` |
| Hensel Code System | `../hensel-code-system/` | `QNFO.UF` |
| Unity of Ultrametric Physics | `../unity-of-ultrametric-physics/` | `QNFO.UF` |
| WBS Taxonomy | `wbs-6-synthesis/docs/WBS.TAXONOMY.md` | canonical registry |
| WBS Agent Protocol | `wbs-6-synthesis/docs/WBS-AGENT-PROTOCOL.md` | plan step format |

## Quick Start

```bash
# Read the paper
open paper.md

# Build PDF — NO TeX engine is installed on this machine (verified 2026-08-04:
# xelatex/pdflatex absent). Use pandoc --mathml (native MathML, no CDN) +
# Edge headless print-to-pdf. Do NOT use --pdf-engine=xelatex or
# -V mainfont="Font With Spaces" (PANDOC-FONT-QUOTE-1 / windows-command-patterns v3.12).
pandoc paper.md -o _paper_tmp.html --standalone --mathml --toc
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --no-sandbox --print-to-pdf=consilience_framework.pdf --virtual-time-budget=30000 "file:///C:/Users/LENOVO/QNFO/ultrametric-physics/consilience-framework/_paper_tmp.html"
del _paper_tmp.html

# Run the MCP server
cd ../consilience-mcp
pip install -r requirements.txt
python server.py
```

## Status

- **P4 (Deep Research)**: ✅ Complete — paper, foundational chain, bridge docs
- **P5 (Publication)**: ✅ MCP tool built + tested, ✅ PDF built, ⏳ Zenodo deposition, ⏳ Cloudflare Worker deployment
- **P0 (Registration)**: ✅ WBS.TAXONOMY.md updated, ⏳ D1 row + KG node creation

---

*Project `QNFO.CON.002` — Cross-Pillar Consilience. Companion to `QNFO.CON.001` (wbs-6-synthesis).*
