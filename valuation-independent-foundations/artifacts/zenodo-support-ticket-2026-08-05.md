# Zenodo Support Ticket — WAF Block on Authenticated API Requests

**To:** Zenodo Support (support@zenodo.org)
**Subject:** API key blocked from creating new versions — HTTP 403 "unusual traffic from your network" with WAF reference codes

---

## 1. Summary

All authenticated API requests to zenodo.org are returning **HTTP 403 Forbidden** with an
nginx-served HTML page stating: *"Access to this resource has been restricted due to unusual
traffic from your network."* Unauthenticated public GET requests to the same records succeed
(HTTP 200). The block appears to be triggered specifically by requests carrying the API Bearer
token, and prevents us from creating new versions of our published deposits.

## 2. Account Information

- **Zenodo account / creator name:** Rowan Brad Quni-Gudzinas (publisher: QNFO)
- **API token prefix (first 6 chars, full token withheld for security):** `BkLOVH`
- **Token type:** Zenodo API access token (created via the Zenodo web UI)

## 3. Affected Records

| Record ID | DOI | Role |
|-----------|-----|------|
| 21795779 | 10.5281/zenodo.21795779 | Latest published version — target for new version upload |
| 21795656 | 10.5281/zenodo.21795656 | Original record in the same concept DOI chain |

## 4. What We Were Trying to Do

Create a new version of record **21795779** (via `POST /api/records/21795779/versions`)
in order to upload three files (`.md`, `.html`, `.pdf`) per our publication workflow.
The files exist locally and are safely mirrored to GitHub and Cloudflare R2 — **no data is
at risk**; we simply cannot push the update through the API.

## 5. Exact Error Responses (verbatim, captured 2026-08-05T09:24:15+02:00)

### 5a. `POST /api/records/21795779/versions` (with Bearer token)
```
HTTP 403 Forbidden
server: nginx
content-type: text/html; charset=utf-8

<html>
<head><title>403 Forbidden</title></head>
<body style="max-width: 600px; margin: 40px auto; padding: 0 20px; line-height: 1.6;">
<h1>403 Forbidden</h1>
<hr>
<p>Access to this resource has been restricted due to unusual traffic from your network.</p>
<p>If you believe this is a mistake, please <a href="/support?ref=2c395f7946baf3433cef01562ce76766&category=problem-report">contact our support line</a> and we will look into your request.</p>
<p>
<strong>Reference:</strong> <code>2c395f7946baf3433cef01562ce76766</code><br>
<strong>Timestamp:</strong> <code>2026-08-05T09:24:15+02:00</code><br>
</p>
</body>
</html>
```

### 5b. `POST /api/records/21795656/versions` (with Bearer token)
Same 403 HTML, reference code **`f2089d1102400bae5ede833eb65d7d59`**, same timestamp.

### 5c. `GET /api/records/21795779` (with Bearer token)
Same 403 HTML, reference code **`33a20d318911cf918715f526a3fb4790`**.

### 5d. Control: `GET /api/records/21795779` (NO token)
**HTTP 200** — succeeds. Public read access is unaffected.

## 6. Diagnostic Evidence — Why We Believe This Is a Token-Triggered WAF Flag, Not an IP Block

The distinguishing observation: **an unauthenticated GET to the same record returns 200,
while any request carrying the Bearer token returns 403.** If the block were purely
IP/network-based (as the message wording suggests), the unauthenticated GET would also fail.
The asymmetry indicates the WAF is keying on the authenticated request — either the token
itself has been flagged/rate-limited, or a rule matches the authenticated request path.

Request flow observed (Python `requests`, TLS 1.3, browser UA `Mozilla/5.0`):

| Request | Auth | Result |
|---------|------|--------|
| GET /records/21795779 | none | 200 |
| GET /records/21795779 | Bearer | 403 WAF |
| POST /records/21795779/versions | Bearer | 403 WAF |
| POST /records/21795656/versions | Bearer | 403 WAF |

## 7. Our Questions

1. **What are Zenodo's documented rate limits for the REST API?** We were not aware formal
   limits existed. Please point us to the documentation, or state the limits (requests per
   minute/hour, per token and per IP).

2. **What triggers the "unusual traffic from your network" WAF block?** Is it a threshold on
   request volume, request rate, failed attempts, or another heuristic?

3. **Is the block keyed to our API token, our IP, or both?** The control test in §6 suggests
   token-keyed; please confirm.

4. **How long does the block last, and how is it lifted?** Is there a cooldown, or does it
   require manual review / whitelisting?

5. **Best practices for legitimate bulk operations:** Are there recommended delays between
   calls, batch endpoints, or documented polite-pool guidance for depositing many files/versions?

6. **Can you verify whether our token `BkLOVH...` is in good standing** (not revoked, not
   suspended, no scope changes)?

## 8. What We Need

- Confirmation of the block and its trigger.
- Guidance on the cooldown or a manual lift for the reference codes above.
- The official rate-limit policy so we can conform our automation to it.

Thank you for your assistance.

---

*Reference codes for your side: `2c395f7946baf3433cef01562ce76766`,
`f2089d1102400bae5ede833eb65d7d59`, `33a20d318911cf918715f526a3fb4790`*
*Ticket prepared 2026-08-05 by QNFO research automation.*
