# 2022 HiMCM B: an executed multi-agent rehearsal

This project applies the [working document](../../HIMCM_Agent_Working_Doc/README.md) to the official 2022 problem **CO2 and Global Warming**. It is retrospective mathematical-modeling practice using the supplied observations through 2021. It is not a competition submission.

**Current paper:** [16-page English LaTeX PDF](paper/latex-r01/build-r05/manuscript-r05.pdf), with Times New Roman text, monochrome figures and zero semicolons. The [current delivery](LATEX_DELIVERY.md) identifies exact versions, three complete sentence-review ledgers, all-page review and build verification. Use the [editable LaTeX source](paper/latex-r01/manuscript-r05.tex) and [build instructions](paper/latex-r01/README-r05.md) for revision.

Current public team repository: [random-thing](https://github.com/ericzhangohoh/random-thing). The [2026-11-04 sharing instruction](../../TEAM_SHARING.md) supersedes private-only destination text in preserved historical delivery records. The current LaTeX paper supersedes the earlier ReportLab presentation. Primary scientific outputs and model selection remain unchanged.

## Read in this order

1. [LaTeX revision report](LATEX_REVISION_REPORT.md): four additional attack contexts, every-sentence reviews, author repairs and final artifact checks. The [original rehearsal report](REHEARSAL_REPORT.md) retains the modeling, implementation and recovery history.
2. [Current state](control/state.md), [task board](control/tasks.md) and [evidence index](control/evidence_index.md): the authoritative current release and receipts. Original handoffs retain their truthful status at publication; later acceptance is recorded separately.
3. [Model specification](models/model_spec-r02.md), [selection decision](models/model_decision-r03.md) and [experiment plan](models/experiment_plan-r03.md): what was fixed, why, and how it was tested.
4. [Current interpretation](models/interpretation-r02.md) and [accepted claim register](control/accepted-claims-g3-r01.json): what the numerical evidence supports, including the losing comparisons and limitations.
5. [Numerical review](qa/numerical-r01/review.md), [implementation recheck](qa/adversarial_implementation/r03/review.md) and [recovery review](qa/recovery-review-r01/review.md): independent evidence, not just author assertions.

The current paper is accepted by A06/A07/A08 for their sentence-review scopes and by T16 for the complete final artifact. Its [acceptance record](control/latex-delivery-acceptance-r01.json) pins the exact r05 source/PDF and r06 register. T11/A04 accepted the former ReportLab r03 under the earlier brief. Those exports and earlier LaTeX candidates remain historical evidence.

## Directory ownership

| Directory | Purpose and owner |
|---|---|
| `control/` | Coordinator: authority, task packets, gates, current state and accepted evidence |
| `inputs/`, `data/` | Admitted official sources and year-keyed observations; origin preserved |
| `models/` | Modeler: definitions, alternatives, equations, selection rationale and bounded interpretation |
| `code/`, `runs/` | Computation: executable analysis, tests, retained dependencies, results and run receipts |
| `paper/`, `figures/`, `code/visualization/` | Writer: evidence-bound prose, figures, export code and PDF candidates |
| `qa/` | Independent reviewers: disjoint attack, comparison and review artifacts |
| `handoffs/` | Versioned producer-to-recipient receipts with exact identities |

Reviewers did not repair the target artifacts. The coordinator alone operates Git. Actual session identities, including reused reviewer contexts, are recorded in [role assignments](control/role_assignments.yaml).

## Reproduce the scientific computation

The accepted scientific run is `runs/T05-scientific-20261103-r03/`. Its [manifest](runs/T05-scientific-20261103-r03/manifest.json) pins 88 retained dependencies and 35 outputs. The [producer handoff](handoffs/T05/computation-r05.md) explains the exact environment and repairs. Python/package versions are recorded; dependency binaries are not bundled.

On the original machine, run from this project directory using the verified interpreter and an unused run ID:

```sh
/Users/ericzhang/.venvs/default/bin/python3 code/experiments/run_analysis_r03.py \
  --project-root "$PWD" \
  --run-id T05-local-reproduction-UNIQUE
```

Replace `UNIQUE` before each execution. Existing run directories are intentionally rejected. On another machine, provide an equivalent environment from the retained requirements and explicitly verify its interpreter/imports before using it. A new execution is candidate evidence, not automatically an accepted replacement.

The actual independent-session recovery used retained source bytes, rather than current mutable code. Its [receipt](runs/T09-recovery-20261103-r02/README.md) records the commands, 32 byte-identical numerical outputs, three semantically equivalent timestamped receipts, two negative probes and a preserved failed first harness attempt. Closed recovery directories are not safe rerun destinations.

## Scope

The runtime tested here is Codex collaboration with actual separate agent sessions. The reusable manual assigns Claude-compatible logical roles, but native Claude agents/teams were not launched. No biological papers were consulted. Gates used explicit user-delegated practice authority, not fabricated human replies. Historical final-period exposure is logged project-wide; the final assessment is not described as globally unseen. The forecasts are conditional trend continuations, not validated long-range climate predictions or causal estimates.
