from beartype.vale import Is

def _is_uint_64(
    x : int,
) -> bool:
    return 0 <= x <= 18446744073709551615

UInt64Validator = Is[_is_uint_64]
