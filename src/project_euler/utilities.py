"""Common utillities for Project Euler problems."""

# TODO


def convert_letter_to_number(letter: str):
    """Convert a letter to its corresponding number in the alphabet."""
    assert len(letter) == 1
    index = ord(letter.lower()) - 96
    assert 1 <= index <= 26
    return index
