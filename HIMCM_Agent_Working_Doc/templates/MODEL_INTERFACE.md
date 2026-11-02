# Model Interface — [Upstream M-ID] to [Downstream M-ID]

- Owner: modeler; source definitions checked by domain-data; implementation checked by computation.
- Revision and accepted architecture/decision:
- Requirement and decision affected:
- Producer artifact/version and consumer artifact/version:
- Implementation maturity: proposed / toy implementation / target implementation / target evidence checked.

Use this record for a consequential dependency between components. A short model can place the same fields in its model specification instead of creating another file. The reviewer tests the interface; the coordinator records acceptance and downstream invalidation. Other roles send proposed changes through their own handoffs.

## Meaning and conversion contract

| Field | Producer meaning | Consumer meaning | Explicit conversion or identity | Evidence / assumption | Check |
|---|---|---|---|---|---|
| Entity / population / eligibility | | | | | |
| Quantity / stock / flow / event | | | | | |
| Unit and denominator | | | | | |
| Time interval / instant / availability time | | | | | |
| Spatial scale / coordinate system | | | | | |
| Array shape / column name / category order | | | | | |
| Missing / zero / invalid value | | | | | |
| Uncertainty and dependence | | | | | |

Name fields rather than relying on unexplained column positions. A conversion requires its own assumptions: cumulative events are not active demand, annual totals are not standing stocks, geographic distance is not delivery time, and a fitted association is not an action-response coefficient.

## Timing, capacity and state

- State carried across the boundary; identity or attributes that must persist:
- Order of observation, decision, reservation, movement, consumption and update:
- When an output becomes known and when resources become usable:
- Shared capacity/stock and who atomically reserves or releases it:
- Conservation equation, including entry, exit, losses and untracked states:
- Delay, expiry, lead time, backlog and unmet demand treatment:
- Feedback from downstream feasibility to upstream choices:
- Any computational rescaling and the quantities it must preserve:

## Validation contract

1. **Small known case:** exact input, independently known output, tolerance and actual result location.
2. **Boundary case:** zero supply/demand, full capacity, no movement or another relevant limit.
3. **Composition check:** verify the combined chain, not only each component in isolation.
4. **Endpoint evidence:** identify the final outcome this interface is supposed to support and what independent evidence checks it.
5. **Uncertainty transfer:** scenario/replication identifiers and correlations preserved; no silent substitution of a mean for a nonlinear uncertain input.
6. **Alternative representation:** explain whether a simpler conversion changes the decision materially.

Record checks actually run, including failures. Passing a distance check does not validate travel-time estimates; a demand fit does not establish feasible service capacity; a schema match does not validate a behavioral relationship.

## Failure and recovery

- A condition that rejects this interface:
- Affected runs, figures, claims and downstream interfaces:
- Safe fallback or narrower answer, with evidence limit:
- Owner of repair and next concrete task:
- Review artifact and accepted version:

Do not pass an unresolved definition to another agent as an implementation detail. Return it to the modeler and coordinator before dependent results are accepted.
