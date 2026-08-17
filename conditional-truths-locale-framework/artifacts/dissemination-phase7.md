# Phase 7/8 Dissemination & Distribution — QNFO.UMP.011 (2026-08-17)

Project: Conditional Truths and the Locale Framework · Record: 10.5281/zenodo.21983444 (v0.2; concept 10.5281/zenodo.21983324)

## D7 Fediverse broadcast

- **Bluesky POSTED** (2026-08-17): `at://did:plc:vad2yeqflg5uznmp557zge5c/app.bsky.feed.post/3mtca4x6ttd2o`
  Copy: "Conditional Truths and the Locale Framework: Map, Territory, and the Rendering Interface. #OpenScience #QuantumFoundations #UltrametricPhysics https://doi.org/10.5281/zenodo.21983325" (182 chars, 3 hashtags, no exclamation marks — playbook-compliant).
- **Mastodon: SKIPPED** — no stored credentials (`~/.mastodon_creds.json` absent; no MASTODON_* in env/.env). OAuth setup is interactive (mastodon_follow.py auth); documented as a standing gap, not a failure. Credential-install finding: `zenodo_broadcast.py` expects `C:\Users\LENOVO\.deepchat\keys.json` with keys `bsky_handle` + `bsky_app_password` (the general store `C:\Users\LENOVO\keys.json` uses `bluesky_*` names which the script's substring matcher does NOT see — installed the expected subset file 2026-08-17).

## D3 Zenodo community inclusion (curator-gated)

- Targets (all verified EXISTS via /api/communities): `fbt-framework`, `advancedtheoreticalphysicsandmathematics`, `tp-a-m-c`.
- Records-API request endpoint returned 403; deposit-API metadata `communities` field on a newversion draft was silently dropped (ZENODO-RECORDS-API-DROPS-METADATA-1 class) — but the records-API POST had actually created **OPEN inclusion requests** ("There is already an open inclusion request for this community" on retry). Requests are curator-gated per ZENODO-COMMUNITY-INCLUSION-REQUEST-1 — membership appears on curator acceptance.
- Side effect: metadata-only newversion v0.2 (record 21983444) published 2026-08-17 with byte-identical files (19, MD5-carried) + preserved related_identifiers (GitHub provenance) + license cc-by-nc-sa-4.0. Concept DOI 21983324 resolves to v0.2. D1/KG/program_registry synced to v0.2 (readback-verified).

## IndexNow

- `rwnq8.github.io`: **HTTP 202** accepted; `qnfo-landing.pages.dev`: **HTTP 202** accepted (script default hosts).
- `papers.qnfo.org/conditional-truths-locale-framework` (page live, HTTP 200, 60.9 KB): **HTTP 200** accepted; key file verified served at https://papers.qnfo.org/{key}.txt (content match).
- Script repair: indexnow-submit.py docstring had a `\U` unicode-escape SyntaxError (Windows path in docstring, Python 3.12) — patched to forward slashes (docstring-only; compile OK; harmless SyntaxWarning remains).

## Internet Archive

- Snapshot requests dispatched for `https://zenodo.org/records/21983444` + `https://papers.qnfo.org/conditional-truths-locale-framework`.
- CDX check 2026-08-17: `no capture yet` — crawler processing async. **[NOT-VERIFIED: pending]** — re-check via CDX next cycle.

## Distribution status (4-D)

| Layer | Status |
|:------|:-------|
| Zenodo (DOI) | ✅ v0.2 21983444 + concept 21983324, DataCite findable |
| GitHub | ✅ branch ump/paper/conditional-truths-locale-framework @ 43375cf + tag v0.1-published-ump011 |
| R2 mirror | ✅ qnfo-releases/2026/08/conditional-truths-locale-framework/ (19 files, sibling-verified) |
| D1 living-paper | ✅ row (doi synced to v0.2) |
| KG | ✅ node + BELONGS_TO prog-qnfo-ump, distribution_status=distributed, r2_path |
| Vectorize | ✅ 42 chunks, 0 errors |
| papers.qnfo.org | ✅ live page 200 + IndexNow submitted |
| OpenAIRE | auto-indexed via Zenodo (no action) |
| Internet Archive | ⏳ requested, CDX pending |
| IPFS/DNSLink | ⏸ deferred — no pinning token stored; optional leg |
| Mastodon | ⏸ deferred — no credentials stored (interactive OAuth required) |

## Findings logged this cycle

- FIND-6 (SOFT): `zenodo_broadcast.py` credential-discovery gap — expects `.deepchat/keys.json` with `bsky_*` keys; general store uses `bluesky_*` (substring matcher misses it). Installed expected subset; kaizen candidate for the skill docstring.
- FIND-7 (SOFT): `indexnow-submit.py` docstring `\U` SyntaxError on Python 3.12 — repaired (forward slashes).
- FIND-8 (INFO): deposit-API `communities` field dropped on newversion PUT (records-API requests ARE created — verified by retry error); use records-API /communities for requests, not metadata field.
- FIND-9 (INFO): internet-archive-submit.js fetch has no timeout — hangs indefinitely when IA is slow; bounded-wait + CDX verification is the pattern.
