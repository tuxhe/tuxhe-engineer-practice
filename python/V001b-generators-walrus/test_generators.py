"""Tests for the V001b practice: the answers, the work they do, and the rules of generators and the walrus."""

from collections.abc import Iterator

import pytest
from generators import clean_tags, first_negative, sum_of_squares


class CountingIterable:
    """An iterable that counts the items handed out, so a test can see how much of it was read."""

    def __init__(self, items: list[int]) -> None:
        self.items = items
        self.read = 0

    def __iter__(self) -> Iterator[int]:
        for item in self.items:
            self.read += 1
            yield item


class CountingTag(str):
    """A tag that counts how many times it is stripped."""

    strips = 0

    def strip(self, chars: str | None = None) -> str:
        CountingTag.strips += 1
        return super().strip(chars)


def test_sum_of_squares() -> None:
    assert sum_of_squares([1, 2, 3]) == 14
    assert sum_of_squares([]) == 0


def test_a_generator_expression_yields_one_item_at_a_time() -> None:
    """Lazy: nothing is computed when it is created; each next() reads one more item, O(1) extra memory."""
    nums = CountingIterable([1, 2, 3, 4])
    squares = (n * n for n in nums)
    assert nums.read == 0
    assert next(squares) == 1
    assert nums.read == 1


def test_a_generator_can_be_read_only_once() -> None:
    """The trap: a second pass over the same generator finds it exhausted and sums nothing."""
    squares = (n * n for n in [1, 2, 3])
    assert sum(squares) == 14
    assert sum(squares) == 0


def test_the_first_iterable_is_evaluated_when_the_generator_is_created() -> None:
    """PEP 289: the outermost `in` runs at once, so an error there shows up here, not when it is read."""
    with pytest.raises(TypeError):
        (n for n in 42)  # type: ignore[attr-defined]  # an int is not iterable


def test_first_negative_stops_at_the_first_one() -> None:
    nums = CountingIterable([3, 1, -2, 5, -7, 8])
    assert first_negative(nums) == -2
    assert nums.read == 3
    assert first_negative([1, 2]) is None


def test_the_list_version_reads_everything_first() -> None:
    """Why not [n for n in nums if n < 0][0]: it builds the whole list before taking one item, and fails on none."""
    nums = CountingIterable([3, 1, -2, 5, -7, 8])
    assert [n for n in nums if n < 0][0] == -2  # noqa: RUF015  (the anti-pattern this test measures)
    assert nums.read == 6


def test_clean_tags() -> None:
    assert clean_tags([" Python ", "", "  ", "RUST"]) == ["python", "rust"]
    assert clean_tags([]) == []


def test_clean_tags_strips_each_tag_once() -> None:
    CountingTag.strips = 0
    tags = [CountingTag(t) for t in [" Python ", "  ", "RUST"]]
    clean_tags(tags)
    assert CountingTag.strips == 3


def test_the_repeated_call_strips_kept_tags_twice() -> None:
    """The version without the walrus calls strip in the if and again in the expression."""
    CountingTag.strips = 0
    tags = [CountingTag(t) for t in [" Python ", "  ", "RUST"]]
    assert [tag.strip().lower() for tag in tags if tag.strip()] == ["python", "rust"]
    assert CountingTag.strips == 5


def test_the_walrus_name_leaks_into_the_enclosing_scope() -> None:
    """PEP 572: a name bound with := inside a comprehension belongs to the function around it, not the loop."""
    kept = [t for tag in [" a ", "b "] if (t := tag.strip())]
    assert kept == ["a", "b"]
    assert t == "b"


def test_the_walrus_cannot_rebind_the_loop_variable() -> None:
    with pytest.raises(SyntaxError, match="cannot rebind comprehension iteration variable"):
        compile("[tag := tag.strip() for tag in tags]", "<v001b>", "eval")


def test_a_comprehension_for_side_effects_builds_a_list_of_nones() -> None:
    """When not to: a comprehension used only to call something builds and throws away a list; use a for loop."""
    seen: list[int] = []
    result = [seen.append(n) for n in [1, 2]]  # type: ignore[func-returns-value]
    assert result == [None, None]


def test_the_dojo_version_with_a_nested_generator_strips_once_too() -> None:
    CountingTag.strips = 0
    tags = [CountingTag(t) for t in [" Python ", "  ", "RUST"]]
    assert [t for t in (tag.strip().lower() for tag in tags) if t] == ["python", "rust"]
    assert CountingTag.strips == 3
