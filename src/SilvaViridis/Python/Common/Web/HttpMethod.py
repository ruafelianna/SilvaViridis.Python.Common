from enum import Enum

class HttpMethod(Enum):
    GET = 0
    HEAD = 1
    POST = 2
    PUT = 3
    DELETE = 4
    MKCOL = 5
    COPY = 6
    MOVE = 7
    OPTIONS = 8
    PROPFIND = 9
    PROPPATCH = 10
    LOCK = 11
    UNLOCK = 12
    PATCH = 13
