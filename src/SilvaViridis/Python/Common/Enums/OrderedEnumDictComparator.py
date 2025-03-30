from collections.abc import Callable, Mapping
from pydantic import validate_call

from .OrderedEnum import OrderedEnum
from .OrderedEnumComparator import OrderedEnumComparator
from ..Interfaces import IComparableTypeHint

@validate_call
def OrderedEnumDictComparator[TEnum : OrderedEnum](
    order : Mapping[TEnum, IComparableTypeHint],
) -> Callable[[type[TEnum]], type[TEnum]]:
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        if self not in order or other not in order:
            return NotImplemented
        return order[self] > order[other]
    return OrderedEnumComparator(compare)
