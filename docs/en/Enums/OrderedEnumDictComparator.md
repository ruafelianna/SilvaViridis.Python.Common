# OrderedEnumDictComparator

`OrderedEnumDictComparator` compares two `TEnum` values using a dictionary, where:

* `TEnum` is `OrderedEnum` or one of it's heirs;
* the keys of the dictionary are of `TEnum` type;
* the values of the dictionary are of `int` type.

#### Example:

```python
from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDictComparator,
)

@OrderedEnumDictComparator(lambda: {
    SomeEnum.Fruit1: 0,
    SomeEnum.Fruit2: 1,
})
class SomeEnum(OrderedEnum):
    Fruit1 = "orange"
    Fruit2 = "apple"
```

```
>>> SomeEnum.Fruit1 > SomeEnum.Fruit2
False
```

[Back](OrderedEnum.md)
