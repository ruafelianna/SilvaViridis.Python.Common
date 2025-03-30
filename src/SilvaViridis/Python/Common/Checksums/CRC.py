from pydantic import validate_call

from .CRC16Type import CRC16Type
from .Lookup import MODBUS_RTU_LOOKUP_TABLE

@validate_call
def crc_16(
    data : bytes,
    crc_type : CRC16Type,
) -> int:
    if crc_type == CRC16Type.modbus_rtu:
        return modbus_rtu(data)
    return NotImplemented

@validate_call
def modbus_rtu(
    data : bytes,
) -> int:
    crc = 0xffff

    for i in range(len(data)):
        crc = (crc >> 8) ^ MODBUS_RTU_LOOKUP_TABLE[(crc ^ data[i]) & 0xff]

    return crc
