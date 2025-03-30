from collections.abc import Sequence
from pydantic import AfterValidator, validate_call

@validate_call
def _is_not_empty_seq[T](
    seq : Sequence[T],
) -> Sequence[T]:
    if len(seq) == 0:
        raise ValueError("The collection should not be empty")
    return seq

NonEmptySequenceValidator = AfterValidator(_is_not_empty_seq)
