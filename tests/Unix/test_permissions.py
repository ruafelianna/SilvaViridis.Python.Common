import pytest

from itertools import product
from functools import reduce

from SilvaViridis.Python.Common.Unix import Permission, UnixPermission

all_combinations = product([p for p in Permission], repeat = 3)
all_combinations_numbered = list(enumerate(all_combinations))

@pytest.mark.parametrize("triplet", all_combinations_numbered)
def test_octal(triplet : tuple[int, tuple[Permission, Permission, Permission]]):
    index, (owner, group, other) = triplet
    assert UnixPermission(owner, group, other).as_octal() == f"{index:03o}"

@pytest.mark.parametrize("triplet", all_combinations_numbered)
@pytest.mark.parametrize("turn_on", [True, False])
def test_chmod(triplet : tuple[int, tuple[Permission, Permission, Permission]], turn_on : bool):
    index, (owner, group, other) = triplet
    user_group = ("" if owner == Permission.none else "u") \
        + ("" if group == Permission.none else "g") \
        + ("" if other == Permission.none else "o")
    sign = "+" if turn_on else "-"
    result = Permission(
        reduce(
            lambda acc, elem: acc | elem,
            (
                index // 64,
                (index % 64) // 8,
                index % 8,
            )
        )
    )
    assert UnixPermission(owner, group, other).as_chmod(turn_on) == f"{user_group}{sign}{result.name}"
