"""Comprehensions in Python: the three parts and the cases they cover.

Rewrite each body as ONE comprehension: a single `return [...]`, `return {...}` or `return {k: v ...}`.
Keep the names, parameters and return types. Run the tests to check your answers.
`common_items` is an interview question: two lines are allowed there, and its complexity is what is graded.
"""

from collections.abc import Hashable, Iterable


def squares_of_evens(nums: list[int]) -> list[int]:
    """Squares of the even numbers, in their original order.

    The three parts: the expression (what to build), the for (where items come from) and the if (which to keep).
    """
    raise NotImplementedError


def unique_lengths(words: list[str]) -> set[int]:
    """The distinct lengths of the words: a set comprehension drops duplicates by itself."""
    raise NotImplementedError


def paid_prices(items: list[tuple[str, float]]) -> dict[str, float]:
    """Map each item name to its price, only for items that cost more than zero: a dict comprehension."""
    raise NotImplementedError


def sign_labels(nums: list[int]) -> list[str]:
    """Label EVERY number "neg", "zero" or "pos": an if-else before the for picks a value, it never filters."""
    raise NotImplementedError


def common_items[T: Hashable](a: list[T], b: Iterable[T]) -> list[T]:
    """Items of `a` that are also in `b`, in the order of `a` (duplicates kept), in O(n + m).

    Interview question. The junior answer, `[x for x in a if x in b]`, is O(n * m): `in` scans a list item by item.
    The trap: anything written inside the if runs again for every item of `a`.
    """
    raise NotImplementedError
