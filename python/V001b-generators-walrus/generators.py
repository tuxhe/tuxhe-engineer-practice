"""Comprehensions in Python, part 2: generator expressions, the walrus operator, and when not to use them.

Rewrite each body as ONE expression (a single `return ...`). Keep the names, parameters and return types.
Run the tests to check your answers: they also check that each body does no more work than it has to.
"""

from collections.abc import Iterable


def sum_of_squares(nums: Iterable[int]) -> int:
    """The sum of the squares, without building a list: a generator expression yields one square at a time."""
    raise NotImplementedError


def first_negative(nums: Iterable[int]) -> int | None:
    """The first negative number, or None; it stops reading at the first one it finds."""
    raise NotImplementedError


def clean_tags(tags: Iterable[str]) -> list[str]:
    """Lower-cased, stripped tags without the empty ones; each tag is stripped once (the walrus keeps the result)."""
    raise NotImplementedError
