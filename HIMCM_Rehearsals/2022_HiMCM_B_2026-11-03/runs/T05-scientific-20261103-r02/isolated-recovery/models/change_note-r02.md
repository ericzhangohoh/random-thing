# T06 change and invalidation note r02

Proposed replacement set: framing-r02, model_spec-r02, model_decision-r02, model_interface-r02 and experiment_plan-r02. Assumptions-r01 remains applicable unchanged. Preserve all r01 files, toy checks, source data, QA outputs and closed runs. Release requires independent review and coordinator G2 r02; author completion is not acceptance.

## What changed and why

1. A01 demonstrated that pooled-development selection and final-segment accuracy diverge. R04 now explicitly separates selected primary rule, observed final best score and unknown future accuracy; origin/horizon instability and reversals must be visible. No candidate or selector changed.
2. The temperature comparison is described relative to the specified linear-time baseline and eligible sequential pair. All declared T1 comparator scores remain visible; no unique CO2 information or causal result is claimed. T1-E's exact time-linear algebra is stated.
3. Historical error envelopes retain their original formula and final misses. Counts are descriptive; 2031 is a tested-horizon display cutoff, not a reliability guarantee. No radius is changed after seeing final data.
4. New per-origin winner/count and leave-one-origin-out pooled ranks are labeled post-A01 robustness diagnostics. They cannot alter original selection and are not represented as predeclared analyses.
5. M06/I05 separate first-crossing event status from whole-domain validity. CROSSED can coexist with later invalidity and mandatory warnings. Invalidity before/at crossing prevents that/later apparent hit; already-above origin and fully valid non-crossing remain distinct. Required fields, precedence and branch tests are explicit.
6. Evaluation chronology now explicitly records A01 final-score exposure before primary execution. A local freeze receipt does not certify that all agents had never seen final scores.

## Unchanged mathematics and data

The supplied vintage, annual/March correction, Mauna Loa/global pairing, baseline, keyed years, CO2 forms D/Q/E, temperature forms T0/T1, log reference, fit equations, development origins/horizons, MAE/tie selector, final assessment period, final refit, thresholds, search horizon and sensitivity windows are unchanged. The author executed byte-equality checks on full M00–M02/M04 and equation-token equality through M05. All eight r01 artifact hashes still match the original inventory.

No new physical model, optimized window, hyperparameter search, climate-policy effect or stochastic distribution is introduced. Independent adversarial evidence is not silently promoted to the primary result set.

## Invalidation and required rechecks

Source admission and T05 ingestion remain valid for unchanged source semantics; no ingestion rerun is required by this repair. New output fields/status handling and diagnostics require updated computation code/tests under a new immutable version/run. Existing ordinary valid-path numerical predictions should reproduce unchanged, because equations and selection are unchanged. If an r01 scientific run exists, retain it and compare common numerical fields; do not overwrite it or relabel it r02. If none exists, implement once after r02 release.

Review r02 status precedence and all new synthetic cases independently; author tests do not certify production. Recheck selection receipt ordering, leakage fixture, actual ranking reversal, envelope misses and all crossing boundary values from primary outputs. Reconcile any discrepancy with adversarial probes before claim release. Manuscript, summary and article require the narrowed labels and later-invalid warnings. The exact primary-run interpretation remains pending a separate T05 handoff.

## Executed author checks

`/Users/ericzhang/.venvs/default/bin/python3 models/boundary_selfcheck-r02.py`: 14 synthetic checks passed, no supplied observations; exact script/results retained. It checks all status precedence branches, negative valid anomaly, nonmonotone first hit, later failures and the T1-E time-linear identity.

`/Users/ericzhang/.venvs/default/bin/python3 models/adversarial_evidence_check-r02.py`: six consistency checks passed on retained A01/A02 outputs, without fitting observations or rewriting QA outputs. MAEs, misses, error signs, origin winners and stored-row scores agree with the reports. This is author consistency checking, not independent validation of the primary run.

Original artifact hash comparison and equation-token/section comparisons passed. No external research, code/data/control/QA mutation, Git operation, package installation or unavailable primary result was introduced.
