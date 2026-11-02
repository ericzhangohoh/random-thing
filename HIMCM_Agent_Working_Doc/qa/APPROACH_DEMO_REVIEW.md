# Independent review: approach-defense scheduling demonstration

**Verdict: ACCEPTED_FOR_SCOPE**

**Date:** 2026-11-02. **Reviewer:** `early_mcm_continue`, independently assigned after the example was authored. The reviewer did not design, write, or repair the target code or narrative. Requested repairs were made by the author; reviewer scripts and outputs are confined to `qa/`.

**Accepted scope:** the eight supplied synthetic scenarios, their stated finite scheduling model, the recorded numerical results, and the walkthrough's explanations of model choice, service tradeoffs, evidence boundaries, ownership, and illustrative handoffs. No unresolved blocking or consequential finding remains for this scope.

**Outside acceptance:** empirical validity, real river capacity or travel safety, arbitrary-input correctness, large-instance performance, unexpected in-transit disruptions, actual human checkpoint approval, live Claude execution, or a working six-agent orchestration system. The example explicitly preserves these limitations.

## Pinned targets

Paths are relative to `HIMCM_Agent_Working_Doc`.

| Target | SHA-256 |
|---|---|
| `examples/APPROACH_DEFENSE_WALKTHROUGH.md` | `ae0d7e12d28cc7e83ffd3b0e85202506c5b6cd9cfb80503367cbd4e786a9cdbb` |
| `examples/approach_demo/inputs.json` | `374f2d431410597180c11ddd969cc964ddeefcaa264fcf47aeaef91d153be710` |
| `examples/approach_demo/run_demo.py` | `9b212e9a3f3d4270719b05534a7ea7fa28797a8ab0745e2c67006ec051de1a57` |
| `examples/approach_demo/results.json` | `8e72891e44f450dbb80c2c16791f5856a2edcaa44ab9c3f57ce4bee767ba3112` |
| `examples/approach_demo/manifest.json` | `e141c86d3e996a7860c6860655e955b6e973f91050b747e8340c12f08fddee0d` |

The review read the complete walkthrough, complete program, input, result and manifest. The final author repairs were read again and the hashes checked. Subsequent scientific changes require review of the affected evidence; this receipt does not silently accept later versions.

## Checks actually executed

Working directory: `/Users/ericzhang/Desktop/himcm/HIMCM_Agent_Working_Doc`.

```bash
python3 examples/approach_demo/run_demo.py --output qa/approach_demo_review/reproduction-r02
python3 qa/approach_demo_review/independent_check.py
```

Both commands exited successfully. The reproduced `results.json` is byte-identical to the pinned result. The revised manifest correctly records the supplied output argument, resolved input/output paths, working directory, and runtime. The earlier reproduction and check receipts remain available as revision 1, preserving the evidence before the manifest repair.

Evidence:

- [Independent checker](approach_demo_review/independent_check.py): reads only the fixture and results; does not import the author's generator, verifier, or optimizer.
- [Independent check receipt, revision 2](approach_demo_review/independent_results-r02.json): per-scenario optima, feasible-assignment counts, and pinned hashes.
- [Reproduction receipt, revision 2](approach_demo_review/reproduction_receipt-r02.json): actual command, completion, result equality, and provenance check.
- [Isolated reproduced result](approach_demo_review/reproduction-r02/results.json) and [manifest](approach_demo_review/reproduction-r02/manifest.json).

The independent checker generates possible camp sequences with repetition allowed initially, then separately rejects wrong dates, wrong numbers of nights, non-downstream travel, excessive first/intermediate/final legs, closed slots, capacity collisions, and unmet service quotas. It enumerates the resulting decisions independently. It also checks every reported baseline and exact witness, requested/accepted/rejected class counts, occupied nights, and accepted mean durations. This is independently written verification of the supplied finite fixture, not an independent empirical source.

| Scenario | Baseline count checked | Independent exact maximum | Independent feasible assignments | Result |
|---|---:|---:|---:|---|
| Base | 3 | 4 | 58 | Matches |
| At least one long request | 3 | 3 | 9 | Matches |
| Daily limit 59 | 1 | 1 | 2 | Matches |
| Daily limit 30 | 1 | 1 | 2 | Matches |
| Daily limit 29 | 0 | 0 | 1 | Matches |
| B/night 2 closed beforehand | 3 | 3 | 21 | Matches |
| Zero demand | 0 | 0 | 1 | Matches |
| All overnight slots closed | 0 | 0 | 1 | Matches |

The author's intentionally overlong final-leg fixture reports `Invalid travel leg: S1/2/60`. The fixed base plan under closure reports `Closed slot: S4/B/2`. These failures are reported as failures of those proposed schedules, not converted into successful outputs.

## Independent reasoning and interpretation

**Base optimum:** only four camp-night slots exist. Each accepted request uses at least one, so at most four groups can be accepted. S1–S4 use one distinct slot each; their two travel legs are 30 and 60 miles in some order. Therefore four is attainable and optimal. Booking-order insertion accepts L first, then S1 via B/night 1 and S3 via A/night 2, yielding three. Both plans use four slots. The count gain reflects a different service mix, not higher slot utilization.

**Quota optimum:** L consumes A/night 1 and B/night 2. At most two further short groups fit in the two remaining slots. A three-group witness exists, so three is exact. The service condition changes policy; it is not a cost-free fairness improvement.

**Travel thresholds:** every short request needs one 60-mile leg because the only camps are at 30 and 60 miles on a 90-mile route. Limits 59 and 30 exclude all short requests; L's three 30-mile legs remain feasible. Limit 29 excludes L as well. The jumps are discrete feasibility effects, not stochastic estimates.

**Known closure:** closing B/night 2 leaves three available slots and makes L's only strictly downstream itinerary impossible. Three short groups can occupy the remaining slots, proving the exact maximum of three. This is a new admission decision using known availability. It does not protect an already accepted group whose original itinerary uses the closed slot.

**Search-domain check:** the base Cartesian domain has `2 × 3^4 = 162` combinations. With L rejected, each night has seven feasible allocations of its two short requests to two camps, giving 49 possibilities. With L accepted, each of the two remaining slots has three possibilities—unused or assigned to one of two eligible short requests—giving nine. Thus 58 feasible assignments is independently explained. The quota retains those nine. Under the closure, seven first-night allocations and three second-night allocations give 21.

The group-count objective, fixed launch dates and durations, strict downstream motion, whole-trip reservation, unit camp capacity, and offline information all match between narrative, fixture and computation. Accepted mean duration is correctly `7/3` versus `2` days and refers only to admitted groups. A campsite-night is not a person, a travel-time measurement, or total seasonal capacity.

## Workflow and handoff consistency

The walkthrough presents G1/G2/G3 packets as illustrative and unapproved. It does not invent a human response or claim that six actual Claude sessions exchanged handoffs. The model decision remains a proposal for a later real project. Required versions, commands, outputs, incomplete work and next review action appear in the sample handoff.

After repair, the modeler writes proposals in `models/decisions/`; the coordinator alone records accepted decisions in `control/decisions.md`. Domain-data owns research notes/dictionaries and immutable source admission. Computation owns transformations, derived data and nonvisual code, including its reusable self-checks. The independent reviewer writes isolated checks in the assigned `qa/<review-id>/`, not in production code. Writer ownership and the rule against editing finished numerical outputs are consistent with the shared-directory protocol.

Canonical verdicts are scoped correctly: the toy optimum can be `ACCEPTED_FOR_SCOPE` while target-scale suitability remains `INSUFFICIENT_EVIDENCE`. Changing an input invalidates dependent routes, runs, claims and figures rather than authorizing a direct edit to a displayed number.

## Findings and resolution record

| ID | Severity | Finding at initial review | Required repair and verified resolution |
|---|---|---|---|
| AD01 | Consequential | The manifest reported a hardcoded default command even when an alternate input/output invocation was used, weakening the demonstration's provenance claim. | Author separated the default example command and recorded actual argv, resolved paths, working directory and runtime. Revision-2 reproduction verifies the custom output directory in the manifest; results remain byte-identical. **Resolved.** |
| AD02 | Consequential | Section 10 assigned domain-data transformations and assigned the reviewer `code/qa/`, conflicting with the established write boundaries. | Author moved dictionaries to research, transformations/derived data/nonvisual code to computation, and isolated reviewer scripts/outputs to its `qa/` assignment. Final text inspected. **Resolved.** |
| AD03 | Consequential | Section 9 could be read as directing the modeler to transfer its decision directly into coordinator-owned `control/`. | Author explicitly separated the modeler proposal from coordinator acceptance and human-response recording. Final text inspected. **Resolved.** |

No unrelated tests were required after the provenance-only code revision and ownership-only narrative repairs. The numerical checks were rerun because the executable version changed, and the affected prose was reread. General input validation, numerical performance at scale, and document export rendering remain outside the stated fixture review.

**Next action:** the coordinator may integrate this example as an executed, independently checked teaching demonstration at the pinned versions. Retain its synthetic-data and runtime limitations. A real contest project must still instantiate the role assignments, obtain its actual required decisions, and run its own evidence-producing workflow.
