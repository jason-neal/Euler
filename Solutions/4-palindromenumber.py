"""Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import numpy as np


def ispalindrome(n):
    """Test if number is palindrome."""
    str_number = str(n)
    reverse_str = ""
    for char in range(len(str_number), 0, -1):
        reverse_str += str_number[char - 1]

    if str_number == reverse_str:
        return True
    else:
        return False


assert ispalindrome(121)
assert ispalindrome(11121112111)
assert not ispalindrome(1234)

threedigits = np.arange(100, 1000)
palindrome_numbers = []
for x in threedigits:
    for y in threedigits:
        product = x * y
        if ispalindrome(product):
            palindrome_numbers.append(product)

print("Largest palindrome product of 3 digit numbers =", np.max(palindrome_numbers))
