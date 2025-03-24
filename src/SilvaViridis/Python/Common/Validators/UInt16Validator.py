from beartype.vale import Is

def _is_uint_16(
    x : int,
) -> bool:
    return 0 <= x <= 65535

UInt16Validator = Is[_is_uint_16]
