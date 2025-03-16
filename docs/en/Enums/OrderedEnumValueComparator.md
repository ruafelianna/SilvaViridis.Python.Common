# OrderedEnumValueComparator

`OrderedEnumValueComparator` compares two `TEnum` values, based on their `value` property
(`TEnum` is `OrderedEnum` or one of it's heirs).

#### Example:

```python
from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumValueComparator,
)

@OrderedEnumValueComparator
class SomeEnum(OrderedEnum):
    Fruit1 = "orange"
    Fruit2 = "apple"
```

```
>>> SomeEnum.Fruit1 > SomeEnum.Fruit2
True
```

[To OrderedEnumPropertyComparator](OrderedEnumPropertyComparator.md)

[To Index](../index.md)
