# T09 computation recovery handoff r01

Status: CLOSED_EXECUTION_CANDIDATE — independent review required before recovery acceptance.
Owner/session: /root/early_mcm_continue. Existing agent with unrelated prior work, previously uninvolved in this rehearsal; not an empty new thread. No other agent supplied the rehearsal's numerical answers or execution commands. Initial file-based acknowledgment: handoffs/T09/computation-r00.md, SHA-256 8f05652411d08ca849d1d79c663d9a5ba11bf85a79143615a7d2a18ef6fce417.

## Reconstructed task and authority

From control/state.md, role_assignments.yaml, tasks/T09.md, intake, G1/G2 records and the named producer handoff, I reconstructed retrospective 2022 HiMCM B practice, the user's delegated coordinator authority, exact G2 mixed revisions and the current closed r03 candidate. Old computation was recorded quiescent. G3/claim/PDF checks were pending in the initial state; state explicitly allowed isolated recovery verification before G3. No human reply or scientific acceptance was invented.

The primary target is runs/T05-scientific-20261103-r03/manifest.json, SHA-256 7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00. Producer handoff handoffs/T05/computation-r05.md hashes to ca0853e2b5433f1ed79fe9ccc5332150bb31dcb80e0a16ffdcca2761f48c2006. Both matched coordinator state. The release is control/accepted-inputs-g2-r02.json, SHA-256 a75cda99288a2318fe9c025be63c71fc2f1801aeab427324c144117833bbe923: framing/spec/interface r02, model decision/experiment plan r03, assumptions r01.

The full initial context is retained in the T09 intake snapshots. Original code, inputs, models, control and closed runs remained read-only. T09 wrote only its two unique recovery subtrees and its own handoffs.

## Closed outputs and identities

Current successful execution: runs/T09-recovery-20261103-r02/.

- manifest.json: ebd484ba9a80113aaff0f3eee6c19aa23e180336b1a92751828479d0892f6bc4 — 278 file identities, verified again before this handoff.
- README.md: 670a7b6d29fbe00da25934d066e63223a5fdaf1ecce05557b55b3d17cdd63dac — readable execution, probe and limitation receipt.
- execution_report.json: 149ce003db697214c013914cf80ea48dc28e0cb5fac337539e6bd7ad280fe9fb.
- output_comparison.json: 74eac20dbc0b7046a646b663cd7528874c93341d248db36436c423fcceb30e7b.
- stale_probe_receipt.json: 5b47e409b17fed4a2254f7b002e7d60d2583c12a0640fc96dd24ecd835aebfab.
- decision_recalculation.json: 2ef0d60a53f43b259a08d7366cfd0a05827c5dd8fc7848bd746368c622dedb3d.

Exact child invocations, working directories, environment overrides, timestamps, exits and stdout/stderr are under commands/. Top-level commands are in top_level_commands.json. Recovered sources/configuration/data/specification are under recovered/; hash-verified original reference outputs under reference/outputs/; newly executed outputs under outputs/.

## What was actually executed

Using /Users/ericzhang/.venvs/default/bin/python3, verified in this worker as Python 3.12.14 with numpy 2.5.3, scipy 1.18.1, pandas 3.0.5 and openpyxl 3.1.5:

    /Users/ericzhang/.venvs/default/bin/python3 -B runs/T09-recovery-20261103-r02/recovery_driver.py
    /Users/ericzhang/.venvs/default/bin/python3 -B runs/T09-recovery-20261103-r02/check_frozen_decision.py

Both exited 0. The driver executes 13 recorded child commands, including two deliberately rejected integrity fixtures; those expected exit-1 results remain explicit. Each child had a 60-second limit and single-thread environment. Test temporary files stayed in the assigned T09 subtree.

The retained retriever recovered all 88 dependencies and verified their hashes; all 23 G2 released identities matched. The 9 ingestion, 28 model and 7 repair unittest methods passed. Original XLSX reingestion matched all three admitted CSVs. Separate development, final and production commands ran from the recovered CWD, using retained code and the exact retained configuration. The T05 wrapper itself was inspected rather than rerun because it snapshots current project files and requires a T05 run ID.

All 32 deterministic output files are byte-identical to r03's declared, hash-verified references. Three timestamped receipts have exact equality of all other fields. Excluded timestamp/dependent-digest fields are enumerated, then fresh receipt links and local chronology are checked against the actual recovered bytes. No numerical field is dropped from comparison. All 12 postrun checks pass.

The original logical run ID is preserved inside the unmodified config for exact reproduction; T09's actual execution identity is its unique directory, logs and manifest. The separate standard-library check recalculates MAE and eligibility from 350 development rows and reproduces the fixed D/E/Q tie rule and sequential T0 versus T1-selected-CO2 decision. It confirms D then T1-D, reading no final forecast or metric files and importing no original analysis/model module. This verifies selection arithmetic on the reproduced forecasts, not independent forecast-model correctness.

Before/after verification confirms 125 primary records unchanged: the primary manifest, 88 retained dependencies, 35 outputs and producer handoff.

## Stale dependency and wrong-reference tests

1. A copied joined table changes only a fixture value from 315.98 to 316.98 while retaining the original expected digest. The actual recovered retrieval command rejects it with Recovered artifact hash mismatch and creates no success receipt. A new versioned valid copy retrieves with the original hash.
2. A copied frozen selection receipt replaces development_metrics_sha256 with an incorrect digest while preserving genuine development output bytes. The retained final-stage command rejects it with Development evidence changed after freeze and produces no final_* artifact. A separately versioned valid six-file development bundle then completes final and production; all 32 deterministic outputs and receipt semantics reproduce again.

Both altered fixtures and failed logs are preserved. They are operational tests on copies, not edited official observations or new scientific conclusions. They demonstrate these integrity failures cannot pass the tested workflow, not OS enforcement or comprehensive anti-forgery security.

## Failed attempt preserved

runs/T09-recovery-20261103-r01/ remains failed and immutable. Its primary reproduction and rejection probes succeeded, but the recovery harness used a filename-prefix rule that accidentally copied production-generated development_error_samples.csv into the restored development bundle. The production command correctly refused to overwrite it. No original scientific defect is inferred.

The r02 retry uses the exact six development-stage outputs. Only the recovery-agent-owned harness changed; no original scientific source/config/data changed. The r01 failure_closure.json, command 13 error, partial outputs and source bytes remain available. The failure receipt's phrase reviewer-owned harness refers to this recovery agent's harness, not an independent acceptance reviewer.

## Inspected versus not established

I inspected the complete producer handoff, runtime/retrieval/wrapper contracts, relevant stage write behavior, released decision/interface/data definitions, and selection-specification sections. I executed byte recovery, existing tests, ingestion, all three scientific stages, comparisons, selector recalculation and copied-fixture failures/restoration. I did not independently rederive the entire climate model, verify current external sources, retune, author/review the final PDF or accept the scientific conclusions.

Prior A01 final-score exposure remains disclosed. Local freeze-before-final order cannot become a global blindness claim. This is Codex/file/runtime work, not Claude-native launch or contest submission. No Git, installation, global settings, biological research or historical solution-paper research was performed.

## Requested next action

Coordinator: pin the notified handoff and T09 manifest; assign independent review of recovery identities, executed commands, comparison exclusions, stale rejection/restoration and failed-attempt preservation. Only that review and coordinator disposition may record recovery acceptance. Scientific/claim/G3/PDF acceptance remains separate. No concrete recovery blocker remains in the completed r02 evidence.
