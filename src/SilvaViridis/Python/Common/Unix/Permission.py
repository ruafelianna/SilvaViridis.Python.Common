from enum import Enum

class Permission(Enum):
    none = 0
    x = 1
    w = 2
    wx = 3
    r = 4
    rx = 5
    rw = 6
    rwx = 7
