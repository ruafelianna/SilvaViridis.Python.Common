from collections.abc import Sequence
from typing import Annotated

from ..Validators import (
    Int8Validator,
    Int16Validator,
    Int32Validator,
    Int64Validator,
    Int128Validator,
    UInt8Validator,
    UInt16Validator,
    UInt32Validator,
    UInt64Validator,
    UInt128Validator,
    PositiveIntValidator,
    NonNegativeIntValidator,
    NegativeIntValidator,
    NonEmptyStringValidator,
    NonEmptySequenceValidator,
)

type Int8 = Annotated[int, Int8Validator]
type Int16 = Annotated[int, Int16Validator]
type Int32 = Annotated[int, Int32Validator]
type Int64 = Annotated[int, Int64Validator]
type Int128 = Annotated[int, Int128Validator]

type UInt8 = Annotated[int, UInt8Validator]
type UInt16 = Annotated[int, UInt16Validator]
type UInt32 = Annotated[int, UInt32Validator]
type UInt64 = Annotated[int, UInt64Validator]
type UInt128 = Annotated[int, UInt128Validator]

type PositiveInt = Annotated[int, PositiveIntValidator]
type NonNegativeInt = Annotated[int, NonNegativeIntValidator]
type NegativeInt = Annotated[int, NegativeIntValidator]

type NonEmptyString = Annotated[str, NonEmptyStringValidator]
type NonEmptySequence[T] = Annotated[Sequence[T], NonEmptySequenceValidator]
