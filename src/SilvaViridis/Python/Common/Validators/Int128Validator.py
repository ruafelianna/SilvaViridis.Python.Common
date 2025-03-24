from beartype.vale import Is

def _is_int_128(
    x : int,
) -> bool:
    return -170141183460469231731687303715884105728 <= x <= 170141183460469231731687303715884105727

Int128Validator = Is[_is_int_128]
