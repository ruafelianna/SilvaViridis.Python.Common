from collections.abc import Callable, Mapping
from pydantic import validate_call

from .OrderedEnum import OrderedEnum
from .OrderedEnumComparator import OrderedEnumComparator
from ..Interfaces import IComparableTypeHint

@validate_call
def OrderedEnumGetDictComparator[TEnum : OrderedEnum](
    get_order : Callable[[], Mapping[TEnum, IComparableTypeHint]],
) -> Callable[[type[TEnum]], type[TEnum]]:
    @validate_call
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        order : Mapping[TEnum, IComparableTypeHint] = dict(get_order())
        if self not in order or other not in order:
            return NotImplemented
        return order[self] > order[other]
    return OrderedEnumComparator(compare)
