import pytest

from functools import reduce

from SilvaViridis.Python.Common.Checksums import CRC16Type, crc_16

from .fixtures import data_list, modbus_rtu_checksums

map_method = {
    CRC16Type.modbus_rtu: modbus_rtu_checksums,
}

def map_data(method : CRC16Type):
    return list(map(lambda d, c: (method, d, c), data_list, map_method[method]))

all_data = reduce(lambda acc, elem: acc + elem, [map_data(method) for method in CRC16Type])

@pytest.mark.parametrize("method,array,crc", all_data)
def test(
    method : CRC16Type,
    array : str,
    crc : int,
):
    assert crc_16(bytes.fromhex(array), method) == crc
