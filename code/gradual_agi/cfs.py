"""Chapter 5 — Synchronization: Ceiling, Floor, and Slope (CFS).

Implements the chapter's baseline objects exactly as stated in the book:

* gap            G_t = C_t - F_t                                   (§5.2)
* Slope          S_t = (F_{t+1} - F_t) / (C_t - F_t)               (§5.2.3)
* recurrence     C_{t+1} = C_t + alpha,  F_{t+1} = F_t + beta*G_t
                 =>  G_{t+1} = alpha + (1 - beta) G_t               (§5.3)
* steady state   G* = alpha / beta  (alpha > 0, beta != 0)          (§5.3)
* regimes 0-5 and the marginal boundary at beta = 2                (§5.7, Table 5.1)
* gap-dependent coupling (illustrative candidate form only)
                 beta(G) = beta_inf + (beta_0 - beta_inf)(G/G_0)^p  (§5.5)
* threshold activation share
                 A_t = (1/N) sum_i 1[C_t > H_i]                     (§5.4)
  and its expected value under logistic thresholds, an exact logistic curve in time
* gated Floor    F_t^gate = 1[F_{t-tau}^cont >= theta]              (§5.6)
* delay          tau = tau_compress(C_t) + tau_floor                 (§5.6)

These are the book's stated models, not fitted laws. The book is explicit that the
regimes are consequences of the stated recurrence, that beta(G) is an illustrative
parameterization, and that no case supplies a statistical fit.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import Callable, Iterable, List, Optional, Sequence


# ---------------------------------------------------------------------------
# Core quantities
# ---------------------------------------------------------------------------

def gap(ceiling: float, floor: float) -> float:
    """Operational within-domain synchronization gap G_t = C_t - F_t."""
    return ceiling - floor


def slope(floor_t: float, floor_next: float, ceiling_t: float) -> float:
    """Observed Slope S_t = (F_{t+1} - F_t) / (C_t - F_t).

    Raises ZeroDivisionError at a zero gap, where the book notes the ratio is undefined.
    """
    g = ceiling_t - floor_t
    if g == 0:
        raise ZeroDivisionError("Slope is undefined at a zero gap (§5.7, Regime 0 note)")
    return (floor_next - floor_t) / g


def gap_recurrence(g0: float, alpha: float, beta: float, periods: int) -> List[float]:
    """Iterate G_{t+1} = alpha + (1 - beta) G_t; returns [G_0, ..., G_periods]."""
    out = [float(g0)]
    for _ in range(periods):
        out.append(alpha + (1.0 - beta) * out[-1])
    return out


def simulate(c0: float, f0: float, alpha: float, beta: float, periods: int):
    """Simulate Ceiling and Floor paths under the baseline recurrence.

    Returns (C, F, G) lists of length periods + 1.
    """
    C, F = [float(c0)], [float(f0)]
    for _ in range(periods):
        g = C[-1] - F[-1]
        F.append(F[-1] + beta * g)
        C.append(C[-1] + alpha)
    G = [c - f for c, f in zip(C, F)]
    return C, F, G


def steady_state_gap(alpha: float, beta: float) -> float:
    """G* = alpha / beta for positive alpha and nonzero beta (§5.3).

    A fixed point exists for beta != 0, but it is approached only when |1 - beta| < 1,
    that is 0 < beta < 2; see `regime`.
    """
    if beta == 0:
        raise ValueError("no steady-state gap without coupling (beta = 0)")
    return alpha / beta


# ---------------------------------------------------------------------------
# Regimes (Table 5.1 and the beta = 2 correction)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Regime:
    number: Optional[int]          # None for the marginal boundary at beta = 2
    name: str
    behavior: str


REGIMES = {
    0: Regime(0, "Pre-threshold", "coupling not yet activated; observed Slope is zero while the gap is nonzero"),
    1: Regime(1, "Stagnation", "beta = 0 after the gate is open; the gap grows as the Ceiling advances"),
    2: Regime(2, "Lagging convergence", "0 < beta < 1; the Floor rises while remaining behind the Ceiling"),
    3: Regime(3, "Steady-state parity", "beta = 1; each period's existing gap is closed before the next Ceiling increment"),
    4: Regime(4, "Overtrust, damped", "1 < beta < 2; gap deviations alternate and shrink around the fixed point"),
    5: Regime(5, "Overtrust, runaway", "beta > 2; gap deviations alternate and grow"),
}
MARGINAL = Regime(None, "Marginal boundary", "beta = 2; coefficient 1 - beta = -1, constant-amplitude oscillation")


def regime(beta: float, threshold_crossed: bool = True) -> Regime:
    """Classify the baseline recurrence by its coupling parameter.

    Regime 0 and Regime 1 cannot be told apart from the adoption trajectory alone;
    the caller must supply independent evidence of threshold crossing.
    """
    if not threshold_crossed:
        return REGIMES[0]
    if beta < 0:
        raise ValueError("the baseline regimes are defined for beta >= 0")
    if beta == 0:
        return REGIMES[1]
    if beta < 1:
        return REGIMES[2]
    if beta == 1:
        return REGIMES[3]
    if beta < 2:
        return REGIMES[4]
    if beta == 2:
        return MARGINAL
    return REGIMES[5]


# ---------------------------------------------------------------------------
# Gap-dependent coupling (illustrative candidate form, §5.5)
# ---------------------------------------------------------------------------

def beta_of_gap(g: float, g0: float, beta0: float, beta_inf: float, p: float) -> float:
    """beta(G) = beta_inf + (beta_0 - beta_inf) (G / G_0)^p.

    Monotone decline as G shrinks requires p > 0 and beta_0 >= beta_inf >= 0.
    The book treats this as an illustrative candidate parameterization, not an identified law.
    """
    if not (p > 0 and beta0 >= beta_inf >= 0):
        raise ValueError("require p > 0 and beta_0 >= beta_inf >= 0")
    return beta_inf + (beta0 - beta_inf) * (g / g0) ** p


def gap_path_variable_beta(g0: float, alphas: Sequence[float], beta_fn: Callable[[float], float]) -> List[float]:
    """Iterate G_{t+1} = alpha_t + (1 - beta(G_t)) G_t with a time-varying Ceiling increment."""
    out = [float(g0)]
    for a in alphas:
        g = out[-1]
        out.append(a + (1.0 - beta_fn(g)) * g)
    return out


# ---------------------------------------------------------------------------
# Threshold heterogeneity (§5.4)
# ---------------------------------------------------------------------------

def active_share(ceiling: float, thresholds: Iterable[float]) -> float:
    """A_t = (1/N) sum_i 1[C_t > H_i]."""
    h = list(thresholds)
    return sum(1 for x in h if ceiling > x) / len(h)


def expected_active_share_logistic(t: float, c0: float, alpha: float, m: float, s: float) -> float:
    """E[A_t] = 1 / (1 + exp(-(C_0 + alpha t - m) / s)) for logistic(m, s) thresholds and C_t = C_0 + alpha t.

    An exact logistic curve in time with timescale s / alpha.
    """
    if s <= 0:
        raise ValueError("scale s must be positive")
    return 1.0 / (1.0 + math.exp(-((c0 + alpha * t) - m) / s))


def sample_logistic_thresholds(n: int, m: float, s: float, seed: int = 0) -> List[float]:
    """Draw n independent logistic(m, s) thresholds (inverse-CDF sampling)."""
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        u = rng.random()
        while u in (0.0, 1.0):
            u = rng.random()
        out.append(m + s * math.log(u / (1.0 - u)))
    return out


# ---------------------------------------------------------------------------
# Gates and delay (§5.6)
# ---------------------------------------------------------------------------

def gated_floor(f_cont: Sequence[float], theta: float, tau: int) -> List[int]:
    """F_t^gate = 1[F_{t-tau}^cont >= theta]; periods before tau are 0 (gate not yet observable)."""
    return [0 if t - tau < 0 else int(f_cont[t - tau] >= theta) for t in range(len(f_cont))]


def total_delay(ceiling: float, tau_compress: Callable[[float], float], tau_floor: float) -> float:
    """tau = tau_compress(C_t) + tau_floor, with tau_compress non-increasing in C_t."""
    return tau_compress(ceiling) + tau_floor


# ---------------------------------------------------------------------------
# Two-anchor Slope calibration (§5.8, professional Go)
# ---------------------------------------------------------------------------

def annualized_two_anchor_slope(g0: float, g1: float, years: float):
    """Annualize gap closure between two same-metric anchors.

    With only two anchors the result is a provisional point estimate, not a confidence
    interval or a fit. Returns (simple, compound):
      simple   = ((G_0 - G_1) / G_0) / years
      compound = 1 - (G_1 / G_0) ** (1 / years)
    The two conventions bracket the book's "about 15-17% per year".
    """
    simple = ((g0 - g1) / g0) / years
    compound = 1.0 - (g1 / g0) ** (1.0 / years)
    return simple, compound
