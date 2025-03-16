# OrderedEnumGetDictComparator

`OrderedEnumGetDictComparator` is almost the same as [`OrderedEnumDictComparator`](OrderedEnumDictComparator.md). The only difference is that this class expects a function that returns a dictionary instead of a static dictionary.

#### Example:

```python
from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumGetDictComparator,
)

@OrderedEnumGetDictComparator(lambda: {
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

[To OrderedEnum](OrderedEnum.md)

[To Index](../index.md)
