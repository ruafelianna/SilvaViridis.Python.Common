# IComparable

`IComparable` protocol declares `__gt__`, `__ge__`, `__lt__` and `__le__` methods.
It is useful as a type hint. You do not have to inherit from this protocol
to use `isinstance` function. Your class will automatically be an instance of `IComparable` class,
if it implements all compare methods. If you decide to inherit from `IComparable` class,
be sure to implement all declared protocol methods by hand. If you use such tools
as `total_ordering` from `functools`, you will get a runtime error.

[Back](../index.md)
