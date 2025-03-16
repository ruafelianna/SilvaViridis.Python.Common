import operator as op
import pytest

from enum import Enum
from itertools import product
from typing import Any, Callable

from SilvaViridis.Python.Common.Interfaces import IComparable

from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDictComparator,
    OrderedEnumGetDictComparator,
    OrderedEnumNameComparator,
    OrderedEnumValueComparator,
)

OE_items = ["s1", "s2", "s3", "s4", "s5"]
OE_pairs = product(OE_items, repeat = 2)
OE_values = ["str1", "str3", "str4", "str5", "str2"]
OE_values_dict = {x[0]: x[1] for x in zip(OE_items + ["s6"], OE_values + ["extra!!"])}
OE_order = [4, 2, 5, 1, 3]
OE_order_dict = {x[0]: x[1] for x in zip(OE_items, OE_order)}
OE_operators = [op.eq, op.ne, op.gt, op.ge, op.lt, op.le]

class comparator_type(Enum):
    dict = 0
    get_dict = 1
    p_name = 2
    p_value = 3

def create_comparator(t : comparator_type) -> tuple[type[OrderedEnum], Callable[[str], IComparable]]:
    oe = OrderedEnum("OrderedEnumTest", OE_values_dict)
    order = {getattr(oe, k): v for k, v in OE_order_dict.items()}
    order_func : Callable[[str], IComparable]

    if t is comparator_type.dict:
        OrderedEnumDictComparator(order)(oe)
        order_func = lambda name, o=OE_order_dict: o[name]
    elif t is comparator_type.get_dict:
        OrderedEnumGetDictComparator(lambda: order)(oe)
        order_func = lambda name, o=OE_order_dict: o[name]
    elif t is comparator_type.p_name:
        OrderedEnumNameComparator(oe)
        order_func = lambda name: name
    elif t is comparator_type.p_value:
        OrderedEnumValueComparator(oe)
        order_func = lambda name: OE_values_dict[name]
    return oe, order_func

OE_comparators = [
    create_comparator(comparator_type.dict),
    create_comparator(comparator_type.get_dict),
    create_comparator(comparator_type.p_name),
    create_comparator(comparator_type.p_value),
]

@pytest.mark.parametrize("comparator", OE_comparators)
@pytest.mark.parametrize("left,right", OE_pairs)
@pytest.mark.parametrize("operator", OE_operators)
def test_eq(
    comparator : tuple[type[OrderedEnum], Callable[[str], IComparable]],
    left : str,
    right : str,
    operator : Callable[[Any, Any], bool],
):
    d, o = comparator
    assert operator(o(left), o(right)) == operator(getattr(d, left), getattr(d, right))

@pytest.mark.parametrize("comparator", OE_comparators)
@pytest.mark.parametrize("value", OE_items)
def test_not_implemented_eq(
    comparator : tuple[type[OrderedEnum], Callable[[str], IComparable]],
    value : str,
):
    d, _ = comparator
    assert not (getattr(d, value) == 7)

@pytest.mark.parametrize("comparator", OE_comparators)
@pytest.mark.parametrize("value", OE_items)
def test_not_implemented_ne(
    comparator : tuple[type[OrderedEnum], Callable[[str], IComparable]],
    value : str,
):
    d, _ = comparator
    assert getattr(d, value) != 7

@pytest.mark.xfail(raises = TypeError)
@pytest.mark.parametrize("comparator", OE_comparators)
@pytest.mark.parametrize("value", OE_items)
@pytest.mark.parametrize("operator", OE_operators[2:])
def test_not_implemented_other(
    comparator : tuple[type[OrderedEnum], Callable[[str], IComparable]],
    value : str,
    operator : Callable[[Any, Any], bool],
):
    d, _ = comparator
    assert operator(getattr(d, value), 7)

@pytest.mark.xfail(raises = TypeError)
@pytest.mark.parametrize("comparator", OE_comparators[:2])
@pytest.mark.parametrize("value", OE_items)
@pytest.mark.parametrize("operator", OE_operators[2:])
def test_not_in_dict(
    comparator : tuple[type[OrderedEnum], Callable[[str], IComparable]],
    value : str,
    operator : Callable[[Any, Any], bool],
):
    d, _ = comparator
    assert operator(getattr(d, value), getattr(d, "s6"))
