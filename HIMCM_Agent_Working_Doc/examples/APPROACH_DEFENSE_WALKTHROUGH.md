# Approach Defense Walkthrough: Campsite Scheduling and Admission

This example shows how an agent team moves from a prompt to a defensible model choice, tests that choice, and writes conclusions with the right strength. It implements the reasoning procedure in [Approach and Justification](../APPROACH_AND_JUSTIFICATION.md), the stages and three checkpoints in the [Working Document](../WORKING_DOC.md), and the fields in the [Model Decision template](../templates/MODEL_DECISION.md).

**Evidence boundary:** the prompt, river, requests and parameters below are deliberately synthetic. They are not an official contest problem, observations from a rafting company or results from a historical paper. The small enumeration program was actually executed. Its outputs establish mathematical properties of this toy instance only. No target-scale scheduler, empirical travel model, live Claude session or complete multi-agent runtime has been tested here.

The G1/G2/G3 packets below are examples of what agents should prepare in a real contest project. They do not record an actual human approval. Producing this teaching example is not a substitute for those decisions in a later project.

## 1. The illustrative prompt

> A river manager must decide which of five advance booking requests to accept and assign every accepted group a campsite for each required night. The river runs from mile 0 to mile 90. Camp A is at mile 30 and Camp B at mile 60. Each camp can host one group per night. All requests are known before any acceptance decision.
>
> The planning horizon is days 1–3. A group launches in the morning of its requested launch day, travels strictly downstream each day, and exits by the end of its final requested day. It must occupy one camp on every intervening night. Every daily leg, including entry and exit, must be at most 60 miles. A group's launch date and duration cannot be changed. No camp is closed in the base case.
>
> Maximize the number of accepted groups and supply a feasible campsite schedule. Explain how the policy affects short and long requests. Compare with accepting requests in booking order whenever a complete itinerary fits. Examine what changes if Camp B is known to be unavailable on night 2 before decisions are made. Give a short recommendation and identify what this example cannot establish about a real operation.

| Booking order | Request | Launch day | Trip duration, days | Required nights | Class |
|---:|---|---:|---:|---|---|
| 1 | L | 1 | 3 | 1 and 2 | Long |
| 2 | S1 | 1 | 2 | 1 | Short |
| 3 | S2 | 1 | 2 | 1 | Short |
| 4 | S3 | 2 | 2 | 2 | Short |
| 5 | S4 | 2 | 2 | 2 | Short |

The problem counts **groups**, not people. Group sizes, vessel fleets, costs, within-day encounters and uncertain travel times are absent. Do not invent those inputs or claim that this model evaluates them. The 60-mile limit is a supplied synthetic constraint, not an empirically supported safety or travel recommendation.

## 2. Interpret before naming a method

The decision sentence is:

> For the river manager, choose advance admissions and overnight assignments for the five supplied requests over days 1–3, subject to fixed launch dates, durations, daily travel and campsite capacities, maximizing the number of accepted groups while reporting which request classes are served.

The first useful deliverable is a requirements map, not an algorithm shortlist.

| ID | Required answer | Mathematical object | Acceptance evidence |
|---|---|---|---|
| R01 | An admissible overnight schedule | Accepted request IDs and one camp per required night | Check every trip leg, date, duration and campsite-night occupancy. |
| R02 | Maximum accepted groups in this toy instance | Integer group count and a witness schedule | Exhaustive enumeration plus a separate resource-bound argument. |
| R03 | Comparison with booking-order admission | Two outcomes under the same requests and constraints | Report count, occupied nights and class-specific admissions/rejections. |
| R04 | Effect of the specified known closure | A second complete decision under one changed capacity | Recompute admission under that scenario; distinguish this from disrupting an already accepted plan. |
| R05 | A bounded management recommendation | A short decision statement and qualifications | Trace every claim to the accepted result set and preserve the service tradeoff. |

Classify the quantities explicitly:

- **Input:** request dates, durations, booking order, river and camp positions.
- **Parameter:** maximum daily mileage and campsite capacity within a scenario.
- **Decision:** accept/reject each request and choose an admissible itinerary.
- **Resource state:** whether each campsite-night is reserved.
- **Outcome:** accepted groups, occupied nights, accepted duration mix and rejection by class.
- **Hard constraint:** every accepted itinerary satisfies dates, travel limits and capacity.
- **Potential preference change:** requiring at least one long trip to be served. This is an optional comparison, not a hidden condition in the original maximum-count objective.

“Fair” has not been defined. Reporting who is rejected does not itself establish fairness. Booking-order priority, equal class access and maximum group count can conflict. The agent must expose that conflict before attaching a fairness label.

### Example G1 packet: interpretation

**Decision needed:** confirm the scope and meaning of success.

**Recommended interpretation:** offline admission from all five known requests; maximize group count; preserve requested dates and durations; report class effects separately. A request may be rejected before acceptance, but an accepted group cannot disappear during its trip.

**Alternative:** require service to at least one long request before maximizing total groups. This adds a substantive service condition and may reduce the maximum count.

**Evidence prepared:** the requirement table, request table, units and the dependency map in the next section.

**Tradeoff and consequence:** maximizing groups can favor shorter requests because they consume fewer nights. The alternative changes the feasible set and therefore the answer.

**Exact confirmation to seek in a real project:** “Confirm the offline, maximum-group interpretation, with class effects reported separately; or select the long-trip service condition.”

**Status in this teaching document:** illustrative packet only; no human response is recorded. In a real project, record the actual response, date and requirements version. While a required G1 decision is pending, independent data checks and reversible toy diagnostics can continue; dependent target-scale modeling waits.

## 3. Explain the mechanism and evidence needs

The bottleneck is not simply the number of camps. It is the set of **campsite-night slots** that a request occupies. A long request can block two shorter requests even when every camp remains fully utilized. A nightly allocation made without looking at the final leg can also produce an apparently tidy but impossible itinerary.

The architecture follows those mechanisms:

```text
request dates + durations + camp positions + travel limit
    ↓ enumerate individually feasible complete itineraries
request-specific itinerary sets, including each occupied campsite-night
    ↓ baseline admission / joint admission-and-assignment comparison
accepted groups + complete schedules + rejected groups
    ↓ independent constraint checks + service-mix accounting
accepted evidence table
    ↓ bounded recommendation and conditions for changing it
```

Each arrow has a concrete interface:

| Transfer | Entity and unit | Timing and obligation |
|---|---|---|
| Inputs → route generator | One request, launch day, integer trip days, distances in miles | All information is available before admission. |
| Route generator → allocator | A complete ordered sequence of `(camp ID, night)` for one request | Include first and final legs in route feasibility. An empty candidate set means that request is individually infeasible. |
| Allocator → checker | Accepted request IDs and assigned routes | Preserve identities and requested dates; never replace rejection with silent removal. |
| Checker → writer | Verified schedules, issue list, scenario ID and metric definitions | An invalid output cannot support a feasible-capacity claim. |

The synthetic input file supplies everything needed for this instance. A real operation would require compatible evidence for travel limits, campground availability, demand and the time at which requests become known. It may also require additional constraints for fleets, launch capacity or uncertain disruptions. Those would reopen the model specification when consequential; they should not be added merely to make the example look sophisticated.

For any new assumption, use the full chain: statement → purpose → evidence → location in the model → expected effect → test → consequence if false. For example, “all requests are known before admission” enables joint optimization, appears in the decision horizon, and fails if bookings arrive online after earlier commitments. A target-scale online recommendation would then require a different evaluation protocol.

## 4. Compare genuine alternatives

Keep three layers separate. The **formulation** defines admissions, routes, capacities and the objective. The **solver** searches that formulation. The **evaluation** checks feasibility, compares outcomes and limits claims. “Use an optimizer” is not a complete approach.

| Candidate | Representation and rationale | Benefit | Sacrifice or failure condition |
|---|---|---|---|
| Credible baseline: booking-order insertion | Process requests in the supplied order. Reserve a complete feasible itinerary if one remains available. | Transparent and respects booking priority; produces a complete feasible output. | Early requests may block a better combination of later requests. Failure to maximize count does not make the schedule infeasible. |
| Joint admission and route assignment | Choose admissions and complete itineraries together under shared campsite-night capacities. | Directly represents the maximum-count decision and competing uses of resources. | Requires known demand and can become computationally difficult at scale. |
| Dynamic daily reassignment | Choose next camps using current occupancy and remaining time. | Potentially appropriate if uncertainty or online response is part of the real task. | It introduces future-feasibility obligations not needed by this fully known fixture. A feasible next night does not guarantee completion. |
| Joint assignment with a long-trip service condition | Add a minimum long-trip admission constraint to the same formulation. | Makes a service preference explicit and quantifies its opportunity cost. | Changes the objective interpretation; it must be presented as a separate policy, not a free improvement. |

For the toy instance, exhaustive enumeration is a suitable solution procedure because every alternative can be listed. It is not the proposed target-scale algorithm. A binary optimizer or a different representation would need its own implementation and performance evidence on the actual problem.

The dynamic alternative is **not selected for this scope** because the prompt contains no online information or adaptation requirement. The document does not claim to have run it or demonstrated its universal inferiority. Reconsider it if a real prompt changes what is known when admissions are made.

### The baseline must be good enough to be meaningful

The baseline reserves an entire route before acceptance. It tries all individually feasible routes in a deterministic order: minimize deviation from equal daily progress, then break ties by camp ID. It never deletes an already accepted request to make later statistics look better.

This is a credible policy because booking order can matter to an operator. It is also a clean comparator because it uses exactly the same route set, demand, travel limits and capacity as the joint approach. A baseline that simply ignores collisions would not meet R01 and could not be used as a feasible competitor.

## 5. Write the mathematics before the implementation

Let `P_i` be the set of all individually feasible complete itineraries for request `i`. A route contains `trip_days_i − 1` overnight slots. Its camp positions are strictly increasing, and every gap in the full sequence from mile 0 through the camps to mile 90 is at most the daily limit. All overnight dates follow directly from the fixed launch date.

Let `x_ip` be one if request `i` is accepted with itinerary `p ∈ P_i`, and zero otherwise. Let `a_ipct` indicate that route `p` occupies camp `c` on night `t`. Let `b_ct` be available capacity, either one or zero in this fixture.

```text
maximize       Σ_i Σ_p∈P_i x_ip

subject to     Σ_p∈P_i x_ip ≤ 1                    for each request i
               Σ_i Σ_p∈P_i a_ipct x_ip ≤ b_ct      for each camp c and night t
               x_ip ∈ {0,1}
```

Rejection means all of a request's route variables are zero. Invalid dates or travel legs never enter `P_i`. If a long-trip service condition is chosen, add:

```text
Σ_i:class(i)=long Σ_p∈P_i x_ip ≥ 1
```

This is the formulation being solved, not a claim that an integer-programming package was used. The demo solves it by enumerating every accept/reject and route combination. Equal-count optima use earlier booking IDs as a deterministic tie-breaker; the reported scientific objective remains group count.

The formulation's justification chain is now explicit:

1. **Task fit:** R01–R03 require feasible admission and comparison, not only a prediction of demand.
2. **Reality fit within the prompt:** groups compete for indivisible campsite-night resources, and a trip needs several connected nights.
3. **Mathematical fit:** route choices preserve whole-trip feasibility, binary decisions represent indivisible groups, and slot constraints prevent double booking.
4. **Evidence fit:** all toy inputs are supplied and labeled synthetic; real-world adequacy remains untested.
5. **Comparative fit:** compare joint allocation with a feasible booking-order rule under identical inputs.
6. **Claim fit:** exhaustive search and a small analytical bound can establish the toy optimum; neither establishes real seasonal capacity.

## 6. Fix a comparison that could reject the favored choice

In an actual project, record this protocol before selecting the winner. The teaching experiment below uses these explicit tests; it is not an empirical preregistered study.

| Experiment | Question | Conditions held fixed | Evidence that changes a decision |
|---|---|---|---|
| E01: base comparison | Does joint allocation admit more groups here? | All requests, capacities, travel limits, dates and objective | Equal outcomes would remove the demonstrated count advantage; an invalid joint schedule rejects its implementation. |
| E02: service condition | Is the higher count compatible with serving the long request? | Same physical instance; one clearly labeled added service condition | A lower maximum reveals a genuine preference tradeoff rather than an implementation defect. |
| E03: boundary cases | Do travel thresholds and degenerate inputs behave correctly? | Change only the stated daily limit, demand or availability | Impossible travel accepted, double booking or nonzero service with no requests rejects the implementation. |
| E04: known closure | Can the policy produce a feasible new plan when B/night 2 is unavailable? | Same demand and travel; closure known before admission | Failure to respect the closed slot rejects the output. |
| E05: fixed-plan stress | Is the base plan itself valid after that capacity changes? | Freeze its original decisions; change availability only | Any closed-slot use invalidates that fixed plan; successful reoptimization does not repair this evidence retroactively. |
| E06: deliberately invalid final leg | Does the checker inspect the exit leg? | One hand-constructed short trip via A under a 59-mile limit | Acceptance by the checker would expose a missing boundary check. |

Metrics are defined before interpretation:

- **Accepted groups:** number of admitted request IDs.
- **Rejected groups:** requests minus admitted groups; all rejection occurs before admission in this offline fixture.
- **Occupied campsite-nights:** sum of required nights across accepted requests, also counted from the schedule.
- **Class-specific acceptance/rejection:** counts within the supplied short and long categories, with the requested denominator visible.
- **Accepted mean trip days:** average requested duration among accepted groups; it is not average nights and not a travel-time observation.
- **Feasibility issues:** explicit failed constraints, not an unexplained Boolean alone.

Do not combine these metrics into arbitrary weighted scores. Count is the base objective. Class effects explain a consequence; the optional service constraint changes policy transparently. No runtime advantage is claimed from this tiny demonstration.

## 7. Execute the small experiment and preserve evidence

The companion directory contains:

- [inputs.json](approach_demo/inputs.json): all synthetic inputs and scenario changes.
- [run_demo.py](approach_demo/run_demo.py): standard-library route generation, baseline, exhaustive search and direct output checks.
- [results.json](approach_demo/results.json): actual machine-readable results, schedules and detected negative cases.
- [manifest.json](approach_demo/manifest.json): SHA-256 hashes of the exact source, input and result artifacts.

From the `HIMCM_Agent_Working_Doc` directory, reproduce the accepted fixture with:

```bash
python3 examples/approach_demo/run_demo.py
```

For a review without overwriting the recorded artifacts:

```bash
python3 examples/approach_demo/run_demo.py --output qa/approach-demo-review/rerun
```

The script does not install dependencies, call a model, contact a service or alter a booking system. The default command rewrites only its generated result and manifest files. In a real contest project, save a new run directory for a changed input or implementation instead of overwriting an accepted run.

This is a fixed teaching fixture, not a general validated scheduling application. Its built-in negative checks refer to the supplied request IDs and scenarios. Arbitrary-input validation, general failure handling and target-scale performance are outside its verified scope. The manifest records the actual argument vector, resolved input/output paths, working directory and Python version; its default example command is labeled separately.

The output checker reconstructs trip legs and slot occupancy from the supplied schedule; it does not call the route generator to declare an itinerary valid. Nevertheless, both functions are in one demonstration program and can share assumptions. Independent review must still compare them with the prompt and use a separate reasoning path. The hash manifest identifies artifacts; it does not certify the mathematics.

### Executed results

| Scenario | Baseline accepted groups | Exact maximum groups | Complete combinations enumerated | Interpretation |
|---|---:|---:|---:|---|
| Base | 3 | 4 | 162 | Joint selection improves count on this fixture. |
| At least one long group | 3 | 3 | 162 | Serving the long request reduces the maximum count. |
| Daily limit 59 miles | 1 | 1 | 2 | Short routes become infeasible; the long route remains feasible. |
| Daily limit 30 miles | 1 | 1 | 2 | Three 30-mile legs remain feasible. |
| Daily limit 29 miles | 0 | 0 | 1 | No request has a feasible complete route. |
| B closed on night 2, known beforehand | 3 | 3 | 36 | Reoptimization yields a different feasible admission plan. |
| Zero demand | 0 | 0 | 1 | The empty plan is feasible. |
| All overnight slots closed | 0 | 0 | 1 | All supplied requests require unavailable overnight resources. |

These are deterministic enumerations, so stochastic confidence intervals are inapplicable. The number of enumerated combinations is a search-domain audit, not a measure of real-world uncertainty. The selected mileage values are diagnostic boundaries, not an empirically calibrated range of likely travel conditions.

The base case includes 162 combinations because L has one route plus rejection, and each of four short requests has two routes plus rejection: `2 × 3^4`. Of those, 58 are feasible. The search checks all combinations; it does not report the best of a few random attempts.

### Witness schedules and the service tradeoff

| Slot | Booking-order baseline | Maximum-count schedule |
|---|---|---|
| A, night 1 | L | S1 |
| B, night 1 | S1 | S2 |
| A, night 2 | S3 | S3 |
| B, night 2 | L | S4 |

The baseline accepts L, S1 and S3; the joint maximum accepts S1–S4. Both occupy all four campsite-night slots. The baseline serves one of one long requests and two of four short requests. The maximum-count schedule serves zero of one long requests and four of four short requests. Accepted mean durations are respectively `7/3` days and `2` days.

The count increase therefore does not come from higher campsite-night utilization. It comes from choosing a different mix of trips. This is the central reasoning lesson: the resource accounting and who receives service explain the numerical comparison.

### An independent mathematical bound

There are four available campsite-night slots. Every request requires at least one. Thus no schedule can accept more than four groups. The displayed maximum-count schedule accepts four and satisfies the travel limits: each short trip uses legs of 30 and 60 miles in some order. This proves the base optimum within the stated toy problem without relying only on the enumeration code.

If L must be accepted, it uses two slots. The remaining two slots can support at most two short requests, so the maximum is at most three groups. The baseline is a feasible three-group witness. This proves the service-constrained optimum.

Under a 59-mile limit, a two-day trip via either camp has a 60-mile leg and is impossible. L travels three 30-mile legs and remains possible. Under 29 miles, even L is impossible. These checks explain the abrupt threshold instead of treating it as numerical noise.

## 8. Turn failed checks into decisions

The experiment yields both positive evidence and specific rejection evidence.

| Candidate claim or artifact | Observed evidence | Correct disposition |
|---|---|---|
| “Booking order always maximizes accepted groups.” | A feasible three-group baseline loses to a feasible four-group schedule on E01. | Reject the universal optimality claim. Retain booking order as a feasible policy with a different priority. |
| “The higher count comes from better slot utilization.” | Both base schedules occupy four nights. | Reject that explanation; identify the shorter accepted trip mix. |
| “The maximum-count answer preserves service to long requests.” | The base optimum rejects L; adding the service constraint lowers the optimum to three. | Reject the claim and expose the preference decision. |
| “The base schedule is robust to B/night 2 closure.” | E05 returns `Closed slot: S4/B/2`. | Reject fixed-plan feasibility under that closure. Report the new three-group plan only as reoptimization before admission. |
| A short trip through A under the 59-mile cap | E06 returns `Invalid travel leg: S1/2/60`. | Reject the intentionally malformed schedule; retain the checker because it catches the constructed defect. |
| “Exhaustive enumeration is suitable for a full competition instance.” | Only a five-request fixture was executed. | **INSUFFICIENT_EVIDENCE** for scale. Obtain actual size and runtime evidence before choosing its target implementation. |

The last row illustrates why absence of a test is different from a failed test. Dynamic reassignment also has no executed comparison here; it is out of scope for the supplied offline decision, not empirically disproved.

A closure discovered after departure is a separate operational problem. The demo has no fallback policy for an in-transit group. It must not relabel cancellation or disappearance as ordinary advance rejection.

## 9. Fill the model decision record and prepare G2

The modeler writes the proposed decision under its assigned `models/decisions/` path and hands it to the coordinator. The coordinator records the accepted version and actual human response in `control/decisions.md`; the modeler does not edit that shared control record. The following content follows the existing template rather than substituting a persuasive paragraph for a decision record.

**D02 — Joint advance admission with a booking-order baseline**

- **Owner and revision:** modeler; teaching revision 1.
- **Requirements served:** R01–R05.
- **Decision timing:** after the executed toy comparison; before any target-scale implementation.
- **Current status:** proposed for an analogous offline task; not human-confirmed.
- **Question and mechanism:** choose indivisible whole-trip commitments that compete for dated campsite resources.
- **Alternatives:** the four candidates in Section 4, with the baseline retained even if the joint model is selected.
- **Comparison conditions:** Section 6 and the saved scenario definitions; no physical constraint is relaxed for the preferred candidate.
- **Observed evidence:** E01 supports a count advantage on the base fixture; E02 exposes a service tradeoff; E03/E06 check boundaries; E04 and E05 distinguish replanning from robustness.
- **Selected provisionally:** route-based joint admission for the known-demand formulation; exhaustive enumeration only as the verified toy solver.
- **Retained:** booking-order admission as the transparent feasible baseline and fallback output if a larger solver cannot be justified.
- **Not selected for this scope:** daily reassignment, because online adaptation is absent from this prompt.
- **Benefits and sacrifices:** accounts for opportunity cost across requests; requires advance information and may favor shorter requests under a count objective.
- **Unresolved evidence:** real travel assumptions, actual demand scale, target solver runtime, additional operating constraints and any online fallback.
- **Dependencies changed:** a service preference changes the admission constraint; a closure changes slot capacity and invalidates affected results.
- **G2 response/date/version:** not recorded in this illustration. Do not fabricate approval.

### Example G2 packet: architecture

**Decision needed:** whether to develop the joint admission formulation for the real offline task while preserving the feasible baseline.

**Recommended option:** complete-itinerary representation plus shared slot constraints, with a target solver selected after a scale check. Use enumeration as a small-instance oracle only.

**Alternative:** retain booking-order admission if its priority is the intended policy or the measured benefit of a more elaborate implementation is negligible under the actual criteria.

**Evidence:** toy feasibility, exact enumeration, independent bounds, service-mix comparison, data feasibility record and explicit untested scale assumptions.

**Tradeoff:** potentially higher count versus booking priority and service to long requests; added computational and information requirements.

**Exact confirmation to seek:** “Confirm this offline architecture and the chosen service objective, with booking-order admission retained as the baseline and target-scale solver choice contingent on feasibility evidence.”

While G2 is pending, agents can inspect real input sizes, improve independent checks and document common data interfaces. They must not describe a proposed architecture as approved or use the toy result to announce a real capacity.

## 10. Assign the six roles and make their handoffs reviewable

The table describes work allocation for a future contest project. It does not claim that six live Claude sessions executed this demo. Multiple sessions should use the setup and coordination documents, task ownership and recorded handoffs; a shared folder alone does not provide those controls.

| Canonical role | Concrete task | Owned output | Handoff must answer |
|---|---|---|---|
| `coordinator` | Maintain R01–R05, decision status, task ownership and G1/G2/G3 packets. | `control/` requirements, state and decisions | What is confirmed, what is proposed, and which work depends on a pending choice? |
| `domain-data` | Check dates, distance units, camp availability and whether future demand is actually known. | Assigned `research/` evidence notes and dictionaries; admit immutable originals into `inputs/` and `data/raw/` | Which entries are observations, supplied facts, assumptions or synthetic scenarios? |
| `modeler` | Specify complete routes, admission variables, capacities, baseline and service alternative. | `models/` specification and model-decision content | Why does the formulation answer the task, and what would cause it to be changed? |
| `computation` | Implement transformations, generators/allocators and self-checks; save manifests and run comparisons. | Assigned nonvisual code, including `code/data/` and `code/qa/`; derived datasets and its own `runs/` | What actually ran, with which inputs, status and outputs? |
| `independent-reviewer` | Inspect every constraint, compare code with specification, derive a separate bound and challenge claim language. | Assigned `qa/<review-id>/` scripts, findings and outputs, plus its own handoff | Which findings are independently established, which rely on shared assumptions, and which remain unresolved? |
| `writer-visuals` | Present the schedule, mix comparison, tradeoff and memo from accepted evidence. | `paper/`, `figures/`, `code/visualization/` | Which result supports each sentence and visual; are qualifications preserved? |

An actionable computation task packet could read:

> **T03:** Implement D02 revision 1 for the admitted input version. Write only the assigned modeling and experiment files plus a new run directory. Preserve input files. Compare the baseline and joint method under E01–E04. Include every first, intermediate and last travel leg; report requested and accepted class counts. Supply commands, input/source hashes, statuses, schedules and metric definitions. Do not claim a real-world optimum or alter the service objective. Return ambiguous requirements to the modeler.

The corresponding review handoff should contain:

```text
Task: T03
Scope: synthetic fixture / specified real instance, never left implicit
Requirement and decision versions: R01–R05; D02 revision <actual revision>
Inputs, source, results: exact paths and hashes
Invocation: exact command and environment
Completed: named experiments that actually ran
Not completed: target-scale or external evidence still missing
Findings: feasibility, comparison, boundary and accounting results
Requested reviewer action: inspect constraints and derive a separate bound
Decision affected: G2 architecture / G3 claim wording
```

The reviewer uses the canonical verdicts:

- **ACCEPTED_FOR_SCOPE:** evidence supports the explicitly bounded claim and known limitations are visible.
- **CHANGES_REQUESTED:** a correctable defect or unsupported claim prevents acceptance; identify the affected artifact and required repair.
- **INSUFFICIENT_EVIDENCE:** available work does not establish the requested claim; specify the missing experiment, source or proof.

A successful toy check may justify `ACCEPTED_FOR_SCOPE` for the toy schedule while the target-scale claim remains `INSUFFICIENT_EVIDENCE`. Acceptance is attached to a claim and version, not to an agent's general competence.

If the travel limit changes, the coordinator marks affected route sets, runs, claims and figures stale. The modeler confirms the revised specification; computation creates a new run; the reviewer rechecks; the writer updates from the new evidence. Editing a number directly in the finished chart is not a valid repair.

## 11. Write the defense using the actual evidence

### Before running a target-scale model

> The task requires advance admission decisions and complete feasible itineraries. We therefore represent each request by its feasible camp sequences and select among them under campsite-night capacities. This preserves travel and timing constraints before optimization. We will compare joint selection with booking-order admission under identical requests and limits, reporting group count together with the accepted duration mix. The small synthetic fixture verifies the formulation's basic logic; target-scale performance and real operating assumptions remain to be tested.

This paragraph justifies a proposed approach without claiming that its future evaluation has already succeeded.

### After this executed toy experiment

> On the five-request synthetic instance, booking-order admission accepts three groups and the joint formulation accepts four. Both schedules use all four campsite-night slots. The improvement in group count is achieved by serving four short requests instead of one long and two short requests. Exhaustive enumeration agrees with the four-slot upper bound and a feasible four-group construction, establishing the optimum for this specified instance. Requiring the long request to be served reduces the optimum to three. These results demonstrate a resource-allocation tradeoff; they do not estimate a real river's seasonal capacity.

### Closure interpretation

> If Camp B is known to be unavailable on night 2 before admissions, the revised instance admits at most three groups. The original four-group schedule uses the closed slot and fails the fixed-plan check. The revised optimum therefore demonstrates pre-admission replanning, not robustness of the original commitments to an unexpected closure.

### Language the evidence does not support

| Unsupported statement | Supported replacement |
|---|---|
| “Our AI system finds the optimal campsite policy.” | “The enumeration finds the maximum accepted count for this fully specified synthetic instance.” |
| “Optimization increases river capacity by one-third.” | “Accepted count changes from three to four on this fixture, with a different mix of accepted durations.” |
| “The method is fairer.” | “It accepts all four short requests and rejects the sole long request; a fairness preference requires an explicit decision.” |
| “The plan is robust because we solved the closure scenario.” | “A new plan is feasible when the closure is known before admission; the fixed original plan fails.” |
| “Six Claude agents have been validated working together.” | “The document assigns six roles; this script tests only the synthetic mathematics and computations.” |

## 12. Prepare G3 and finish the recommendation

The G3 packet links each conclusion to evidence rather than asking for approval of an unverified draft.

| Claim | Supporting evidence | Boundary |
|---|---|---|
| C01: base optimum is four groups | Saved exhaustive result, complete schedule and four-slot bound | Only the synthetic input and stated constraints. |
| C02: the long-trip service requirement reduces the optimum to three | Quota scenario, three-group witness and remaining-slot bound | Describes a policy preference, not an empirical fairness standard. |
| C03: closure known in advance permits a three-group plan | Closure run and output check | No after-departure fallback is modeled. |
| C04: the base plan itself fails that closure | Explicit closed-slot violation | A failure of that fixed plan, not a proof that all adaptive policies fail. |
| C05: target-scale suitability is unresolved | No target-scale data or solver experiment exists | Must remain unresolved until that evidence is supplied. |

**Example G3 decision needed:** accept the bounded answers and select the service preference for the recommendation.

**Recommended packet content:** the result table, witness schedules, reviewer findings, claim-evidence table and draft memo below. Identify any unresolved reviewer issue with its canonical verdict. The coordinator records the actual human answer, date and result version in a real project; this example records none.

**Draft memo supported by the toy evidence:**

> For the supplied three-day example, admit S1–S4 if the priority is to serve the largest number of groups. This plan serves four groups and occupies every available campsite-night. It rejects the long request. If serving that request is a required service commitment, use the three-group plan containing L, S1 and S3 instead. Both plans respect the specified travel and camp limits.
>
> If B is unavailable on night 2 and this is known before booking decisions, recompute admission using that availability; at most three groups can be accepted. Do not treat that replan as protection for groups already committed under the original schedule. Before using this approach operationally, check actual travel constraints, request timing, availability and any additional service obligations, then evaluate the solver on the real instance.

The final deliverable should preserve these distinctions in its summary, figures and nontechnical document. G3 approves the claims actually supported by evidence; it does not promote a teaching prototype into a deployed system.

## 13. What transfers to a new problem

The reusable procedure is: define the decision; expose the resource or mechanism; establish feasible representations; keep a credible baseline; state what would reject each candidate; run the smallest discriminating experiment; inspect service or population changes; and write the conclusion at the level the evidence supports.

For a new prompt, replace the synthetic problem, data, preference choices and test cases. Retain the reasoning discipline. A forecasting problem, for example, would use forecast origins and held-out targets instead of campsite slots; its comparison and evidence obligations would change accordingly.

The historical inspiration is the [six-paper 2012 B comparison](../research/cases/2012_MCM_B_complete_local_comparison.md), especially its distinctions between admission and disappearance, throughput and accepted mix, feasibility and optimality, and replanning and fixed-plan robustness. Those papers supplied questions to ask; their reported capacities were not imported into this example. The example's quantitative evidence comes only from its saved synthetic inputs, executed program and explicit mathematical arguments.
