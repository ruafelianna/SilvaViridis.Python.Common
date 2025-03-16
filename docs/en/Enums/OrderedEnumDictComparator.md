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

class SomeEnum(OrderedEnum):
    Fruit1 = "orange"
    Fruit2 = "apple"

order = {
    SomeEnum.Fruit1: 0,
    SomeEnum.Fruit2: 1,
}

OrderedEnumDictComparator(order)(SomeEnum)
```

```
>>> SomeEnum.Fruit1 > SomeEnum.Fruit2
False
```

[To OrderedEnum](OrderedEnum.md)

[To Index](../index.md)
