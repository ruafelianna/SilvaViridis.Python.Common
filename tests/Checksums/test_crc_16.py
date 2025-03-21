import pytest

from SilvaViridis.Python.Common.Checksums import CRC16Type, crc_16

@pytest.mark.parametrize("array,method,crc", [
    ("01 03 00 00 00 01", CRC16Type.modbus_rtu, 0x0a84),
    ("01 03 02 ab cd", CRC16Type.modbus_rtu, 0xe106),
])
def test(
    array : str,
    method : CRC16Type,
    crc : int,
):
    assert crc_16(bytearray.fromhex(array), method) == crc
