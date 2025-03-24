from collections.abc import Callable, Mapping

from .OrderedEnum import OrderedEnum
from .OrderedEnumComparator import OrderedEnumComparator
from ..Interfaces import IComparable

def OrderedEnumDictComparator[TEnum : OrderedEnum](
    order : Mapping[TEnum, IComparable],
) -> Callable[[type[TEnum]], type[TEnum]]:
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        if self not in order or other not in order:
            return NotImplemented
        return order[self] > order[other]
    return OrderedEnumComparator(compare)
