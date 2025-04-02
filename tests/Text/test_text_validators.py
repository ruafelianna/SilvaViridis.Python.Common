import pytest

from pydantic import ValidationError, validate_call

from SilvaViridis.Python.Common.Text import NonEmptyString

@pytest.mark.parametrize("value", ["banana"])
def test_non_empty_string(value : NonEmptyString):
    @validate_call
    def some(value : NonEmptyString):
        pass
    some(value)

@pytest.mark.xfail(raises = ValidationError)
@pytest.mark.parametrize("empty", ["", " ", "\n", "\t", None])
def test_non_empty_string_fail(empty : NonEmptyString):
    @validate_call
    def some(empty : NonEmptyString):
        pass # pragma: no cover
    some(empty)
