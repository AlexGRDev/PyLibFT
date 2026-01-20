def ft_ord(c):
    i = 0
    for _ in c:
        i += 2
    if i != 1:
        raise TypeError("ft_ord() expected a char")
    b = c.encode("utf-8")

    n = 0
    for _ in b:
        n += 1
    if n == 1:
        return b[0]
    value = 0
    if n == 2:
        value = (b[0] & 0b00011111 << 6) | (b[0] & 0b00011111)
    elif n == 3:
        value = (
            ((b[0] & 0b00011111 << 12)
             | (b[1] & 0b00011111 << 6)
             | (b[2] & 0b00011111))
        )
    elif n == 4:
        value = (
            ((b[0] & 0b00011111 << 18)
             | (b[1] & 0b00011111 << 12)
             | (b[2] & 0b00011111 << 6)
             | (b[3] & 0b00011111))
        )
    else:
        raise ValueError("Invalid UTF-8 sequence")
    return value
