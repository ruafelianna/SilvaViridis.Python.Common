def lrc(
    bytes : bytearray,
) -> int:
    lrc = 0

    for b in bytes:
        lrc = (lrc + b) & 0xff

    return ((lrc ^ 0xff) + 1) & 0xff
