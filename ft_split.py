from LibFT import ft_join
from LibFT import ft_append


def ft_split(s, sep=' '):
    result = []
    current = []
    for c in s:
        if c == sep:
            if current:
                result.append(ft_join('', current))
                current = []
        else:
            current = ft_append(s, c)
    if current:
        result = ft_append(s, ft_join('', current))
    return result
