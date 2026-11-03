# Accepted practice paper and evidence

Completed 2026-11-04, Australia/Sydney. The project folder and scientific run IDs retain the 2026-11-03 start date. This is a retrospective practice delivery under the user's explicit delegation, not a live competition submission.

## Final paper

**[Read the accepted 16-page English paper](paper/exports/2022_HiMCM_B_practice-complete-r03.pdf).**

SHA-256: `27182592954ee011e2c9f94b7c9a86465b3be44e3fba94d7ab1e3e3c3ef39573`.

The exact r03 candidate was accepted after author closure and independent review. Its footer retains the version label “Complete candidate r03”; this external delivery record establishes that version's acceptance without altering the reviewed bytes. Earlier Phase A and complete r01/r02 files remain retained as drafts and repair evidence.

| Pages | Content |
|---|---|
| 1 | One-page summary with all three CO2 continuations and material limitations |
| 2 | Contents |
| 3-14 | Data definitions, all questions 1.a-d and 2.a-c, equations, model comparisons, six figures, uncertainty, sensitivity and conclusions |
| 15 | One-page nontechnical Scientific Today article |
| 16 | References, practice/AI disclosure and project-wide evaluation exposure |

## What was independently accepted

| Scope | Exact evidence |
|---|---|
| Scientific values and 17 bounded claims | [T10 review](qa/numerical-r01/review.md), binding current r03 computation |
| Frozen-selection and invalid-path diagnostic repairs | [A03 recheck](qa/adversarial_implementation/r03/review.md) |
| Replacement-agent recovery and stale-dependency evidence | [T13 review](qa/recovery-review-r01/review.md) |
| Every page of the final PDF, requirements, tables and figure bindings | [T11 review](qa/pdf-review-r00/review.md): all 16 pages visually inspected and 299 checks passed |
| Adversarial final claim wording | [A04 review](qa/adversarial_paper/r01/review.md): ten attack families; no open claim defects |
| Reusable workflow and truthful integration indexes | [Versioned integration reviews](qa/integration-review-r01/); each receipt names its actual reviewed versions and scope |

T11 and A04 found no remaining defect requiring another PDF revision. Author checks alone did not confer acceptance. The coordinator adopted the bounded review decisions for this exact practice release; there is no fabricated human reply. [The task board](control/tasks.md) and [current state](control/state.md) reconcile final disposition separately from the preserved producer receipts.

## Evidence and editable sources

- [Scientific manifest](runs/T05-scientific-20261103-r03/manifest.json), retaining 88 dependencies and 35 outputs.
- [Accepted claim register](control/accepted-claims-g3-r01.json) and [claim-to-evidence map](models/claim-evidence-r02.json).
- [Readable manuscript](paper/manuscript-complete-r03.md), [structured manuscript](paper/manuscript-complete-r03.json) and [PDF builder](paper/build_report-r03.py).
- [Figure register](paper/figure-register-r02.json), [figure source](code/visualization/render_figures-r02.py) and [writer closure](handoffs/T07/writer-visuals-r03.md).
- [Executed recovery receipt](runs/T09-recovery-20261103-r02/README.md) and [rehearsal/repair report](REHEARSAL_REPORT.md).

To rebuild the paper without overwriting the accepted artifact, use an unused output name from this project directory:

```sh
/Users/ericzhang/.venvs/default/bin/python3 paper/build_report-r03.py \
  --source paper/manuscript-complete-r03.json \
  --output /private/tmp/2022b-paper-rerender-UNIQUE.pdf
```

Replace `UNIQUE` first and verify the actual local interpreter and dependencies. The recorded author command used the same builder and source. Rebuilt PDFs are new candidates requiring inspection; this instruction does not claim byte-identical PDF generation. Do not rerun fixed-path assembly/figure scripts over accepted sources. Make a new version if the manuscript or figures need editing. Scientific reproduction instructions are in the [project README](README.md).

## Meaning and limits of completion

The exercise tested actual Codex agent assignments, file handoffs, review/repair loops, numerical reproduction and full PDF export for one problem. Multiple GPT-6 Astra reviewers attacked different failure surfaces; reused reviewer contexts are identified honestly. Claude-native agents/teams, automatic general-purpose orchestration and live contest submission were not tested.

The paper preserves ranking instability, stronger later comparators, the 2016 error-envelope miss, source-definition discrepancies and the limits of extrapolation. It makes no claim of causal climate sensitivity, globally unseen assessment, probability coverage or reliable century-scale forecasts. No biological research was performed.

## Private delivery destination

The authorized destination is **[ericzhangohoh/himcm-workflow-private](https://github.com/ericzhangohoh/himcm-workflow-private)**. The old `himcm` address was found to resolve to a public renamed repository. The coordinator created and verified this separate private repository, changed origin and successfully pushed the existing history. No new rehearsal content is sent to the public repository, and its visibility/content were not changed by this task.

This file is prepared before its own release commit. Final synchronization is reported only after the coordinator pushes this release, verifies the exact private repository identity and matches remote `main` to the local commit. Git history and the final delivery response identify that commit. An unrelated preexisting deletion of `MCM-ICM-master/README.md` is excluded from the task's staging.
