""" Largerst Prime Factor.
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import numpy as np


def factors(n):
    """Find all factors of n."""
    numbers = np.arange(1, np.sqrt(n) + 1)
    factor_mask = n % numbers == 0
    factors = list(numbers[factor_mask])
    for fact in factors:
        factors.append(n / fact)
#    print(factors)
    return factors


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def prime_factors(n):
    """Find all prime factors of n."""
    all_factors = factors(n)
    prime_factors = []
    for fact in all_factors:
        if isprime(fact):
            print("{} is prime".format(fact))
            prime_factors.append(fact)
    return prime_factors


def largest_prime_factor(n):
    """Find largets prime factor of n."""
    pfs = prime_factors(n)
    print("pfs", pfs)
    return max(pfs)


def new_large_prime_factor(n):
    largest = None
    for num in range(1, np.sqrt(n)):
        if n % num == 0:
            # factor
            other_factor = n / num
            if isprime(other_factor):
                largest = other_factor
                break
            elif isprime(num):
                largest = num
    return largest


n = 11
print("factors of {} = {}".format(n, factors(n)))

print("prime factors of {} = {}".format(n, prime_factors(n)))

print("largest factor of {} = {}".format(n, largest_prime_factor(n)))

#print("new largest factor of {} = {}".format(n, new_large_prime_factor(n)))
# test number
test_number = 13195
# test prime_factors
# assert [5, 7, 13, 29] == prime_factors(test_number)

assert largest_prime_factor(test_number) == 29
assert new_large_prime_factor(11) == (11)

print("starting problem")
problem_number = 600851475143
# answer = largest_prime_factor(problem_number)
#answer = new_large_prime_factor(problem_number)
#print("largets prime factor of {} is {}".format(problem_number, answer))
