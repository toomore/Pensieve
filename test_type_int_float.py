# -*- coding: utf-8 -*-
from timeit import timeit


def replace_comm(strings):
    return strings.replace(',', '') if ',' in strings else strings

def covstr(strings):
    """ convert string to int or float. """
    strings = replace_comm(strings)
    try:
        result = int(strings)
    except ValueError:
        result = float(strings)
    return result

def aa(strings):
    strings = replace_comm(strings)
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
    # 1.1373090744
    print timeit(CC_B)
    # 4.28914999962
    print timeit(DD_A)
    # 1.16217088699
    print timeit(DD_B)
    # 0.669591903687
