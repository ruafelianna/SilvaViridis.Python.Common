from collections.abc import Callable
from pydantic import validate_call

from .OrderedEnum import OrderedEnum
from .OrderedEnumComparator import OrderedEnumComparator

@validate_call
def OrderedEnumPropertyComparator[TEnum : OrderedEnum](
    attr : str,
) -> Callable[[type[TEnum]], type[TEnum]]:
    @validate_call
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        return getattr(self, attr) > getattr(other, attr)
    return OrderedEnumComparator(compare)
