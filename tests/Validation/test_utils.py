import pytest

from pydantic import validate_call
from typing import Annotated, Any

from SilvaViridis.Python.Common.Interfaces import IComparable
from SilvaViridis.Python.Common.Validation import create_validator__is_instance

data_non_strict = [
    (5, (IComparable,)),
    (5, (int,)),
    ("5", (int,)),
    ("hello", (int, str)),
]

data_non_strict_fail = [
    ("hello", (int,)),
    ("hello", (int, float)),
]

data_strict = [
    (5, (IComparable,)),
    (5, (int,)),
    ("hello", (int, str)),
]

data_strict_fail = [
    ("hello", (int,)),
    ("5", (int,)),
]

@pytest.mark.parametrize("value,check_type", data_non_strict)
def test_create_validator_instance_non_strict(value : Any, check_type : tuple[type, ...]):
    @validate_call
    def func(v : Annotated[Any, create_validator__is_instance(check_type)]):
        pass
    func(value)

@pytest.mark.parametrize("value,check_type", data_strict)
def test_create_validator_instance_strict(value : Any, check_type : tuple[type, ...]):
    @validate_call
    def func(v : Annotated[Any, create_validator__is_instance(check_type, strict = True)]):
        pass
    func(value)

@pytest.mark.xfail(raises = ValueError)
@pytest.mark.parametrize("value,check_type", data_non_strict_fail)
def test_create_validator_instance_non_strict_fail(value : Any, check_type : tuple[type, ...]):
    @validate_call
    def func(v : Annotated[Any, create_validator__is_instance(check_type)]):
        pass # pragma: no cover
    func(value)

@pytest.mark.xfail(raises = ValueError)
@pytest.mark.parametrize("value,check_type", data_strict_fail)
def test_create_validator_instance_strict_fail(value : Any, check_type : tuple[type, ...]):
    @validate_call
    def func(v : Annotated[Any, create_validator__is_instance(check_type, strict = True)]):
        pass # pragma: no cover
    func(value)
