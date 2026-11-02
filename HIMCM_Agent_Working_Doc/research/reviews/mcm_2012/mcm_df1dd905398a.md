# MCM 2012 B — Team 15417 — priority, schedule repair and discrete feasibility thresholds

- Source ID: `mcm_df1dd905398a`
- Source: `MCM-ICM-master/2012美赛特等奖/B-15417-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pp.1–26, including summary, memo, all inline code, results, references and the complete `Boat.java`/`River.java` appendix.
- Visual supplement: physical pp.8–9, 11–13 and 19 inspected for displacement diagrams, movement and efficiency equations, threshold plots, propulsion-ratio plot and the critical comparator implementation.
- Numeric reproduction: **NOT_REPRODUCED**. No Java program, randomized schedule or reported experiment was executed. Code findings below are static inspection, not execution results.
- Award provenance: Outstanding filename label, not independently verified. Body headers identify Team 15417.
- Page convention: physical pp.1–2 are the summary and memo; printed page 1 begins at physical p.3.
- Source limitation: no separate original problem statement was present in the corpus inventory.

## Architecture and justification

The authors identify three objectives: maximize completed trips, reduce encounters represented by overtaking, and minimize requests that require rescheduling. They distinguish predesigned trips that customers select from requested trips that must satisfy a chosen duration. This distinction determines whether a late provisional itinerary can simply be relabeled or must be repaired (pp.3–4, 10).

The schedule is a campsite-by-night occupancy table. A boat object records propulsion, requested duration, remaining days and current location. The river object owns the request queue, table and completed-trip list. The paper explains both the representation and the implementation, including the day-versus-night convention. This is a useful example of letting the mathematical state structure determine the software structure.

The stated priority rule serves boats with fewer remaining days first and breaks ties in favor of slower boats. The reasoning is that time-critical and less mobile boats have fewer opportunities to recover from delay. The preferred movement is the rounded-up remaining distance divided by remaining days, plus a small forward bias, capped by the daily travel limit. This balances pacing against leaving space for later arrivals.

## Conflict resolution and planning-time repair

If a preferred camp is occupied, the algorithm searches toward the boat's previous camp for an available alternative. If none exists, it displaces an already assigned boat and propagates the search until a gap is found (pp.5–8). The two diagrams show why even a high-priority boat may need its provisional assignment changed: the lower-priority boat cannot physically move upstream. This is a constructive lesson that hard feasibility takes precedence over a preference score.

The argument for eventual resolution is that no new boat enters until existing boats have been reassigned, so a displaced chain should ultimately reach a space vacated during movement. That is a useful invariant to test, but a complete implementation should also check unique assignment, nonnegative movement, maximum travel and termination on adversarial small cases.

New boats are admitted from a first-come queue only after existing boats move. If the head request cannot be placed, admission stops for the day, retaining the first-come restriction at the cost of possible unused capacity. Requests that cannot finish before season closure are skipped. A provisional late trip is erased from every earlier table cell, reset and returned to the front of the queue (pp.9–10).

This repair is valid only as an offline planning operation before reservations become commitments. It changes the departure date rather than guaranteeing the customer's originally requested date. The source stores duration and propulsion, but not a customer's allowable departure window. Earlier gaps left by removing the boat are not refilled through a full rollback, which explains part of the efficiency cost. A useful working-document rule is to distinguish revisable planning state from already promised dates and to record exactly what a repair is authorized to change.

## Static code inspection reveals a consequential mismatch

The complete appendix makes the implementation unusually inspectable. It also changes the interpretation of the paper's principal scheduling rule. `Boat.compareTo` returns `-1` when the current boat is motorized and the other is oar-powered with equal remaining days (p.19, code lines 196–200). In the natural-order priority queue used by the program, this gives **motor boats precedence on ties**, contrary to the prose's slow-boat preference. The comparative effect cannot be inferred without rerunning both versions, but the reported policy and printed code are not identical.

The movement function also adds the literal value four rather than reading the declared `MOVEMENT_CONSTANT` (pp.17, 19). Changing the named constant alone would not alter the supplied implementation. The shown code uses fixed daily distance constants of eighty and forty miles; reproducing the travel-hours sweeps requires changing those values consistently.

These findings illustrate why a reviewer should check the actual branch direction and parameter use, rather than assume comments and symbol names describe executable behavior. A two-boat priority fixture and a one-parameter movement fixture would directly verify the intended policy.

## Verification code is valuable, but its coverage must be explicit

The appendix includes `checkSchedule`, which scans completed boats to check duration and excessive movement between recorded camps (pp.23–24). This is a strong positive contribution: the authors provide a separate schedule checker rather than rely only on the generator's intent.

The checker does not independently test every required invariant. It does not check the final camp-to-exit distance, negative intercamp movement, or duplicate appearances of one boat on a night; it stops after finding the first matching campsite. It also inspects only boats in the completed list. A robust validation pass should reconcile all requested, admitted, completed, deferred and removed boats with the final table and should check every leg, including entry and exit.

The crossover routine counts changes in relative ordering between successive nights and new entrants placed downstream of an existing boat (pp.24–25). This is a defined proxy for encounters, not a complete continuous-time encounter model. The source supplies neither a proof of minimum crossovers nor a comparative crossover-results table. Thus the memo's claim of an absolute minimum of interaction is unsupported by the displayed evidence.

## A useful discovery: flooring creates sharp feasibility changes

The maximum number of camps a boat can advance is a floored ratio of daily distance to campsite spacing. Small changes in travel hours, river length or campsite count can therefore add or remove a whole reachable campsite. The paper notices repeated jumps in rescheduling outcomes and traces them to simultaneous movement thresholds for slow and fast boats (pp.11–12).

This is valuable reasoning: the authors explain a surprising numerical pattern through the model's discrete structure rather than smoothing it away as random noise. The pattern they call “magic numbers” is conditional on uniform spacing, fixed speeds and a fixed daily travel cap. It should be described as a reachability threshold, not as a universal design rule for real rivers.

The reported drop from about 630.5 to 439.6 trips near one travel-hours threshold is material, despite the broad claim that the model is insensitive. Robustness must include values on both sides of such thresholds, unequal campsite spacing, daily speed variation and lost campsites. A solution optimized exactly at a discontinuity may have little margin against ordinary variation. Conversely, when adding camps changes the entire uniform grid, the feasible sets are not simply nested, so monotonic conclusions require care.

The forward-bias experiment reports an increase from about 557.9 to 617.8 trips when adding one campsite of extra desired movement, while reducing rescheduling. Larger biases eventually worsen rescheduling. This is a useful ablation structure: identify a mechanism, vary one rule and observe both throughput and a service-cost metric. The claimed best bias range still depends on the tested grid and should be accompanied by saved configurations and held-out scenarios.

## Efficiency: a resource bound is helpful, but use the realized schedule

The paper derives the campsite-night budget `182Y` for its 183-day season. Dividing by average nights per trip gives a relaxed capacity benchmark, and multiplying completed trips by average duration estimates utilized campsite-nights (p.12). This is more informative than reporting throughput alone because it distinguishes a larger system from a more efficiently used one.

The benchmark is conditional on the duration mix. It is not a globally achievable optimum over all mixes and travel constraints. The exact occupied-cell count is already available in the final schedule and should be used instead of assuming the requested mean duration equals the mean duration among completed trips. End-of-season skipping and rescheduling can change that mix. Startup and terminal reachability can also leave unavoidable empty cells, but the claim that the true best efficiency is about 99 percent is not established by a bound or proof.

The source reports a mean of 659.371 trips and approximately 98.8 percent utilization for 44 camps, a ten-hour travel allowance, a movement bias of four and a uniform request mix. It describes ten sets of one thousand iterations. This replication is useful, although raw runs, seeds, dispersions and the precise experiment driver are absent. The appendix shows a single-run program, not the full sweep and aggregation procedure.

The Gaussian experiment is implemented by rounding and clipping durations to the permitted range (pp.25–26). This piles tail probability at the endpoints; it is not a truncated normal obtained by conditioning or resampling. Its actual mean and campsite consumption should be computed from the generated and accepted trips. The prose's statement that cutoffs prevent an accurate efficiency estimate is unnecessary when the complete schedule is available.

## Scope of the managerial recommendation

The model is a constructive offline heuristic with a strong occupancy representation, explicit repair and unusually extensive code. It supplies evidence for high utilization in selected uniform-grid scenarios. It does not establish globally optimal throughput, minimum human contact or guaranteed preservation of every customer's initial departure date.

The memo also calls carrying capacity `Y`, while the summary defines a seasonal trip count. `Y` is the simultaneous overnight campsite capacity; seasonal throughput is a different quantity. A stakeholder document must preserve the units and time horizon of the result rather than compress them into a single ambiguous capacity number.

## Transferable workflow rules

1. Separate throughput, encounter proxies and rescheduling costs in the objective specification.
2. Represent the schedule as a resource-by-time table and make its invariants independently checkable.
3. Let hard feasibility override a priority preference during conflict resolution.
4. Audit comparator signs and actual parameter references against the stated policy.
5. Distinguish offline repair from changes to committed customer dates.
6. Examine both sides of discrete reachability thresholds and retain a practical margin.
7. Compare utilization with a valid resource bound using realized accepted durations.
8. Specify whether bounded random inputs are clipped, truncated or resampled.
9. Keep one numerical experiment record behind each reported average and figure.
10. State simultaneous capacity, seasonal throughput and service quality separately.

## Reading ledger

All 26 physical pages were read, including every line of the complete Java appendix and its duplicated inline algorithms. Material diagrams, formulas and plots were inspected separately; the comparator reversal was confirmed in the original rendered code. No program was executed or performance claim reproduced.
