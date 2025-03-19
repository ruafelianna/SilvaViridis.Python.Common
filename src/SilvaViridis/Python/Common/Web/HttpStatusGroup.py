from enum import Enum

class HttpStatusGroup(Enum):
    information = 1
    success = 2
    redirect = 3
    client_error = 4
    server_error = 5
