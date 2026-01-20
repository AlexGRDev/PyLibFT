def ft_join(sep, iterable):
    result = ''
    first = True
    for x in iterable:
        if not first:
            result += sep
        result += x
        first = False
    return result
