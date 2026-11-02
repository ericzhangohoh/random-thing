# MCM 2012 B — Team 13955 — a priority scheduler and a capacity experiment

- Source ID: `mcm_a0e5e63c77e2`
- Source: `MCM-ICM-master/2012美赛特等奖/B-13955-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pp.1–18, including abstract, all method details, every result table, limitations, references and manager memo.
- Visual supplement: physical pp.5–15 inspected for definitions, priority examples, complete algorithm flowchart, four-group trajectories, capacity tables and fitted contour surface.
- Numeric reproduction: **NOT_REPRODUCED**. No scheduler, simulation or surface fit was executed; reported numerical results remain author claims.
- Award provenance: Outstanding filename label, not independently verified. Cover and page headers verify Control 13955.
- Source limitations: no executable code is supplied, and no separate original problem statement was present in the corpus inventory.

## Architecture and why it is useful

The paper makes a scheduling rule operational before estimating carrying capacity. The river is an ordered array of campsites; each group has a location, elapsed time, intended duration, maximum daily travel distance and priority. A waitlist represents groups that have not launched, and an unlimited-capacity exit represents completed trips. Each simulated day updates the state of all groups.

The scheduler searches from the downstream end for an empty campsite, identifies groups that can reach it and gives preference to the group furthest behind its intended progress. This downstream-to-upstream sweep can reuse sites vacated by groups that move farther downstream. The representation makes campsite exclusion, travel limits and departures concrete. Worked examples and a flowchart explain the algorithm's intended behavior (pp.6–9).

Capacity is then estimated by increasing daily arrivals until late trips or a persistent waitlist appear (p.12). This separates two tasks that are often conflated: producing a feasible schedule and measuring how much demand a particular scheduling policy can serve. The paper's most transferable idea is to preserve that separation and log completed trips, lateness and unserved demand separately.

## Assumptions define a narrower problem

The model permits groups to stay at the same campsite for multiple nights. It limits oar trips to 12 or 18 days and motorized trips to 6 or 12 days, although the restated problem allows a wider duration range. It assumes nine travel hours per day, yielding maximum daily distances of 36 and 72 miles, and ignores weather, river flow and campsite closures (pp.4–5).

These choices reduce the action space and make the experiment manageable, but the resulting capacity applies to that selected service menu. The memo's broad claim about all varying durations is therefore stronger than the demonstrated scope. The later duration-distribution table also needs to specify exactly how each distribution is assigned within the propulsion-specific restrictions.

The uniform spacing is stated as `225/Y` while all `Y` camps are described as strictly between launch and exit. The endpoint convention must be specified: `Y` interior camps normally produce `Y+1` gaps. The paper also alternates days and nights. A simulator must explicitly define launch day, the number of camp nights and the exit day before a deadline rule can be verified.

## Priority is a useful heuristic, not a deadline guarantee

Priority is the fraction of allotted time elapsed divided by the fraction of river distance covered: `P=(d/t)/(l/225)` (p.5). This is dimensionless and interpretable: values above one indicate progress behind a linear reference schedule. Waitlisted groups receive priority one to avoid the undefined zero-distance ratio.

The algorithm tries to advance delayed groups and hold back early groups. However, relative progress does not fully encode deadline feasibility. Two groups with similar priority may have different remaining distances, propulsion limits or bottleneck access. A useful additional check is whether the remaining distance can be covered within the remaining travel days, plus whether a feasible sequence of camps exists. Those checks test a hard promise directly rather than relying on a proxy score.

The written implementation contract has unresolved cases:

- The movement rules and flowchart distinguish `P>1` and `P<1` but do not specify `P=1`, even though all waitlisted groups start at exactly one.
- The formal reachable-set expression only supplies an upper travel bound. The accompanying prose supplies the downstream restriction, but both bounds should appear in the executable eligibility condition.
- Ties, groups already moved that day, sites vacated during the update and groups remaining in place need explicit handling. A daily state update must not accidentally allow multiple moves or reuse a campsite already reserved for that night.
- The exit rule permits departure only when elapsed time equals intended duration (p.8), yet the capacity experiment reports completed late trips. If elapsed time has already exceeded the target, an equality-only condition would prevent exit altogether. The implemented late-trip behavior and the published rule must be reconciled.

No code is supplied to resolve these questions. They are reasons for a precise state-transition specification and small hand-checkable fixtures, not proof that every reported simulation used the same error.

## What the demonstration establishes

The four-group example includes a six-night motorized trip, an eighteen-night oar trip and twelve-night trips of each propulsion type, inserted midseason (pp.10–11). The table and plots make waiting at campsites, bursts of travel and priority changes visible. This is more informative than a single aggregate capacity number because it exposes how the policy treats different groups.

The table's night labels skip ten and continue through twenty. Its priority values and exits therefore need reconciliation with the stated day/night definitions before accepting the claim that every group spends exactly its planned number of nights. The plots show a small set of trajectories, not exhaustive deadline verification. A validator should compute launch-to-exit duration and maximum leg distance directly from every saved group record.

The Grand Canyon example uses cited campsite and management information, assumes an equal propulsion and duration mix, and increases daily arrivals (p.12). The source reports 2,988 completed trips at eighteen arrivals per day with no late trips; nineteen arrivals produce five late trips, and higher arrival rates create a waitlist. This identifies a tested operating point for the heuristic under those inputs. It does not establish a global maximum over all admissible launch calendars or allocation rules.

The paper explicitly notes that some launched groups remain on the river when the 180-day simulation ends. These groups are then ignored. That is material to a seasonal capacity claim: launched, completed and still-active trips are different counts. A model should either stop launches early enough to finish before closure, extend the simulation to drain the system, or define capacity as a launch-rate measure and report the terminal inventory separately.

## Sensitivity experiments and the limits of a fitted surface

The authors vary the campsite count and propulsion ratio, then vary duration mix (pp.13–15). This is a useful two-dimensional experiment design: it reveals interactions that one-variable sensitivity might miss. The tables provide direct managerial inputs rather than only an abstract sensitivity coefficient.

The recommendation of a universal 1:1 oar-to-motor ratio is not supported by every displayed row. At 100 camps, the reported best value is at 1:4; at 200 and 250 camps, 1:2 slightly exceeds 1:1 (p.13). A smoothed contour surface should not override the raw table or manufacture a single optimum. The size of small differences also needs comparison with simulation variability and search uncertainty.

The authors acknowledge that their fitted surface extrapolates poorly and recommend running the underlying scheduler for new inputs (p.14). This is a valuable restraint: a convenient surrogate is useful only within a tested domain, and its visual smoothness does not establish accuracy. The surface equation, fit errors and independent evaluation points are not supplied, so it cannot be used as a verified prediction tool.

The ratio changes also mix policy and demand. If arrivals are generated differently as the ratio changes, the experiment must report rounding, waitlist ordering, randomization and duration assignment. Without those details, unexpected changes can reflect the input generator or heuristic tie-breaking rather than a general property of river capacity.

## Case-study realism is not validation of the recommendation

The paper compares its roughly 3,000-trip estimate with an actual figure around 1,000 and attributes the difference to omitted environmental or management constraints (p.16). That discrepancy is a useful warning about the model's scope. It is not empirical validation of the larger recommendation. The result should be called campsite-and-scheduling capacity under stated assumptions, distinct from ecological carrying capacity or an approved operating limit.

Likewise, subtracting existing annual trips `X` from a fresh simulated capacity does not establish that `3000−X` trips can be added around the actual bookings (p.15). Existing launch dates, durations and campsite commitments matter. An incremental scheduling problem should initialize the model with those commitments and preserve them, or explicitly state that the whole season can be rescheduled.

## Transferable workflow rules

1. Separate a scheduling policy from the experiment used to estimate its capacity.
2. Represent the state explicitly and make the daily update order inspectable.
3. Treat priority scores as heuristics; verify hard deadlines and travel feasibility separately.
4. Define endpoint, day/night and finite-season conventions before writing code.
5. Log completed, late, waiting and still-active groups as distinct outcomes.
6. Include every exceptional branch in the algorithm contract, especially equality, ties and missed deadlines.
7. Compare a heuristic with alternative rules or exact small-instance solutions before calling its output optimal.
8. Check recommendations against raw tables before smoothing or fitting response surfaces.
9. Distinguish physical scheduling capacity from ecological or managerial capacity.
10. Test additional demand against the actual existing schedule rather than subtracting aggregate counts.

## Reading ledger

All 18 physical pages were read, including every simulation and sensitivity-table entry, limitations, references and final memo. Material visuals were inspected separately to resolve the priority formula, equality branches, skipped night label and the raw-table/contour recommendation discrepancy. No numerical model was reproduced.
