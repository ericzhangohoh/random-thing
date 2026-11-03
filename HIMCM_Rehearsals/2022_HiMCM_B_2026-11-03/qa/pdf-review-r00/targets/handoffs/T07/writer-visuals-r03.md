# T07 writer-visuals r03 — closed complete candidate

Owner: `/root/rehearsal_writer`. Status: **READY_FOR_INDEPENDENT_T11_AND_A04_REVIEW**. Phase B authorized by G3-r01. Author completion is not final independent PDF acceptance. Published atomically after checks below.

## Delivered report

Complete 16-page English retrospective practice report: one-page summary (p1), contents (p2), complete 1.a–d / 2.a–c solution (pp3–14), one-page Scientific Today article (p15), references and truthful practice/AI/evaluation-exposure disclosure (p16). Six figures display accepted data/paths/errors; no visualization fitting, new selection, score calculation or threshold search. No fake team number, external submission, Claude runtime or human approval.

## Exact closed files

- `paper/exports/2022_HiMCM_B_practice-complete-r03.pdf`
  SHA-256 `27182592954ee011e2c9f94b7c9a86465b3be44e3fba94d7ab1e3e3c3ef39573`
- `paper/manuscript-complete-r03.json`
  SHA-256 `ee197c1f519f8e989fb002995b30b07cde8bf19ddd41d9f0bb7f52b03fb5adb6`
- `paper/manuscript-complete-r03.md`
  SHA-256 `76c9b3de561214a0bd970c17afe95335f0559e31c8f35950dbea345177fe1616`
- `paper/assemble_manuscript-r03.py`
  SHA-256 `61c3cc8bde9fec3aa5989e4f0931f6878019ba511f1c8c0fd192927be8cd5f6d`
- `paper/build_report-r03.py`
  SHA-256 `debda6742fff74c5528a6c8233bcb352b15f51a4d7de824f4a6f25e03144206d`
- `code/visualization/render_figures-r02.py`
  SHA-256 `9f9e8d00602c4c355ad0a5ec5805f9125bedc28fdb3bfd54333a39e09df02482`
- `paper/figure-register-r02.json`
  SHA-256 `8fa87fea3acb2ea2dcbfdcaa8092d5230db776619a7b300b0d2f28f406587ccc`
- `paper/author-receipts/complete-r03.json`
  SHA-256 `8e013f4bfe0606fc310756f56884bcbc5df4d50e24c5b2b8fb202a21e4ee3570`

The author receipt pins all figure PNG/PDF files, generation sources, accepted dependencies, rendered-page images and page-to-claim/requirement map. The figure register pins accepted input tables and display transforms. Scientific manifest: `7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00`. Accepted writing manifest: `90682c659d044fb089672a4f3c42c5ec1b7b6aaa5851a0cf54263ea02d146d89`; accepted claims: `2b4056fba13ce75f8ebce73a8872fa391da19872e95eda6d43ac762267ab32d4`.

## Commands and observed results

Working directory: `/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03`. All four commands completed with exit 0.

```sh
/Users/ericzhang/.venvs/default/bin/python3 code/visualization/render_figures-r02.py
```

```sh
/Users/ericzhang/.venvs/default/bin/python3 paper/assemble_manuscript-r03.py
```

```sh
/Users/ericzhang/.venvs/default/bin/python3 paper/build_report-r03.py --source paper/manuscript-complete-r03.json --output paper/exports/2022_HiMCM_B_practice-complete-r03.pdf
```

```sh
/opt/homebrew/bin/pdftoppm -r 110 -png paper/exports/2022_HiMCM_B_practice-complete-r03.pdf /private/tmp/himcm-2022b-pdf-review-complete-r03
```

## Author checks and preserved failures

- Reopened PDF: exactly 16 pages; all intended titles on intended pages, six figure images, no DRAFT/PENDING/TODO/replacement-glyph text. Summary and article each occupy one page.
- Rendered actual r03 PDF at 110 dpi. Personally inspected all 16 PNG pages in order: text/equations, tables, figure labels, captions, margins and footers. No remaining layout defect found. PNG hashes and absolute paths are in the author receipt.
- Rechecked all 35 scientific output hashes and all manuscript-bound figure hashes. All 17 accepted claims appear in the page claim map. Read-only writer helper checked prose/tables against accepted r03 values and interpretation, with no correction found. This is writer assistance, not independent review.
- Summary/article retain D/Q rank reversal, conditional crossings, 1951–1980 baseline, annual/March and CO2/CO2-equivalent distinctions, 2016 miss, noncausality and no guaranteed long-range reliability. T1-Q comparator remains explicit. Full-history linear-time T0 wording is scoped.
- Retained complete r01 PDF after a real 17-page spill failed the planned-16 assertion. R02 compacted repeated crossing boundaries without deleting values. R03 relocates the F01 annotation and advances revision/figure paths; scientific prose/tables unchanged from r02. Earlier drafts/failures remain.
- PDF skill marker ran exactly once before Phase A authoring and was not repeated. No prohibited data/model/run/control/QA/Git edits or installations.

## Review request

Coordinator may start parallel T11 artifact review and A04 adversarial review against exact r03 PDF and this closed handoff. Check every page, numerical/figure fidelity, requirements and summary/article caveats. Final independent acceptance and repairs remain outside this author handoff. R03 is immutable; any correction receives a new revision.
