# Multi-agent rehearsal and adversarial repair report

Date: 2026-11-03. Problem: official 2022 HiMCM B, **CO2 and Global Warming**. This English record describes work actually executed, its confirmed failures and its limits. Final PDF acceptance and repository delivery are recorded separately so a completed numerical run is never mistaken for a completed paper.

## 1. Objective and authority

The user requested a complete non-biological historical-problem rehearsal: exercise the agents' assignments and handoffs, produce the final PDF, repair defects and sync to a private GitHub repository. The user then explicitly requested more agents to attack the approach before repair. This authorized retrospective practice, not live contest submission, biological research, software installation or global settings changes.

The coordinator retained G1, G2 and G3 evidence packets and labeled the decisions `DELEGATED_PRACTICE_DECISION`. It did not invent a human response to satisfy a checkpoint. The reusable workflow now explains this delegation case. Scientific acceptance, recovery acceptance, PDF acceptance and external delivery remain separate decisions.

## 2. Actual division of work

| Role | Actual work and handoff | Who checked it |
|---|---|---|
| Coordinator | Requirements, ownership, dependency graph, gate packets, attack dispatch, reconciliation and private Git synchronization | Reviewers checked named operating-contract changes and evidence; final integration is separately recorded |
| Domain/data | Admitted official PDF/XLSX, reconciled all 127 printed values, established years, units, baseline and source discrepancies | T04 framing/source review; later independent numerical checks |
| Modeler | Proposed competing forms, justified the simple baseline, froze chronological selection, answered attacks and wrote 17 bounded claims | T04/T08, A01/A02 and T10 |
| Computation | Implemented ingestion and models, ran tests and separate development/final/production stages, retained exact dependencies, repaired confirmed execution defects | Independent numerical review and A03 tamper/diagnostic probes |
| Writer/visuals | Authored methods first, verified an actual draft export, then consumed G3-accepted evidence for the full paper | Own every-page inspection followed by separate T11 and A04 review |
| Independent reviewer | Independently derived key numbers, verified claim bindings, reviewed recovery and reviewed named workflow changes | Published exact-version scoped verdicts, not edits to the author's targets |
| Additional adversaries | A01 attacked validation/selection; A02 attacked structural choices; A03 attacked implementation contracts; A04 attacks final claim wording | Authors respond, then the reviewer rechecks repairs |
| Recovery replacement | Reconstructed current state from files and reproduced retained computation in an isolated directory | T13 independent receipt/hash/equivalence review |

The main reviewer and the two additional adversarial reviewer contexts used GPT-6 Astra. A02 and A03 used the same actual reviewer context on separate tasks; A04 reuses A01. These are not falsely counted as four new independent reviewers. An attempted additional fresh spawn hit the platform's thread limit. The recovery session had unrelated previous work but had not participated in this rehearsal; it was not described as an empty new context. An author-arranged implementation preflight and writer editorial assistance are distinct from formal independent acceptance.

Each assignment named allowed writes and upstream evidence. Handoffs identify completed artifact paths and hashes. Reviewers wrote their own QA subtrees and returned repair requests; the responsible author produced a new version. Closed rejected runs, drafts and verdicts remain available.

## 3. Why this approach was defensible

The question asks for comparison and explanation with a small annual time series, not a process-based climate simulation. The team therefore selected transparent models that could be computed, challenged and explained within the evidence available:

- **D:** a ten-year recent CO2 drift anchored at the latest available observation.
- **Q:** a quadratic concentration trend fitted by ordinary least squares.
- **E:** an exponential concentration trend fitted in log space.
- **T0:** a linear temperature-anomaly trend in time.
- **T1-D/Q/E:** a descriptive log-CO2 temperature association combined with each forecast CO2 path.

The simple D baseline asks whether complexity earns its place. Competing Q and E forms expose curvature assumptions; T0 asks whether the CO2 association adds predictive value beyond time. Models are not treated as causal climate mechanisms. Source definitions are part of the model: supplied CO2 observations are annual despite a March caption, temperature anomalies use 1951-1980, and the cited 685 ppm OECD benchmark is CO2-equivalent rather than pure CO2.

The team fixed development origins 1981, 1986, 1991, 1996 and 2001, with horizons 1-10 years and development targets ending by 2011. Pooled development MAE determines the CO2 selection. The temperature decision then compares T0 with the pipeline using that selected CO2 model. The final 2012-2021 assessment starts from 2011 without refitting. Production parameters are refitted through 2021 only after that assessment. Future CO2 inputs are predicted, not substituted with future observed CO2.

The resulting selection is D followed by T1-D. This is a **prespecified sequential selection**, not a claim that T1-D is the global winner among every possible temperature pipeline. The design is simple enough to reproduce and strict enough to reveal when a more complex competitor wins under a different evaluation.

## 4. Attempts to refute the approach

| Attack | Evidence and strongest objection | Disposition |
|---|---|---|
| Development selection instability | Q wins three of five origins; removing either of two origins changes the pooled winner. A single pooled score is not a robust universal ranking. | Keep the frozen D decision, disclose instability and all candidate scores; no silent retuning |
| Final-period ranking reversal | Q's final CO2 MAE is about 1.398 ppm versus D's 2.145 ppm. | Repair the claim contract: “selected by the declared development rule” is supportable; “uniformly most accurate” is not |
| Temperature eligibility | T1-Q has a slightly better final score than selected T1-D, but was not eligible in the frozen sequential comparison. | Show all declared comparators and explicitly state sequential eligibility |
| Missing simple alternatives | Structural reviewer evaluated additional 20-year drift and quadratic-temperature alternatives; these did not beat the chosen development temperature pipeline. | No forced model expansion; retain bounded comparison evidence |
| Shared-trend association | Level association weakens under trend/difference diagnostics; T1-E composition can be linear in time. | No causal coefficient, unique CO2 information or policy-effect claim |
| Error-envelope miss | Selected temperature pipeline misses the 2016 historical envelope: absolute error about 0.222 C exceeds radius about 0.197 C. | Preserve the miss; do not widen the envelope after seeing it or call it a confidence interval |
| Distant crossing years | A ten-year historical test cannot validate predictions through 2100 or beyond. | Label all distant outcomes conditional continuations; 2031 only marks the maximum tested-horizon display cutoff |
| Source comparability | Annual/March, CO2/CO2-equivalent and baseline differences can change the meaning of an apparent comparison. | Carry the discrepancies into technical and public-facing claims |

The independent reviewers also distinguished tiny numerical differences from physical significance. The supplied annual 2004 ten-year CO2 change is 18.74 ppm, below 2003's 18.77 ppm; this resolves the arithmetic ranking in the supplied data without claiming that the small gap is scientifically meaningful or directly testing a March-only historical claim.

The attack protocol accepts defenses when the evidence supports them. Reviewers were not required to invent defects or demand more complexity merely to fill a quota.

## 5. Confirmed implementation defects and repairs

Two A03 findings were actual implementation defects, even though the original ordinary historical results happened to be correct:

1. **Frozen selection could be altered.** Editing selected IDs in the saved receipt, while leaving development CSVs unchanged, was accepted by the old execution path and reported `selection_changed=false`. The repaired loader validates semantic receipt fields against hash-verified development predictions and metrics, recomputes the original selection and rejects inconsistencies before final or production writes. Seven independently executed tamper cases now fail before changing stage files; valid controls pass.
2. **Nonpositive CO2 was undercounted.** The old diagnostics counted after invalid values became null, so a direct negative prediction could produce a zero nonpositive count. The repair counts the direct failure cause before prefix invalidation. Independent injections verify negative/zero counts, exclusion of unevaluated suffixes and separation from nonfinite failures.

The author created r03 source and a new r03 run. All 35 scientific outputs remain equivalent to r02, with only enumerated provenance and unchanged-selector metadata differences. No equation, split, threshold, ranking criterion or original observation was tuned in response to final results. A03 accepted the repaired execution contract; T10 separately accepted current scientific evidence and claims. Original r02 source, runs and failed attacks are preserved.

Earlier author-arranged preflight also found four implementation problems before historical execution: failure-status translation, null propagation, final-table hash checking and a missing failure reason. These were fixed before the main run and are labeled author-arranged preflight rather than independent final acceptance.

## 6. Workflow failures and durable repairs

| Observed failure or ambiguity | Repair incorporated into the reusable workflow |
|---|---|
| A delegated practice request did not fit a human-reply-only gate description | Explicit practice delegation, exact authority quote and labeled coordinator decisions; actual reviews remain mandatory |
| Worker `python3` differed from the parent environment and lacked SciPy | Each worker verifies its own executable and imports; use an explicit verified interpreter; preserve the failed attempt |
| An adversary inspected final scores before the main run's selection receipt | Project-wide evaluation-access ledger; freeze forms/rules before exposure; no globally blind-holdout claim |
| A zero-byte unfinished handoff became visible | Publish a completed temporary file by atomic rename, then notify the recipient with the final hash; existence alone is not readiness |
| Recovery fixture selected too many files by prefix | Preserve failed T09 r01; retry in r02 using the exact development-stage file list; do not alter scientific code |
| Previously private GitHub address now resolved to a public renamed repository | Verify exact identity and visibility immediately before sync; create a separate private destination and record the change |

No recipient accepted the unfinished handoff. The recovery harness's accidental inclusion of a later-stage output caused the computation's exclusive-write guard to reject the retry correctly. These cases are useful failure evidence, not hidden or relabeled successful runs.

## 7. Verification evidence and its limits

- The repaired scientific run retained 88 exact dependencies and 35 outputs. Its 44 unittest methods include ingestion, model and repair suites, with additional mutation subcases. Tests and isolated owner reproduction passed.
- T10 used separate direct workbook parsing and independent numerical formulas rather than importing the production models. It recorded 4,776 scalar/numerical checks, 132 trace/rank checks, 155 residual-fit checks and 235 current claim-binding checks. All 17 bounded claims were accepted for the named r03 evidence. Counts are finite checks, not proofs of universal correctness.
- T09's replacement agent recovered the retained files, reingested the workbook, ran the 44 tests and reproduced all 32 deterministic output files byte-for-byte. The other three outputs match semantically except the explicitly allowed timestamps and dependent receipt digests, whose new links were checked.
- T09 executed a tampered dependency and a wrong frozen-output reference on copies. Both were rejected; valid versioned replacements succeeded. It verified 125 primary records unchanged and retained its failed first harness attempt.
- T13 independently ran 721 receipt/hash/equivalence checks and accepted the T09 recovery evidence. It did **not** claim a second execution of production, tests or negative probes.
- PDF authoring, every-page inspection and final adversarial wording review have their own exact-version receipts; their final status belongs in the delivery record, not an inferred consequence of numerical acceptance.

The data and model permit bounded historical comparisons and conditional scenarios. They do not establish causal attribution, probability coverage, reliable long-range climate forecasts, arbitrary-input correctness, security against coordinated evidence forgery, or broad concurrency/load robustness. Actual Codex role assignment and handoffs were exercised; native Claude agents/teams remain untested. No biological research was performed.

## 8. How to use the repaired workflow next time

Start with the [Execution Playbook](../../HIMCM_Agent_Working_Doc/EXECUTION_PLAYBOOK.md) and bootstrap prompt. Create a new project root and intake; do not reuse this project's gates, accepted claims or run IDs as approval for a new problem. Assign real sessions to the six logical roles and give each a task packet with owned paths, dependencies, deliverables and acceptance criteria.

After source admission and framing, freeze candidate forms, baseline, selection rule and evaluation access. Dispatch adversaries to different failure surfaces: assumptions/alternatives, validation/leakage and implementation/provenance. Require each finding to provide a counterexample, consequence, minimal repair and recheck. Have the responsible author answer the finding; a reviewer verifies the repaired version. Record “limitation disclosed” separately from “bug fixed.”

Release computation only against accepted definitions, and release final prose only against accepted numbers and bounded claims. A replacement agent must be able to recover exact retained bytes and identify current authority without relying on the previous chat. Review the actual exported PDF, including public-facing summary and article, before recording delivery. Check the remote repository's exact identity and privacy again before pushing.
