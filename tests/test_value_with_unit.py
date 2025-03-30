import operator as op
import pytest

from collections.abc import Callable
from itertools import product
from typing import Any

from SilvaViridis.Python.Common import ValueWithUnit as VwU
from SilvaViridis.Python.Common.Interfaces import IComparableTypeHint

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

OrderedEnumDictComparator(order)(SizeUnit)

OE_value_pairs = [(1, 1), (1, 2), (2, 1)]
OE_units = list(SizeUnit)
OE_unit_pairs = product(OE_units, repeat = 2)
OE_operators = [op.eq, op.ne, op.gt, op.ge, op.lt, op.le]
OE_checks : list[Callable[[VwU[IComparableTypeHint, SizeUnit], VwU[IComparableTypeHint, SizeUnit]], bool]] = [
    lambda x, y: (x.unit == y.unit) and (x.value == y.value),
    lambda x, y: (x.unit != y.unit) or (x.value != y.value),
    lambda x, y: (x.unit > y.unit) or ((x.unit == y.unit) and (x.value > y.value)),
    lambda x, y: (x.unit > y.unit) or ((x.unit == y.unit) and (x.value >= y.value)),
    lambda x, y: (x.unit < y.unit) or ((x.unit == y.unit) and (x.value < y.value)),
    lambda x, y: (x.unit < y.unit) or ((x.unit == y.unit) and (x.value <= y.value)),
]
OE_operators_dict = {x[0]: x[1] for x in zip(OE_operators, OE_checks)}

@pytest.mark.parametrize("v1,v2", OE_value_pairs)
@pytest.mark.parametrize("u1,u2", OE_unit_pairs)
@pytest.mark.parametrize("operator", OE_operators)
def test_op(
    v1 : IComparableTypeHint, v2 : IComparableTypeHint,
    u1 : SizeUnit, u2 : SizeUnit,
    operator : Callable[[Any, Any], bool]
):
    left = VwU(v1, u1)
    right = VwU(v2, u2)
    assert operator(left, right) == OE_operators_dict[operator](left, right)

@pytest.mark.parametrize("unit", OE_units)
def test_str(
    unit : SizeUnit,
):
    assert str(VwU(1024, unit)) == f"1024{unit.value}"

@pytest.mark.parametrize("unit", OE_units)
def test_hash(
    unit : SizeUnit,
):
    assert hash(VwU(1024, unit)) == hash((1024, unit))

@pytest.mark.parametrize("unit", OE_units)
def test_not_implemented_eq(
    unit : SizeUnit,
):
    assert not (VwU(7, unit) == 7)

@pytest.mark.parametrize("unit", OE_units)
def test_not_implemented_ne(
    unit : SizeUnit,
):
    assert VwU(7, unit) != 7

@pytest.mark.xfail(raises = TypeError)
@pytest.mark.parametrize("unit", OE_units)
@pytest.mark.parametrize("operator", OE_operators[2:])
def test_not_implemented_other(
    unit : SizeUnit,
    operator : Callable[[Any, Any], bool],
):
    assert operator(VwU(7, unit), 7)
