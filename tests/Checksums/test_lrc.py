import pytest

from SilvaViridis.Python.Common.Checksums import lrc

from .fixtures import data_list, lrc_checksums

all_data = list(map(lambda d, c: (d, c), data_list, lrc_checksums))

@pytest.mark.parametrize("array,checksum", all_data)
def test(
    array : str,
    checksum : int,
):
    assert lrc(bytes.fromhex(array)) == checksum
