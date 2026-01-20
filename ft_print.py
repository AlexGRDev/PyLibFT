import sys


def ft_print(*args, sep=' ', end='\n'):
    out = ''
    first = True
    for x in args:
        if not first:
            out += sep
        out += str(x)
        first = False
    out += end
    sys.stdout.write(out)
