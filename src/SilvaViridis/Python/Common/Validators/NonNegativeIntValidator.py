from beartype.vale import Is

def _is_not_negative(
    x : int,
) -> bool:
    return x >= 0

NonNegativeIntValidator = Is[_is_not_negative]
