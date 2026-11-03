# Current LaTeX author candidate: r05

The primary editable source is `manuscript-r05.tex`. Its directly compiled PDF is `build-r05/manuscript-r05.pdf`. The complete bound register is `sentence-register-r06.json`, with a readable Markdown companion. It contains 314 records from 93 prose/caption/reference blocks and inventories all non-sentence tables, equations, headings and plot text. `sentence-delta-r05.json` compares the earlier independently read r02 candidate with this one by exact text identity.

Working directory: `/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/paper/latex-r01`.

## Build and fonts

The local installation must provide XeLaTeX, fontspec, NewTX math, booktabs, graphicx, array, float, caption, fancyhdr and hyperref. Actual Times New Roman regular, bold, italic and bold-italic files are referenced under `/System/Library/Fonts/Supplemental/`. No proprietary font files are bundled. Body text, headings, captions, tables and plot labels use actual Times New Roman. Mathematical symbols and operators use Times-compatible NewTX/TeX Gyre Termes fonts. `pdffonts-r05.txt` records the final embeddings.

The final candidate was compiled with this exact command three times, with separate pass logs retained under `build-r05/`:

```sh
/Library/TeX/texbin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-r05 manuscript-r05.tex
```

To reproduce without overwriting reviewed bytes, choose a fresh output directory and run three passes:

```sh
mkdir build-local-reproduction-r05
/Library/TeX/texbin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-local-reproduction-r05 manuscript-r05.tex
/Library/TeX/texbin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-local-reproduction-r05 manuscript-r05.tex
/Library/TeX/texbin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-local-reproduction-r05 manuscript-r05.tex
```

Compilation metadata can differ, so independent PDF byte identity is not promised. The manuscript reads the fixed vector figures `../../figures/latex-r01/F01-r02.pdf` through `F06-r02.pdf`. Their input and output identities are in `figure-register-r02.json`. The renderer is `../../code/visualization/latex-r01/render_figures-r02.py`, using `/Users/ericzhang/.venvs/default/bin/python3`. It displays accepted scientific outputs without fitting or recomputing scores and refuses to overwrite prior figures.

## Revisions and verification

R03 implements the consolidated independent sentence repairs. There are 16 changed old records and three added records relative to r02, with 295 records retaining exact text. All old IDs remain stable. Only the Figure 5 legend changes outside prose, from internal acceptance wording to “Fitted log-CO2 curve”. Numerical tables, equations, model selection and C18 diagnostic wording remain unchanged.

R04 adds widow control and keeps equation lead-ins with their displays. R05 keeps the conclusion together on its own page. All 314 registered texts are identical across r03, r04 and r05. Earlier sources, PDFs, logs and registers remain preserved. The current README is this revisioned file, while the earlier README remains historical evidence.

The final third-pass log has no warnings, overfull or underfull boxes, missing characters or unresolved references. The PDF has 16 pages, with summary on page 1, conclusion on page 14, article on page 15 and references/disclosure on page 16. All registered prose reconciles to actual PDF text, and the combined ASCII/fullwidth semicolon count is zero. Author visual and font checks are documented in `author-receipt-r05.json`. Independent sentence rechecks and T16 acceptance are separate.

The PDF skill marker ran exactly once for the original T15 edit operation and was not repeated for these repairs. Original ReportLab and earlier LaTeX artifacts are untouched. No installation or proprietary-font redistribution was needed.
