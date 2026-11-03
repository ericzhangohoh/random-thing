# T05 computation handoff r04 — full numerical execution

Producer/session: /root/rehearsal_computation. Status: COMPLETE_FOR_ASSIGNED_EXECUTION; pending independent numerical/claim review, not scientific acceptance. Primary calculations preceded comparison with reviewer outputs.

## Accepted inputs and execution

Consumer receipt computation-r03 verifies all23 accepted-inputs-g2-r02 identities before dependent execution. Current core: framing/spec/interface r02; decision/experiment r03; assumptionsr01. Released spec/interface match preflight-tested bytes; r03 is editorial only and correctly named in metadata. Frozen supplied observations:63paired years1959–2021, annual Mauna LoaCO2 ppm/global anomaly relative1951–1980; temperature1958 retained separately. FixedC_ref315.98ppm. No live/revised/post2021 data. Original equations, splits, selector, ties and envelope formula stayed unchanged after A01global final-score exposure.

Actual command, working directory PROJECT_ROOT:

```
/Users/ericzhang/.venvs/default/bin/python3 code/experiments/run_analysis_r02.py --project-root /Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03 --run-id T05-scientific-20261103-r02
```

Exit0;2.139seconds; explicit Python3.12/packageversions retained,60second subprocesslimits and singleBLAS/OpenMPthread. Every executed SVDregression fullrank/finite. Actual order:37own tests, originalworkbook reingestion, separatedevelopment command, persistedselection12:03:52.843964UTC, separatefinal starting12:03:52.950258UTC loadingreceipt, separateproductionrefit. This proves local unchanged-rule order, not a globally unseen/blinded holdout: A01already exposed finalscores.

## Pinned evidence

All35output hashes and exact executed source are in manifest. Authoritative bytes are run-local reproduction snapshots, not mutable currentcode.

| Artifact | SHA256 |
|---|---|
| `runs/T05-scientific-20261103-r02/manifest.json` | `33beee2a51123a789d83e60ae02f22c05b73acecc69e17d02168d455110e5870` |
| `runs/T05-scientific-20261103-r02/outputs/selection_frozen.json` | `854025467691e937361aaa4b1a414881023d2911efe39f512b51d2e21ff1c636` |
| `runs/T05-scientific-20261103-r02/outputs/final_assessment_receipt.json` | `6bc7b405bb916ff55e1ce315d1c79d5d3a37f1cf0f32349e0a908ea278ea5813` |
| `runs/T05-scientific-20261103-r02/outputs/development_metrics.csv` | `631e378ca23bb831504d27278aeeceba32824ce579429e4c5a6e2fa881f86dde` |
| `runs/T05-scientific-20261103-r02/outputs/final_metrics.csv` | `d471dc4062bbda197b28fc33992c766dca8eb41a314993633d223fb651169510` |
| `runs/T05-scientific-20261103-r02/outputs/forecast_summary.csv` | `4eede8b2a3802f0af79d01b381bd5228cb8033d738228e81dc70818644602885` |
| `runs/T05-scientific-20261103-r02/outputs/thresholds.csv` | `803e6eade5fd59777f8b90cd77a8b6f19c2181d6b7d3ccf5b0301a1415cf6cec` |
| `runs/T05-scientific-20261103-r02/outputs/relationship_diagnostics.csv` | `b000ef97c31fe4099b542313658fcf75d837b03c0c3107dcbf58bca621f84695` |
| `runs/T05-scientific-20261103-r02/outputs/historical_error_envelopes.csv` | `1b3980a6a093cc436bddfb9016fa9022460f823f9e3c21d216176b0ff4f04f4c` |
| `runs/T05-scientific-20261103-r02/outputs/rank_stability.csv` | `a31653853e4dd67334c3a629388653fdb8bc5cb04093cf8b59657d8df0488c6d` |
| `runs/T05-scientific-20261103-r02/outputs/window_sensitivity.csv` | `a2de6f5e4315a0e05d88f5e1e2cbc86c145a25dfc9163fd97d02d2eda73f6195` |
| `runs/T05-scientific-20261103-r02/reproduction-check.json` | `190ecb7900efa182d74643e7418d357458acd22a5968b171f71bdea91647f8f2` |

## Computed selection and assessment

| Model | Development MAE | Final MAE | Unit |
|---|---:|---:|---|
| D | 1.481220 | 2.144500 | ppm |
| Q | 1.759031 | 1.398408 | ppm |
| E | 3.788758 | 8.241773 | ppm |
| T0 | 0.100011 | 0.124803 | °C anomaly |
| T1-D | 0.087214 | 0.093147 | °C anomaly |
| T1-Q | 0.083687 | 0.090526 | °C anomaly |
| T1-E | 0.095634 | 0.121659 | °C anomaly |

Frozen choices: D, then T1-D from eligible pairT0/T1-D. T1-Q is a better declared comparator, not retrospectively substituted. Q wins finalCO2MAE and3/5developmentorigins; D wins2/5. Omitting1986or1991 changes diagnostic pooled winner toQ. All ten finalD errors are negative,bias−2.1445ppm. Post-assessment rank summaries never feed selection. D is not uniformly most accurate.

SelectedD historical envelope contains10/10finalerrors; T1-D9/10. In2016,h5,T1-D signederror−0.2222921344°C exceeds fixedradius0.1971251779 by0.0251669564°C. The miss remains and no radius was enlarged. These dependent checks do not establish probability coverage. Future envelopes stop2031 because tenyears is the longest tested horizon, not a reliability guarantee.

## Required projections

| CO2 path | 2050ppm | 2100ppm | First annual685ppm |
|---|---:|---:|---:|
| D | 487.79 | 610.79 | 2131 |
| Q | 496.81 | 688.33 | 2100 |
| E | 466.29 | 583.70 | 2136 |

None reaches685by2050. This conditional pureCO2exercise does not test OECD’s different CO2-equivalent quantity. Everycandidate,includinglosers,has2050/2100,gaps andrawcrossing/predecessoroutputs.

Selected fullT1-D2050/2100 anomalies1.53904/2.38817°C; annual1.25/1.50/2.00°C crossings2036/2048/2076 against1951–1980. Alternatives: T0=2044/2059/2089; T1-Q=2035/2046/2067; T1-E=2043/2058/2088. These beyond2031dates are conditional, not realized/persistent/preindustrial/Paris-target dates. Actualpaths are valid and nondecreasing2021–2300; synthetic tests exercisefailurebranches.

Last30 selectedD remains unchanged underitsrecent rule. T1-D last30refit gives2050/2100=1.64488/2.59910°C andcrossings2033/2044/2068,3/4/8years earlier. This is window sensitivity,not probability or reselection. Allsevenfullpaths and only declaredselected-form last30cases are retained.

All36decade windows independently recomputed:1994–2004increase18.74ppm vs1993–2003prior max18.77; margin−0.03,rank2. Annual evidence cannot reconstructMarch or establishmeasurement significance.

Fullperiod Pearson(C,T)=.961318; Pearson(logC,T)=.960366; logR²=.922302. Linear/quadratic-detrended correlations.551057/.491659; firstdifferences.355269(n62). Doublingcontrast2.61741°C is descriptive,not causal sensitivity. T1-E is algebraicallylinear in futuretime; no uniqueCO2information, p-value, equilibrium sensitivity or policyeffect follows.

## Machine-readable output map

All names are under runs/T05-scientific-20261103-r02/outputs/. CSVs carry run/data/spec hashes; retained output_schema-r02.json defines units/grain. Consumers may format,not refit.

- development_forecasts350rows; final_forecasts70rows:origin/target/horizon/trainrange/n/actual/prediction/error/status/forecastCO2input. Corresponding metrics giveoverall/origin/horizon MAE/RMSE/bias.
- development/final/production_coefficients:allparameters,window/count,SVDrank/method,produceridentity/reference. Corresponding residual/fitdiagnostic tables retain fitvalues,mean/RMSE/lag1correlation.
- selection_frozen,final_assessment_receipt,production_receipt JSON:choices,hashes andlocal chronology.
- production_forecasts711rows:79years×(7full+2selectedlast30). threshold_search_paths2520rows:2021–2300.
- forecast_summary18rows; thresholds19rows:everyrequired2050/2100/685/temperaturethreshold,rawboundaries,validdomain/prefix,firstinvalidreason/year,monotonicity,beyondhorizon. path_diagnostics givesvalidity,decreasecounts,Qturningpoint/growth.
- ten_year_changes/comparison andrelationship_diagnostics/series support arithmetic/plots.
- historical/production_error_envelopes,development_error_samples,horizon_evidence givefixedradii,miss/excess andh1–10evidence/h1/5/10flags.
- rank_stability,comparison_ranks,window_sensitivity,structural_sensitivity preserve reversals,eligibility,originfragility andalternativepaths.
- numerical_checks andclaim_candidates JSON are authorchecks/computedcandidatefacts pendingreview.

## Checks and retention actually executed

37owntests passed beforefits:9ingestion+28model/negative/leakage/tamper checks. Includes knowncoefficients/forecasts,tenelapsedyears,missing/duplicate/future/nonpositive rejection,rankdeficiency,referenceinvariance,foldfuture-mutation invariance,forecastproducer sensitivity,nullfailedrows,final-tabletamper andr02crossingprecedence/re-entry/negative-validanomaly. Workbook reingestion reproduced admittedCSVs. Twelvepostrunchecks passed; all350development,70final and711productiondisplay rows haveOKstatus.

44dependencies were actually recovered/rehashed in a freshisolateddirectory:executedsource,original/processedinput,currentcore,release/gates/reviews,consumerreceipt,schema,config,environment/versionrecords. Separatedevelopment/final/production reran from recoveredbytes. All32numericaloutputs are byte-identical; selection matches. Three timestampedstage-receipts naturally differ in executionmetadata/hashchains; exclusions areexplicit. Python/packagebinaries are notbundled. Recoverability/determinism does not prove scientificaccuracy.

Author-arranged staticreviewer /root/rehearsal_computation/implementation_preflight identified fourpre-execution failure-contractissues. Upstreamstatus,nullpropagation,final-tablehashguard andfailure-reason repairs/tests are recorded in code/qa/preflight-review-r01.md and retained snapshots. Static before-behavior is not mislabeled a historicalrunfailure or independentacceptance.

## Independent-evidence reconciliation

Separate immutable T05-reconciliation-20261103-r01 compared619primary entries with A01/A02:decisions,developmentoverall/origin/horizonmetrics,70finalerrors/finalMAEs,2050/2100values,selectedradii/misses,leave-one-origin-out and350sharedA02predictions. Allpass; maxdifference7.958078640513122e-13. Its13dependencies were actually recovered and comparisonoutput reproduced byte-for-byte. This is author reconciliation of independent evidence,not freshacceptance. A02 exploratoryforms/through2011association andA01exploratory29yearhindcast were notadded to primaryscope.

Reconciliation manifestSHA256 `a00238c8c548d9676e3716ebd6be87823dab19dc7c0f41bd106436d05ed82534`; comparisonSHA256 `6efd95691c576d7a4e04d75e96956d816613db99db5b658baf75b91dc22acc7f`.

## Limits and next actions

No unreviewedsciencechange,sourceoriginal/closedrun/model/control/reviewer/PDF/Git edit,installation/network orbiology occurred. Earlier failedenvironment/ingestion/preflight evidence retained. No longrangeaccuracy/causality/coverage guarantee. First scientificinvocation succeeded; pre-execution repairs areseparate.

Root:pinprimary/reconciliation manifests androute independentnumerical/adversarialreview. Reviewer:recalculate decade/forecast/score/crossing and auditlocalfreeze/globalexposure,forecastCO2input,failurestatuses,narrowedclaims. Modeler:interpret rankinstability,sequentialeligibility,envelopemiss,sensitivity. Writer:use immutabletables andretain annual/March,CO2/CO2-equivalent,baseline/proxy/extrapolation distinctions in summary/body/article. Furthererror-detection/restart/invalidation exercisesrequire separateactualexecution; theircompletion andfinalPDFacceptance are notfabricated here.
