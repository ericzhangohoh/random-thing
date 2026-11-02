# Failure and Recovery Exercises

These are document-level scenario checks. They verify whether the protocol gives an unambiguous next action; they are not tests of Claude's live enforcement or of a fitted scientific model.

| Injected situation | Expected response | Required evidence of recovery |
|---|---|---|
| A forecast uses random splits despite temporal deployment | Reviewer identifies future-information leakage; modeler revises protocol; computation reruns; writer removes stale winner claims | Revised experiment, new runs, updated claim table |
| A source's price units change from per kWh to per MWh | Domain-data flags incompatible units; coordinator marks affected accounting, plans and claims stale | Corrected dictionary, transformation check, rerun and claim reconciliation |
| Two sessions begin editing the manuscript | Stop competing writes, preserve both revisions, assign one writer and reconcile with evidence | Ownership record and reconciled revision; no silent newest-file choice |
| A solver exits successfully but reports infeasible | Computation records scientific failure and inspects formulation/data; no result presented as a feasible plan | Solver status, diagnostic case and repaired or narrowed task |
| A Monte Carlo search finds a good plan | Report best-found scope and comparison; do not call it globally optimal without evidence | Baseline comparison, replications and bounded claim |
| A required input is missing | Domain-data proposes compatible source/proxy/range or narrowed claim; escalate substantive scope change | Source/proxy rationale, scenario or recorded limitation |
| A reviewer authored the component being reviewed | Label self-check or assign a fresh reviewer | Honest independence statement and scoped acceptance |
| A session restarts after context loss | Read state, role, task, decisions, dependency versions and last handoff before editing | Restart acknowledgment and exact next action |
| The baseline outperforms a complex candidate | Retain baseline or diagnose a justified structural issue; preserve unfavorable evidence | Decision record with real comparison and limits |
| An upstream parameter changes after figures are finalized | Trace affected runs/claims/figures and regenerate them from a new run | Invalidation list, refreshed outputs and review |
| A PDF export clips equations | Writer repairs export/source and re-renders; reviewer checks the actual replacement | Inspected final artifact and version/hash |
| The deadline is near and an optional extension remains incomplete | Coordinator prioritizes required outputs, valid evidence and export; label extension unimplemented | Latest complete version, scope decision and honest manuscript |

## Human checkpoints exercised

G1 blocks dependent work on an unconfirmed substantive interpretation. G2 requires a concrete architecture and comparison rationale, while allowing reversible prototypes. G3 requires actual evidence-backed conclusions. No checkpoint treats silence as approval or asks the human to approve an empty plan.

## Limits of this verification

These exercises show that the written protocol assigns responsibilities and evidence consistently. They do not demonstrate that a live multi-agent system will obey every instruction. Native configuration requires separate live testing in an environment with Claude Code installed.
