class StringHelper:
    @staticmethod
    def is_none_or_empty(
            value : str | None,
        ) -> bool:
            return value is None or len(value) == 0

    @staticmethod
    def is_none_or_whitespace(
            value : str | None,
        ) -> bool:
            return StringHelper.is_none_or_empty(value) or value.isspace() # type: ignore[reportOptionalMemberAccess] - always not None
