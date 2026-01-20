def ft_chr(code):
    if code < 0:
        raise ValueError("ft_chr() arg not in range")
    if code <= 0x7F:
        b = bytes([code])
    elif code <= 0x7FF:
        b1 = 0b11000000 | (code >> 6)
        b2 = 0b10000000 | (code & 0b00111111)
        b = bytes([b1, b2])
    elif code <= 0xFFFF:
        b1 = 0b11100000 | (code >> 12)
        b2 = 0b10000000 | ((code >> 6) & 0b00111111)
        b3 = 0b10000000 | (code & 0b00111111)
        b = bytes([b1, b2, b3])
    elif code <= 0x10FFFF:
        b1 = 0b11110000 | (code >> 18)
        b2 = 0b10000000 | ((code >> 12) & 0b00111111)
        b3 = 0b10000000 | ((code >> 6) & 0b00111111)
        b4 = 0b10000000 | (code & 0b00111111)
        b = bytes([b1, b2, b3, b4])
    else:
        raise ValueError("ft_chr() arg not in range")
    return b.decode("utf-8")
