import pytest

from pydantic import BaseModel, ValidationError
from typing import Annotated, Any

from SilvaViridis.Python.Common.Validation import CheckMode, create_validator__has_attributes

class SomeClass:
    SomeAttribute1 = 1
    SomeAttribute2 = 2

classes = [SomeClass]
attrs_exist = [
    ["SomeAttribute1", "SomeAttribute2"],
]
attrs_dont_exist = [
    ["SomeAttribute", "AndOtherAttribute"],
]

@pytest.mark.parametrize("cls", classes)
@pytest.mark.parametrize("attrs", attrs_exist)
def test_has_attr_all(cls : type, attrs : list[str]):
    validator = create_validator__has_attributes(attrs)
    class OtherClass(BaseModel):
        some_field : Annotated[Any, validator]
    OtherClass(some_field = cls())

@pytest.mark.parametrize("cls", classes)
@pytest.mark.parametrize("attrs_e", attrs_exist)
@pytest.mark.parametrize("attrs_de", attrs_dont_exist)
def test_has_attr_any(cls : type, attrs_e : list[str], attrs_de : list[str]):
    attrs = attrs_e + attrs_de
    validator = create_validator__has_attributes(attrs, CheckMode.any)
    class OtherClass(BaseModel):
        some_field : Annotated[Any, validator]
    OtherClass(some_field = cls())

@pytest.mark.xfail(raises = ValidationError)
@pytest.mark.parametrize("cls", classes)
@pytest.mark.parametrize("attrs_de", attrs_dont_exist)
@pytest.mark.parametrize("attrs_e", attrs_exist)
def test_has_attr_fail_all(cls : type, attrs_de : list[str], attrs_e : list[str]):
    attrs = attrs_de + attrs_e
    validator = create_validator__has_attributes(attrs, CheckMode.all)
    class OtherClass(BaseModel):
        some_field : Annotated[Any, validator]
    OtherClass(some_field = cls())

@pytest.mark.xfail(raises = ValidationError)
@pytest.mark.parametrize("cls", classes)
@pytest.mark.parametrize("attrs", attrs_dont_exist)
def test_has_attr_fail_any(cls : type, attrs : list[str]):
    validator = create_validator__has_attributes(attrs, CheckMode.any)
    class OtherClass(BaseModel):
        some_field : Annotated[Any, validator]
    OtherClass(some_field = cls())
