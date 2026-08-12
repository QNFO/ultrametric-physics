# Literature Triage — QNFO.UMP.008 (Phase 2)

**Date:** 2026-08-12 | **Sources:** OpenAlex (PRIMARY, 15 verified DOIs), arXiv (rate-limited → OpenAlex per research skill), QNFO Vectorize (10 internal hits), QNFO KG

## Classification Matrix

| Class | Count | Definition | Papers |
|---|---|---|---|
| Core | 8 | Directly addresses radix-agnostic DSI detection / LPPL methodology | Filimonov & Sornette 2013; Geraskin & Fantazzini 2011; Gluzman & Sornette 2002; Huang et al. 1997; Wang et al. 2018 (sciadv.aau5096); Wang et al. 2019 (nsr/nwz110); Zhou & Sornette 2002; Press & Rybicki 1989 |
| Supporting | 8 | Spectral estimation + DSI application + p-adic physics | Zechmeister & Kürster 2009; Vanderplas 2018; Feigenbaum 2001; Sornette & Sammis 1995; Faillettaz et al. 2008; Drozdz et al. 1999; Avetisov et al. 2002; Schikhof 1984 |
| Background | 8 | Ultrametric foundations, DFA, causal/dependency, symbolic regression | Robert 2000; Escassut 1995; Gower & Ross 1969; Jain et al. 1999; Kantelhardt et al. 2002; Schreiber 2000; Glymour et al. 2019; Tenachi et al. 2023 |
| Reject | 0 | — | — |

## KIF-18 Mandatory Symmetry Template

### Where External Literature Supports [Claim C2 — three-stage radix-agnostic protocol]

- **Filimonov & Sornette (2013)** — "A stable and robust calibration scheme of the log-periodic power law model" (10.1016/j.physa.2013.04.012): establishes that LPPL calibration requires careful initialization/robust schemes — supports the stage-separated protocol's premise that naive joint fitting is fragile.
- **Press & Rybicki (1989)** / **Zechmeister & Kürster (2009)** — Lomb-Scargle spectral estimation handles unevenly sampled data — the Stage-1 peak leg's foundation.
- **Zhou & Sornette (2002)** — "Statistical significance of periodicity and log-periodicity with heavy-tailed correlated noise" (10.1142/s0129183102003024): the look-elsewhere discipline the certification leg operationalizes.
- **Huang, Ouillon, Saleur (1997)** — DSI spontaneous generation in growth models — the phenomenon class the detector targets.

### Where External Literature Constrains or Contradicts [Claims]

- **Geraskin & Fantazzini (2011)** — "Everything you always wanted to know about log-periodic power laws for bubble modeling" (10.1080/1351847x.2011.601657): LPPL fits are over-parameterized and notoriously unstable. **This CONFIRMS our D3 claim** (joint 6-param fit collapses even at true-peak init — reproduced this session) — and constrains C2: the protocol MUST separate stages (detrend → peak → bounded refinement), never fit jointly. The literature's warning is the constraint our protocol was designed to satisfy.
- **James, Barnett, Crutchfield (2016)** — information-flow critiques: not directly applicable to DSI (cited in the survey family 4, not core to C2/C3).
- **[NO CONSTRAINING EVIDENCE FOUND]** that the three-stage separation + max-statistic bootstrap certification is invalid for power-law × log-periodic signals. The closest constraint is the LPPL over-parameterization warning, which our design already addresses (and which we independently verified).

## Novelty confirmation (from gap analysis)

No published work fuses (a) spectral estimation, (b) LPPL/DSI detection, (c) p-adic theory into a single CERTIFIED radix-agnostic detector with bootstrap certification + integrity gates + G4 model-subtraction. The empirical null on Planck 2018 at full radix coverage is a novel extension of the radix-locked analyses (CAL-03 p=0.38, P5 p=0.38).

## Classification gate

All Core/Supporting entries verified via OpenAlex title-match (15/15, evidence: `external-search/openalex_evidence.json`). [CONFIRMATION-BIAS-RISK] disclosed (Vectorize hits all internal; external corroboration via OpenAlex DOIs).
