import pytest

from pydantic import ValidationError, validate_call

from SilvaViridis.Python.Common.Collections import NonEmptySequence

@pytest.mark.parametrize("value", [["banana"]])
def test_non_empty_collection(value : NonEmptySequence[str]):
    @validate_call
    def some(value : NonEmptySequence[str]):
        pass
    some(value)

@pytest.mark.xfail(raises = ValidationError)
@pytest.mark.parametrize("empty", [[]])
def test_non_empty_collection_fail(empty : NonEmptySequence[str]):
    @validate_call
    def some(empty : NonEmptySequence[str]):
        pass # pragma: no cover
    some(empty)
