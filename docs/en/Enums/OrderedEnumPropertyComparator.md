# OrderedEnumPropertyComparator

`OrderedEnumPropertyComparator` compares two `TEnum` values using a given property, where:

* `TEnum` is `OrderedEnum` or one of it's heirs;
* the name of the property is given to the decorator as `str`.

There are two predefined decorators, that are built on top of `OrderedEnumPropertyComparator`,
using `Enum`'s properties `name` and `value`:

* [`name` property comparator](OrderedEnumNameComparator.md)
* [`value` property comparator](OrderedEnumValueComparator.md)

[To OrderedEnum](OrderedEnum.md)

[To Index](../index.md)
