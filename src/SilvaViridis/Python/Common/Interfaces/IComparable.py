from typing import Annotated, Any, Protocol, runtime_checkable

from ..Validation import create_validator__implements_magic_methods

@runtime_checkable
class IComparable(Protocol):
    def __gt__(self, other : Any, /) -> bool: ...
    def __ge__(self, other : Any, /) -> bool: ...
    def __lt__(self, other : Any, /) -> bool: ...
    def __le__(self, other : Any, /) -> bool: ...

IComparableValidator = create_validator__implements_magic_methods(("__gt__", "__ge__", "__lt__", "__le__"))

type IComparableTypeHint = Annotated[Any, IComparableValidator]
