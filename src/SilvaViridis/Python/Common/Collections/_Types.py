from collections.abc import Sequence
from typing import Annotated

from ._Validators import (
    NonEmptySequenceValidator,
)

type NonEmptySequence[T] = Annotated[Sequence[T], NonEmptySequenceValidator]
