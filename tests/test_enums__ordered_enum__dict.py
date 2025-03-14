import pytest

from typing import (
    Any,
    Callable,
)

from src.SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDictComparator,
)

@OrderedEnumDictComparator(lambda: order)
class OE(OrderedEnum):
    s1 = "str1"
    s2 = "str3"
    s3 = "str4"
    s4 = "str5"
    s5 = "str2"
    s6 = "extra!!"

order = {
    OE.s1: 4,
    OE.s2: 2,
    OE.s3: 5,
    OE.s4: 1,
    OE.s5: 3,
}

@pytest.mark.parametrize("left,right,expected", [
    (OE.s1, OE.s1, True),
    (OE.s1, OE.s2, False),
    (OE.s1, OE.s3, False),
    (OE.s1, OE.s4, False),
    (OE.s1, OE.s5, False),
    (OE.s2, OE.s1, False),
    (OE.s2, OE.s2, True),
    (OE.s2, OE.s3, False),
    (OE.s2, OE.s4, False),
    (OE.s2, OE.s5, False),
    (OE.s3, OE.s1, False),
    (OE.s3, OE.s2, False),
    (OE.s3, OE.s3, True),
    (OE.s3, OE.s4, False),
    (OE.s3, OE.s5, False),
    (OE.s4, OE.s1, False),
    (OE.s4, OE.s2, False),
    (OE.s4, OE.s3, False),
    (OE.s4, OE.s4, True),
    (OE.s4, OE.s5, False),
    (OE.s5, OE.s1, False),
    (OE.s5, OE.s2, False),
    (OE.s5, OE.s3, False),
    (OE.s5, OE.s4, False),
    (OE.s5, OE.s5, True),
])
def test_eq(left : OE, right : OE, expected : bool):
    assert (left == right) == expected

@pytest.mark.parametrize("left,right,expected", [
    (OE.s1, OE.s1, False),
    (OE.s1, OE.s2, True),
    (OE.s1, OE.s3, True),
    (OE.s1, OE.s4, True),
    (OE.s1, OE.s5, True),
    (OE.s2, OE.s1, True),
    (OE.s2, OE.s2, False),
    (OE.s2, OE.s3, True),
    (OE.s2, OE.s4, True),
    (OE.s2, OE.s5, True),
    (OE.s3, OE.s1, True),
    (OE.s3, OE.s2, True),
    (OE.s3, OE.s3, False),
    (OE.s3, OE.s4, True),
    (OE.s3, OE.s5, True),
    (OE.s4, OE.s1, True),
    (OE.s4, OE.s2, True),
    (OE.s4, OE.s3, True),
    (OE.s4, OE.s4, False),
    (OE.s4, OE.s5, True),
    (OE.s5, OE.s1, True),
    (OE.s5, OE.s2, True),
    (OE.s5, OE.s3, True),
    (OE.s5, OE.s4, True),
    (OE.s5, OE.s5, False),
])
def test_ne(left : OE, right : OE, expected : bool):
    assert (left != right) == expected

@pytest.mark.parametrize("left,right,expected", [
    (OE.s1, OE.s1, False),
    (OE.s1, OE.s2, True),
    (OE.s1, OE.s3, False),
    (OE.s1, OE.s4, True),
    (OE.s1, OE.s5, True),
    (OE.s2, OE.s1, False),
    (OE.s2, OE.s2, False),
    (OE.s2, OE.s3, False),
    (OE.s2, OE.s4, True),
    (OE.s2, OE.s5, False),
    (OE.s3, OE.s1, True),
    (OE.s3, OE.s2, True),
    (OE.s3, OE.s3, False),
    (OE.s3, OE.s4, True),
    (OE.s3, OE.s5, True),
    (OE.s4, OE.s1, False),
    (OE.s4, OE.s2, False),
    (OE.s4, OE.s3, False),
    (OE.s4, OE.s4, False),
    (OE.s4, OE.s5, False),
    (OE.s5, OE.s1, False),
    (OE.s5, OE.s2, True),
    (OE.s5, OE.s3, False),
    (OE.s5, OE.s4, True),
    (OE.s5, OE.s5, False),
])
def test_gt(left : OE, right : OE, expected : bool):
    assert (left > right) == expected

@pytest.mark.parametrize("left,right,expected", [
    (OE.s1, OE.s1, True),
    (OE.s1, OE.s2, True),
    (OE.s1, OE.s3, False),
    (OE.s1, OE.s4, True),
    (OE.s1, OE.s5, True),
    (OE.s2, OE.s1, False),
    (OE.s2, OE.s2, True),
    (OE.s2, OE.s3, False),
    (OE.s2, OE.s4, True),
    (OE.s2, OE.s5, False),
    (OE.s3, OE.s1, True),
    (OE.s3, OE.s2, True),
    (OE.s3, OE.s3, True),
    (OE.s3, OE.s4, True),
    (OE.s3, OE.s5, True),
    (OE.s4, OE.s1, False),
    (OE.s4, OE.s2, False),
    (OE.s4, OE.s3, False),
    (OE.s4, OE.s4, True),
    (OE.s4, OE.s5, False),
    (OE.s5, OE.s1, False),
    (OE.s5, OE.s2, True),
    (OE.s5, OE.s3, False),
    (OE.s5, OE.s4, True),
    (OE.s5, OE.s5, True),
])
def test_ge(left : OE, right : OE, expected : bool):
    assert (left >= right) == expected

@pytest.mark.parametrize("left,right,expected", [
    (OE.s1, OE.s1, False),
    (OE.s1, OE.s2, False),
    (OE.s1, OE.s3, True),
    (OE.s1, OE.s4, False),
    (OE.s1, OE.s5, False),
    (OE.s2, OE.s1, True),
    (OE.s2, OE.s2, False),
    (OE.s2, OE.s3, True),
    (OE.s2, OE.s4, False),
    (OE.s2, OE.s5, True),
    (OE.s3, OE.s1, False),
    (OE.s3, OE.s2, False),
    (OE.s3, OE.s3, False),
    (OE.s3, OE.s4, False),
    (OE.s3, OE.s5, False),
    (OE.s4, OE.s1, True),
    (OE.s4, OE.s2, True),
    (OE.s4, OE.s3, True),
    (OE.s4, OE.s4, False),
    (OE.s4, OE.s5, True),
    (OE.s5, OE.s1, True),
    (OE.s5, OE.s2, False),
    (OE.s5, OE.s3, True),
    (OE.s5, OE.s4, False),
    (OE.s5, OE.s5, False),
])
def test_lt(left : OE, right : OE, expected : bool):
    assert (left < right) == expected

@pytest.mark.parametrize("left,right,expected", [
    (OE.s1, OE.s1, True),
    (OE.s1, OE.s2, False),
    (OE.s1, OE.s3, True),
    (OE.s1, OE.s4, False),
    (OE.s1, OE.s5, False),
    (OE.s2, OE.s1, True),
    (OE.s2, OE.s2, True),
    (OE.s2, OE.s3, True),
    (OE.s2, OE.s4, False),
    (OE.s2, OE.s5, True),
    (OE.s3, OE.s1, False),
    (OE.s3, OE.s2, False),
    (OE.s3, OE.s3, True),
    (OE.s3, OE.s4, False),
    (OE.s3, OE.s5, False),
    (OE.s4, OE.s1, True),
    (OE.s4, OE.s2, True),
    (OE.s4, OE.s3, True),
    (OE.s4, OE.s4, True),
    (OE.s4, OE.s5, True),
    (OE.s5, OE.s1, True),
    (OE.s5, OE.s2, False),
    (OE.s5, OE.s3, True),
    (OE.s5, OE.s4, False),
    (OE.s5, OE.s5, True),
])
def test_le(left : OE, right : OE, expected : bool):
    assert (left <= right) == expected

@pytest.mark.parametrize("value", [OE.s1, OE.s2, OE.s3, OE.s4, OE.s5])
@pytest.mark.parametrize("operator", [OE.__eq__, OE.__ne__, OE.__gt__, OE.__ge__, OE.__lt__, OE.__le__])
def test_not_implemented(value : OE, operator : Callable[[OE, Any], bool]):
    assert operator(value, 7) == NotImplemented

@pytest.mark.parametrize("value", [OE.s1, OE.s2, OE.s3, OE.s4, OE.s5])
@pytest.mark.parametrize("operator", [OE.__gt__, OE.__ge__, OE.__lt__, OE.__le__])
def test_not_in_dict(value : OE, operator : Callable[[OE, Any], bool]):
    assert operator(value, OE.s6) == NotImplemented
