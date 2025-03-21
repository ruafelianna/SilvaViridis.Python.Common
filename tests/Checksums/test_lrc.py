import pytest

from SilvaViridis.Python.Common.Checksums import lrc

@pytest.mark.parametrize("array,checksum", [
    ("01 03 00 00 00 01", 0xfb),
    ("01 03 02 ab cd", 0x82),
])
def test(
    array : str,
    checksum : int,
):
    assert lrc(bytearray.fromhex(array)) == checksum
