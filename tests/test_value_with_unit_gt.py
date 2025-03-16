import pytest

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

@pytest.mark.parametrize("left,right,expected", [
    (VwU(1, SizeUnit.b), VwU(1, SizeUnit.b), False),
    (VwU(1, SizeUnit.b), VwU(1, SizeUnit.kb), False),
    (VwU(1, SizeUnit.b), VwU(1, SizeUnit.mb), False),
    (VwU(1, SizeUnit.b), VwU(1, SizeUnit.gb), False),
    (VwU(1, SizeUnit.b), VwU(2, SizeUnit.b), False),
    (VwU(1, SizeUnit.b), VwU(2, SizeUnit.kb), False),
    (VwU(1, SizeUnit.b), VwU(2, SizeUnit.mb), False),
    (VwU(1, SizeUnit.b), VwU(2, SizeUnit.gb), False),
    (VwU(2, SizeUnit.b), VwU(1, SizeUnit.b), True),
    (VwU(2, SizeUnit.b), VwU(1, SizeUnit.kb), False),
    (VwU(2, SizeUnit.b), VwU(1, SizeUnit.mb), False),
    (VwU(2, SizeUnit.b), VwU(1, SizeUnit.gb), False),
    (VwU(1, SizeUnit.kb), VwU(1, SizeUnit.b), True),
    (VwU(1, SizeUnit.kb), VwU(1, SizeUnit.kb), False),
    (VwU(1, SizeUnit.kb), VwU(1, SizeUnit.mb), False),
    (VwU(1, SizeUnit.kb), VwU(1, SizeUnit.gb), False),
    (VwU(1, SizeUnit.kb), VwU(2, SizeUnit.b), True),
    (VwU(1, SizeUnit.kb), VwU(2, SizeUnit.kb), False),
    (VwU(1, SizeUnit.kb), VwU(2, SizeUnit.mb), False),
    (VwU(1, SizeUnit.kb), VwU(2, SizeUnit.gb), False),
    (VwU(2, SizeUnit.kb), VwU(1, SizeUnit.b), True),
    (VwU(2, SizeUnit.kb), VwU(1, SizeUnit.kb), True),
    (VwU(2, SizeUnit.kb), VwU(1, SizeUnit.mb), False),
    (VwU(2, SizeUnit.kb), VwU(1, SizeUnit.gb), False),
    (VwU(1, SizeUnit.mb), VwU(1, SizeUnit.b), True),
    (VwU(1, SizeUnit.mb), VwU(1, SizeUnit.kb), True),
    (VwU(1, SizeUnit.mb), VwU(1, SizeUnit.mb), False),
    (VwU(1, SizeUnit.mb), VwU(1, SizeUnit.gb), False),
    (VwU(1, SizeUnit.mb), VwU(2, SizeUnit.b), True),
    (VwU(1, SizeUnit.mb), VwU(2, SizeUnit.kb), True),
    (VwU(1, SizeUnit.mb), VwU(2, SizeUnit.mb), False),
    (VwU(1, SizeUnit.mb), VwU(2, SizeUnit.gb), False),
    (VwU(2, SizeUnit.mb), VwU(1, SizeUnit.b), True),
    (VwU(2, SizeUnit.mb), VwU(1, SizeUnit.kb), True),
    (VwU(2, SizeUnit.mb), VwU(1, SizeUnit.mb), True),
    (VwU(2, SizeUnit.mb), VwU(1, SizeUnit.gb), False),
    (VwU(1, SizeUnit.gb), VwU(1, SizeUnit.b), True),
    (VwU(1, SizeUnit.gb), VwU(1, SizeUnit.kb), True),
    (VwU(1, SizeUnit.gb), VwU(1, SizeUnit.mb), True),
    (VwU(1, SizeUnit.gb), VwU(1, SizeUnit.gb), False),
    (VwU(1, SizeUnit.gb), VwU(2, SizeUnit.b), True),
    (VwU(1, SizeUnit.gb), VwU(2, SizeUnit.kb), True),
    (VwU(1, SizeUnit.gb), VwU(2, SizeUnit.mb), True),
    (VwU(1, SizeUnit.gb), VwU(2, SizeUnit.gb), False),
    (VwU(2, SizeUnit.gb), VwU(1, SizeUnit.b), True),
    (VwU(2, SizeUnit.gb), VwU(1, SizeUnit.kb), True),
    (VwU(2, SizeUnit.gb), VwU(1, SizeUnit.mb), True),
    (VwU(2, SizeUnit.gb), VwU(1, SizeUnit.gb), True),
])
def test_gt(
    left : VwU[IComparable, SizeUnit],
    right : VwU[IComparable, SizeUnit],
    expected : bool,
):
    assert (left > right) == expected
