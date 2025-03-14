from typing import Callable

from .OrderedEnum import OrderedEnum
from .OrderedEnumComparator import OrderedEnumComparator

def OrderedEnumPropertyComparator[TEnum : OrderedEnum](
    attr : str,
) -> Callable[[type[TEnum]], type[TEnum]]:
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        return getattr(self, attr) > getattr(other, attr)
    return OrderedEnumComparator(compare)
