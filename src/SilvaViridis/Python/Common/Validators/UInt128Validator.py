from beartype.vale import Is

def _is_uint_128(
    x : int,
) -> bool:
    return 0 <= x <= 340282366920938463463374607431768211455

UInt128Validator = Is[_is_uint_128]
