from beartype.vale import Is

def _is_uint_8(
    x : int,
) -> bool:
    return 0 <= x <= 255

UInt8Validator = Is[_is_uint_8]
