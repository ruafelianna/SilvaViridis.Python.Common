from typing import Annotated, Any, Protocol, runtime_checkable

from ..Validation import create_validator__is_instance

@runtime_checkable
class IComparable(Protocol):
    def __gt__(self, other : Any, /) -> bool: ...
    def __ge__(self, other : Any, /) -> bool: ...
    def __lt__(self, other : Any, /) -> bool: ...
    def __le__(self, other : Any, /) -> bool: ...

IComparableValidator = create_validator__is_instance((IComparable,))

type IComparableTypeHint = Annotated[Any, IComparableValidator]
