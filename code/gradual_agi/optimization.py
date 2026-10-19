"""Chapter 6 — Optimization: Choosing Among Trajectories.

Chapter 6 states selection rules, not numerical results. This module implements those
rules so they can be applied to a declared problem:

* Indexed Optimality: an "optimal" claim is relative to a declared subject, objective
  set, constraints, evaluator, horizon and uncertainty assumptions (§6.3.8).
* Local scalarization: a bounded actor may combine objectives with a declared rule; the
  result is optimal only for that indexed problem (§6.3.2, §6.5.1).
* Pareto nondominance (§6.5.2).
* Nash bargaining as a bounded selector, with the disagreement constraint u_i >= d_i (§6.5.3).
* Horizon dependence: rankings can reverse across horizons (§6.4.6).

The book supplies no universal scalar, no calibrated utilities and no discounting model,
and neither does this module. Any numbers passed in are the caller's declared inputs.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Mapping, Optional, Sequence, Tuple


@dataclass(frozen=True)
class Index:
    """The indices an optimality claim must declare (§6.3.8)."""
    subject: str
    objectives: Tuple[str, ...]
    constraints: str
    evaluator: str
    horizon: str
    uncertainty: str

    def missing(self) -> List[str]:
        return [k for k, v in self.__dict__.items() if v in ("", (), None)]


@dataclass
class IndexedResult:
    index: Index
    selected: Optional[str]
    rule: str
    note: str = "Optimal only for this indexed problem; not a claim of optimality for all parties or for civilization."


def dominates(a: Sequence[float], b: Sequence[float]) -> bool:
    """True if a is at least as good as b on every objective and strictly better on one (higher is better)."""
    return all(x >= y for x, y in zip(a, b)) and any(x > y for x, y in zip(a, b))


def nondominated(candidates: Mapping[str, Sequence[float]]) -> List[str]:
    """Pareto-nondominated candidate names (§6.5.2). Nondominance is not a single selection."""
    names = list(candidates)
    return [n for n in names if not any(dominates(candidates[m], candidates[n]) for m in names if m != n)]


def scalarize(candidates: Mapping[str, Sequence[float]], weights: Sequence[float], index: Index) -> IndexedResult:
    """Weighted-sum local scalarization under a declared index (§6.3.2)."""
    if index.missing():
        raise ValueError(f"undeclared indices: {index.missing()} — an optimality claim is incomplete without them")
    if len(weights) != len(index.objectives):
        raise ValueError("one weight per declared objective")
    scores = {n: sum(w * x for w, x in zip(weights, v)) for n, v in candidates.items()}
    best = max(scores, key=scores.get)
    ties = [n for n, s in scores.items() if math.isclose(s, scores[best])]
    return IndexedResult(index, best if len(ties) == 1 else None,
                         rule=f"weighted sum, weights={tuple(weights)}",
                         note="Tie: the declared rule does not select." if len(ties) > 1 else IndexedResult.note)


def nash_bargaining(feasible: Mapping[str, Sequence[float]], disagreement: Sequence[float]) -> Optional[str]:
    """Nash Bargaining Solution over a finite feasible set (§6.5.3).

    Maximizes prod_i (u_i - d_i) subject to u_i >= d_i for all i. Returns None when no
    agreement leaves every party at least as well off as disagreement. The book retains
    NBS as a bounded selector: its use presupposes validated cardinal utilities and
    disagreement points, which the present case base does not supply.
    """
    admissible = {n: u for n, u in feasible.items() if all(ui >= di for ui, di in zip(u, disagreement))}
    if not admissible:
        return None
    def product(u):
        return math.prod(ui - di for ui, di in zip(u, disagreement))
    return max(admissible, key=lambda n: product(admissible[n]))


def cumulative(path: Sequence[float], horizon: int) -> float:
    """Undiscounted cumulative value of a per-period path over the first `horizon` periods."""
    return sum(path[:horizon])


def ranking_by_horizon(paths: Mapping[str, Sequence[float]], horizons: Sequence[int]) -> Dict[int, List[str]]:
    """Rank trajectories by cumulative value at each declared horizon (§6.4.6).

    No discounting model is imposed; the book declines to add an unvalidated one.
    """
    return {h: sorted(paths, key=lambda n: cumulative(paths[n], h), reverse=True) for h in horizons}
