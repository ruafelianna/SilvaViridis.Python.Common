import pytest

from typing import Callable

from SilvaViridis.Python.Common.Web import HttpStatus, HttpStatusGroup

codes = [code for code in range(100, 600) if code in HttpStatus]

@pytest.mark.parametrize("code", codes)
def test_groups(
    code : int,
):
    assert HttpStatus(code).get_group() == HttpStatusGroup(code // 100)

@pytest.mark.parametrize("code", codes)
@pytest.mark.parametrize("group", [
    (HttpStatusGroup.information, HttpStatus.is_information),
    (HttpStatusGroup.success, HttpStatus.is_success),
    (HttpStatusGroup.redirect, HttpStatus.is_redirect),
    (HttpStatusGroup.client_error, HttpStatus.is_client_error),
    (HttpStatusGroup.server_error, HttpStatus.is_server_error),
])
def test_is_group(
    code : int,
    group : tuple[HttpStatusGroup, Callable[[HttpStatus], bool]],
):
    group_enum, is_group = group
    assert is_group(HttpStatus(code)) == (code // 100 == group_enum.value)
