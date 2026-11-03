# A01 repair re-review r02

**Canonical overall verdict: ACCEPTED_FOR_SCOPE.** Scope is the A01 temporal-selection, uncertainty and accuracy-claim specification repair in the exact r02 targets pinned by `recheck-results-r02.json`. No unresolved blocking or consequential A01 specification defect remains. This is not acceptance of numerical implementation, primary result tables, threshold boundary code, paper or PDF. Main reviewer owns crossing semantics and coordinator owns the project exposure ledger.

## Severity normalization

The r01 `P1` shorthand maps to canonical **consequential**, not automatically **blocking**. A01-1 was a confirmed consequential R04 interpretation defect, now closed. A01-2/3/4 were conditional consequential risks only if overclaims appeared, not existing numerical defects. A01-5 identified no specification defect; its implementation evidence gap remains outside this acceptance. A legacy “untouched” heading/row is **editorial** in context because explicit r02 amendments prohibit a project-wide unseen-holdout claim; it cannot be copied into final prose without the stated qualification. No open A01 blocker is inferred from that label.

## What was independently checked

I read the actual author response and handoff, then inspected complete r01-to-r02 diffs for framing, model specification, interface, decision and experiment plan against the previously read r01 bodies. I checked the repaired clauses themselves rather than relying on the response table. A compact independent script verified all 12 handoff artifact hashes, original input/model hashes, unchanged M00–M02/M04/M07 text, and retained origin/MAE/tie/sequential-selection rules: 21 checks passed. Fourteen current targets are pinned, including unchanged assumptions and T06 handoff. No historical fitting was rerun, no final evidence was reset, and original A01 r00/r01 evidence remains preserved.

## Finding closure and guards

| Finding | Actual repaired contract | Re-review outcome |
|---|---|---|
| A01-1: selection called “most accurate” despite instability | framing r02 R04/Boundaries replaces the definition with three distinct concepts: pooled-development selection, final-score best model, and unknown future accuracy. M08 requires separate ranks, origin/horizon evidence, reversal and no uniform winner. Decision D09 preserves the original selector. | CLOSED, consequential defect repaired. No retrospective switch to Q is authorized. |
| A01-2: sequential pipeline confused with global temperature winner | M08 limits selection to T0 versus T1 driven by selected CO2; I07 preserves every declared T1 comparison and labels eligibility; E08 requires their scores. | Guard accepted. T1-Q's lower development/final MAE cannot be hidden or mistaken for a newly selected primary. |
| A01-3: empirical band mistaken for calibrated coverage/reliability | M07 retains exact original radii; M08 requires every miss and prohibits resizing, inferred probability and a validated 2031 date. I07 requires actual year/horizon, absolute error, radius, containment and excess. | Guard accepted. Final T1-D 2016 miss and D's signed bias must survive production reconciliation. |
| A01-4: short tests certify distant forecasts | Unchanged M07 plus framing's new summary/article requirement preserve conditional 2050/2100 and threshold language, structural/window sensitivity, and no universal reliability date. | Guard accepted; no new long-horizon validity claimed. |
| A01-5: forecast-input leakage/freeze integrity | Original fold-local equations and predicted CO2 use remain; E03 retains fixture mutation. M03/I04 now explicitly distinguish local receipt ordering from A01's prior final-score exposure. | Specification accepted; production tests and code inspection still required. |

The reported adversarial numbers in author_response-r02 match the previously pinned A01 findings: D/Q development MAE 1.48122/1.75903 ppm; final Q/D 1.39841/2.14450; Q wins three origins; excluding 1986 or 1991 changes pooled selection; T1-D 2016 error magnitude .222292°C exceeds .197125°C radius. These remain reviewer evidence pending primary reproduction, not automatically accepted primary publication values. New per-origin counts and leave-one-origin-out summaries are explicitly post-assessment diagnostics, with I07's `introduced_after_assessment=true`; they cannot change the selector. This directly satisfies the required repair without obscuring chronology.

## Remaining downstream conditions, not reopened specification defects

Primary implementation must reproduce or explain all adversarial comparisons, enforce original selection, show every envelope miss, and pass its own availability/freeze tests. Any discrepancy triggers investigation, not copying QA numbers. Final summary/article must retain the narrowed interpretation. The original E04 heading and decision D04 phrase still say “untouched,” but the first-page experiment disclaimer, M03/I04 and decision exposure paragraph explicitly override a global reading. That is optional editorial cleanup, not an evidence-reset permission. Any future scientific redesign informed by exposed final errors requires post-holdout labeling and new validation.

No author targets were edited by A01. Only new A01 QA/handoff revisions were created. Earlier CHANGES_REQUESTED is retained as historical review state; this r02 ACCEPTED_FOR_SCOPE is the single current A01 verdict.
