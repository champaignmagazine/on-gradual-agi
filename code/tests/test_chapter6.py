"""Chapter 6 rules on hypothetical inputs. The book supplies no numerical utilities; these
examples exist only to check that the rules behave as the chapter states."""
import unittest

from gradual_agi import optimization as opt

IDX = opt.Index(subject="hypothetical firm", objectives=("benefit", "safety"), constraints="budget",
                evaluator="firm board", horizon="3 years", uncertainty="point estimates")


class Nondominance(unittest.TestCase):
    def test_front(self):
        c = {"A": (3, 1), "B": (2, 2), "C": (1, 3), "D": (1, 1)}
        self.assertEqual(opt.nondominated(c), ["A", "B", "C"])   # a set, not a single choice


class IndexedOptimality(unittest.TestCase):
    def test_requires_declared_indices(self):
        bad = opt.Index("firm", ("benefit", "safety"), "budget", "", "3 years", "point")
        with self.assertRaises(ValueError):
            opt.scalarize({"A": (1, 1)}, (0.5, 0.5), bad)

    def test_weights_change_selection(self):
        c = {"A": (3, 1), "C": (1, 3)}
        self.assertEqual(opt.scalarize(c, (0.8, 0.2), IDX).selected, "A")
        self.assertEqual(opt.scalarize(c, (0.2, 0.8), IDX).selected, "C")

    def test_tie_does_not_select(self):
        self.assertIsNone(opt.scalarize({"A": (3, 1), "C": (1, 3)}, (0.5, 0.5), IDX).selected)


class NashBargaining(unittest.TestCase):
    def test_disagreement_constraint(self):
        # Without u_i >= d_i, the product of two negative gains could be selected
        f = {"X": (0, 0), "Y": (5, 4), "Z": (7, 2)}
        self.assertIsNone(opt.nash_bargaining({"X": (0, 0)}, (1, 1)))
        self.assertEqual(opt.nash_bargaining(f, (1, 1)), "Y")     # (4*3=12) > (6*1=6)


class Horizons(unittest.TestCase):
    def test_rankings_can_reverse(self):
        paths = {"fast": [5, 5, 1, 1, 1, 1], "slow": [1, 2, 4, 5, 6, 6]}
        r = opt.ranking_by_horizon(paths, [2, 6])
        self.assertEqual(r[2][0], "fast")
        self.assertEqual(r[6][0], "slow")


if __name__ == "__main__":
    unittest.main()
