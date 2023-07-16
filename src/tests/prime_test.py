"""Unit tests for the primality module."""
from project_euler.primality import is_prime


def test_small_primes():
    """Test if small primes are correctly identified."""
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)


def test_large_prime():
    """Test if a large prime is correctly identified."""
    assert is_prime(964278853154007512147452438423)
    assert is_prime(273220899647801318236942012067)
    assert is_prime(975514491869703338660461695811)
    assert not is_prime(47314851230985235923402982)
    assert not is_prime(32423908402983491234109248)
