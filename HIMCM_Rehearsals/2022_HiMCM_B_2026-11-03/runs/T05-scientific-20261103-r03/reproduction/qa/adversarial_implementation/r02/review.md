# A03 full implementation adversarial review r02

**CHANGES_REQUESTED** for two confirmed negative-path implementation defects. Existing closed-run numerical forecasts are not shown wrong: independent isolated rerun reproduces all32 numerical outputs exactly, and the original selection is independently consistent with development scores. This verdict requests owner repairs/new versioned run evidence before claiming the failure-contract and frozen-stage safeguards are complete.

Same independent A02/A03 reviewer, no new-context claim. Targets: closed T05-scientific-20261103-r02 manifest SHA256 `33beee2a51123a789d83e60ae02f22c05b73acecc69e17d02168d455110e5870`; computation-r04 handoff as routed. `pins.json` records all44 retained dependency and35 output hashes plus manifest. All were verified and copied before tests; original target hashes reverified unchanged afterward. Sources actually executed are `snapshot/code/experiments/analysis_r02.py` and `snapshot/code/modeling/climate_models_r02.py`; mutable source files are not authority.

Pre-probe strategy `strategy.md`; scripts `probe.py`, `diagnostic-probe.py`; evidence `results.json`, `execution.log`, `probe-console.log`, `diagnostic-results.json`, `diagnostic-console.log`. Commands use `/Users/ericzhang/.venvs/default/bin/python3`; all writes remain under owned QA. Global final exposure through A01 is acknowledged; no new selector or scientific model proposed.

## A03-F01 — Freeze receipt can silently change primary selection [P2]

**Target contract:** final stage must load a frozen development selection; identity and table guards should prevent silent stale/tampered selections, and `selection_changed=false` should not certify a contradictory receipt.

**Strongest defense:** complete closed run has an external manifest hash for selection_frozen.json, and its actual D/T1-D choices match development. Final stage also checks unchanged receipt during its own execution. These protect the present reviewed closed run but do not validate an edited receipt arriving between development and final stages before manifest closure.

**Concrete test:** copied unchanged development evidence plus selection receipt into `tampered-selection/`. Changed ONLY selected_co2_id D→Q and selected_temperature_id T1-D→T1-Q, retaining original development MAEs, temperature_selection_candidates=[T0,T1-D], identity and CSV hashes. Called actual copied `Analysis.final()`.

**Observed:** final returned successfully; final_assessment_receipt.json has status COMPLETED, selected Q/T1-Q and `selection_changed:false`. Thus final accepts a selected temperature outside its stated eligible pair and a CO2 model inconsistent with declared minimization. It hashes the already-modified receipt and treats that as its baseline. `results.json.tampered_selection` retains this executed evidence.

**Consequence/scope:** stage-boundary integrity defect, affecting I04/M03/E03–E04 and reproducibility/unchanged-selector assertions. Not evidence existing production forecasts are wrong or that actual authors changed selection. Severity P2 due misleading success if a stale/edited selection receipt is loaded.

**Minimum repair:** validate receipt selected IDs, candidate eligibility and scores against verified development evidence and declared selection rule before final or production. A stage-runner-owned expected receipt digest can additionally guard any mutation; do not rely solely on receipt self-reported fields. This is validation of the original selector, not a new scientific selection or use of final errors.

**Recheck:** the exact IDs-only tamper above must fail explicitly before creating final outputs; changed eligibility/score fields must also fail when inconsistent with development metrics; unchanged receipt must still run and preserve original D/T1-D. New code/run version, prior closed bytes retained.

## A03-F02 — Nonpositive diagnostic count loses the violation [P3]

**Target contract:** `path_diagnostics.nonpositive_co2_count` accurately describes evaluated CO2 path violations.

**Strongest defense:** invalid_count and individual path statuses remain correct; actual historical-fit future paths are positive, so current numerical outputs contain no missed violation. This lowers severity but does not make the count correct on its declared failure branch.

**Concrete test:** subclassed copied Analysis solely to return D=-1 at2023, calling original production assembly; all other behavior unchanged. In completed fixture `nonpositive-complete/`, both full and last30 D2023 rows have status NONPOSITIVE_CO2, value null; invalid_count278 correctly counts the invalid suffix. Both diagnostic rows nevertheless report nonpositive_co2_count0. The code counts non-null values<=0 after nonpositive rows were nulled.

**Outcome:** confirmed counterexample routed initially by main reviewer and independently executed here. `diagnostic-results.json` preserves rows and completed-production result. First preliminary fixture stopped later on a reviewer fixture FileExistsError (over-copied development_error_samples from old outputs); that reviewer setup failure is preserved in results.json and does not replace this successful fresh corrected fixture.

**Consequence/scope:** misleading diagnostic on invalid synthetic path, R02–R04 path-validity evidence. P3; no present positive-path numerical impact.

**Minimum repair:** count direct NONPOSITIVE_CO2 statuses or record explicit raw evaluations/count before nulling. Define count over evaluated years before prefix invalidation, not unexecuted future years. Preserve null output for invalid forecasts and existing invalid-suffix semantics.

**Recheck:** injected path must yield count1 per affected path/window plus the correct invalid suffix; ordinary original positive paths remain count0 and forecasts unchanged.

## Attacks that passed

- Copied all44 retained artifacts with exact hashes, reran separate development/final/production from recovered snapshot/CWD. All32 non-timestamp numerical outputs match closed originals byte-for-byte. Three stage receipts differ as expected in timestamps/hash chains; not passed off as equal. No mutable original input was used by these stage invocations.
- Changed all post1991 CO2 by+1000ppm and temperatures by−100°C in in-memory copied fixture. All seven origin1991 fits and future2001 predictions unchanged. Increasing the upstream D forecast slope changes T1-D forecast, confirming actual predicted-CO2 dependence.
- Changed copied development forecast bytes: load_frozen explicitly rejects. Changed copied final forecast bytes: production explicitly rejects. These guards work; F01 is specifically semantic receipt tampering.
- Crossing before subsequent nonpositive CO2 preserves CROSSED2023 while declaring invalid domain from2024. Invalid2022 followed by later mathematical crossing returns INVALID_PATH/no firstyear. Negative valid temperature anomaly correctly crosses later without a positivity failure. These match r02 first-passage/valid-prefix semantics.

No broad reimplementation of the main reviewer's4776 ordinary numerical checks was claimed. No independent assertion about final PDF or fresh-worker bootstrap is included. Owners repair F01/F02; reviewer will recheck exact changed versions. Original candidate can remain numerically informative while safeguards are corrected, with no holdout reset.
