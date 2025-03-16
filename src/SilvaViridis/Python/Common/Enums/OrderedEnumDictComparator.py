from typing import Callable

from .OrderedEnum import OrderedEnum
from .OrderedEnumComparator import OrderedEnumComparator

def OrderedEnumDictComparator[TEnum : OrderedEnum](
    order : dict[TEnum, int],
) -> Callable[[type[TEnum]], type[TEnum]]:
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        if self not in order or other not in order:
            return NotImplemented
        return order[self] > order[other]
    return OrderedEnumComparator(compare)
