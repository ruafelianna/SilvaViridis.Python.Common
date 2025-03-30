from pydantic import conint

from ._Consts import (
    MIN_INT_8,
    MIN_INT_16,
    MIN_INT_32,
    MIN_INT_64,
    MIN_INT_128,
    MIN_UINT_8,
    MIN_UINT_16,
    MIN_UINT_32,
    MIN_UINT_64,
    MIN_UINT_128,
    MAX_INT_8,
    MAX_INT_16,
    MAX_INT_32,
    MAX_INT_64,
    MAX_INT_128,
    MAX_UINT_8,
    MAX_UINT_16,
    MAX_UINT_32,
    MAX_UINT_64,
    MAX_UINT_128,
)

Int8Validator = conint(ge = MIN_INT_8, le = MAX_INT_8)
Int16Validator = conint(ge = MIN_INT_16, le = MAX_INT_16)
Int32Validator = conint(ge = MIN_INT_32, le = MAX_INT_32)
Int64Validator = conint(ge = MIN_INT_64, le = MAX_INT_64)
Int128Validator = conint(ge = MIN_INT_128, le = MAX_INT_128)

UInt8Validator = conint(ge = MIN_UINT_8, le = MAX_UINT_8)
UInt16Validator = conint(ge = MIN_UINT_16, le = MAX_UINT_16)
UInt32Validator = conint(ge = MIN_UINT_32, le = MAX_UINT_32)
UInt64Validator = conint(ge = MIN_UINT_64, le = MAX_UINT_64)
UInt128Validator = conint(ge = MIN_UINT_128, le = MAX_UINT_128)

PositiveIntValidator = conint(gt = 0)
NonNegativeIntValidator = conint(ge = 0)
NonPositiveIntValidator = conint(le = 0)
NegativeIntValidator = conint(lt = 0)
