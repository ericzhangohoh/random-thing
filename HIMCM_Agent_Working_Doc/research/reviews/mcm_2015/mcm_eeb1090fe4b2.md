# Full review: 2015 Problem D, Team 38727 — A sustainability profile for Bhutan

- Source ID: `mcm_eeb1090fe4b2`
- Source: `MCM-ICM-master/2015美赛特等奖/D-38727-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pp.1–19, including both reference pages. Printed page numbers are one below physical page numbers.
- Visual supplement: physical pp.3–9 and 13–16 inspected for all index definitions, threshold rules, radar diagrams and before/after parameter tables.
- Numeric reproduction: **NOT_REPRODUCED**. No source-data reconstruction or country-index calculation was executed. Static formula checks below concern the printed specification.
- Award provenance: explicit Outstanding filename label; not independently verified here.
- Original problem: the [official three-page statement](../../sources/2015_ICM_Problem_D.pdf) was read in full.

## Architecture and decision purpose

The paper defines sustainability through six kinds of instability: institutional, environmental, political, social, economic and disaster susceptibility. It retains these dimensions as a profile rather than compressing everything into one total. A country crossing a proposed threshold in any dimension is flagged as unsustainable; remaining below the thresholds is explicitly not sufficient proof of sustainability (pp.2–3).

This architecture helps a decision maker locate the area requiring attention. It also avoids complete compensation: a favorable economic score does not automatically cancel a severe environmental problem. The threshold of five and the choice of dimensions remain modeling judgments, however. A useful workflow should ask what decision follows from each threshold and how that threshold is justified.

Eight countries are used to illustrate differences between profiles. Bhutan is then selected using historical LDC status, data completeness and perceived implementation feasibility (pp.7–8). These are the authors' 2015 case-selection conditions, not current country facts. The exercise demonstrates possible use of the dashboard; it does not validate universal applicability or predictive performance.

## Strong practice: expose the chain from diagnosis to a specific intervention

The report moves from diagnosed weaknesses to education, transport, sanitation, building standards and economic-development initiatives (pp.9–13). The education proposal names a women's university, four study areas, financing arrangements and service obligations. The transport proposal identifies a main road, bridge and winter-access work. The sanitation proposal distinguishes finance, public-health behavior and new-building standards.

These details make a recommendation more inspectable than a list of generic development priorities. They expose implementation questions: who would act, what would be built or changed, what workforce is needed, and which measured outcomes might respond. The report also recognizes spillovers across sectors and the influence of neighboring countries on environmental conditions. A local decision need not control every quantity used to evaluate its eventual performance.

## Measurement specification needs repair before reuse

Visual inspection confirms that several apparent issues are in the displayed formulas, not merely extraction errors:

- The institutional index adds six terms but divides by five. Its terms mix percentages, normalized ratios and an education category ranging from one to five, although the prose states equal initial weights. The transformation to the advertised zero-to-ten scale is not specified (pp.3–4).
- Some inversions are written as one minus a percentage or index, followed by division by 100 elsewhere. The units and order of operations must be resolved from actual input data. The later tables mix fractional entries such as 0.658 with percentage headings (pp.13–14).
- The political index multiplies three components and divides by three. This is not their arithmetic mean. Multiplication introduces interactions and a zero-component veto that require explicit justification. In the displayed youth term, increasing the variable defined as male youth unemployment decreases the index, so the intended direction needs reconciliation (pp.4–5).
- The social index adds a positively signed happiness estimate despite interpreting larger index values as greater instability. The refugee-category rule starts with `2 >= log(mu)`, which overlaps subsequent cases. Since `mu` is defined as a country share divided by the maximum share, its log is nonpositive for positive inputs in the reference set. This definition cannot be used as an unambiguous classification without repair (p.5).
- The schooling bins leave exact cut points such as 11.7 undefined. A normalized remittance ratio is divided by 100 again in the economic index (pp.4, 6). A data dictionary and tiny boundary examples would reveal such differences before a country-level result is interpreted.

The diagrams, tables and narrative also need a common numerical source. For example, the institutional value stated in the Bhutan discussion does not appear at the same magnitude in the corresponding radar chart, and the risk parameter table is not transparently reconciled with the plotted axis (pp.9, 15–16). This review does not infer an unavailable spreadsheet's actual formulas. It records that the printed method is insufficient to reproduce the displayed results unambiguously.

## Twenty-year assessment is a conditional scenario

The authors specify future parameter values with short rationales, hold all unmentioned values constant, and recalculate the sustainability profile (pp.13–16). The tables are helpful because they expose which assumptions create the result. They also acknowledge adverse changes, including greater inequality and worse air-quality conditions, instead of assuming every indicator improves.

The numbers are scenario assumptions, however, rather than outputs of an estimated intervention-response model. For instance, the claimed future improvements in sanitation and infant mortality are motivated verbally, but no expenditure-to-coverage, coverage-to-outcome or time-to-effect calculation is supplied. Calling the recalculated profile a prediction would overstate the evidence. A defensible statement is conditional: *if these specified parameter changes occur, this index calculation produces the following profile*, after repairing its definitions.

The report does not provide a quantified budget, alternatives with comparable costs, an implementation schedule or a no-plan twenty-year counterfactual. Consequently it cannot establish cost-effectiveness or attribute all assumed future improvement to the proposed package. A current-versus-future comparison includes background trends as well as potential intervention effects.

## Validation and limitations

The authors discuss missing data, weighting, threshold selection and cross-border effects, and identify several of these as future work (pp.16–17). This is useful recognition of the index's boundaries. The claims of robustness and low sensitivity are not accompanied by numerical perturbation experiments, threshold-crossing analysis or independent benchmark tests.

The assertion that using a small set of indicators makes the measure resistant to manipulation is not demonstrated. Improving an indicator is not necessarily equivalent to improving the broader condition it is intended to represent. The review should therefore distinguish genuine outcome improvement, measurement changes and optimization of a proxy.

References are present on pp.18–19, but some entries are incomplete or point to unrelated-looking domains. The data agent must check the actual endpoint, definition, date and scale rather than accepting a plausible organization name as sufficient provenance.

## Transferable operating rules

1. Preserve a decision-relevant profile when aggregation would hide unacceptable weaknesses.
2. Justify thresholds independently of how attractive a radar chart looks.
3. Give every indicator a direction, unit, range, reference population and missing-data rule.
4. Check category boundaries, zero inputs, maximum inputs and one-variable changes before building a composite score.
5. Map a diagnosis to a concrete action, implementation capacity, cost and causal response.
6. Label assumed future values as scenarios until supported by a predictive or causal model.
7. Compare a proposed plan with a future no-plan counterfactual under the same outside conditions.
8. Generate tables, figures and narrative numbers from the same accepted result artifact.

## Reading ledger

- Physical pp.1–10: summary, definitions, complete index formulas, comparison countries, Bhutan selection and diagnosis read in full.
- Physical pp.11–15: intervention details and every current/future parameter table read in full.
- Physical pp.16–19: projected-profile discussion, strengths, limitations and references read in full.
- All material formula pages, tables and radar figures were inspected visually. No numerical reproduction is claimed.
