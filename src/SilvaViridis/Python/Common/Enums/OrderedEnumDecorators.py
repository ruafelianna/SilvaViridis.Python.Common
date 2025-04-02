from collections.abc import Callable, Mapping
from functools import total_ordering
from pydantic import validate_call
from typing import Any

from .OrderedEnum import OrderedEnum
from ..Interfaces import IComparableTypeHint

@validate_call
def BaseComparator[TEnum : OrderedEnum](
    compare : Callable[[TEnum, TEnum], bool],
) -> Callable[[type[TEnum]], type[TEnum]]:
    @validate_call
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

@validate_call
def DictComparator[TEnum : OrderedEnum](
    order : Mapping[TEnum, IComparableTypeHint],
) -> Callable[[type[TEnum]], type[TEnum]]:
    @validate_call
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        if self not in order or other not in order:
            return NotImplemented
        return order[self] > order[other]
    return BaseComparator(compare)

@validate_call
def GetDictComparator[TEnum : OrderedEnum](
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
    return BaseComparator(compare)

@validate_call
def PropertyComparator[TEnum : OrderedEnum](
    attr : str,
) -> Callable[[type[TEnum]], type[TEnum]]:
    @validate_call
    def compare(
        self : TEnum,
        other : TEnum,
    ) -> bool:
        return getattr(self, attr) > getattr(other, attr)
    return BaseComparator(compare)

NameComparator = PropertyComparator("name")

ValueComparator = PropertyComparator("value")
