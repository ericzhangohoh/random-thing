# T08 independent model repair and protocol review

**Canonical verdict: ACCEPTED_FOR_SCOPE.** Reviewer: /root/rehearsal_reviewer, 2026-11-03. Independent of target design/authorship/repair. No unresolved blocking, consequential or editorial finding remains in this scope. This does not replace A01's own recheck, accept historical numerical results, or release the final PDF.

## Exact scope and identities

Final core: framing-r02, model_spec-r02, model_interface-r02, model_decision-r03, experiment_plan-r03 and unchanged assumptions-r01. Reviewed closed T06 author response/change note/r02 self-check artifacts and the closed r03 editorial follow-up. Also reviewed current WORKING_DOC §10.4, COORDINATION, templates/TASK and templates/REVIEW, against actual A01/A02 evidence, G2-r01, evaluation-access ledger and T05 preflight-r02 receipt/log.

`target-inventory-final.json` pins and retains 33 exact target/evidence files. Original r02 snapshots and initial inventory are preserved. Principal identities:

| Target | SHA-256 |
|---|---|
| r02 artifact inventory | 8d31c1742f492b9fd8122e17039345df4ebfcfeec438d02c1a466e755dc644d6 |
| model_spec-r02 | ba81a65550193a8775f2275224329d6bad339191ffccf4cf33c9a1094ea1c796 |
| model_interface-r02 | 2b93537df100d6a1cb51df5bba8ad7d069aab436c776df22c2b9a390e29bd216 |
| model_decision-r03 | 72f812b54306925d089e1f045f2d41b2279995cd2a46d48e010bbf853176b341 |
| experiment_plan-r03 | 89da0621ff7774ad47a257ea144a6a1952257dfe85fe936ce033db40c3660170 |
| r03 artifact inventory | a2bccb3cd24b1e58fa38284a02dd7a9df025b9d5bdb894daa2e982c001c8d276 |
| WORKING_DOC | 678b61f85be2ce2a943a70f00098007e19c023ee8254487ca67c6c8376ea42f2 |
| COORDINATION | ec7d6dc38703bb5064e256e696466ee940e0f4964b8bac941263ad16556e9449 |
| templates/TASK | f458596de433532f1f0d19d7f0cf9394149c057e44a5a8fe0e08afbadeb36e17 |
| templates/REVIEW | 6fed428535399266c519327252cf548c491de750678972f4475d6e0dde1e5ef7 |

All original eight r01 artifacts independently match my T04 retained bytes, not merely a current producer manifest. All eleven r02 artifacts remain unchanged after r03. Readable core diffs are retained. No target/control/Git writes occurred.

## Checks actually executed

Used exact `/Users/ericzhang/.venvs/default/bin/python3` for isolated checks:

- Inventory/hash verification, r01/T04 byte preservation and M00/M01/M02/M04 section equality.
- Independent finite-sequence oracle: 1,875 four-year CO2/T0/T1 cases with missing, negative, zero, below-threshold and above-threshold values. Expected event status, first year, whole-domain validity, earliest invalidity, prefix endpoint and monotonicity all agree with the isolated pure helper extracted from the inspected author script. Its top-level writes/tests were not executed. Evidence: `check_contract.py`, `contract-checks.json`.
- Diff-only r03 recheck: each file equals r02 after exactly its title revision and the specified residual “untouched” label replacement. All closed r02 hashes still match. Evidence: `editorial-recheck.json`. Unchanged mathematical checks were not repeated.

The finite-sequence check is independent semantic evidence for the bounded author helper, not production validation or a historical fit. Simplified T1 oracle cases pair target/upstream values; separate upstream-invalid-at-hit coverage was inspected in the author test rather than independently executed here. Inspected the 14 author boundary tests, six saved-adversarial-evidence consistency checks and their code/results; these remain author checks. Inspected T05 preflight-r02 manifest/log: explicit Python 3.12 executable, 28 passed model tests and historical_fits_executed=false. Did not rerun production tests or certify their complete coverage/recovery.

## Substantive findings

### Selection and claim repair

Original data vintage/baseline/year join, D/Q/E and T0/T1 equations, chronological splits, MAE/tie selector, sequential temperature eligibility, envelope formula, sensitivity window and threshold/search domain remain unchanged. M03/M05 and experiment diffs introduce no new fit/tuning rule. Winner counts and leave-one-origin-out summaries are expressly post-assessment diagnostics, not revised selectors.

A01's R04 defect is repaired: framing/R04, M08, D09 and I07 distinguish pooled-development selection, final-segment ranking and unknown future accuracy. Reversal/instability must appear in the answer; a final challenger cannot silently replace the selected primary rule. All T1 comparator scores remain visible with the eligible sequential pair identified. Envelope miss rows retain error/radius/excess; neither radius inflation nor a guaranteed reliable-through-2031 claim is allowed.

A02's objections are considered on their merits. The CO2 comparison is bounded to the specified linear-time baseline, and T1-E's exact linear-in-future-time identity is stated. No unique predictive information, causal parameter or long-horizon guarantee is inferred. The author response distinguishes confirmed defects, limitations and exploratory alternatives. Required numerical outputs and source distinctions remain intact.

### Crossing semantics

M06 and I05 agree. Invalid origin fails first. A valid already-above origin retains its separate status. A first annual crossing established on a contiguous valid prefix survives later invalidity, but mandatory fields expose full-domain failure, earliest invalid year/reason and prefix-scoped monotonicity. Invalidity before or at an apparent hit prevents crossing inference, even if later values recover. Only an entirely valid subthreshold domain gets bounded non-crossing. Nonpositive CO2 is invalid; negative anomalies remain valid.

Statuses are mutually exclusive under the stated ordering. Raw boundary values and an adjacent later-invalid warning are mandatory. The event is not erased and full-path validity is not falsely certified. Optional analytical roots cannot override invalid-prefix failure. These fields are implementable/testable; ordinary fitted equations and scientific selection are unchanged.

### Team-wide evaluation exposure and reusable rules

G2-r01 records original forms/splits/selector before A01's assessment. The actual ledger and r02 core acknowledge A01's numerical final-2012–2021 access before the main selection receipt. Local execution order can demonstrate faithful implementation of a prior rule; it cannot restore project-wide unseen scores. Table visibility, score computation and score-informed redesign are differentiated. Later redesign requires new evidence or narrower claims.

This T08 reviewer has now read A01 final score/reversal/miss evidence and notified the coordinator for its exposure ledger. No new historical fits were made here. Adversarial numbers remain challenge evidence, not accepted primary results.

WORKING_DOC §10.4 requires falsifiable independent attacks, strongest defenses, author response, changed-version rechecks and a team-wide access record. COORDINATION assigns disjoint QA paths, actual identities, honest reuse of a reviewer, evaluation permission/freeze boundaries and owner-controlled disposition. TASK/REVIEW add usable exposure fields. These changes address the demonstrated gap while preserving author/reviewer/coordinator boundaries. Reviewer numbers do not become votes, and no finding quota is required. Wording-only changes need claim/export checks; substantive changes invalidate affected evidence.

## Finding and repair record

| ID | Canonical severity | Evidence/location | Requested repair | Recheck |
|---|---|---|---|---|
| T08-E01 | editorial | r02 model_decision D04 and experiment_plan E04 retained isolated “untouched” labels despite explicit exposure caveats. Out-of-context reuse could mislead. | Replace only those labels with final-assessment wording under unchanged frozen rules; preserve r02. | CLOSED: complete r03 files inspected; exact replacement-only checks passed. No mathematical rerun required. |

No unresolved blocking/consequential issue was found. No historical forecast, selected primary output, uncertainty probability, full production implementation, final conclusion or authored PDF is accepted by this receipt.

## Next action

Coordinator may combine this exact scoped verdict with A01's separate changed-version recheck in delegated G2-r02. Computation must consume the mixed r02/r03 release set, preserve new run identities and its own boundary/leakage tests, and maintain local freeze ordering without claiming global blindness. Primary outputs must reproduce or explain adversarial evidence before claims are released. Independent numerical/claim and rendered-PDF reviews remain required. Changed consequential bytes require affected re-review; this verdict does not transfer by filename alone.
