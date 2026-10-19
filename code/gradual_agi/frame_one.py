"""Chapter 9 — Participation: What Survives Empirical Contact (Frame One).

Recomputes the summary arithmetic Chapter 9 reports from the counts and exposures
printed in the book. The underlying case records (Packet A / Packet B) are not part of
this repository; these functions check the reported totals and the stated rate-ratio
interval, not the case evidence itself.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Tuple

# ---------------------------------------------------------------------------
# Counts as printed in §9.1.1, §9.3.1, §9.2.1, §9.4 and §9.5
# ---------------------------------------------------------------------------

FRAME_ONE_PROJECTS = 49
PILOT_CASES = 10
CONFIRMATORY_ROWS = 21

MATURE = {"Present": 11, "SearchedNotFound": 2, "Unknown": 1}            # 14 mature cases
RIGHT_CENSORED = {"Present": ("F1-021", "F1-033", "F1-038", "F1-039", "F1-047"),
                  "Unknown": ("F1-031", "F1-035")}                         # 7 right-censored cases

AI_RELEVANCE = {"explicit_project_side": 20, "contextual_moderate_confidence": 1}

# Secondary descriptive pass over the 16 primary acts (§9.2.1)
MANIFESTNESS = {"Explicit": 16, "Implicit": 0}
MATERIALITY = {"Intangible": 10, "Mixed": 5, "Tangible": 1}

# Primary-signature Act Forms (§9.4): 13 of 16 are M5 Contestatory / Claim-making
M5_PRIMARY = 13

# Strongest case-level linkage among the 11 mature consequence-assessable Present cases (§9.5)
LINKAGE = {"L4": 0, "L3": 6, "L2": 3, "L1": 0, "L0": 2}

# Mature cases with RealizationLevel = Present (§9.6): one direct-authority comparator, two non-veto
REALIZATION_PRESENT = {"direct_authority": ("F1-044",), "non_veto": ("F1-025", "F1-048")}

# Broad-resistance episodes (§9.7)
EPISODES = {"pre2026": (23, 152.18), "2026_through_Aug28": (10, 88.61)}   # (events, project-months)


def reconcile() -> Dict[str, int]:
    """Check that the reported Frame One totals are internally consistent. Raises AssertionError if not."""
    mature = sum(MATURE.values())
    censored = sum(len(v) for v in RIGHT_CENSORED.values())
    present_matrix = MATURE["Present"] + len(RIGHT_CENSORED["Present"])
    assert mature == 14, mature
    assert censored == 7, censored
    assert mature + censored == CONFIRMATORY_ROWS
    assert present_matrix == 16, present_matrix
    assert sum(AI_RELEVANCE.values()) == CONFIRMATORY_ROWS
    assert sum(MANIFESTNESS.values()) == present_matrix
    assert sum(MATERIALITY.values()) == present_matrix
    assert M5_PRIMARY <= present_matrix
    assert sum(LINKAGE.values()) == MATURE["Present"]
    assert sum(len(v) for v in REALIZATION_PRESENT.values()) == 3
    return {"confirmatory_rows": CONFIRMATORY_ROWS, "mature": mature, "right_censored": censored,
            "primary_signature_matrix": present_matrix, "outcome_level_cases": mature}


# ---------------------------------------------------------------------------
# Rates and the crude rate ratio (§9.7)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class RateRatio:
    rate_a_per100: float
    rate_b_per100: float
    ratio: float
    ci95: Tuple[float, float]


def rate_per_100(events: int, exposure: float) -> float:
    return 100.0 * events / exposure


def poisson_rate_ratio(events_b: int, exposure_b: float, events_a: int, exposure_a: float, z: float = 1.959964) -> RateRatio:
    """Crude rate ratio (b / a) with a Wald interval on the log scale.

    Assumes independent Poisson counts: SE(log RR) = sqrt(1/events_a + 1/events_b).
    As the book notes, this ignores multiple episodes within projects and heterogeneous
    rates across projects.
    """
    ra, rb = events_a / exposure_a, events_b / exposure_b
    rr = rb / ra
    se = math.sqrt(1.0 / events_a + 1.0 / events_b)
    lo, hi = math.exp(math.log(rr) - z * se), math.exp(math.log(rr) + z * se)
    return RateRatio(100 * ra, 100 * rb, rr, (lo, hi))


def resistance_rate_ratio() -> RateRatio:
    """The §9.7 comparison: 2026 through August 28 versus pre-2026."""
    (ea, xa), (eb, xb) = EPISODES["pre2026"], EPISODES["2026_through_Aug28"]
    return poisson_rate_ratio(eb, xb, ea, xa)
