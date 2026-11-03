# T04 canonical independent review r01

**Verdict: ACCEPTED_FOR_SCOPE.** Date: 2026-11-03. Reviewer: `/root/rehearsal_reviewer` (independent of target design/authorship/repair). No unresolved blocking or consequential finding in the scope below. This is not human approval, empirical model validation, ingestion-code acceptance or final PDF acceptance.

## Scope and exact identity

Reviewed closed T01 r01 source admission/dictionary/quality, closed T02 r01 framing/model specification/decision/assumptions/experiment/interface and modeler toy evidence, closed T03 r01 outline/export plan, intake/requirements-r00, and the five reusable workflow files listed below. Coordinator's later scope message added the environment repair in roles/computation.md and EXECUTION_PLAYBOOK.md plus inspection of T05 environment evidence. No target/control file was edited.

`target-inventory.json` contains the exact SHA-256 and retrievable snapshot of all 50 reviewed/evidence files. Both producer inventories were independently checked against current bytes and sizes before snapshots; all 23 T01 and 8 T02 entries matched. Retention covers original inputs, source extracts, closed target packets and workflow files. Prior preliminary snapshots/review remain in `qa/framing-r00/`; this canonical receipt supersedes that incomplete status, not those bytes.

| Principal target | SHA-256 |
|---|---|
| T01 artifact inventory | 4c4161752d7eac5dd01a01d35be18e7b10a65701f77cdcf6b66e943fd5d68451 |
| T02 artifact inventory | d5051bbb0ceda4562a6ac0e3dc6893227a803c6fe7fb23ad3a9683d3ff27bc16 |
| models/model_spec-r01.md | 4c3de3faa1234fe8e9add94fe2b6c7a655808ceb351b6c2dfea775d894f3c7da |
| paper/outline-r01.md | 3a5c3a726bd74fcf338564d3735b611b7ce4093dc4b2cc1e511abbd13c446c33 |
| paper/export_plan-r01.md | cc52b929ce02fd2a621dc2a47cae0fce554eda8378afef39e105ea6a09f9414e |
| WORKING_DOC.md | 92454a0757851a5f8ba57828859eaf089d2094e59ef624909aa3820712b05ebc |
| EXECUTION_PLAYBOOK.md | 3062c1701420cd12786c624a2bfa8ad39db3d816e261229919331e467e09537b |
| setup/BOOTSTRAP_PROMPT.md | 91cc0f36c816dfbebd1c468c53e2d85ed29ab958f8d8f0311b6bc214fa6f1010 |
| templates/DELIVERY.md | b345ee121e52f2772d09b77f5e002d2cb0f8fdc582f50eb25d17f794bad0f1a9 |
| roles/computation.md | dbcd30cbdaeaa89b986124c178f583c1acd456efcbd24598e60daaa06e3dda92 |

## Checks and evidence

### Official coverage and data

Read the actual four-page statement, independently extracted it with pypdf, rendered all pages with Poppler and inspected the renders. Page 1 questions 1a–1d, 2a–2c and 3 map to R01–R08 and the T03 evidence destinations; page 2 delivery requirements map to R09. R10–R11 are honestly identified as rehearsal requirements. Source captions/tables on pages 3–4 were included, not just the task paraphrase.

Independently parsed the XLSX with ZIP/OOXML without importing producer code. Found 63 CO2 observations (1959–2021), 64 temperature observations (1958–2021), unique contiguous years and 63 year-key matches. Recomputed all 36 ten-year intervals ending 1969–2004 at supplied hundredth precision. The 1994–2004 increase is 18.74 ppm; prior maximum 1993–2003 is 18.77 ppm. This supports only the supplied annual-data comparison; it is not a significant physical difference or a reconstruction of all historical March periods. Executable/result evidence: `../framing-r00/independent_data_check.py` and `independent-data-checks.json`.

Read retained NOAA annual/monthly/news and NASA baseline/index evidence. Independently opened the official OECD report and checked the relevant climate passage: [OECD report, printed p83 / physical p85](https://www.oecd.org/content/dam/oecd/en/publications/reports/2012/03/oecd-environmental-outlook-to-2050_g1g14e69/9789264122246-en.pdf). Its 685-ppm value is greenhouse-gas CO2-equivalent; its CO2-only 2050 scenario is about 530 ppm. This agrees with T01's correction. Current reference observations/revisions are excluded from historical fits; supplied Mauna Loa annual concentration remains an indicator, and temperature retains the 1951–1980 baseline. Remote OECD evidence is retained as labeled selected text, not falsely represented as a local original PDF.

### Model rationale and mathematical contract

Read the complete closed six-document T02 packet and toy code/output. D/Q/E represent recent absolute growth, constant absolute acceleration and constant proportional growth, with real structural differences and explicit extrapolation limitations. At least Q/E are full-history fitted descriptions as requested; the drift baseline is clearly labeled as an endpoint-based forecast comparator. Every candidate retains 2050, 2100 and threshold outputs even when it loses selection or becomes invalid.

Units and interfaces agree: x is decades, Q derivative divides by ten, exponential comparisons return ppm, T1 takes the log of a dimensionless ratio, beta has anomaly units per log-concentration unit. Log reference changes shift the intercept and leave predictions invariant. The source year join and fixed reference are explicit. The last-30-year sensitivity keeps this fixed scale without using later observed values to forecast earlier targets.

Development origins 1981/1986/1991/1996/2001 and horizons 1–10 stop at 2011. Final assessment fits only through 2011 and predicts 2012–2021 without refitting. I04 requires an immutable saved selection receipt before final assessment. Both CO2 selection and T0/T1 choice use development only; other linked paths remain declared comparators. The final ranking cannot replace a frozen winner. Every linked forecast uses predicted future CO2, avoiding observed-covariate leakage. The full supplied table was already visible; the packet correctly limits 'untouched' to computation, not blinded human exposure. Overlapping development targets are not falsely called independent samples.

Thresholds are first integer annual central-path crossings after 2021, with already-at-origin, invalid-path and bounded non-crossing statuses. Scanning handles nonmonotone first passages; endpoint agreement in 2050 is not substituted. The 2300 search endpoint is disclosed; absence by then does not mean never. Requested temperature thresholds preserve their actual baseline and are not Paris-target dates.

Level, linear/quadratic-detrended and first-difference associations address common trends without claiming causal identification. Reliability claims are restricted to tested horizons, and the empirical maximum-error envelope is explicitly not a confidence/prediction interval or guaranteed coverage bound. Future interval display ends in 2031; 2050/2100 values and later crossings remain conditional extrapolations. Poor holdout results must narrow claims rather than trigger silent retuning.

Inspected 17 passed synthetic modeler checks and their spec/script identity. They establish toy mathematical feasibility, not correctness of future computation code. I did not rerun that author script or independently fit historical forecast candidates in T04. Independent implementation tests, substantive numerical review and claim review remain required later.

### Writing, authority and operational repair

T03 covers every numbered answer and proposes a feasible 17-page allocation under 25 total. Summary/article have explicit one-page boundaries; actual export, every-page visual inspection and final cross-section numeric reconciliation are mandatory. All scientific slots remain pending accepted evidence. No invented team identifier, live status or PDF success is asserted.

The four delegated-practice edits fit the user's explicit instruction recorded in intake: choose a historical non-biological problem, complete the workflow, repair problems and synchronize. They preserve G1–G3 evidence/review and honest DELEGATED_PRACTICE_DECISION records, with no fabricated human answer or implied contest submission. The broader reusable documentation describes Claude Code setup; intake and planned disclosure accurately state this test uses actual Codex collaboration and sequenced logical roles. No claim of live Claude orchestration is accepted.

The added environment rules directly address the observed T05 failure. Read the preserved r01 traceback (CLT Python 3.9 missing SciPy metadata), r02 environment.json (explicit default venv Python 3.12), and recorded subprocess commands/test output. The repaired workflow requires each worker to resolve its own exact executable/imports, record that executable, avoid silent installation/switching, preserve failure and retry under a new run ID. This is an appropriate bounded repair. T05's full ingestion implementation/recovery claims were not independently audited here; this inspection supports the workflow/environment finding only.

Author/reviewer boundaries are intact in the inspected record: workers own their artifacts, coordinator owns control/ and decisions, reviewer only writes qa/ and its handoffs. Actual producer/consumer receipts distinguish provisional source consumption from accepted release. No draft existence, chat notification or elapsed time substitutes for acceptance.

## Findings and limitations

No blocking/consequential finding remains in the reviewed scope. One optional editorial improvement: include the already verified contextual May 2022 rounded 421-ppm statement explicitly in the final source clarification box. T01 has the evidence and the numbered questions are already covered, so this does not block acceptance.

No historical model fit, forecast score, winner, threshold year, probabilistic uncertainty claim, full ingestion-code acceptance, final scientific conclusion, authored PDF, final page count or external submission is covered by this verdict. Model forms are plausible empirical experiments, not climate-process validation. Reading source definitions and checking arithmetic cannot establish future accuracy.

## Next action

Coordinator may use this version-specific review in G1/G2 delegated-practice packets and release T01/T02/T03 for their named admission/design/planning uses. Computation must acknowledge exact accepted versions and pass its own specification/boundary/leakage tests before full historical computation; then freeze selection before final assessment. Preserve failures and all retained dependencies. Later independent numerical/claim and rendered-PDF reviews must inspect the exact closed artifacts. Any consequential target change needs affected re-review; this verdict does not transfer silently.
