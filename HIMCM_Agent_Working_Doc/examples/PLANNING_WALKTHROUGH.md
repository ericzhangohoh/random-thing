# Walkthrough: From Lifecycle Accounting to a Feasible Transition Plan

**Historical anchor:** [2023 HiMCM B](../../HIMCM_备赛资料/02_历年真题/2023/2023_HiMCM_Problem_B.pdf), concerning bus electrification, environmental/financial consequences and a phased plan. This is an operational illustration, not a numerical solution.

## 1. Requirement and interface map

The coordinator verifies the complete official statement and maps its required cities, funding conditions, planning horizon and decision letter. The modeler separates three functions:

`service demand and fleet → lifecycle/financial accounting → feasible yearly replacement decisions → comparison and recommendation`.

Accounting estimates consequences. Planning chooses actions. A search algorithm solves the resulting decision formulation. These functions must not be collapsed into the name of one algorithm.

## 2. Domain-data handoff

Provide service requirements, fleet composition, vehicle/battery characteristics, electricity and fuel assumptions, purchase/maintenance/disposal costs, charging constraints and sources. Align units and years. Label scenario assumptions and avoid treating a maximum possible subsidy as a guaranteed receipt.

If a critical input is unavailable, offer a defensible range or identify the claim that cannot yet be supported. A city-level average is not automatically adequate for route-level feasibility.

## 3. Modeler handoff

Define integer replacement variables by year; fleet conservation; minimum service; annual spending and infrastructure capacity; and the environmental and financial outputs. Specify when vehicles and charging assets become available and when payments occur.

A baseline might replace the oldest eligible vehicles as funds permit. A candidate optimization should use the same service assumptions and accounting boundary. If objectives conflict, present a tradeoff or justified preference rather than mixing incomparable units with arbitrary weights.

Specify a tiny known-answer instance. It should expose whether budget, fleet balance and charging constraints are implemented correctly. Submit the proposed architecture, tradeoffs and validation design at G2.

## 4. Computation handoff

Deliver the baseline and candidate schedules, yearly state transitions, constraint residuals, cost/emission tables, solver status and any optimality bound. A schedule must remain feasible every year; a favorable ten-year total cannot repair an infeasible first year.

Run relevant scenarios for subsidy, demand, energy prices and charging limits. Use justified ranges. Save the actual decision changes, not only a smooth objective curve.

## 5. Reviewer challenges

- Does accounting include the same lifecycle stages for the alternatives?
- Is available funding being counted twice or assumed at its maximum without support?
- Are route range, charging and service requirements checked at an adequate resolution?
- Does the implementation match the model's stated budget and timing constraints?
- Is a reported optimum global, bounded within a formulation, or only the best searched schedule?
- Does transfer to another city require different constraints or just new parameters?

Each finding identifies the owner, affected run and necessary rerun. The reviewer does not edit the schedule to make it feasible.

## 6. Integrate and communicate

The G3 packet presents the actual schedule, quantified tradeoffs, uncertainties, operating assumptions and conditions that would change the recommendation. The decision letter explains practical sequence and consequences in accessible language.

A defensible recommendation may be conditional. For example, an early replacement phase may depend on confirmed charging capacity. The workflow should preserve that condition, rather than deleting it to make the letter sound decisive.

## 7. What this exercise checks

The workflow connects submodels through explicit units and timing, tests feasibility before making claims, separates algorithm choice from formulation, and allows later constraints to revise earlier decisions. Actual numerical performance requires executing the specified model and experiments.
