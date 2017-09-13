"""Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import numpy as np


def smallest_multiple(n):
    """Smallest multiple of numbers 1 thru n."""
    numbers = np.arange(n) + 1
    num = n

    while True:
        if np.all(num % numbers):
            return num
        else:
            num += 1


assert smallest_multiple(10) == 2520

prob_num = 20
sm = smallest_multiple(prob_num)
print("Smallest multiple of 1 thru {} = {}".format(prob_num, sm))
