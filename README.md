# ICLR 2027 JEPA papers

The virtual environment is `.venv/` inside this repository. Set it up and run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python fetch_jepa_papers.py --print-abstracts
```

`fetch_jepa_papers.py` uses `openreview-py` with API v2 at
`https://api2.openreview.net` and venue `ICLR.cc/2027/Conference`.
It reads the venue's configured submission invitation and under-review venue ID,
then fetches all pages using `get_all_notes`. Active means under review or accepted;
withdrawn, desk-rejected, rejected, and deleted notes are excluded.

It searches for `jepa` case-insensitively in title, abstract, and keywords, including
variants such as `I-JEPA` and `V-JEPA`. This is a metadata search: a paper that only
mentions JEPA in its body will not match. A match may use JEPA only as a baseline;
reading the method is needed to establish its contribution.

The script prints the active submission count, JEPA match count, and every matching
title. It writes a UTF-8 JSON array to **`jepa_papers.md`**, as requested, despite
the Markdown extension. Each object has exactly `title`, `abstract`, `keywords`,
and `pdf_url`. An unavailable PDF has a null URL. The file is only replaced after
a successful fetch. An empty array means no matches were visible to that client,
not necessarily that the venue contains no matching submissions.

The successful search export currently contains **337 matching papers**, with
337 distinct titles and a PDF URL for each. `jepa_papers.json` is a byte-identical
copy of the original JSON in `jepa_papers.md`. `jepa_abstracts.md` presents the
same titles, keywords, abstracts, and PDF links as readable Markdown.
`jepa_reading_plan.md` contains an initial shortlist based on abstracts only.

For a future fetch directly into the conventional JSON filename:

```bash
.venv/bin/python fetch_jepa_papers.py --mode search --output jepa_papers.json
```

The JSON copy and abstract catalog are snapshots; fetching new results does not
automatically refresh the other files.

## Combined world-model and hierarchy abstracts

`wm_papers.py` now requires **both world-model terminology and hierarchy-related
terminology** in the title, abstract, or keywords. The two categories can occur in
different fields of the same paper. A JEPA mention is not required. Run:

```bash
.venv/bin/python wm_papers.py
```

This defaults to anonymous search, even when login credentials are set in the
environment. Authentication remains available through an explicit `--login`, but
the normal metadata workflow does not use it. Abstracts and paper titles are not
printed unless `--print-abstracts` is supplied. A successful fetch writes:

- `hierarchy-wm.json`: matching papers, including their abstracts, in the
  downloader's four-field array format.
- `hierarchy-wm_source.json`: retrieval source, selection rule, and match counts.
- `hierarchy-wm_checkpoint.json`: saved search progress for resuming interrupted
  runs; it is reused after completion until `--restart` requests a fresh search.

Search retrieves hierarchy-related candidates using hierarchy, hierarchical,
multiscale, multi-scale, subgoal(s), nested, pyramid, and matryoshka. It then checks
**both** categories locally, rather than assuming a multiword API query means
Boolean AND. Searches use 1,000-note pages and a one-second delay. Hierarchy terms
cover hierarchical planners/representations, multiscale/cross-scale prediction,
nested embeddings, latent pyramids, and subgoals. Search-index coverage remains
unverified, and metadata mentions may describe baselines rather than the paper's
main contribution.

If the previous `wm_papers_checkpoint.json` exists, the default run imports its
matching records and reuses its venue configuration. It backs up the complete old
checkpoint before starting the new hierarchy searches, retaining cached metadata.
The migrated search continues to use that existing checkpoint filename.

On HTTP 429, the script stops without retrying or sleeping for an hour. Saved
matches are exported as `hierarchy-wm_partial.json`, while any existing completed
`hierarchy-wm.json` is preserved. Run the same command after the server's reset time
to resume at the failed page. A saved, unexpired cooldown prevents further API
requests, including when `--restart` is specified. Anonymous requests can also be
rate-limited. If an old version is still retrying, stop it with Ctrl+C first.

An existing broad world-model JSON can still be filtered entirely offline:

```bash
.venv/bin/python wm_papers.py --input wm_papers.json
```

This also creates `hierarchy-wm.json` and its source report while leaving the input
unchanged. No main-paper review is implied by the screening.

The export preserves the downloader's four-field format. The script prints a
download command for `hierarchy-wm.json`, including its actual count as
`--limit`. Only the PDF downloader normally needs `--login`; fetching abstracts
and filtering saved metadata do not download PDFs or write credentials.

A partial preview was produced from the old cached search: **112 combined
matches from 1,473 saved world-model records** in `hierarchy-wm_partial.json`.
Its separate source report marks the combined search as incomplete.

## Hierarchy-focused download list

`hierarchy_jepa.json` contains 18 selected records from `jepa_papers.json`,
preserving the same four fields and their source order. It is a JSON array that
can be passed directly to the downloader. Selection was reviewed from the saved
titles, abstracts, and keywords, covering hierarchical models/planners, multiscale
prediction, nested latent representations, and hierarchy analysis. It includes
related kinds of hierarchy beyond hierarchical JEPA world models. Main-paper
PDFs have not been read for this selection.

To download the full selected list with one login:

```bash
.venv/bin/python download_jepa_papers.py --login --input hierarchy_jepa.json --limit 18 --output-dir papers/hierarchy
```

Omitting `--limit` still downloads at most 10 entries. The selected list is a
snapshot; updates to `jepa_papers.json` do not automatically update it.

## Download the first 10 saved papers

```bash
.venv/bin/python download_jepa_papers.py --limit 10
```

This reads the first 10 entries of `jepa_papers.json` in their existing order and
uses `openreview-py` to download only their main-paper attachments. It does not
repeat the metadata search. PDFs are saved as `papers/first10/<note_id>.pdf`,
with per-paper results in `papers/first10/download_report.json`. Existing valid
PDFs are reused. Responses must have a PDF header; if `pdfinfo` is installed,
they must also pass a PDF parser check. HTML challenges and corrupt files are
reported as failures. Failed downloads do not stop attempts on the other papers.

The agent's initial attempts failed at DNS resolution. The subsequent report from
the user's shell contains **10 `ChallengeRequiredError` responses and no PDFs**:
those requests reached OpenReview but require browser verification.

First open a saved PDF URL in your browser and complete any verification shown.
To test OpenReview's documented account authentication on just one paper, run:

```bash
.venv/bin/python download_jepa_papers.py --login --limit 1 --output-dir papers/auth-check
```

The script prompts for your username and password (password input is hidden),
or uses the corresponding environment variables if already set. It does not save
credentials. The installed client handles its supported login/MFA flow. If the
single authenticated download works, repeat with `--login --limit 10`. Account
authentication has not been verified to clear this separate browser challenge;
browser verification does not automatically transfer session cookies to Python.

`--download-pdfs` saves the main submission attachments in `papers/<note_id>.pdf`.
If `pdftotext` is installed, it also creates text copies beside the PDFs. Attachment
or extraction failures are reported and produce a nonzero exit status; the JSON
export remains available. No reviews or supplementary attachments are fetched.

## If OpenReview returns `ChallengeRequiredError` (403)

This error blocks submission metadata, including abstracts. Downloading no PDFs
does not resolve it. The script now prints the supplied browser challenge URL and
request ID, exits with code 2, and preserves any existing output.

As an alternative metadata retrieval method, try:

```bash
.venv/bin/python fetch_jepa_papers.py --mode search --print-abstracts
```

This uses the documented API v2 `/notes/search` endpoint through
`OpenReviewClient.search_notes`, searches title, abstract, and keywords, paginates
each field, removes duplicates, and validates the venue, submission invitation,
and active status. It saves the same JSON format, prints abstracts, and does not
download PDFs. It reports the number of active **search candidates**, rather than
claiming to have scanned every submission. The search index may omit new papers
or handle JEPA variants differently from a complete substring scan. A search
result count is therefore not a proven exhaustive venue-wide count.

Search may also receive a challenge. Open the challenge URL provided by OpenReview
and complete its normal verification in a browser. Browser verification does not
automatically transfer browser cookies/session state to Python. Optional account
authentication is supported below, but has not been verified to resolve this
challenge. If API access remains blocked, contact OpenReview support with the
request ID. The website URL's `#tab-active-submissions` fragment only selects the
browser tab; it is not an API endpoint or a static list of papers.

API reference: [OpenReview API v2](https://docs.openreview.net/reference/api-v2/openapi-definition).

Publicly visible submissions need no credentials. If authorized access is needed,
set `OPENREVIEW_TOKEN`, or both `OPENREVIEW_USERNAME` and `OPENREVIEW_PASSWORD`,
in your shell environment. Do not commit credentials. Results cover submissions
visible to the account; the client cannot reveal private submissions it cannot read.

## Method-summary plan

1. First export and inspect matching titles and abstracts, with no PDF downloads.
   Any summaries at this stage must be labeled as based on abstracts only.
2. Later download matching main-paper PDFs and read each paper's main body:
   introduction, method, and experiments. Do not use
   reviews, supplements, or appendices as summary evidence.
3. Write a separate `jepa_method_summaries.md`, with each paper's title and PDF link,
   learning objective, encoder/predictor design, masking or target construction,
   collapse prevention, difference from prior JEPA methods, and main evaluation.
   Cite the main-body sections/pages; distinguish JEPA proposals from papers
   that merely mention or evaluate JEPA.

Current environment status: `openreview-py` 2.8.0 is installed in `.venv/`.
The user successfully ran search mode and saved the 337-paper export. Live
retrieval in the agent's shell remains blocked by network/DNS restrictions, but
the saved metadata is available locally. The complete-list API previously
returned `ChallengeRequiredError`. No main-paper PDFs have been downloaded or
read; the reading shortlist is based only on the saved abstracts.

Run the offline checks with:

```bash
.venv/bin/python -m unittest discover -s tests -v
```
# iclr2027
