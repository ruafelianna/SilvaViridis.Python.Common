import pytest

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
