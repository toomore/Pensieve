# -*- coding: utf-8 -*-
from timeit import timeit


a = dict.fromkeys(range(10))
b = range(10)

def aa():
    10 in a

def bb():
    10 in b

if __name__ == '__main__':
    print timeit(aa)
    # 0.199939012527
    print timeit(bb)
    # 0.444370031357
