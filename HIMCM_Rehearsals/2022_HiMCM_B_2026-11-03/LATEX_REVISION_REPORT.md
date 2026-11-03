# LaTeX revision and sentence-level attack report

This revision implements the user's request for an English academic paper in LaTeX and Times New Roman, monochrome presentation, natural sentence variation, additional independent attackers and at most three semicolons in the whole paper. The [current delivery](LATEX_DELIVERY.md) identifies the final artifact. The [original rehearsal report](REHEARSAL_REPORT.md) retains the earlier modeling, computation and recovery history.

## Execution and handoffs

The coordinator froze the accepted scientific inputs and assigned T15 the manuscript and figure paths. Four new GPT-6 Astra contexts received separate attack scopes and disjoint QA paths. Reviewers did not edit the paper. A05 challenged the approach, while A06, A07 and A08 inspected every registered sentence independently for argument, evidence and readability. They also inspected the actual text to find omissions from the register.

The writer released an exact source/PDF/register packet. The coordinator consolidated findings into [six required repairs](control/latex-repair-r01.md), preserving optional suggestions and the source of each objection. The writer produced new versions without overwriting the rejected candidates. Each sentence reviewer checked changed wording and nearby reasoning, kept individual judgments for unchanged exact text, and returned a complete final-version ledger. T16 consumed the closed writer handoff and all three closed sentence reviews before independently inspecting and rebuilding the final artifact. The coordinator then checked integration and publication.

| Task | Producer | Recipient | Concrete handoff |
|---|---|---|---|
| T15 | Writer | Three sentence reviewers and T16 | [Closed source/PDF/register repair packet](handoffs/T15/writer-visuals-r02.md) |
| A05 | Model attacker | Coordinator, writer and A07 | [Corrected model attack](handoffs/A05/independent-reviewer-r02.md) |
| A06 | Argument reviewer | Coordinator and T16 | [Final argument handoff](handoffs/A06/argument-r04.md) |
| A07 | Evidence reviewer | Coordinator and T16 | [Final evidence handoff](handoffs/A07/sentences-r03-final.md) |
| A08 | Reader reviewer | Coordinator and T16 | [Final reader handoff](handoffs/A08/reader-r03-final.md) |
| T16 | Main artifact reviewer | Coordinator | [All-page and independent-build acceptance](handoffs/T16/independent-reviewer-r01.md) |

## What the attacks changed

The six required repairs addressed substantive precision as well as style:

1. Restored the qualification that retrospective tests truncate one supplied workbook by observation year. They do not reconstruct historical data releases. Related availability phrases now say exactly what was known from that supplied vintage.
2. Replaced an unsupported saturation-parameter identification assertion with the narrower absence of an established physically justified capacity. No unperformed identification study is implied.
3. Rewrote awkward summary language about association in observed levels.
4. Replaced internal selection-receipt terminology with ordinary language about when final-period scores had been examined.
5. Explained threshold cases directly, including paths already above the threshold at the origin and valid paths without a crossing by the cutoff.
6. Clarified that reported dates are threshold crossings on conditional annual paths, preserving their limits in the nontechnical article.

Optional refinements separated the 2016 envelope miss from the 2031 display cutoff, distinguished a prespecified selection rule from its eventual winner, clarified sequential model selection, removed internal acceptance jargon and connected detrending claims to their supporting table. Figure 5's legend was clarified. No observation or result was changed for stylistic effect. Sentence length and paragraph movement now follow the argument, without fabricated mistakes or concealed AI use.

Relative to the first fully reviewed LaTeX candidate, 16 existing records changed, three were added and 295 retained exact text. R04 fixed a stranded equation lead-in and a two-word paragraph tail. R05 kept the conclusion together. All 314 registered texts are identical across r03, r04 and r05. Earlier versions remain available for inspection.

## Approach challenge: weighting matters

A05 found that the existing development forecasts support a useful sensitivity test. There are 50 origin/horizon tasks for each candidate but only 30 distinct target years. Twenty target years appear twice. Giving every target year equal total weight therefore asks a different comparison question from giving every forecast task equal weight.

| Development aggregation | D MAE (ppm) | Q MAE (ppm) | E MAE (ppm) |
|---|---:|---:|---:|
| Original equal forecast-task weights | 1.4812200000 | 1.7590314104 | 3.7887582225 |
| Mean absolute error within each target year, then mean over 30 years | 1.6103500000 | 1.5228424486 | 3.9444846702 |

A07 recomputed the errors from predicted and observed values using independent Decimal arithmetic. The alternate aggregation favors Q. It changes the origin weighting, while each horizon's marginal weight remains one tenth. A05's first review used a loose horizon-weight description, which A07 caught and A05 corrected in a new canonical r02 report. The earlier report remains part of the audit trail.

The [accepted C18 record](control/accepted-claims-latex-r01.json) adds this as post-assessment sensitivity. D remains the original selected concentration model and T1-D the sequential temperature model. The diagnostic neither creates an untouched test nor justifies selecting again after seeing later-period results. The paper explains why the original forecast-task criterion matches its chosen evaluation unit, while exposing the dependence on that choice.

## Verified final artifact

The final paper has 16 pages, actual Times New Roman text and plot labels, compatible NewTX/TeX Gyre Termes mathematics and monochrome figures. The combined ASCII/fullwidth semicolon count is zero in both source and PDF. All 314 records reconcile to the actual PDF. Headings, equations, tables and labels are separately inventoried rather than silently excluded from coverage.

The three complete final ledgers contain 942 individual record bindings, with sentence-specific rationales and no required repairs left open. T16 read all 16 final pages and independently rebuilt the source through three clean XeLaTeX passes. The rebuilt extracted text and all rendered page hashes match the released PDF. Its 1,785 checks passed. The earlier scientific outputs were rehashed unchanged, while the original numerical tests were not rerun for this revision.

## Reuse and limits

The [sentence-review protocol](../../HIMCM_Agent_Working_Doc/SENTENCE_REVIEW_PROTOCOL.md) turns this execution into repeatable task prompts, handoff contracts and release checks. Three review roles require three independently authored review chains. Renaming an existing context does not create a new independent agent, and a coverage script does not prove that an agent read the paper.

Acceptance applies to the pinned artifacts and finite checks. It does not establish that three agreeing reviewers make a claim true, that long-range extrapolations are reliable, or that native Claude teams have been exercised. The earlier scientific and evaluation limitations remain explicit. No biological papers were researched.
