from pydantic import validate_call

@validate_call
def lrc(
    data : bytes,
) -> int:
    lrc = 0

    for b in data:
        lrc = (lrc + b) & 0xff

    return ((lrc ^ 0xff) + 1) & 0xff
