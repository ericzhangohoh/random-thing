# Handoff — T06 — modeler — r01 (repair packet r02)

Producer /root/rehearsal_modeler; date 2026-11-03; recipient coordinator/root, independent reviewer, then computation. Status: author response and boundary repair complete, proposed for independent review. Not self-accepted, not G2 r02 release, and not primary-run scientific interpretation.

## Inputs and consumer receipt

Acknowledgment `handoffs/T06/modeler-r00.md` pins task, current state, G1/G2 r01, evaluation ledger, original six model docs, A01/A02 reports and actual probe code, A01 final result JSON and T05 ingestion handoff. Additional result/dependency bytes actually consumed:

- `qa/adversarial_validation/development_probe_r01.json` — `3d98a37dda245eeeefa20ff7e9d5c9ced3b6aca86d36d74bef8fdf8a074a4601`
- `qa/adversarial_structure/probe-results-r01.json` — `eebc16ea385a5edbb06805497ae5a6da0581004d2ce5eb211d4ffbebcd9f2ea0`
- `models/assumptions-r01.md` — `824af993532cd8a35204fa8c137db490c8f2cec0345c6b08454825ebe24c77e9`

G1/G2 r01 released the supplied-vintage annual Mauna Loa ppm / global anomaly against 1951–1980 interface and original frozen forms/rule. Those are unchanged. T05 ingestion handoff describes 63/64 source rows and63 common-year pairs; this author does not claim new data/implementation certification. A01/A02 are independent adversarial evidence; this author has now read final2012–2021 scores, preserving the existing exposure ledger. No global unseen-holdout claim remains available.

## Outputs and exact identity

| Artifact | SHA-256 |
|---|---|
| `models/adversarial_evidence_check-r02.json` | `dc45b6f010a46920b79b1d9d7f74801b8d0f13071605901aaabd648c82157bec` |
| `models/adversarial_evidence_check-r02.py` | `381415ece316d63d7594d3a952e493f0034e66a4ea02b28d0c6b96d3641d7508` |
| `models/author_response-r02.md` | `79b4976a165761ad5a91f26940ac27789ad27acd5c0a831370db3fb4c71300d5` |
| `models/boundary_checks-r02.json` | `5a5b3aeab52e380ec1b4daadac03c1699b61e365f947755656ca7da703ead61d` |
| `models/boundary_selfcheck-r02.py` | `c1f1fbcc8e6c6460e6ea824a470e8b2c00bd0a2f97c3c42557dadd9a09745b20` |
| `models/change_note-r02.md` | `2c691bb4991174d797fb4e53f4a384f199d0d79400b9653477be70702fb97ab3` |
| `models/experiment_plan-r02.md` | `33e90253678a07056412103997d3f0d7dc536392712ce9b2ff29ec72b0d85f14` |
| `models/framing-r02.md` | `3ca133e3dd74d75a68f989e0867fca25be5d20302fa7ab4c799023f6c5b2d51a` |
| `models/model_decision-r02.md` | `33900567efa1294e858d121568ac1d3588286c23d9dc6c01803f9b5430b9a462` |
| `models/model_interface-r02.md` | `2b93537df100d6a1cb51df5bba8ad7d069aab436c776df22c2b9a390e29bd216` |
| `models/model_spec-r02.md` | `ba81a65550193a8775f2275224329d6bad339191ffccf4cf33c9a1094ea1c796` |
| `models/artifact-hashes-r02.json` | `8d31c1742f492b9fd8122e17039345df4ebfcfeec438d02c1a466e755dc644d6` |

Complete replacement core: framing, model_spec, model_decision, model_interface and experiment_plan r02, plus unchanged assumptions-r01. Original r01 artifacts retain exact hashes. Author response records each finding's strongest defense, disposition, evidence, repair and recheck. Change note maps affected consumers and invalidation.

## Author decision on the attacks

Accept A01's narrow “most accurate” wording objection: pooled-development selection, best final-segment score and unknown future accuracy must be distinguished. Independent evidence shows instability/reversal; primary results must reproduce or explain it. Preserve original equations, candidates, chronological splits, MAE/tie selector, sensitivity windows and threshold/search domain. No switch of frozen primary rule, refitted envelope or new candidate search occurs.

Report the temperature choice as the selected sequential pipeline and show all declared comparator scores. Narrow predictive-value language to the specified linear-time baseline; no unique CO2 information or causal beta follows. Keep the time-linear identity of T1-E explicit. A02 alternatives remain exploratory, not retroactively predeclared candidates.

Keep original historical-error radii and require every miss/observed error. 2031 remains only a maximum tested-horizon display cutoff, not a guaranteed reliability date. Add per-origin winner/count and leave-one-origin-out pooled-rank summaries as explicitly post-assessment diagnostics; they cannot alter selection. Author response cites adversarial numbers only, without mislabeling them primary results.

## Resolved M06 boundary

First annual crossing is established only on a contiguous valid prefix from the origin. Preserve CROSSED if it occurs before later invalidity; report search_domain_valid=false, valid_through_year, invalid_from_year/reason and monotonicity scope. Later failure does not erase the event but invalidates any claim of full-domain path validity.

Invalid origin or invalidity before/at a putative crossing yields INVALID_PATH and first_year=null, even if values later recover. A valid already-above origin gets AT_OR_BEFORE_ORIGIN plus any later warning. Only a fully valid subthreshold domain gets NO_CROSSING_THROUGH_2300. Required-input validity precedes same-year threshold checks; negative anomalies are valid, nonpositive CO2 is not. Spec/interface r02 are complete, not a patch that requires guessing precedence.

Computation received the bounded proposal promptly and was explicitly told it is unreleased pending independent review/root.

## Checks actually performed

Executed `/Users/ericzhang/.venvs/default/bin/python3 models/boundary_selfcheck-r02.py`: 14 synthetic author checks passed, no supplied observations. Cases cover status precedence, valid crossing/later nonpositive/nonfinite/missing/evaluation failure, invalid-before/at crossing, resumed validity, invalid origin, already-above origin, bounded non-crossing, valid negative anomaly, exact/fractional crossings, nonmonotone first hit and T1-E algebra. Results pin current spec/interface/script hashes.

Executed `/Users/ericzhang/.venvs/default/bin/python3 models/adversarial_evidence_check-r02.py`: six author consistency checks passed on retained A01/A02 results, with no fitting or QA writes. MAEs match error arrays; misses match radii; D's final errors are negative; final Q MAE is lower; Q wins three origins; A02 scores match its stored predictions.

Executed original eight-artifact r01 hash preservation check; byte-equality of M00–M02 and M04; inline mathematical/code-token equality through M05; current self-check hash consistency; new packet inventory. Inspected model-choice/time-split preservation and per-finding evidence. These are author checks, not independent review or primary implementation validation. No new historical fits, accepted primary numbers, final PDF work or Git operation occurred.

## Invalidation, unresolved work and requested action

Writes stayed within new models revisions and own T06 handoffs. Original files, code, data, control, QA and closed runs were not edited. No source/ingestion rerun is required. Status/schema/diagnostic consumers need a new code/run version and relevant tests; common ordinary forecast values should reproduce unchanged. Preserve any existing r01 scientific run; never relabel or overwrite it.

Coordinator: assign independent review of full r02 core, author response, exposure wording, exact M06 precedence/fields/tests and original-rule preservation. Only after acceptance, record delegated G2 r02 and send exact hashes to computation. Computation must independently implement/retest boundary cases and diagnostics, retain local freeze ordering without a global unseen-data claim, and reconcile primary outputs with adversarial evidence. Writer must receive the narrowed claim contract and later-invalid warnings. This task ends at the repair packet; later T05 primary-run interpretation awaits a separate root notification.
