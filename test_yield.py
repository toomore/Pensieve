# -*- coding: utf-8 -*-
from timeit import timeit

simple = range(10)

def aa():
    for i in simple:
        yield i

def bb():
    result = []
    for i in simple:
        result.append(i)

    return result

if __name__ == '__main__':
    print timeit(aa)
    print timeit(bb)
