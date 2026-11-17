"""Tests for the V001a practice: the cases, the order of the three parts, and one comprehension per body."""

import ast
import inspect
from collections.abc import Callable, Iterator

import pytest
from comprehensions import common_items, paid_prices, sign_labels, squares_of_evens, unique_lengths


def test_squares_of_evens() -> None:
    assert squares_of_evens([1, 2, 3, 4, -6]) == [4, 16, 36]
    assert squares_of_evens([1, 3]) == []
    assert squares_of_evens([]) == []


def test_unique_lengths() -> None:
    assert unique_lengths(["a", "bb", "cc", "ddd"]) == {1, 2, 3}
    assert unique_lengths([]) == set()


def test_paid_prices() -> None:
    items = [("tea", 2.5), ("free", 0.0), ("refund", -1.0), ("cake", 4.0)]
    assert paid_prices(items) == {"tea": 2.5, "cake": 4.0}
    assert paid_prices([]) == {}


def test_sign_labels_keeps_every_number() -> None:
    assert sign_labels([-2, 0, 5]) == ["neg", "zero", "pos"]
    assert sign_labels([]) == []


class CountingIterable:
    """An iterable that counts how many times it is walked: `in` on it walks it, just like on a list."""

    def __init__(self, items: list[str]) -> None:
        self.items = items
        self.walks = 0

    def __iter__(self) -> Iterator[str]:
        self.walks += 1
        return iter(self.items)


def test_common_items_keeps_order_and_duplicates() -> None:
    assert common_items(["a", "b", "a", "c"], ["c", "a"]) == ["a", "a", "c"]
    assert common_items([], ["a"]) == []
    assert common_items(["a"], []) == []


def test_common_items_walks_b_once() -> None:
    """O(n + m): b is read once into a set. Walking it per item of a (x in b, or set(b) in the if) is O(n * m)."""
    b = CountingIterable(["x", "y", "z"])
    common_items(["y", "q", "z", "x"], b)
    assert b.walks == 1


def test_the_junior_answer_walks_b_for_every_item() -> None:
    """What the interviewer is checking: `in` on a non-set walks it again for each item."""
    b = CountingIterable(["x", "y", "z"])
    a = ["q", "q", "q", "q"]
    assert [x for x in a if x in b] == []
    assert b.walks == len(a)


def test_the_parts_run_for_then_if_then_expression() -> None:
    """Read 3-1-2, run 1-2-3: item by item, in one pass (Python 3.13 reference, 6.2.4)."""
    trace: list[str] = []

    def source(xs: list[int]) -> Iterator[int]:
        for x in xs:
            trace.append(f"for {x}")
            yield x

    def keep(n: int) -> bool:
        trace.append(f"if {n}")
        return n % 2 == 0

    def square(n: int) -> int:
        trace.append(f"expr {n}")
        return n * n

    assert [square(n) for n in source([1, 2]) if keep(n)] == [4]
    assert trace == ["for 1", "if 1", "for 2", "if 2", "expr 2"]


def test_if_else_after_the_for_is_a_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        compile("[n for n in nums if n > 0 else 0]", "<practice>", "eval")


def _body(func: Callable[..., object]) -> list[ast.stmt]:
    definition = ast.parse(inspect.getsource(func)).body[0]
    assert isinstance(definition, ast.FunctionDef)
    return [n for n in definition.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant))]


@pytest.mark.parametrize("func", [squares_of_evens, unique_lengths, paid_prices, sign_labels])
def test_body_is_one_comprehension(func: Callable[..., object]) -> None:
    body = _body(func)
    assert len(body) == 1, f"{func.__name__}: the body must be a single return statement"
    assert isinstance(body[0], ast.Return)
    assert isinstance(body[0].value, (ast.ListComp, ast.SetComp, ast.DictComp))
