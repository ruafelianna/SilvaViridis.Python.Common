# OrderedEnum

`OrderedEnum` class is used as a base class for enumerations, that should support ordering.
It declares `__gt__`, `__ge__`, `__lt__` and `__le__` methods, but doesn't implement them.
The implemetation of these methods comes from several decorators,
that can be used to achieve a required order rule. They are:

* [Function comparator](OrderedEnumComparator.md)
* [Dictionary comparator](OrderedEnumDictComparator.md)
* [GetDictionary comparator](OrderedEnumGetDictComparator.md)
* [Property comparator](OrderedEnumPropertyComparator.md)
* [`name` property comparator](OrderedEnumNameComparator.md)
* [`value` property comparator](OrderedEnumValueComparator.md)

Be sure to **both** inherit from `OrderedEnum` and use one of the listed decorators,
otherwise you will get a runtime error due to non-implemented compare methods.
You can also build your own decorator, based on the listed ones.

The methods `__eq__`, `__ne__` and `__hash__` are implemented in the base class,
so there is no point in re-implementing them.

[To Index](../index.md)
