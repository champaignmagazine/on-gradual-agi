import math
import unittest

from gradual_agi import cfs


class WorkedExample(unittest.TestCase):
    """§5.3: G0 = 4, alpha = 1, beta = 0.5 gives G1 = 3, G2 = 2.5, G3 = 2.25, approaching G* = 2."""

    def test_sequence(self):
        self.assertEqual(cfs.gap_recurrence(4, 1, 0.5, 3), [4, 3, 2.5, 2.25])

    def test_steady_state(self):
        self.assertEqual(cfs.steady_state_gap(1, 0.5), 2)
        self.assertAlmostEqual(cfs.gap_recurrence(4, 1, 0.5, 60)[-1], 2, places=12)

    def test_simulation_matches_gap_recurrence(self):
        C, F, G = cfs.simulate(10, 6, 1, 0.5, 5)
        self.assertEqual(G, cfs.gap_recurrence(4, 1, 0.5, 5))

    def test_observed_slope_equals_beta_in_baseline(self):
        # §5.2.3: under the one-period recurrence S_t and beta coincide algebraically
        C, F, _ = cfs.simulate(10, 6, 1, 0.37, 4)
        for t in range(4):
            self.assertAlmostEqual(cfs.slope(F[t], F[t + 1], C[t]), 0.37)

    def test_slope_undefined_at_zero_gap(self):
        with self.assertRaises(ZeroDivisionError):
            cfs.slope(5, 5, 5)


class Regimes(unittest.TestCase):
    def test_table_5_1(self):
        self.assertEqual(cfs.regime(0).number, 1)
        self.assertEqual(cfs.regime(0.5).number, 2)
        self.assertEqual(cfs.regime(1).number, 3)
        self.assertEqual(cfs.regime(1.5).number, 4)
        self.assertEqual(cfs.regime(3).number, 5)
        self.assertEqual(cfs.regime(0.5, threshold_crossed=False).number, 0)

    def test_beta_2_is_marginal_not_divergent(self):
        # The book corrects Series #4, which grouped beta >= 2 as divergent
        self.assertIsNone(cfs.regime(2).number)
        g = cfs.gap_recurrence(5, 1, 2, 6)
        dev = [x - cfs.steady_state_gap(1, 2) for x in g]
        self.assertTrue(all(math.isclose(abs(d), abs(dev[0])) for d in dev))

    def test_behaviour(self):
        gstar = cfs.steady_state_gap(1, 1.5)
        dev = [x - gstar for x in cfs.gap_recurrence(4, 1, 1.5, 6)]
        self.assertTrue(all(a * b < 0 for a, b in zip(dev, dev[1:])))          # alternate
        self.assertTrue(all(abs(b) < abs(a) for a, b in zip(dev, dev[1:])))    # shrink
        dev5 = [x - cfs.steady_state_gap(1, 2.5) for x in cfs.gap_recurrence(4, 1, 2.5, 6)]
        self.assertTrue(all(abs(b) > abs(a) for a, b in zip(dev5, dev5[1:])))  # grow
        g1 = cfs.gap_recurrence(4, 1, 0, 5)
        self.assertEqual(g1, [4, 5, 6, 7, 8, 9])                               # stagnation: gap grows
        self.assertTrue(all(x == 1 for x in cfs.gap_recurrence(4, 1, 1, 5)[1:]))  # parity: G = alpha

    def test_no_zero_steady_state_with_positive_alpha(self):
        # §5.5: under persistent alpha > 0, G* = 0 cannot be a steady state
        for b in (0.1, 0.5, 1.0, 1.9):
            self.assertGreater(cfs.steady_state_gap(1, b), 0)


class VariableCoupling(unittest.TestCase):
    def test_monotone_decline(self):
        vals = [cfs.beta_of_gap(g, 4, 0.6, 0.1, 1.5) for g in (4, 3, 2, 1, 0.5)]
        self.assertTrue(all(b < a for a, b in zip(vals, vals[1:])))
        self.assertAlmostEqual(cfs.beta_of_gap(4, 4, 0.6, 0.1, 1.5), 0.6)

    def test_parameter_conditions(self):
        with self.assertRaises(ValueError):
            cfs.beta_of_gap(1, 4, 0.1, 0.6, 1)   # beta_0 < beta_inf
        with self.assertRaises(ValueError):
            cfs.beta_of_gap(1, 4, 0.6, 0.1, 0)   # p must be positive

    def test_steady_state_condition(self):
        # alpha = beta(G*) G* at any fixed point of the variable-coupling recurrence
        f = lambda g: cfs.beta_of_gap(g, 4, 0.6, 0.1, 1.5)
        g = cfs.gap_path_variable_beta(4, [1.0] * 400, f)[-1]
        self.assertAlmostEqual(f(g) * g, 1.0, places=6)


class Thresholds(unittest.TestCase):
    def test_active_share(self):
        self.assertEqual(cfs.active_share(5, [1, 4, 5, 9]), 0.5)   # strict inequality C_t > H_i

    def test_expected_share_is_logistic_in_time(self):
        self.assertAlmostEqual(cfs.expected_active_share_logistic(10, 0, 1, 10, 2), 0.5)
        # timescale s / alpha: doubling alpha halves the time to the same share
        self.assertAlmostEqual(cfs.expected_active_share_logistic(5, 0, 2, 10, 2),
                               cfs.expected_active_share_logistic(10, 0, 1, 10, 2))

    def test_realized_share_approaches_expectation(self):
        h = cfs.sample_logistic_thresholds(20000, 10, 2, seed=1)
        for t in (6, 10, 14):
            self.assertAlmostEqual(cfs.active_share(t, h), cfs.expected_active_share_logistic(t, 0, 1, 10, 2), delta=0.015)

    def test_fixed_ceiling_gives_no_s_curve(self):
        # With a fixed Ceiling the active set is fixed and aggregate increments decline
        C, F, G = cfs.simulate(10, 0, 0, 0.3, 8)
        inc = [b - a for a, b in zip(F, F[1:])]
        self.assertTrue(all(b < a for a, b in zip(inc, inc[1:])))


class GatesAndDelay(unittest.TestCase):
    def test_gate(self):
        self.assertEqual(cfs.gated_floor([0.1, 0.4, 0.8, 0.9, 0.95], theta=0.75, tau=2), [0, 0, 0, 0, 1])

    def test_delay_floor_not_compressed(self):
        comp = lambda c: 10 / (1 + c)
        self.assertLess(cfs.total_delay(9, comp, 6), cfs.total_delay(1, comp, 6))
        self.assertGreaterEqual(cfs.total_delay(1e9, comp, 6), 6)


class GoCalibration(unittest.TestCase):
    def test_15_to_17_percent_per_year(self):
        # §5.8: G0 ≈ 2.47 pp, G1 ≈ 1.71 pp over about two years imply S ≈ 15-17% per year
        simple, compound = cfs.annualized_two_anchor_slope(2.47, 1.71, 2.0)
        self.assertEqual(round(100 * simple), 15)
        self.assertEqual(round(100 * compound), 17)


if __name__ == "__main__":
    unittest.main()
