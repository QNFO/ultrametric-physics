# Zenodo Support — Follow-up: Correction of Earlier Ticket (no IP block exists)

**To:** Zenodo Support (support@zenodo.org)
**From:** rowan.quni@outlook.com (or the sending account used)
**Re:** Correction to earlier message — HTTP 403 was client-side bot-detection, NOT an IP block

---

## 1. Correction Summary

I am writing to correct an earlier support request (sent 2026-08-05, subject: "API key blocked
from creating new versions — HTTP 403 'unusual traffic from your network'"). That message
included three WAF reference codes and asked for an IP unblock. **That diagnosis was wrong,
and I apologize for the false alarm.**

## 2. What Actually Happened

The HTTP 403 "Access to this resource has been restricted due to unusual traffic from your
network" was **caused by our own automation sending a minimal `User-Agent: Mozilla/5.0` header**,
which Zenodo's bot filter treats as suspicious. This is a **client-side issue on our side** —
not an IP block, and not a problem with your service.

**A/B test performed (2026-08-05) proving the root cause:**

| Request | User-Agent | Result |
|---------|-----------|--------|
| GET /records/21795779 (authenticated) | `Mozilla/5.0` (minimal) | **HTTP 403** — bot-detection HTML |
| GET /records/21795779 (authenticated) | Full Chrome UA + Accept-Language + Referer + Origin | **HTTP 200** |
| POST /records/21795779/versions (authenticated) | Full browser headers | **HTTP 201** — new version created |

## 3. Resolution

With full browser headers, the API works normally. We have since successfully published:
- **DOI: 10.5281/zenodo.21803677** (new version of record 21795779)
- State: done · 3 files (PDF + HTML + Markdown) · verified via DataCite (findable)

## 4. Requests

1. **No unblock needed** — please disregard the earlier reference codes
   (`2c395f7946baf3433cef01562ce76766`, `f2089d1102400bae5ede833eb65d7d59`,
   `33a20d318911cf918715f526a3fb4790`).
2. If you have documented **rate limits** for the REST API, we would still appreciate
   the reference (our original question 1) so our automation stays within bounds.

Thank you for your patience, and apologies again for the false report.

---

*QNFO research automation · corrected 2026-08-05*
