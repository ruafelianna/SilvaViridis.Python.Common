from beartype.vale import Is

def _is_int_8(
    x : int,
) -> bool:
    return -128 <= x <= 127

Int8Validator = Is[_is_int_8]
