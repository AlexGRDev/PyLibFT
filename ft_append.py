def ft_append(lst, value):
    index = 0
    for _ in lst:
        index += 1
    lst[index:index] = [value]
    return lst
