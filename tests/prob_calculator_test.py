# -*- coding: utf-8 -*-
"""Test module."""
import unittest
from src.probability_calculator import prob_calculator

prob_calculator.random.seed(95)


class UnitTests(unittest.TestCase):
    """Test module."""

    maxDiff = None

    def test_hat_class_contents(self):
        """Test the contents of the Hat class.

        This test verifies that the Hat object is created with the correct contents.

        Args:
            self: The test case object.

        Returns:
            None

        """
        hat = prob_calculator.Hat(red=3, blue=2)
        actual = hat.contents
        expected = ["red", "red", "red", "blue", "blue"]
        self.assertEqual(
            actual, expected, "Expected creation of hat object to add correct contents."
        )

    def test_hat_draw(self):
        """Test the draw method of the Hat class.

        This test verifies that the draw method returns the expected number of random items from\
 the hat cont\
ents.
        It also checks that the number of items in the hat contents is reduced after the draw.

        Args:
            self: The test case object.

        Returns:
            None

        """
        hat = prob_calculator.Hat(red=5, blue=2)
        actual = hat.draw(2)
        expected = ["blue", "red"]
        self.assertEqual(
            actual,
            expected,
            "Expected hat draw to return two random items from hat contents.",
        )
        actual = len(hat.contents)
        expected = 5
        self.assertEqual(
            actual, expected, "Expected hat draw to reduce number of items in contents."
        )

    def test_prob_experiment(self):
        """Test the experiment function.

        This test verifies that the experiment function returns the expected probability based on\
 the provided inputs.
        It checks the probability for different scenarios and compares it to the expected values.

        Args:
            self: The test case object.

        Returns:
            None

        """
        hat = prob_calculator.Hat(blue=3, red=2, green=6)
        probability = prob_calculator.experiment(
            hat=hat,
            expected_balls={"blue": 2, "green": 1},
            num_balls_drawn=4,
            num_experiments=1000,
        )
        actual = probability
        expected = 0.272
        self.assertAlmostEqual(
            actual,
            expected,
            delta=0.01,
            msg="Expected experiment method to return a different probability.",
        )
        hat = prob_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
        probability = prob_calculator.experiment(
            hat=hat,
            expected_balls={"yellow": 2, "blue": 3, "test": 1},
            num_balls_drawn=20,
            num_experiments=100,
        )
        actual = probability
        expected = 1.0
        self.assertAlmostEqual(
            actual,
            expected,
            delta=0.01,
            msg="Expected experiment method to return a different probability.",
        )


if __name__ == "__main__":
    unittest.main()
