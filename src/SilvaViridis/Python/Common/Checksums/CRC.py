from .CRC16Type import CRC16Type
from .Lookup import MODBUS_RTU_LOOKUP_TABLE

def crc_16(
    bytes : bytearray,
    crc_type : CRC16Type,
) -> int:
    if crc_type == CRC16Type.modbus_rtu:
        return modbus_rtu(bytes)
    return NotImplemented

def modbus_rtu(
    bytes : bytearray,
) -> int:
    crc = 0xffff

    for i in range(len(bytes)):
        crc = (crc >> 8) ^ MODBUS_RTU_LOOKUP_TABLE[(crc ^ bytes[i]) & 0xff]

    return crc
