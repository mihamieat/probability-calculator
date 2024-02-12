# -*- coding: utf-8 -*-
"""Probability calculator module."""
import copy
import random


class Hat:
    """Hat class."""

    def __init__(
        self,
        **kwargs,
    ):
        """Initialize an object with keyword arguments.

        This method initializes an object with the provided keyword arguments.
        At least one argument must be provided, otherwise a ValueError is raised.

        Args:
            **kwargs: Keyword arguments to initialize the object.

        Returns:
            None

        Raises:
            ValueError: If no keyword arguments are provided.

        """
        if not kwargs:
            raise ValueError("At least one argument must be provided.")
        self.kwargs = kwargs
        self.contents = self.content()

    def content(self):
        """Get the contents of the hat.

        Returns:
            list: A list of the balls in the hat.
        """
        return [key for key, value in self.kwargs.items() for _ in range(value)]

    def draw(self, num_balls_drawn: int = 0):
        """Draw a specified number of balls from the hat.

        Args:
            num_balls_drawn (int, optional): The number of balls to draw from the hat.\
 Defaults to 0.

        Returns:
            list: A list of the balls drawn from the hat.
        """
        contents = self.contents
        drawn = []
        if len(contents) < num_balls_drawn:
            return contents
        for _ in range(num_balls_drawn):
            random_index = random.randint(0, len(contents) - 1)
            drawn.append(contents[random_index])
            contents.pop(random_index)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Perform a probability experiment.

    This function conducts a probability experiment by drawing balls from a hat.
    It calculates the probability of satisfying the expected ball counts based on \
the provided inputs.

    Args:
        hat: The hat object.
        expected_balls: A dictionary specifying the expected balls and their counts.
        num_balls_drawn: The number of balls to draw in each experiment.
        num_experiments: The number of experiments to perform.

    Returns:
        float: The probability of satisfying the expected ball counts.

    """
    m = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        nb_expectation_satisfied = sum(
            drawn.count(color) >= count for color, count in expected_balls.items()
        )
        if nb_expectation_satisfied == len(expected_balls):
            m += 1

    return m / num_experiments
