# Full review: 2011 MCM B, Team 11759 — Optimizing VHF Repeater Coordination Using Cluster Analysis

- Source ID: `mcm_ee4be8627fef`
- Source: `MCM-ICM-master/2011美赛特等奖/B-11759-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–51, including references, all full-page network diagrams and both printed MATLAB listings. Some code lines are physically clipped at the PDF's right edge; all visible content was read, but missing line endings cannot be recovered from this source.
- Visual supplement: physical pages 5–6,8,11,15–18,20–22,24–25,29–35,37,44,49 inspected for equations, flowcharts, topology, coverage circles, parity labels, result counts and clipped code.
- Numeric reproduction: **NOT_REPRODUCED**. Neither placement algorithm nor radio traffic was executed.
- Award provenance: filename labels Outstanding; team-specific designation not independently verified.
- Page convention: physical and printed page numbers agree.

## Strongest reusable architecture

The paper builds two alternative network-growth policies around the same demand representation: **cluster potential users → choose a dense starting region → grow a connected repeater network → track geographic coverage separately from channel availability → add capacity when needed → inspect frequency-offset parity → compare urban and rural layouts → vary clustering and physical range → extend demand and terrain scenarios**. The useful contribution is the separation of distinct design deficits and the comparison of policies for addressing them, rather than a single complicated optimization formula.

In the Snaking policy, a chain expands toward promising clusters of uncovered users. Additional private-line repeaters are inserted when coverage exceeds the current channel budget. In the Branching policy, an initial backbone is constructed, uncovered demand is reclustered, and the most promising remaining cluster is connected from the closest existing network node. Capacity is added after the open network has sufficient coverage (pp.6–14). Thus the two models differ meaningfully in both topology and the timing of capacity decisions.

The central state variables are covered users, available channels, served users as their minimum, and a nonnegative channel deficit (p.8). Removing covered points before subsequent clustering makes marginal coverage explicit. This is a transferable method for facility location, emergency service and communications problems: distinguish who is geographically reachable from who can actually be served.

## Approach justification and problem interpretation

**Explicit author reasoning:** k-means concentrates attention on user groups; scoring centers by nearby population favors high immediate benefit; growing from an existing network preserves connectivity; reclustering remaining users avoids repeatedly prioritizing already served locations. Branching provides more useful long-distance connections, while Snaking seeks a smaller equipment count (pp.11–14,18,22). Physical repeater range is linked to antenna height, so a reduction in equipment count can require more expensive individual installations (pp.5,24–25).

**Reviewer interpretation:** the comparison illustrates an important objective distinction. Fewest installations, local communication capacity and long-distance reach are not interchangeable. A strong workflow should identify those outcomes before ranking designs and preserve the tradeoff instead of calling every result “optimal.”

The task interpretation is materially narrower than universal coverage of a specified set of 1,000 users. The authors assume more potential users than the number required and stop once a selected subset of 1,000 is covered with enough modeled channels (pp.4–5,8). On p.26 they explain that exactly 1,000 potential users can cause the algorithm to keep moving around the final isolated user; they retain the larger-pool assumption. This is an acknowledged algorithm/scope interaction, not a demonstrated solution to every placement of 1,000 simultaneous users. A requirement ambiguity record must expose that choice.

## Assumptions, inputs and module interfaces

The region has a 40-mile radius, frequency band 145–148 MHz, 600 kHz input/output offset and 54 CTCSS tones. Assumptions include known geographic demand, equal handheld range/power, Euclidean distances, users distinct from repeaters, a closed network and negligible obstruction by people or antennas, while mountains can obstruct propagation (pp.4–6).

The urban and rural examples contain 1,400 potential users. A typical parameter set uses five clusters, 10-mile handheld/repeater coverage, 15-mile repeater transmission distance, 150-foot towers and 25 kHz channel spacing (p.16). The rural distribution consists of eight towns plus scattered users (p.19). These are constructed scenarios rather than calibrated observations with estimated uncertainty.

A practical implementation contract would pass user coordinates and physical constraints to placement; placement would return sites, equipment types and adjacency; a separate frequency module would return feasible assignments and conflicts; a service evaluator would return reachable endpoint pairs and simultaneous load. In this paper, parity is assigned after placement (pp.15–22), while channel availability is largely represented by a scalar budget. That makes the interfaces visible, but a final simultaneous-interference/service certificate is not supplied.

The authors model CTCSS as adding usable channels and distinguish local extra capacity from long-distance tone lines (pp.6,17–18,21–22). This is their abstraction, not independent verification that overlapping transmissions are physically orthogonal. The domain/data role should verify that mapping before a modeler treats a tone count as a capacity multiplier.

## Reported results and extensions

The urban Snaking example reports nine open repeaters and eight CTCSS repeaters, totaling 17 (p.16). The rural Snaking example reports ten plus eight, totaling 18 (p.19). Branching uses more equipment to support long-distance communication: the rural report gives eight open plus 17 CTCSS, totaling 25 (p.22). The full-page maps make the distinction visible: a chain winds through demand, whereas the branching design has a spine and lateral connections (pp.29–34).

For 10,000 required users, the authors generate 12,000 potential users and reduce channel spacing from 25 to 10 kHz (p.22). This is a joint demand-and-technology scenario, not a pure tenfold-load experiment with all other constraints fixed. Mountainous terrain is discussed qualitatively: a single high peak may improve line of sight, while multiple peaks may require valley routes (p.23). No terrain raster, visibility computation or mountain case result is presented.

Frequency parity diagrams disclose odd loops in the Snaking network. The authors accept some out-of-band leakage and argue that an alternative path permits delivery (pp.16–17,20). These diagrams are useful because they reveal a downstream constraint created by a geometric design. They do not establish simultaneous traffic feasibility under the stated frequencies.

## Validation actually present

The paper compares two policies on both urban and rural distributions. It varies cluster count, transmission distance/tower height and potential-user pool size (pp.24–25). At distances 10, 15 and 20 miles, the displayed open-repeater counts are 10, 8 and 7, illustrating the equipment-count versus tower-height tradeoff. Cluster count changes have relatively modest effects in the shown rural instances, but seed control and repeated-run uncertainty are not documented.

A particularly informative stress test increases the candidate population while retaining the requirement to serve only 1,000: the reported open-repeater requirement drops from ten for 1,400 potential users to three for 3,000 and one for 10,000, with eight CTCSS repeaters in each case (p.25). That result follows from easier subset selection. It is evidence about the chosen service definition and a trigger to revisit scope, not evidence that higher demand generally needs fewer facilities.

No independent traffic simulator, measured radio test, exact small-instance optimum or global lower-bound comparison is presented. The results support examples of heuristic placements under the authors' abstraction. They do not certify an absolute minimum repeater count for the original physical problem.

## Bounded independent checks

There are visible result-accounting conflicts. The urban Branching prose gives eight open plus 17 CTCSS but calls the total 26 (pp.17–18). The 10,000-user paragraph gives 19 open plus 33 CTCSS but calls the total 42 (p.22); arithmetic would produce 52. These conflicts should remain unresolved in a review until a run manifest or equipment table identifies the intended counts. Repeating the headline alone would propagate an unsupported answer.

The neighborhood-distance expression on p.8 visibly subtracts squared coordinate differences inside the square root, although the following algorithms use Euclidean addition. The printed Snaking code assigns both initial coordinates from the first cluster-coordinate column (p.37, lines 61–62), and some loops use five clusters even where the listed parameter is ten. The Branching implementation starts toward the second-highest-scoring cluster (p.43), which matches the narrative but differs from the farthest-target pseudocode description on p.13. These are specification/implementation checks, not a completed reproduction.

The listings on pp.36–51 depend on external user-coordinate files and contain visibly cut-off long lines, confirmed in the rendered PDF (for example pp.37,44,49). The appendix is valuable for understanding control flow, but its presence alone does not make the published experiment executable.

## Communication and transferable workflow rules

The two flowcharts give a concise comparison of when each method revisits coverage and capacity. The large appendix maps let a reader inspect coverage circles and backbone structure. Keeping topology, channel labels and user points visually distinct is a strong communication practice.

- Track separate deficits for coverage, capacity and connectivity, and state the acceptance test for each.
- Compare genuinely different construction policies with the same demand scenarios and evaluation contract.
- Recompute marginal demand after serving users; do not repeatedly optimize the original total.
- Distinguish local service from long-distance service before selecting the “best” network.
- Feed frequency or routing infeasibility back into placement instead of treating it as cosmetic labeling.
- Separate algorithm settings, physical design parameters and changed technology assumptions in sensitivity studies.
- When a failure is avoided by changing the target population, reopen the requirement interpretation.
- Derive totals, plots and prose from one equipment/run table; retain contradictions until resolved.
- Label terrain proposals and capacity abstractions by their actual evidence level.

## Reading ledger

All visible text read: pp.1–8,9–16,17–24,25–32,33–40,41–45,46–51. Relevant rendered pages inspected: pp.5–6,8,11,15–18,20–22,24–25,29–35,37,44,49. Both full printed code listings and references reviewed; physically clipped code endings remain unavailable. No model execution or numerical reproduction claimed.
