from typing import Callable

from .OrderedEnum import OrderedEnum
from .OrderedEnumComparator import OrderedEnumComparator
from ..Interfaces import IComparable

def OrderedEnumGetDictComparator[TEnum : OrderedEnum](
    get_order : Callable[[], dict[TEnum, IComparable]],
) -> Callable[[type[TEnum]], type[TEnum]]:
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        order : dict[TEnum, IComparable] = dict(get_order())
        if self not in order or other not in order:
            return NotImplemented
        return order[self] > order[other]
    return OrderedEnumComparator(compare)
