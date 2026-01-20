import sys


def ft_input(prompt=''):
    if prompt:
        sys.stdout.write(prompt)
    data = sys.stdin.readline()
    if data.endswith('\n'):
        data = data[:-1]
    return data
