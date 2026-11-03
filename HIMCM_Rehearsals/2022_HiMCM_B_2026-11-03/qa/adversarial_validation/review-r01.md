# A01 adversarial temporal validation review r01

Verdict: **CHANGES_REQUESTED for the R04 claim contract; ACCEPTED_FOR_SCOPE for the frozen numerical architecture.** No demonstrated reason to change equations or silently replace the selected model. Required minimal repair: distinguish the development-selected primary rule from the model with the best final-segment score, and explicitly report that the available evidence does not identify a uniformly most accurate model. This is a clarification of the scientific answer, not new selection. Implementation and final paper remain unreviewed.

## Independence and evidence

I read the actual four-page official statement via its fulltext, dictionary, intake/state, task, all six model r01 documents, and toy script/results. I did not read prior reviewers' conclusions or primary computation forecast outputs. Independent scripts implement regressions from processed CSV, then verify every joined value against XLSX worksheet XML: 63 CO2 rows, 64 temperatures, 63 pairs, zero maximum discrepancy. No external observations used. Input/spec hashes are in development_probe_r01.json; complete review hashes are in artifact-hashes-r01.json.

Hypotheses were written in handoffs/A01/independent-reviewer-r00.md before calculations. Development calculations ran first; the selection receipt identified D and T1-D. I then explicitly evaluated 2012–2021. Those final outcomes are now consumed by this review and were reported to root. Any redesign informed by them is post-holdout. The assessment script imports the development script, which deterministically rewrites the same development receipt before assessment; this is disclosed, not an independent immutable freeze facility. No primary freeze integrity is certified here.

Commands used explicit `/Users/ericzhang/.venvs/default/bin/python3` on probe_r01.py, assessment_r01.py and source_check_r01.py. These are small independent checks, not validation of the primary implementation. Scope excludes final PDF/rendering, scientific source adjudication, and policies.

## Attack 1 — “most accurate” is defined as a development winner even after contradictory assessment

Target: framing-r01 Boundaries: “Most accurate means the predefined development winner at horizons 1–10 years, separately assessed on a final segment.” R04 asks which model is considered most accurate and why.

Strongest defense: precommitting a deterministic selector protects against final-set overfitting; M03 already says reversal narrows conclusions. This defense supports retaining D as the primary rule. It does not make D the most accurate model on every relevant observed evaluation.

Evidence: pooled development MAE D=1.48122, Q=1.75903, E=3.78876 ppm. Q wins 3 of 5 origins, including the latest two: at 1996, Q=1.09212 versus D=1.96210; at 2001, Q=.33664 versus D=2.95300. Removing either the 1986 or 1991 origin changes the pooled winner to Q. This is a diagnostic, not a new selector. Final-segment MAE reverses: Q=1.39841, D=2.14450, E=8.24177 ppm. D underpredicts all ten final observations.

Outcome: confirmed limitation of winner stability, and a narrow semantic defect in defining accuracy solely through selection. Severity P1 if propagated to summary/article; architecture remains valid. Scientific consequence: evidence supports a frozen development choice and a final-segment challenger, not stable general superiority.

Minimal repair: revise framing/decision/output contract to require “D is the predeclared pooled-development selection; Q performs better on the later assessment; no uniform winner is established.” Keep actual IDs dependent on computation confirmation. Carry origin instability and final ranking into R04 and article. Do not switch primary model using these results.

Recheck: revised wording separates selection, assessment and unknown future accuracy; primary tables reproduce reversal, and no claim calls D best across all origins or reliable for 2050/2100.

## Attack 2 — sequential CO2 selection is not temperature-optimal selection

Target: M05 chooses T0 versus the T1 pipeline driven by selected CO2, not all T1 candidates.

Strongest defense: this is an explicitly defined coherent sequential pipeline, and other temperature pipelines are retained. It is a legitimate task choice and not leakage.

Evidence: development MAE T1-Q=.0836869°C, T1-D=.0872137°C, T0=.1000108°C; final MAE T1-Q=.0905255°C, T1-D=.0931466°C, T0=.124803°C. The advantage is small and no significance is claimed.

Outcome: not an equation/selection defect. P1 only for a claim that T1-D is the empirically best of all four temperature pipelines; otherwise disclosed design limitation. Minimal repair: call it the selected sequential pipeline and show the stronger comparator. Do not enlarge candidate search retroactively. Recheck: all declared candidate scores visible and language matches eligible set.

## Attack 3 — historical envelopes do not establish a future reliability date

Target: M07 maximum-error radii and 2031 display cutoff.

Strongest defense: the specification expressly denies confidence-interval and guaranteed-coverage status, evaluates misses without resizing, and says the ten-year horizon is only historically assessed. This is scientifically honest if retained in the paper.

Evidence: D contains all 10 final years, but the errors have one sign and reach −4.07 ppm at h=10. T1-D misses h=5/2016: absolute error .222292°C exceeds B5=.197125°C. Ten temporally related containment checks are not ten independent trials. Five development origins produce 50 pairs but only 30 distinct target years. B_h also pools j<=h, so radii are not calibrated horizon-specific quantiles.

Outcome: no defect in the defined descriptive envelope. Confirmed counterexample to interpreting it as a bound on annual outcomes. Severity P1 only if “reliable through 2031,” “100% coverage,” or “90% interval” appears without the required distinction. Minimal repair: display observed misses, call bands historical error references, and say 2031 is a tested-horizon cutoff, not a validated end date. No radius tuning using final misses. Recheck: miss is retained and the narrative denies inferred future probability.

## Attack 4 — short-horizon selection cannot justify 2050/2100 accuracy

Target: whether R03/R07 distant numerical values are supported as predictions.

Strongest defense: all three forms are required by the problem and explicitly framed as conditional extrapolations. Data cannot supply a 79-year test with adequate training, and a missing physics model is not a license to invent inputs.

Evidence: 2021 fits give D/Q/E values at 2100 of 610.79/688.33/583.70 ppm, and T1-D/T1-Q/T1-E of 2.388/2.839/2.217°C. A single exploratory pre-2012 29-year hindcast from 1981 to 2010 gives D/Q/E absolute errors 9.96/15.09/17.67 ppm; the linked-temperature ranking differs. This point is deliberately NOT a new validation design or selection criterion. It demonstrates how little distant evidence is available, not a robust long-horizon winner.

Outcome: disclosed limitation, not demonstrated architecture failure. No validated reliability date beyond (or even throughout) the ten-year window exists. Required minimal action is preserve conditional language beside every distant number; adding an elaborate model or broad search is not warranted by this attack. Recheck final paper, especially summary and article.

## Attack 5 — realized future CO2 or normalization leaks into temperature scores

Target: M00/M03/M05 availability constraints.

Strongest defense: fixed 1959 origin/reference, training-local OLS, and forecast rather than actual future CO2 explicitly prevent this.

Evidence: independent predictions at origin 1981 are exactly unchanged after multiplying all later CO2 by three and adding 99°C to later temperatures. This checks our equation-level implementation only. It does not verify the production implementation or freeze file ordering.

Outcome: no specification-level leakage found. Implementation certification remains INSUFFICIENT_EVIDENCE pending code/run review. Recheck author code with its required fixture mutation and frozen-receipt tests; no scientific redesign necessary.

## Coverage and repair boundary

All five major attack families evaluated against six model documents and independent calculations. Only Attack 1 requests a normative clarification to the present wording. Attacks 2–4 constrain conclusions using concrete evidence, but most defenses already exist in r01. Attack 5 is a specification-level pass and an explicit implementation-review gap. Primary outputs, final charts/PDF and empirical source interpretations are not certified. No edits made to authors' model/code/data/control/paper. No fabricated defect count or probability-of-correctness claim.
