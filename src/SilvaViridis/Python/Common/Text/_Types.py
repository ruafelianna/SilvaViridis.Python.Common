from typing import Annotated

from ._Validators import (
    NonEmptyStringValidator,
)

type NonEmptyString = Annotated[str, NonEmptyStringValidator]
