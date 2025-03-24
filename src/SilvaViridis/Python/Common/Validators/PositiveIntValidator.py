from beartype.vale import Is

def _is_positive(
    x : int,
) -> bool:
    return x > 0

PositiveIntValidator = Is[_is_positive]
