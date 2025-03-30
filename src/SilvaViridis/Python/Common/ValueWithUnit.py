from functools import total_ordering
from typing import Any

from .Enums import OrderedEnum
from .Interfaces import IComparableTypeHint

@total_ordering
class ValueWithUnit[TValue : IComparableTypeHint, TUnit : OrderedEnum]:
    def __init__(
        self,
        value : TValue,
        unit : TUnit,
    ):
        self._value = value
        self._unit = unit

    @property
    def value(
        self,
    ) -> TValue:
        return self._value

    @property
    def unit(
        self,
    ) -> TUnit:
        return self._unit

    def __str__(
        self,
    ):
        return f"{self.value}{self.unit.value}"

    def __hash__(
        self,
    ) -> int:
        return hash((self._value, self._unit))

    def __eq__(
        self,
        other : Any,
    ) -> bool:
        if isinstance(other, type(self)):
            return (
                self.value == other.value
                and self.unit == other.unit
            )
        return NotImplemented

    def __gt__(
        self,
        other : Any,
    ) -> bool:
        if isinstance(other, type(self)):
            return (
                self.unit > other.unit
                or (
                    self.unit == other.unit
                    and self.value > other.value
                )
            )
        return NotImplemented
