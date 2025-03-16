# ValueWithUnit

`ValueWithUnit` class is used to declare an object, that has two properties - `value` of type `TValue` and `unit` of type `TUnit` (`TValue` should implement [`IComparable`](Interfaces/IComparable.md) protocol, and `TUnit` should inherit from [`OrderedEnum`](Enums/OrderedEnum.md) class). The main purpose of the class is to provide convinient compare methods, checking both value and unit, and a basic formatting.

**NB** This class does not take into account conversion of units. It's main purpose is to provide a convinient plain way to sort values with units, first by unit and then by value.

### Example:

```python
from SilvaViridis.Python.Common import ValueWithUnit

from SilvaViridis.Python.Common.Enums import (
    OrderedEnum,
    OrderedEnumDictComparator,
)

class TimeIntervalUnit(OrderedEnum):
    milliseconds = "ms"
    seconds  = "s"
    minutes = "m"
    hours = "h"

order = {
    TimeIntervalUnit.milliseconds: 0,
    TimeIntervalUnit.seconds: 1,
    TimeIntervalUnit.minutes: 2,
    TimeIntervalUnit.hours: 3,
}

OrderedEnumDictComparator(order)(TimeIntervalUnit)

t1 = ValueWithUnit(2, TimeIntervalUnit.minutes)
t2 = ValueWithUnit(1, TimeIntervalUnit.hours)
```

```
>>> t1 > t2
False
>>> f"{t2} {t1}"
1h 2m
```

[To Index](index.md)
