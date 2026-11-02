# Full review: 2011 MCM B, Team 10496 — Clustering on a Network

- Source ID: `mcm_de9286d69ab7`
- Source: `MCM-ICM-master/2011美赛特等奖/B-10496-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–34, including all network examples, pseudocode and references.
- Visual supplement: physical pages 10–12,15–16,18,20–24,26 and31–33 inspected for probability expressions, population maps, routing labels, algorithm specifications and result tables.
- Numeric reproduction: **NOT_REPRODUCED**. No population generator, clustering implementation, channel assignment or traffic simulation was executed.
- Award provenance: filename labels Outstanding; team-specific designation not independently verified.
- Page convention: physical PDF pages; printed body pages are one less.

## Strongest reusable architecture

The paper develops a connected network-design pipeline: **define service quality → generate spatial demand scenarios → locate repeaters by clustering → connect components → assign a hub, frequencies and privacy-line routing → simulate requests → examine the cost/service tradeoff → stress the network with tenfold demand and terrain changes**. Its strongest lesson is that geographic coverage, physical connectivity and service capacity are separate properties requiring separate checks.

The problem concerns repeaters in a40-mile-radius region, with a145–148MHz band,600kHz input/output offset and54 privacy lines (p.5). The authors define service quality Q as processed requests divided by attempted requests, including uncovered endpoints as failures, and use a time-stepped queue to evaluate a proposed network (pp.8–9). A service threshold remains a parameter so designs can be compared at different required levels.

A uniform population is retained as a benchmark, while Gaussian-like clumps approximate more concentrated communities (pp.11–12). K-means supplies demand-centered initial sites; disconnected groups are connected by a shortest-link/minimum-spanning-tree-inspired procedure; a central hub is selected using closeness centrality; channel layers radiate outward from it (pp.17–21). Privacy-line assignments localize transmissions to appropriate branches instead of making every call occupy the whole network (pp.15–17).

## Approach justification and scope

**Explicit author reasoning:** population clustering avoids wasting installations in empty regions; connecting components is necessary if covered users should reach each other; a central hub creates a notion of inward and outward routing; short average graph distance reduces both channel-chain length and nodes occupied by a call (pp.16–20). The simple blanket-coverage alternative is used as a baseline, and its poor traffic performance motivates the branch-routing design (pp.14–15).

**Reviewer interpretation:** the model architecture follows distinct failure modes. A placement can cover people but be disconnected; a connected network can have inadequate simultaneous capacity; adding coverage can increase bottleneck load. This is a useful pattern for infrastructure problems where a map alone is not an answer. The modular adjacency interface also helps explain which parts need to change under terrain effects.

A major scope change must remain visible. The paper explicitly reinterprets “1,000 simultaneous users” as1,000 potential users making requests at a parameterized rate, because it judges literal simultaneous demand unrealistic (p.5). This enables a queueing/service model, but it does not answer the strongest literal concurrency requirement. The working document should require an ambiguity ledger and consequences of alternative interpretations rather than silently substituting an easier task.

## Assumptions and data

Assumptions include circular broadcast regions, repeaters communicating when their coverage disks touch, approximately9-mile repeater range, roughly3-mile handheld reach, negligible transmission/switching delay, courteous users who avoid busy local channels, equal average load and a strong bias toward nearby calls (pp.6–8). Blind conflicting requests are delayed rather than counted as failed, a simplification the authors explicitly admit began as temporary and remained unfinished (p.7).

The authors also treat600kHz as the minimum distinguishable frequency spacing, using five successive frequency pairs (pp.7,13). That is an additional assumption: the supplied duplex offset does not itself establish a general channel spacing. Hardware interpretation and an optimization model must be distinguished before using the resulting channel count.

Population scenarios use5,10,20 or40 clumps plus a uniform case, with five generated populations for each type (pp.11–12,22). A southeastern-US population-density image supplies a visual plausibility comparison; there is no fitted spatial calibration or held-out regional validation. Request generation biases destinations by graph distance, with a parameter λ=1 (p.10). Consequently both placement and traffic depend on a synthetic demand model.

## Module handoffs and reported results

The site-generation algorithm exposes inputs and outputs in pseudocode: user locations and range constraints become repeater positions/ranges, then an adjacency matrix, then channel assignments (p.18). This is a clear interface for splitting work among agents. Physical equipment count differs from site count because some locations contain paired repeaters for opposite directions (pp.13,21–22). A reusable data schema must distinguish those units.

For15 initial clusters, reported mean equipment counts range from37.0 to43.4 across the five demand patterns (p.22). Coverage failures range from about5.8 to21.8 users (p.23). Transmission success ranges from0.830 for five clumps to0.977 for the uniform case; the naive baseline is roughly0.22–0.31 (p.24). These results support conditional comparative performance, not universal98% service.

Tenfold demand exposes the hub bottleneck: the authors report roughly half of10,000 attempted transmissions completed over200 time units, compared with about700 for the naive network (pp.24–25). They propose recursive local subnetworks to absorb short-distance demand, but explicitly state that implementation and analysis were unfinished (p.25). Mountainous terrain is likewise a proposed extension: alter position-dependent visibility/ranges, refine locations, and retain the graph-based channel/routing logic where appropriate (p.27). Neither extension should be recorded as tested success.

## Validation actually present

The study compares several population patterns, several cluster counts and a naive design. Traffic quality is simulated ten times to estimate variability, with standard deviations approximately0.003–0.014 in the displayed cases (p.23). This is useful evidence about Monte Carlo variability under the generator, not1.5% real-world predictive error. The paper uses “sensitivity” for some replication variability; parameter sensitivity and stochastic uncertainty should be labeled separately.

The tables reveal a nonmonotone effect that is more informative than the general prose. In the five-clump case, transmission success increases from0.715 at five initial clusters to0.850 at ten, then falls to0.814 at25 (p.24). Adding infrastructure does not necessarily improve the combined coverage/routing/traffic system. That makes a search over feasible designs more appropriate than assuming monotone gains.

The authors candidly identify nondeterministic k-means, hub congestion, finite privacy-line capacity, delayed duplicate signals and weather-sensitive links (pp.28–30). Their destination-label scheme permits only about25 distinct sites, with feasible initial cluster counts often smaller. Result rows beyond that practical cap require a separate routing-feasibility check before being treated as deployable.

## Bounded independent checks

The printed population density on p.11 has a positive quadratic exponent and lacks the usual negative half factor; as written it is not the stated Gaussian density. The request probability on p.10 mixes a binomial coefficient, λ power and factorial with an undefined k and is not a conventional Poisson formula. These are visible specification defects. They prevent faithful reconstruction from the paper alone; the intended synthetic-generator code was not available here to resolve them.

The claim that a minimum-spanning-tree-style connection minimizes the number of additional repeaters is also stronger than established (pp.19–20). Minimizing Euclidean link length is not automatically equivalent to minimizing discrete relay count, especially if alternative junction locations are allowed. Similarly, the smallest successful network produced by this heuristic is a feasible best-found result, not a certified lower bound on all possible networks (p.10). Keep optimization guarantees separate from the useful heuristic architecture.

## Communication and transferable workflow rules

The paper's metric-first exposition, explicit algorithm inputs/outputs and comparison tables make its reasoning inspectable. The appendix maps show how spatial demand changes the proposed network. Its frank unfinished-work statements are also valuable because they preserve what was and was not demonstrated.

- Define service and concurrency before choosing an algorithm; record any reinterpretation of task wording.
- Test coverage, connectivity, interference feasibility and capacity separately.
- Design a simple baseline and evaluate it with the same traffic assumptions.
- Separate physical sites, equipment count, frequency pairs and routing labels in the schema.
- Preserve nonmonotone results; more resources can worsen congestion or violate a different limit.
- Distinguish stochastic replication variability from parameter sensitivity and external predictive accuracy.
- Stress the architecture at the required scale increase and identify the mechanism of failure.
- Mark proposed extensions as unimplemented until code and evidence exist.
- State heuristic best-found claims without implying an unproved global minimum.

## Reading ledger

All text read: pp.1–8,9–17,18–25,26–34. Relevant visuals inspected: pp.10–12,15–16,18,20–24,26,31–33. All pseudocode, appendix maps and references reviewed. No simulation or hardware behavior independently reproduced.
