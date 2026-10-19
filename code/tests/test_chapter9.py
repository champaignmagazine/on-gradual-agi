import unittest

from gradual_agi import frame_one as f1


class Reconciliation(unittest.TestCase):
    def test_totals(self):
        r = f1.reconcile()
        self.assertEqual(r["confirmatory_rows"], 21)
        self.assertEqual(r["mature"], 14)
        self.assertEqual(r["right_censored"], 7)
        self.assertEqual(r["primary_signature_matrix"], 16)


class RateRatio(unittest.TestCase):
    """§9.7: 15.11 vs 11.29 per 100 project-months; rate ratio ≈ 0.75, 95% CI 0.36 to 1.57."""

    def test_printed_values(self):
        rr = f1.resistance_rate_ratio()
        self.assertEqual(round(rr.rate_a_per100, 2), 15.11)
        self.assertEqual(round(rr.rate_b_per100, 2), 11.29)
        self.assertEqual(round(rr.ratio, 2), 0.75)
        self.assertEqual((round(rr.ci95[0], 2), round(rr.ci95[1], 2)), (0.36, 1.57))

    def test_interval_includes_no_change(self):
        lo, hi = f1.resistance_rate_ratio().ci95
        self.assertLess(lo, 1)
        self.assertGreater(hi, 1)


if __name__ == "__main__":
    unittest.main()
