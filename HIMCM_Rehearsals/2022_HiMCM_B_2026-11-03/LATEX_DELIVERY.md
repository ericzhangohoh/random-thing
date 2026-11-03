# Current delivery: reviewed LaTeX paper

Accepted on 2026-11-04, Australia/Sydney, for the user's non-biological historical-problem rehearsal and public team sharing. This is the current paper. The earlier [delivery](DELIVERY.md) remains a record of the former ReportLab release.

## Read and edit

- [Final English PDF, 16 pages](paper/latex-r01/build-r05/manuscript-r05.pdf).
- [Editable LaTeX source](paper/latex-r01/manuscript-r05.tex) and [exact build instructions](paper/latex-r01/README-r05.md).
- [Sentence register](paper/latex-r01/sentence-register-r06.md), [revision report](LATEX_REVISION_REPORT.md) and [machine-readable acceptance](control/latex-delivery-acceptance-r01.json).
- [Reusable three-reviewer protocol](../../HIMCM_Agent_Working_Doc/SENTENCE_REVIEW_PROTOCOL.md) for future papers.

The paper uses genuine XeLaTeX, actual Times New Roman text and plot labels, matching NewTX/TeX Gyre Termes mathematical fonts, and black/gray figures. Font files are not bundled. Build in a fresh directory using an installation that supplies the documented fonts and packages. The final paper contains **zero ASCII semicolons and zero fullwidth semicolons**, satisfying the user's combined limit of three. The summary occupies page 1, conclusion page 14, nontechnical article page 15 and references/disclosure page 16.

## Exact accepted versions

| Artifact | SHA-256 |
|---|---|
| `manuscript-r05.tex` | `1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55` |
| `build-r05/manuscript-r05.pdf` | `2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac` |
| `sentence-register-r06.json` | `2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c` |

The acceptance JSON pins the author closure, all final reviewer reports and ledgers, source/PDF/register, C18 evidence and original scientific manifest. Old candidate names and their pending or rejected verdicts are retained as revision history. They are not the current release.

## Independent reviews

Four new GPT-6 Astra contexts were assigned distinct attacks. A05 examined model/evaluation assumptions. A06, A07 and A08 each reviewed the complete registered paper from their own perspective and searched for omitted text. The existing main reviewer then independently rebuilt and inspected the final PDF.

| Reviewer | Scope | Final record |
|---|---|---|
| A05 | Model choice and weighting sensitivity | [Corrected model review r02](qa/latex-attacks/model-r01/review-r02.md) |
| A06 | Argument, approach justification, precision and cadence | [Final review](qa/latex-attacks/argument-r01/revised-r03/review.md), [complete ledger](qa/latex-attacks/argument-r01/revised-r03/ledger.md) |
| A07 | Facts, numbers, citations and evidence strength | [Final review](qa/latex-attacks/evidence-r01/sentences-r03/review.md), [complete ledger](qa/latex-attacks/evidence-r01/sentences-r03/sentence-ledger.json) |
| A08 | Reader comprehension, wording and text coverage | [Final review](qa/latex-attacks/reader-r01/revised-r03/review.md), [complete ledger](qa/latex-attacks/reader-r01/revised-r03/sentence-ledger.md) |
| T16 | All-page final artifact, fonts, rebuild and review completeness | [Final review](qa/latex-pdf-review-r01/review.md), [closed handoff](handoffs/T16/independent-reviewer-r01.md) |

Each final sentence ledger covers **314 sentence/fragment records in 93 prose blocks**, with 54 additional non-sentence items inventoried. Reviewers first read all 311 records in the earlier candidate. After repair, each checked the 16 changed and three added records with their surrounding argument, retaining exact-text evidence for the other 295. Final layout-only revisions preserved all 314 texts, and each reviewer bound its full ledger to the delivered r05/r06 bytes. These are complete review chains, not a claim that every unchanged sentence was freshly reread at every layout pass.

T16 directly inspected all 16 final pages and independently completed three XeLaTeX passes in an isolated directory. Extracted text and all 16 rendered pages matched the released PDF. Its 1,785 checks passed, including all three 314-record bindings, actual fonts, monochrome pixels and punctuation. No required sentence or artifact repairs remain open.

## Scientific scope and publication

The accepted primary run, observations, equations and model selection are unchanged. C18 adds an independently checked alternative-weighting sensitivity result from existing predictions. It is explicitly post-assessment and does not select a new winner or provide fresh validation. The prior 44-test scientific suite and recovery results remain earlier evidence, not a new numerical rerun during this presentation revision. See the [revision report](LATEX_REVISION_REPORT.md) for the actual repairs and limits.

The destination is the user-selected **public** [ericzhangohoh/random-thing](https://github.com/ericzhangohoh/random-thing). The coordinator verifies a normal push, remote main and the published PDF blob before reporting synchronization. Repository history records the final release commit. Local acceptance and successful remote upload are separate checks. No private-repository guarantee is made for this explicitly public destination.

This is retrospective practice using actual Codex collaboration. Native Claude teams, live contest submission, arbitrary-input correctness, causal climate inference and century-scale forecast reliability are outside the verified scope. Biological research remains excluded.
