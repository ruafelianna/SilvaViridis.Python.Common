from enum import Enum

class CRC16Type(Enum):
    # 16bit; x^16 + x^15 + x^2 + 1; 0x8005; 0xa001
    modbus_rtu = 0x8005,
