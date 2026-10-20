# Code: the book's calculations

Reference implementations of the calculations in *On Gradual AGI*, Chapters 5, 6 and 9. Pure Python 3.9+ with no dependencies.

```bash
cd code
python -m gradual_agi                       # print the numbers the book reports
python -m unittest discover -s tests -v     # 28 checks against the printed values
```

To install it as a package (Python 3.9+), run `pip install ./code` from the repository root, then `python -m gradual_agi` from anywhere.

| Module | Chapter | What it implements | Checked against the book |
| --- | --- | --- | --- |
| `gradual_agi/cfs.py` | 5 Synchronization | gap, Slope, baseline recurrence `G(t+1) = α + (1 − β)G(t)`, steady state `G* = α/β`, regimes 0–5 and the marginal boundary at β = 2, the illustrative β(G) form, threshold activation share and its exact logistic expectation, gated Floor, delay decomposition, two-anchor Slope annualization | §5.3 worked example (4 → 3 → 2.5 → 2.25 → 2); Table 5.1; §5.4 logistic result; §5.8 professional Go calibration (≈15–17% per year) |
| `gradual_agi/optimization.py` | 6 Optimization | Indexed Optimality (declared indices), local scalarization, Pareto nondominance, Nash bargaining with the disagreement constraint, horizon-dependent ranking | Chapter 6 gives rules, not numbers; tests use clearly hypothetical inputs |
| `gradual_agi/frame_one.py` | 9 Empirical contact | reconciliation of the Frame One counts; resistance-episode rates and the crude Poisson rate ratio with a log-scale 95% interval | §9.1.1 and §9.3.1 counts; §9.2.1 descriptive pass; §9.5 linkage grades; §9.7: 15.11 vs 11.29 per 100 project-months, ratio 0.75 (0.36 to 1.57) |

**Limits.** These are the book's stated models, not fitted laws. The regimes follow from the stated recurrence; β(G) is an illustrative parameterization; no case in the book supplies a statistical fit. The Chapter 9 functions recompute summaries from the counts printed in the book. The Frame One case records themselves are not in this repository, so the code checks the arithmetic, not the case evidence.

Licensed under the MIT License (see `LICENSE`).
