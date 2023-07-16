"""Project Euler sequences."""
from functools import lru_cache
from itertools import permutations


def gen_pandigital(k, include_zero=False):
    """Generate all pandigital numbers of length k, sorted by value."""
    if include_zero:
        digits = reversed(list(range(k + 1)))
    else:
        digits = reversed(list(range(1, k + 1)))
    for perm in permutations(digits):
        yield int("".join(str(d) for d in perm))


@lru_cache(maxsize=None)
def triangle_numbers(n):
    """Generate the n-th triangle number."""
    return (n * (n + 1)) // 2


@lru_cache(maxsize=None)
def is_triangle_number(t):
    """Check if a number t is a triangle number."""
    return 0.5 * ((8 * t + 1) ** 0.5 - 1) % 1 == 0


@lru_cache(maxsize=None)
def pentagonal_numbers(n):
    """Generate the n-th pentagonal number."""
    return (n * (3 * n - 1)) // 2


@lru_cache(maxsize=None)
def is_pentagonal(t):
    """Check if a number p is a pentagonal number."""
    if t < 1:
        return False
    return ((24 * t + 1) ** 0.5 + 1) % 6 == 0


@lru_cache(maxsize=None)
def hexagonal_numbers(n):
    """Generate the n-th hexagonal number."""
    return n * (2 * n - 1)
