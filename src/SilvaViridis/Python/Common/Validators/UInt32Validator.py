from beartype.vale import Is

def _is_uint_32(
    x : int,
) -> bool:
    return 0 <= x <= 4294967295

UInt32Validator = Is[_is_uint_32]
