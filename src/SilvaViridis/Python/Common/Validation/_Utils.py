from pydantic import AfterValidator, validate_call
from typing import Any

@validate_call
def create_validator(*types : type, strict : bool = False):
    def validate(value : Any) -> Any:
        for t in types:
            if isinstance(value, t):
                return value
            if not strict:
                try:
                    return t(value)
                except (TypeError, ValueError):
                    continue
        raise ValueError("No matching type found")

    return AfterValidator(validate)
