# PDF export plan - 2022 HiMCM B - r01

Status: T03 planning only. No PDF authoring, manuscript typesetting, figure generation or artifact-marker execution occurred. The supplied PDF was read and rendered to temporary images solely for inspection. Scientific outputs are `PENDING_EVIDENCE`.

## Deliverable and ownership

Create one polished English PDF, targeting 14-18 pages with the 17-page allocation in `paper/outline-r01.md`. All content counts toward the absolute limit of 25 pages. Include a one-page Summary Sheet, contents, complete solution, standalone article for Scientific Today no longer than one page, references and honest practice/AI disclosure. No separate cover page, fabricated team identity, live-contest status or external submission.

The project assigns final exports/sources to `paper/`, figures to `figures/`, and later visualization code to `code/visualization/`. This explicit project destination takes precedence over the PDF skill's generic `output/pdf/` default. T03 itself only authorizes this plan, the outline and its handoffs; later proposed paths require a new coordinator assignment.

## Available tools: executed checks versus locations

The workspace dependency locator returned bundle `26.1026.10807`, rooted at `/Users/ericzhang/.cache/codex-runtimes/codex-primary-runtime/dependencies`.

| Item | Location/version | T03 check |
|---|---|---|
| Active Python | `/Users/ericzhang/.venvs/default/bin/python3` | Executed import checks |
| Bundled Python | `dependencies/python/bin/python3` under bundle root | Located, not executed |
| ReportLab | 5.0.1 | Imported; preferred authoring engine |
| pypdf | 6.21.2 | Imported; used for all-page source extraction/count |
| pdfplumber | 0.11.10 | Imported |
| Matplotlib | 3.11.2 | Imported only; no plot code |
| NumPy / SciPy | 2.5.3 / 1.18.1 | Imported only; no model computation |
| pandas / openpyxl | 3.0.5 / 3.1.5 | Imported only; workbook not consumed |
| Active Node | `/opt/homebrew/bin/node` | Located, not run |
| Bundled Node | `dependencies/node/bin/node` under bundle root | Located, not run |
| Active Poppler | `/opt/homebrew/bin/pdftoppm`, `/opt/homebrew/bin/pdfinfo` | Version 26.07.0 queried; metadata checked; all four source pages rendered and visually inspected |
| Bundled Poppler | `dependencies/bin/override/pdftoppm`, `dependencies/bin/override/pdfinfo` and `dependencies/native/poppler/bin/` | Located, not run |
| Artifact marker | `/Users/ericzhang/.codex/plugins/cache/openai-primary-runtime/pdf/26.1026.10807/skills/pdf/container_tools/mark_artifact_operation_started.mjs` | Located and source read; not run |

Matplotlib automatically used a temporary cache because the default home cache is not writable. Later figure commands should set `MPLCONFIGDIR` to a dedicated writable temporary directory. Do not change global configuration or install packages. Current capabilities suffice; imports are not proof of a successful report export.

## Artifact marker: run later, exactly once

Immediately before the first authorized PDF create/edit authoring command, run this successfully exactly once, as the PDF skill requires. Do not run it during T03 or for read-only source rendering.

```sh
/Users/ericzhang/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/ericzhang/.codex/plugins/cache/openai-primary-runtime/pdf/26.1026.10807/skills/pdf/container_tools/mark_artifact_operation_started.mjs --operation-kind create --expected-output-count 1 --output-format pdf
```

Then immediately perform the first authorized PDF-authoring action. Record the command/success in the later handoff. One final PDF is expected; review PNGs are intermediates. If the later task edits an existing PDF instead, change the kind to `edit`. Do not mark a planning Markdown write as the first PDF authoring operation.

## Proposed later artifacts

| Proposed path | Purpose |
|---|---|
| `paper/manuscript-rNN.md` | Reviewable English source bound to accepted claim IDs |
| `paper/claim_requests-rNN.md` | Proposed scientific wording for coordinator/modeler review |
| `paper/figure_register-rNN.md` | Source hashes/columns, units, transforms, captions and review state |
| `paper/build_report-rNN.py` | Reproducible ReportLab composition; no model fitting |
| `code/visualization/render_figures-rNN.py` | Rendering from immutable accepted tables only |
| `figures/Fxx-rNN.pdf` or `.png` | Versioned, sharp figures with readable labels |
| `paper/2022_HiMCM_B_practice-rNN.pdf` | Distinct candidate/final export; preserve last accepted version |
| `/private/tmp/himcm-pdf-review-Txx-rNN/` | Temporary review pages/extracted text if assigned in the next task |
| `handoffs/Txx/writer-visuals-rNN.md` | Hashes, commands, actual checks, limitations and review request |

The coordinator assigns exact names. Writer self-checks are not independent acceptance; reviewer findings stay in reviewer-owned paths. The writer does not edit `qa/` or the official control evidence index.

## Composition choices

- Use ReportLab, Letter pages, comfortable margins, an available embedded font covering required symbols, clear heading hierarchy and page numbers. Letter is a design choice following the source, not an additional official rule.
- Aim for body text around 10.5-11 points with comfortable leading, captions around 9 points or larger and readable tables. Cut repetition or split dense tables before shrinking type.
- Give the summary and article explicit page boundaries. Generate contents from final pagination and recheck after edits. Avoid blank dividers and orphan headings.
- Use supported subscript/superscript for CO2 and equations; define symbols nearby. Verify glyphs and minus signs visually. Use ordinary ASCII hyphens in prose per the PDF skill; no unsupported dash or black-square replacements.
- Use high contrast and distinguish lines by labels/styles as well as color. Mark observed/forecast boundaries, units and temperature baseline. State the meaning of any uncertainty shading.
- Use short table headers, aligned numeric columns, repeated headers on splits and adequate whitespace. Keep every candidate and every requested threshold visible. Distinguish zero, no crossing, missing and failure.
- Put human-readable citations near claims and include only references actually used. No tool tokens, internal placeholder text or unsupported bibliography entries in the final PDF.

## Later execution sequence

1. Read the new task/current state and exact accepted data/model/run/claim revisions. Verify hashes and record a consumer receipt. Resolve units, baseline, source benchmark, threshold convention and reliability scope before dependent prose.
2. Populate source and display register only from released evidence; route substantive wording corrections to the owner. Write summary/article after the argument stabilizes.
3. Execute the marker once immediately before first PDF authoring. Make a minimal early candidate to expose font, equation and pagination issues. This is later-task work.
4. Build the complete versioned candidate. Visualization code may format accepted values, never refit models, silently clean data, recompute threshold definitions or alter rankings.
5. Reopen actual PDF with pypdf/pdfinfo. Check page count and required sections. Extract text for coverage, missing glyphs, placeholders, references and numeric reconciliation.
6. Render every page with Poppler at readable resolution. Inspect all pages, plus dense tables/equations/figures and summary/article at full readable size. Re-render after every meaningful revision; old PNGs cannot verify a new PDF.
7. Send version-pinned PDF/source hashes and author self-check receipt to coordinator for independent content/PDF review. Repair author-owned defects in new revisions; do not modify reviewer findings.
8. After accepted review and coordinator release, preserve the exact accepted PDF and supporting sources. Record final count/hash/evidence versions and return the artifact with the PDF skill's output citation. External submission is outside scope.

## Final checks to execute later

| Check | Pass condition |
|---|---|
| Official coverage | Every 1.a-1.d, 2.a-2.c and 3 has a direct answer or explicit supported limitation |
| Page constraints | Actual PDF is at most 25 pages including all front/back matter; summary one page; article within one page |
| Evidence identity | Claims/figures/tables trace to accepted immutable versions without stale dependencies |
| Numeric consistency | Summary, tables, captions, body, article and conclusion agree with accepted values/units |
| Interpretation | Training/validation years, anomaly baseline, source quantities, causal wording and extrapolation limits remain accurate |
| Visual fidelity | Every page has no clipping, overlap, lost symbols, tiny labels, poor figures or inappropriate breaks |
| Navigation | Contents, page numbers, headings, figure/table references and citation numbers agree |
| References | Sources were consulted and support uses; metadata and URLs/DOIs are readable |
| Disclosure | Actual retrospective practice, AI roles/review and delegated decisions described honestly within cap |
| Final identity | SHA-256 identifies the exact visually reviewed and accepted PDF |

The writer executes self-checks, then the independent reviewer verifies the pinned candidate; coordinator records acceptance. A missing accepted table, conflicting claim, changed upstream version, failed page rule or unreadable rendering prevents release. Continue unaffected work and request bounded repair. Successful export alone is not an accepted solution.

## T03 boundary

Executed: workspace dependency lookup; Python package imports/versions; source PDF metadata, count and complete extraction; Poppler version query; rendering and visual review of all four source pages; marker discovery/read.

Inspected/planned only: marker invocation, PDF-authoring code, minimal authored export, figures, scientific-result validation, final report pagination/visual QA and independent PDF acceptance. These await accepted evidence and a new task.
