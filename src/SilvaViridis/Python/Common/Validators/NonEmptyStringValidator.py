from beartype.vale import Is

from ..Text import StringHelper as SH

NonEmptyStringValidator = Is[SH.is_not_none_and_not_whitespace]
