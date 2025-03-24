from collections.abc import Callable
from functools import total_ordering
from typing import Any

from .OrderedEnum import OrderedEnum

def OrderedEnumComparator[TEnum : OrderedEnum](
    compare : Callable[[TEnum, TEnum], bool],
) -> Callable[[type[TEnum]], type[TEnum]]:
    def decorator(
        cls : type[TEnum],
    ) -> type[TEnum]:
        def __gt__(
            self : TEnum,
            other : Any,
        ) -> bool:
            if isinstance(other, cls):
                return compare(self, other)
            return NotImplemented

        cls.__gt__ = __gt__

        return total_ordering(cls)

    return decorator
