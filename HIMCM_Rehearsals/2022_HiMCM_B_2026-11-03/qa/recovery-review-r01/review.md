# T13 independent recovery review

**ACCEPTED_FOR_SCOPE.** Reviewer /root/rehearsal_reviewer, 2026-11-03. Open blocking/consequential/editorial defects: 0/0/0. This is bounded recovery receipt, isolation and equivalence acceptance. It does not repeat T10 mathematical validation or accept the final PDF.

## Exact targets and checks

Closed T09 handoff `handoffs/T09/computation-r01.md` SHA-256 `5548ca63d2e67a246245aa498d66c53adb0b022f9ca5b0145052077daefe77ad`; successful recovery manifest `runs/T09-recovery-20261103-r02/manifest.json` SHA-256 `ebd484ba9a80113aaff0f3eee6c19aa23e180336b1a92751828479d0892f6bc4`. The primary reference is the T10-accepted scientific r03 manifest `7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00`.

I executed `verify.py` using `/Users/ericzhang/.venvs/default/bin/python3`: 721 receipt, identity and comparison checks pass in `checks.json`. `target-inventory.json` pins 545 files and retained copies: the closed recovery manifest and its 278 inventoried files, closed handoff, and the complete preserved failed r01 subtree. All recovery inventory digests and sizes match. All 88 recovered dependencies match the primary manifest's identities; all 23 released G2 identities match. The recorded 125 before/after primary records are identical and their current bytes independently match.

I independently compare actual recovery outputs with hash-verified primary reference bytes, both for the ordinary recovered run and the separately restored valid-reference run. Each has exactly the expected 35 filenames. All 32 deterministic files match byte-for-byte. For three receipt files, all non-excluded fields match exactly. Exceptions are only selection frozen_at; final started_at/finished_at/selection_frozen_at/loaded_selection_sha256; production finished_at/loaded_selection_sha256/final_assessment_sha256. The fresh digest links, final-output links and stage timestamp order are separately verified. No scientific field is excluded. All 12 postrun checks pass in both output sets.

## Execution and isolation evidence

I read the complete recovery driver and separate selector-check source, producer handoff, command receipts and relevant logs. Thirteen child commands are recorded with exact Python, recovered/fixture working directories, single-thread environment, local TMPDIR, 60-second bounds and exits. The logs substantiate 9 ingestion + 28 model + 7 repair test methods, all passing. Workbook reingestion independently matches all three admitted CSV byte streams. This reviewer did not rerun those 44 tests or the production stages: their execution evidence is T09's retained logs, independently hash-verified here. My independently executed work is the 721 receipt/hash/comparison checks.

The driver uses retained source/configuration/data from the recovered tree, retains the original logical scientific run ID for exact reproduction and records a separate physical T09 directory and execution identity. It deliberately does not rerun the T05 wrapper that snapshots current files. Source inspection and command arguments support writes within the T09 subtree; this is not a claim of OS-enforced isolation. The selector check reads 350 development forecasts only, implements the existing D/E/Q tie rule and sequential temperature eligibility, and obtains D/T1-D. It checks selection arithmetic, not independent model forecasting. These values agree with T10's prior independent evidence.

## Rejection, restoration and failed-attempt preservation

The actual altered joined-table fixture differs from the expected digest, and the retained retriever log records exit 1 with the expected hash-mismatch message. No retrieval success receipt exists. The separate valid v02 copy matches the original joined-table digest and retrieved successfully.

The wrong-reference fixture contains a zero development-metrics digest while preserving genuine development outputs. Its retained final command exits 1 with “Development evidence changed after freeze”; no final_* outputs exist in that failed fixture. The separate valid v02 development bundle completes final/production and independently passes the same 32-byte/3-semantic comparisons described above. Neither failed fixture was overwritten or presented as a successful ordinary run.

Failed recovery r01 remains present with failure_closure.json, driver traceback, failed command 13 receipt/log, partial outputs and original harness bytes. The error names development_error_samples.csv: the harness selected development-prefixed filenames and accidentally included a production-generated file, so production correctly refused overwrite. The r02 source uses exactly the six development-stage files instead. This repairs the recovery harness; it changes no scientific source or results. The r01 receipt's “reviewer-owned” phrase is explicitly clarified in the closed handoff as referring to the recovery worker, not this independent reviewer.

## Limits and disposition

No owner repair is needed. Root may record scoped recovery acceptance. This demonstrates file-based continuation by an existing previously uninvolved agent, not an empty new context, independently invented commands from scratch, comprehensive security against coordinated forgery or a new blind holdout. Prior global final-score exposure remains disclosed. T10 owns scientific/claim acceptance; G3 remains coordinator authority; PDF/layout/length/citation inspection remains separate. Direct root dispatch authorized this task; control/tasks/T13.md was absent at initial inspection and was not fabricated or edited. Reviewer writes were confined to the assigned QA and T13 handoff paths.
