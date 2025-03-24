from beartype.vale import Is

def _is_int_16(
    x : int,
) -> bool:
    return -32768 <= x <= 32767

Int16Validator = Is[_is_int_16]
