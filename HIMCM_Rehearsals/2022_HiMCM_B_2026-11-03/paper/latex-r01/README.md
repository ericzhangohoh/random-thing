# LaTeX practice report

The primary manuscript is `manuscript-r02.tex`. The sentence-review candidate is `build-r02/manuscript-r02.pdf`, compiled directly with XeLaTeX in three successful passes. `sentence-register-r03.json` binds all 311 sentence or explicitly classified fragment records to the exact source and PDF. Its Markdown companion supports reading. Every record matches normalized actual PDF text, with cross-page sentences handled explicitly. Tables, equations, headings, plot labels and document furniture are inventoried separately.

The accepted scientific run remains `T05-scientific-20261103-r03`. The 17 original claims remain bounded by `control/accepted-claims-g3-r01.json`. The additional target-year weighting paragraph, VAL06, uses only the separately accepted C18 diagnostic in `control/accepted-claims-latex-r01.json`. It does not change selection or constitute new validation.

## Fonts and compilation

Required local fonts are the installed Times New Roman regular, bold, italic and bold-italic files under `/System/Library/Fonts/Supplemental/`. The source references those files and does not distribute them. Body text, headings, captions, tables and plot labels use actual Times New Roman. Mathematical glyphs and operators use the Times-compatible NewTX/TeX Gyre Termes font families. The preamble explicitly sets math operators to NewTX's Termes family so that Latin Modern is not silently substituted. `pdffonts-r02.txt` records the actual embedded fonts.

A reproduction can be built from this directory into a new output directory, keeping reviewed bytes immutable:

```sh
mkdir build-local-reproduction
/Library/TeX/texbin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-local-reproduction manuscript-r02.tex
/Library/TeX/texbin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-local-reproduction manuscript-r02.tex
/Library/TeX/texbin/xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build-local-reproduction manuscript-r02.tex
```

No installation is required in the verified environment. PDF byte identity across independent builds is not promised because compilation metadata can differ. Numerical source identities are separately pinned.

The figures are vector PDFs under `../../figures/latex-r01/`, with matching PNGs and the accepted-table hash register `figure-register-r01.json`. Their source is `../../code/visualization/latex-r01/render_figures-r01.py`. It only displays accepted data and refuses to overwrite prior figure outputs. Use a new versioned output path if regenerating a changed figure.

## Preserved revisions and failures

The initial setup attempt used an incorrect relative path and an absent build directory, producing no PDF. `setup-failure-r00.txt` records that repair. The first actual XeLaTeX build, `build-r01/`, is retained with `manuscript-r01.tex`. Its first pass had expected unresolved references, two sub-point overfull lines, and a Latin Modern math-operator fallback. R02 adds modest emergency line stretch and explicitly sets Times-compatible math operators. The final third-pass log has no warnings, overfull or underfull boxes, missing characters or undefined references.

The first register extraction retained two explicit unmatched entries because they crossed page boundaries. `register_sentences-r02.py` and register revision r03 resolve those matches across adjacent pages after excluding headers and page numbers. Nothing was silently omitted. The PDF skill marker ran exactly once for this new edit operation, immediately before first authoring, and is recorded in `marker-receipt.txt`.

Author checks do not constitute independent sentence or PDF acceptance. Future repairs must preserve this candidate and create a new source, PDF and bound register revision.
