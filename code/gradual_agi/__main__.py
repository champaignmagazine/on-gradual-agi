"""python -m gradual_agi  — reproduce the numbers printed in Chapters 5 and 9."""
from . import cfs, frame_one


def main() -> None:
    print("Chapter 5, §5.3 worked example: G0 = 4, alpha = 1, beta = 0.5")
    g = cfs.gap_recurrence(4, 1, 0.5, 3)
    print("  G1..G3 =", ", ".join(f"{x:g}" for x in g[1:]), f"; steady state G* = {cfs.steady_state_gap(1, 0.5):g}")

    print("\nChapter 5, Table 5.1: regime by beta")
    for b in (0, 0.5, 1, 1.5, 2, 2.5):
        r = cfs.regime(b)
        label = f"Regime {r.number}" if r.number is not None else "Boundary"
        print(f"  beta = {b:<4g} {label}: {r.name}")

    s, c = cfs.annualized_two_anchor_slope(2.47, 1.71, 2.0)
    print(f"\nChapter 5, §5.8 professional Go two-anchor calibration: {100*s:.1f}% (simple) to {100*c:.1f}% (compound) per year")

    print("\nChapter 5, §5.4: logistic thresholds give an exact logistic expected active share")
    for t in (0, 5, 10, 15, 20):
        print(f"  t = {t:>2}: E[A_t] = {cfs.expected_active_share_logistic(t, 0, 1, 10, 2):.3f}")

    print("\nChapter 9, Frame One reconciliation:", frame_one.reconcile())
    rr = frame_one.resistance_rate_ratio()
    print(f"Chapter 9, §9.7 resistance episodes: {rr.rate_a_per100:.2f} vs {rr.rate_b_per100:.2f} per 100 project-months; "
          f"rate ratio {rr.ratio:.2f} (95% CI {rr.ci95[0]:.2f} to {rr.ci95[1]:.2f})")


if __name__ == "__main__":
    main()
