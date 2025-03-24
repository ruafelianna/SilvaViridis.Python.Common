from beartype.vale import Is

def _is_int_32(
    x : int,
) -> bool:
    return -2147483648 <= x <= 2147483647

Int32Validator = Is[_is_int_32]
