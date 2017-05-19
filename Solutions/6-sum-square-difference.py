"""Sum square difference:
Problem 6
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
"""
import numpy as np


def sum_sqr_diff(n):
    """Sumsqure difference of first n natural numbers."""
    x = np.arange(1, n + 1)

    return np.sum(x)**2 - np.sum(x**2)


print(sum_sqr_diff(10))
assert sum_sqr_diff(10) == 2640

print("Sum square difference of 100 = ", sum_sqr_diff(100))
