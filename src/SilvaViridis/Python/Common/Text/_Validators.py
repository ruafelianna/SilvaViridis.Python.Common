from pydantic import AfterValidator, validate_call

from .StringHelper import StringHelper as SH

@validate_call
def _is_not_none_and_not_whitespace(
    text : str | None,
) -> str:
    if SH.is_not_none_and_not_whitespace(text):
        return text
    raise ValueError("The string value shouldn't be None, empty or whitespace")

NonEmptyStringValidator = AfterValidator(_is_not_none_and_not_whitespace)
