"""Project Euler sequences."""


def triangle_numbers(n):
    """Generate the n-th triangle number."""
    return (n * (n + 1)) // 2


def is_triangle_number(t):
    """Check if a number t is a triangle number."""
    return 0.5 * ((8 * t + 1) ** 0.5 - 1) % 1 == 0
