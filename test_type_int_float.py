# -*- coding: utf-8 -*-
from timeit import timeit


def covstr():
    """ convert string to int or float. """
    try:
        result = int(strings)
    except ValueError:
        result = float(strings)
    return result

def aa():
    return float(strings) if '.' in strings else int(strings)

if __name__ == '__main__':
    print timeit(covstr, setup='strings=1')
    print timeit(aa, setup='strings=1')
    print timeit(covstr, setup='strings=1.1')
    print timeit(aa, setup='strings=1.1')
