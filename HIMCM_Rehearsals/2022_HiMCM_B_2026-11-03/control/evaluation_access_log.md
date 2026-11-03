# Evaluation-data exposure ledger

The complete supplied table was visible from intake. No human or model blindness is claimed. This ledger distinguishes seeing the table, computing assessment scores, and using scores to revise a design.

## Freeze and first numerical access

1. T02 r01 fixed forms, splits, eligible candidates and the MAE/tie selection rule before actual-data model fitting. G2 r01 adopted those exact rules.
2. A01 saved development-only hypotheses/probes, then independently computed final 2012–2021 scores in `qa/adversarial_validation/assessment_r01.json`. This preceded the primary T05 numerical selection receipt. A01 found D MAE2.1445 versus Q1.39841ppm and a T1-D envelope miss in2016. These scores cannot become an unseen assessment for later redesign.
3. A02 computed omitted-comparator scores on development only. It did not compute alternative final-period scores. In later A03 implementation work, the same reviewer received the global exposure context; this is one reused reviewer, not a new blind context.

## Subsequent access and permitted interpretation

| Role/session | Actual exposure | Consequence |
|---|---|---|
| Coordinator /root | Read A01 reported final scores and evidence | Logged global exposure; kept original forms/selector; requested truthful claim repairs. |
| Modeler /root/rehearsal_modeler, T06 | Read A01 assessment arrays/report and A02 development results; checked their consistency | r02/r03 interpretation/valid-prefix repairs preserve original numerical design; additional rank summaries are labeled post-assessment diagnostics. |
| Reviewer /root/rehearsal_reviewer, T08 | Explicitly read A01 final-score evidence while checking repairs | Its review is not based on globally unseen final outcomes; no model-selection change authorized. |
| Writer /root/rehearsal_writer, T07A | Read A01/A02 reports and this ledger as planning context | Probe scores are not accepted primary results; numerical report slots remain pending. |
| Computation /root/rehearsal_computation, T05 | Notified of global exposure and instructed to preserve the original forms/selector | Must retain its own development-selection-before-final execution records without claiming all agents kept final scores unseen. |

Any new model, fitting window or selection rule informed by this exposure is post-assessment development and needs new validation or a narrower claim. Interpretation and correctness repairs do not erase the history. The original fixed design can still be assessed computationally with fitting/selection restricted to development data; that narrower fact is not a claim of global blindness.
