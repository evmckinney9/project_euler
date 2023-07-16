"""Check if a number is prime."""

import random
from typing import Callable


def is_prime_miller_rabin(n: int, k: int = 5) -> bool:
    """Check if a number is prime using the Miller-Rabin primality test.

    The Miller-Rabin test is a probabilistic test, which means it might incorrectly
    identify a composite number as prime. However, this is rare if a sufficient
    number of tests are performed. By default, 5 tests are performed. This makes the
    function quite fast for large numbers.

    Args:
        n: The number to check.
        k: The number of random tests to perform.

    Returns:
        True if the number passed the tests and is likely to be prime, False otherwise.
    """
    if n < 2:
        return False
    for _ in range(k):
        a = random.randint(1, n - 1)
        x = pow(a, n - 1, n)  # Compute a^(n-1) % n using Python's built-in function
        if x != 1:
            return False
    return True


def is_prime(
    n: int, primality_test: Callable[[int], bool] = is_prime_miller_rabin
) -> bool:
    """Check if a number is prime.

    For numbers less than 10^6, a simple deterministic test is used.
    For larger numbers, a user-specified primality test is used
    (default is the Miller-Rabin test).

    Args:
        n: The number to check.
        primality_test: The primality test function to use for large numbers.

    Returns:
        True if the number is prime, False otherwise.
    """
    if n < 10**6:
        # Simple deterministic test
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    else:
        # Use the provided primality test function
        return primality_test(n)
