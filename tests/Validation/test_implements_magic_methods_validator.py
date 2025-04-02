import pytest

from pydantic import BaseModel, ValidationError
from typing import Annotated, Any

from SilvaViridis.Python.Common.Validation import CheckMode, create_validator__implements_magic_methods

class SomeClass:
    def __eq__(self, other : Any): return True
    def __hash__(self): return 1

classes = [SomeClass]
mm_exist = [
    ["__eq__", "__hash__"],
]
mm_dont_exist = [
    ["__gt__", "__lt__"],
]

@pytest.mark.parametrize("cls", classes)
@pytest.mark.parametrize("mm", mm_exist)
def test_has_attr_all(cls : type, mm : list[str]):
    validator = create_validator__implements_magic_methods(mm)
    class OtherClass(BaseModel):
        some_field : Annotated[Any, validator]
    OtherClass(some_field = cls())

@pytest.mark.parametrize("cls", classes)
@pytest.mark.parametrize("mm_e", mm_exist)
@pytest.mark.parametrize("mm_de", mm_dont_exist)
def test_has_attr_any(cls : type, mm_e : list[str], mm_de : list[str]):
    mm = mm_e + mm_de
    validator = create_validator__implements_magic_methods(mm, CheckMode.any)
    class OtherClass(BaseModel):
        some_field : Annotated[Any, validator]
    OtherClass(some_field = cls())

@pytest.mark.xfail(raises = ValidationError)
@pytest.mark.parametrize("cls", classes)
@pytest.mark.parametrize("mm_de", mm_dont_exist)
@pytest.mark.parametrize("mm_e", mm_exist)
def test_has_attr_fail_all(cls : type, mm_de : list[str], mm_e : list[str]):
    mm = mm_de + mm_e
    validator = create_validator__implements_magic_methods(mm, CheckMode.all)
    class OtherClass(BaseModel):
        some_field : Annotated[Any, validator]
    OtherClass(some_field = cls())

@pytest.mark.xfail(raises = ValidationError)
@pytest.mark.parametrize("cls", classes)
@pytest.mark.parametrize("mm", mm_dont_exist)
def test_has_attr_fail_any(cls : type, mm : list[str]):
    validator = create_validator__implements_magic_methods(mm, CheckMode.any)
    class OtherClass(BaseModel):
        some_field : Annotated[Any, validator]
    OtherClass(some_field = cls())
