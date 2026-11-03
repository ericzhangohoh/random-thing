# A05 canonical corrected review handoff r02

Reviewer: `/root/latex_model_attack`. Canonical report: `qa/latex-attacks/model-r01/review-r02.md`. Original r01 remains unchanged.

**Verdict: ACCEPTED_FOR_SCOPE.** A07 independently verified the weighting diagnostic’s scores and counts. Its correction to my r01 interpretation is valid and is now incorporated: marginal horizon weights remain exactly 1/10. Origin weights change from 1/5 each to 1/4 at origins 1981 and 2001 and 1/6 at origins 1986, 1991 and 1996. Joint origin–horizon and calendar-year weights change.

I independently executed `check-marginals-r02.py` on the pinned accepted CSV using exact `Fraction` arithmetic for all three models, without importing A07 code or A05 r01 calculation code. `marginal-weights-r02.json` retains every joint weight and origin/horizon aggregate. All assertions pass. No score or original selection changes.

The r02 report replaces the inaccurate horizon-weight phrase, records the correction openly, and provides proposed adopted text with no semicolon. A07 acceptance is limited to A05-1. Root owns registration of the new C18 post-assessment diagnostic. This is neither fresh validation nor permission to reselect D, and no revised manuscript/PDF acceptance is asserted.

No new primary fits, source changes, target edits, Git, installation or PDF inspection occurred. `corrected-artifacts-r02.json` pins the report, check script/results, preserved r01, original CSV, and A07 report. Bounded correction complete.
