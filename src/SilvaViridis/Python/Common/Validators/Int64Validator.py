from beartype.vale import Is

def _is_int_64(
    x : int,
) -> bool:
    return -9223372036854775808 <= x <= 9223372036854775807

Int64Validator = Is[_is_int_64]
