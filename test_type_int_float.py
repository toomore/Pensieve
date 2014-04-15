# -*- coding: utf-8 -*-
from timeit import timeit


def covstr(strings):
    """ convert string to int or float. """
    strings = strings.replace(',', '') if ',' in strings else strings
    try:
        result = int(strings)
    except ValueError:
        result = float(strings)
    return result

def aa(strings):
    strings = strings.replace(',', '') if ',' in strings else strings
    return float(strings) if '.' in strings else int(strings)

def CC_A():
    covstr('1')

def CC_B():
    covstr('1.1')

def DD_A():
    aa('1')

def DD_B():
    aa('1.1')

if __name__ == '__main__':
    print timeit(CC_A)
    print timeit(CC_B)
    print timeit(DD_A)
    print timeit(DD_B)
