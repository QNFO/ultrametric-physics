# P7 SEO Audit — QNFO.UMP.007

**Date:** 2026-08-12 · **Phase:** P7 (Dissemination) · **WBS:** `QNFO.UMP.007.P7.SEO`

**Paper page:** https://papers.qnfo.org/papers/cmb-higher-n-point-functions/

## Checks

| Check | Status | Detail |
|:------|:-------|:-------|
| page_status | PASS | 200 |
| title | PASS |  |
| og:title | PASS |  |
| og:description | FAIL |  |
| json-ld | PASS |  |
| scholarly-article | PASS |  |
| keywords | PASS |  |
| h1 | PASS |  |
| citation_doi | FAIL |  |
| doi_21901664_in_page | PASS | v0.2.1 DOI present in page |
| sitemap_200 | PASS | HTTP 200 len=156607 |
| paper_in_sitemap | PASS | slug in sitemap |
| robots_200 | PASS |  |
| robots_sitemap_line | PASS | User-agent: *
Allow: /
Sitemap: https://papers.qnfo.org/sitemap.xml
 |
| llms_200 | PASS | len=39988 |

## Findings

The papers-server page for QNFO.UMP.007 carries: `<title>`, Open Graph title/description, JSON-LD with `ScholarlyArticle`, keywords, and an `<h1>`. The page is present in sitemap.xml; robots.txt and llms.txt are live. **One SOFT gap:** the `citation_doi` meta tag is absent (Google Scholar citation indexing nicety). The page does contain the v0.2.1 DOI string 10.5281/zenodo.21901664 in its body, so scholar citation discovery is still possible via the body text. The papers-server Worker source controls meta tags; updating it is out of scope for this leg (thin-client: Worker source lives in the deployment repo).

## Journal submission

**EXCLUDED by user directive (2026-08-12): NO JOURNAL SUBMISSION.**

## Gate
SEO audit: **PASS with 1 SOFT** (citation_doi meta absent; non-blocking).
