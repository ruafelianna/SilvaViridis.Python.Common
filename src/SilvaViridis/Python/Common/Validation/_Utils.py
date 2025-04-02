from collections.abc import  Callable
from enum import Enum
from pydantic import AfterValidator, validate_call
from typing import Any

from SilvaViridis.Python.Common.Collections import NonEmptySequence
from SilvaViridis.Python.Common.Text import NonEmptyString

class CheckMode(Enum):
    all = 0
    any = 1

@validate_call
def validate_is_instance[T](
    value : T,
    types : NonEmptySequence[type],
    strict : bool,
    msg : str,
) -> T:
    for t in types:
        if isinstance(value, t):
            return value
        if not strict:
            try:
                return t(value)
            except (TypeError, ValueError):
                continue
    raise ValueError(msg)

@validate_call
def validate_all_or_any[TObj, TElem](
    obj : TObj,
    collection : NonEmptySequence[TElem],
    condition : Callable[[TObj, TElem], bool],
    mode : CheckMode,
    msg : str,
) -> TObj:
    ex = ValueError(msg)
    for elem in collection:
        result = condition(obj, elem)
        if mode == CheckMode.all and not result:
            raise ex
        elif mode == CheckMode.any and result:
            return obj
    if mode == CheckMode.all:
        return obj
    else:
        raise ex

@validate_call
def create_validator__is_instance(
    types : NonEmptySequence[type],
    strict : bool = False,
):
    @validate_call
    def validate[T](value : T) -> T:
        return validate_is_instance(
            value,
            types,
            strict = strict,
            msg = "No matching type found",
        )
    return AfterValidator(validate)

@validate_call
def create_validator__has_attributes(
    attrs : NonEmptySequence[NonEmptyString],
    mode : CheckMode = CheckMode.all,
):
    @validate_call
    def validate[T](value : T) -> T:
        @validate_call
        def check_has_attr(obj : T, elem : str):
            return hasattr(obj, elem)

        return validate_all_or_any(
            value,
            attrs,
            check_has_attr,
            mode,
            f"The object of type = {type(value)}, value = {repr(value)} doesn't contain {mode.name} of the required attributes: {attrs}",
        )
    return AfterValidator(validate)

object_magic_methods_cache : dict[str, Any | None] = {}

@validate_call
def create_validator__implements_magic_methods(
    methods : NonEmptySequence[NonEmptyString],
    mode : CheckMode = CheckMode.all,
):
    @validate_call
    def validate[T](value : T) -> T:
        @validate_call
        def check_magic_methods(obj : T, elem : str):
            if elem not in object_magic_methods_cache:
                object_magic_methods_cache[elem] = getattr(object, elem, None)
            method = getattr(type(obj), elem, None)
            return method is not None and method != object_magic_methods_cache[elem]

        return validate_all_or_any(
            value,
            methods,
            check_magic_methods,
            mode,
            f"The object of type = {type(value)}, value = {repr(value)} doesn't implement {mode.name} of the required magic methods: {methods}",
        )
    return AfterValidator(validate)
