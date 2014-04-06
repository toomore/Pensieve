# -*- coding: utf-8 -*-
from timeit import timeit

def aa():
    tuple(i for i in xrange(10))

def bb():
    tuple([i for i in xrange(10)])

if __name__ == '__main__':
    print timeit(aa)
    # 2.26480102539
    print timeit(bb)
    # 1.89851403236
