import operator as op
import pytest

from typing import Any, Callable

from SilvaViridis.Python.Common import ValueWithUnit as VwU
from SilvaViridis.Python.Common.Interfaces import IComparable

from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDictComparator,
)

class SizeUnit(OrderedEnum):
    b = ""
    kb = "k"
    mb = "m"
    gb = "g"

order = {
    SizeUnit.b: 0,
    SizeUnit.kb: 1,
    SizeUnit.mb: 2,
    SizeUnit.gb: 3,
}

SizeUnit = OrderedEnumDictComparator(order)(SizeUnit)

@pytest.mark.parametrize("value,expected", [
    (VwU(1024, SizeUnit.b), "1024"),
    (VwU(1024, SizeUnit.kb), "1024k"),
    (VwU(1024, SizeUnit.mb), "1024m"),
    (VwU(1024, SizeUnit.gb), "1024g"),
])
def test_str(
    value : VwU[IComparable, SizeUnit],
    expected : str,
):
    assert str(value) == expected

@pytest.mark.parametrize("value,expected", [
    (VwU(1024, SizeUnit.b), (1024, SizeUnit.b)),
    (VwU(1024, SizeUnit.kb), (1024, SizeUnit.kb)),
    (VwU(1024, SizeUnit.mb), (1024, SizeUnit.mb)),
    (VwU(1024, SizeUnit.gb), (1024, SizeUnit.gb)),
])
def test_hash(
    value : VwU[IComparable, SizeUnit],
    expected : tuple[int, SizeUnit],
):
    assert hash(value) == hash(expected)

@pytest.mark.parametrize("unit", [
    SizeUnit.b,
    SizeUnit.kb,
    SizeUnit.mb,
    SizeUnit.gb
])
def test_not_implemented_eq(
    unit : SizeUnit,
):
    assert not (VwU(7, unit) == 7)

@pytest.mark.parametrize("unit", [
    SizeUnit.b,
    SizeUnit.kb,
    SizeUnit.mb,
    SizeUnit.gb
])
def test_not_implemented_ne(
    unit : SizeUnit,
):
    assert VwU(7, unit) != 7

@pytest.mark.xfail(raises = TypeError)
@pytest.mark.parametrize("unit", [
    SizeUnit.b,
    SizeUnit.kb,
    SizeUnit.mb,
    SizeUnit.gb
])
@pytest.mark.parametrize("operator", [op.gt, op.ge, op.lt, op.le])
def test_not_implemented_other(
    unit : SizeUnit,
    operator : Callable[[VwU[int, SizeUnit], Any], bool],
):
    assert operator(VwU(7, unit), 7) == NotImplemented
