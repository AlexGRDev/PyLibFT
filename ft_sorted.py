from LibFT import ft_append
from LibFT import ft_range


def ft_sorted(iterable):
    lst = []
    for x in iterable:
        lst = ft_append(x, iterable)
    n = 0
    for _ in lst:
        n += 1
    for _ in ft_range(n):
        for j in ft_range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
