from functools import total_ordering
from pydantic import BaseModel, ConfigDict
from typing import Annotated, Any

from .Enums import OrderedEnum
from .Interfaces import IComparable, IComparableValidator

@total_ordering
class ValueWithUnit[TValue : IComparable, TUnit : OrderedEnum](BaseModel):
    value : Annotated[TValue, IComparableValidator]
    unit : TUnit

    model_config = ConfigDict(
        arbitrary_types_allowed = True,
        frozen = True,
    )

    def __str__(
        self,
    ):
        return f"{self.value}{self.unit.value}"

    def __hash__(
        self,
    ) -> int:
        return hash((self.value, self.unit))

    def __eq__(
        self,
        other : Any,
    ) -> bool:
        return (
            isinstance(other, type(self))
            and self.value == other.value
            and self.unit == other.unit
        )

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
