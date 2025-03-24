import pytest

from typing import Any, Callable

from SilvaViridis.Python.Common.Text import StringHelper as SH

@pytest.mark.parametrize("value,expected", [
    (None, True),
    ("", True),
    ("    ", False),
    ("\t\t\t", False),
    ("\n\n\n", False),
    ("aaa", False),
])
def test_none_or_empty(value : str | None, expected : bool):
    assert SH.is_none_or_empty(value) == expected

@pytest.mark.parametrize("value,expected", [
    (None, True),
    ("", True),
    ("    ", True),
    ("\t\t\t", True),
    ("\n\n\n", True),
    ("aaa", False),
])
def test_none_or_whitespace(value : str | None, expected : bool):
    assert SH.is_none_or_whitespace(value) == expected

def to_str_1(value : int) -> str:
    return str(value + 1)

@pytest.mark.parametrize("value,to_str,expected", [
    (None, None, ""),
    ("", None, ""),
    ("    ", None, "    "),
    ("\t\t\t", None, "\t\t\t"),
    ("\n\n\n", None, "\n\n\n"),
    ("aaa", None, "aaa"),
    (12345, None, "12345"),
    (None, str, ""),
    (12345, to_str_1, "12346"),
])
def test_to_str_empty_if_none(value : Any, to_str : Callable[[Any], str], expected : str):
    assert SH.to_str_empty_if_none(value, to_str) == expected
