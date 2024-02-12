# -*- coding: utf-8 -*-
"""Main module."""
# This entrypoint file to be used in development. Start by reading README.md
from src.probability_calculator import prob_calculator

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
PROBABILITY = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000,
)
print("Probability:", PROBABILITY)
