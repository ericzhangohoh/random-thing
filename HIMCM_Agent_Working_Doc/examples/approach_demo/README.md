# Executed Campsite Scheduling Teaching Fixture

This directory contains the runnable evidence for the [approach-defense walkthrough](../APPROACH_DEFENSE_WALKTHROUGH.md). All inputs are synthetic. The program verifies a five-request mathematical example; it does not estimate real seasonal capacity, validate an operational travel limit, test target-scale performance or exercise live Claude agents.

## Reproduce in a new output directory

From the `HIMCM_Agent_Working_Doc` directory, run:

```bash
python3 examples/approach_demo/run_demo.py --output qa/approach-demo-rerun-01
```

Use an unused output directory. For another rerun, change the final directory name to `approach-demo-rerun-02` or another unused name. The script overwrites generated files if that output directory already contains them. Keeping a new directory preserves the recorded result and earlier review evidence.

Python 3 and its standard library are the only dependencies. The command writes `results.json` and `manifest.json` in the selected output directory and prints a compact scenario summary. The manifest records the actual invocation, resolved paths, working directory, Python version, calculation status and SHA-256 hashes of source, input and result. The labeled default command in the manifest is an example, not a substitute for its actual invocation record.

## Files and evidence scope

| File | Purpose |
|---|---|
| [inputs.json](inputs.json) | Synthetic river, five booking requests and eight scenario definitions. |
| [run_demo.py](run_demo.py) | Complete-route generation, booking-order baseline, exhaustive allocation and direct schedule checks. |
| [results.json](results.json) | Recorded executed results, witness schedules, class counts, feasibility issues and negative checks. |
| [manifest.json](manifest.json) | Identity and execution provenance for those recorded artifacts. |

The model assumes all requests are known before admission, fixed launch dates and durations, strictly downstream daily movement, and one group per campsite-night. Accepted trips reserve a complete itinerary. It checks the launch leg, intermediate legs and exit leg. Group counts are not passenger counts.

This is a fixed teaching fixture. Built-in negative tests refer to its supplied request IDs and scenario structure. Arbitrary-input validation, general application failure handling, uncertain travel, within-day encounters and after-departure disruption management are outside the verified scope. Hashes establish artifact identity, not mathematical validity.

## Eight executed scenarios

| Scenario | Booking-order count | Exact count | What it checks |
|---|---:|---:|---|
| Base | 3 | 4 | Joint admission versus a feasible transparent baseline. |
| Require the long trip | 3 | 3 | Explicit service preference and its cost in group count. |
| Daily limit 59 miles | 1 | 1 | A short route's 60-mile leg becomes infeasible. |
| Daily limit 30 miles | 1 | 1 | The three-leg long route still fits. |
| Daily limit 29 miles | 0 | 0 | Every request becomes individually infeasible. |
| B closed on night 2, known before admission | 3 | 3 | Replanning under changed slot availability. |
| Zero demand | 0 | 0 | Empty-instance accounting. |
| All overnight slots closed | 0 | 0 | Resource infeasibility. |

Two additional negative checks deliberately test a too-long final leg and the fixed base plan under the closure. Both must be flagged. Reoptimizing after changing an input is different from proving that the original fixed plan remains feasible.

The base count optimum is also supported by a short independent argument: there are four campsite-night slots, every request requires at least one, and a four-group schedule is displayed. Requiring the long trip uses two slots and leaves room for at most two short trips. The walkthrough supplies the complete reasoning and qualifications.

## Independent review

The [independent review receipt](../../qa/APPROACH_DEMO_REVIEW.md) records the canonical verdict **ACCEPTED_FOR_SCOPE** and pins the reviewed versions. Supporting source, rerun results and independent enumeration are under [qa/approach_demo_review](../../qa/approach_demo_review/). Its checker does not import the demo's route generator. Consult the receipt's versions and scope before transferring its verdict to a changed file. This toy-specific verdict does not establish a real contest solution or a functioning multi-agent runtime.
