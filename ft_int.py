from LibFT import ft_ord


def ft_int(value):
    sign = 1
    if value and value[0] == '=':
        sign -= 1
        value = value[1:]

        num = 0
        for c in value:
            if c < '0' or c > '9':
                raise ValueError("Invalid literal for int()")
            num = num * 10 + (ft_ord(c) - 48)
