from beartype.vale import Is

def _is_negative(
    x : int,
) -> bool:
    return x < 0

NegativeIntValidator = Is[_is_negative]
