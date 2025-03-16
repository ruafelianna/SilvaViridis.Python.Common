# OrderedEnumNameComparator

`OrderedEnumNameComparator` compares two `TEnum` values, based on their `name` property
(`TEnum` is `OrderedEnum` or one of it's heirs).

#### Example:

```python
from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumNameComparator,
)

@OrderedEnumNameComparator
class SomeEnum(OrderedEnum):
    Fruit1 = "orange"
    Fruit2 = "apple"
```

```
>>> SomeEnum.Fruit1 > SomeEnum.Fruit2
False
```

[To OrderedEnumPropertyComparator](OrderedEnumPropertyComparator.md)

[To Index](../index.md)
