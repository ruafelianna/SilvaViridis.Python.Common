from typing import TypeGuard

class StringHelper:
    @staticmethod
    def is_not_none_and_not_empty(
            value : str | None,
        ) -> TypeGuard[str]:
            return value is not None and len(value) > 0

    @staticmethod
    def is_not_none_and_not_whitespace(
            value : str | None,
        ) -> TypeGuard[str]:
            return StringHelper.is_not_none_and_not_empty(value) and not value.isspace()

    @staticmethod
    def is_none_or_empty(
            value : str | None,
        ) -> bool:
            return not StringHelper.is_not_none_and_not_empty(value)

    @staticmethod
    def is_none_or_whitespace(
            value : str | None,
        ) -> bool:
            return not StringHelper.is_not_none_and_not_whitespace(value)
