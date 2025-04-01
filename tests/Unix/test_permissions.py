import pytest

from itertools import product
from functools import reduce

from SilvaViridis.Python.Common.Unix import PermissionLevel, UnixPermissions

all_combinations = product([p for p in PermissionLevel], repeat = 3)
all_combinations_numbered = list(enumerate(all_combinations))

@pytest.mark.parametrize("triplet", all_combinations_numbered)
def test_create(triplet : tuple[int, tuple[PermissionLevel, PermissionLevel, PermissionLevel]]):
    _, (user, group, other) = triplet
    up = UnixPermissions(user = user, group = group, other = other)
    assert (up.user, up.group, up.other) == (user, group, other)

@pytest.mark.parametrize("triplet", all_combinations_numbered)
def test_octal(triplet : tuple[int, tuple[PermissionLevel, PermissionLevel, PermissionLevel]]):
    index, (user, group, other) = triplet
    assert UnixPermissions(user = user, group = group, other = other).as_octal() == f"{index:03o}"

@pytest.mark.parametrize("triplet", all_combinations_numbered)
@pytest.mark.parametrize("turn_on", [True, False])
def test_chmod(triplet : tuple[int, tuple[PermissionLevel, PermissionLevel, PermissionLevel]], turn_on : bool):
    index, (user, group, other) = triplet
    user_group = ("" if user == PermissionLevel.none else "u") \
        + ("" if group == PermissionLevel.none else "g") \
        + ("" if other == PermissionLevel.none else "o")
    sign = "+" if turn_on else "-"
    result = PermissionLevel(
        reduce(
            lambda acc, elem: acc | elem,
            (
                index // 64,
                (index % 64) // 8,
                index % 8,
            )
        )
    )
    assert UnixPermissions(user = user, group = group, other = other).as_chmod(turn_on) == f"{user_group}{sign}{result.name}"
