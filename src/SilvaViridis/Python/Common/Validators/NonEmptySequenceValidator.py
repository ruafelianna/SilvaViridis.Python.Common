from beartype.vale import Is
from collections.abc import Sequence

def _is_not_empty_seq[T](
    seq : Sequence[T],
):
    return len(seq) > 0

NonEmptySequenceValidator = Is[_is_not_empty_seq]
