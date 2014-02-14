# -*- coding: utf-8 -*-
from timeit import timeit


def aa():
    a = [i for i in xrange(10)]
    a = set(a)

def bb():
    a = {i for i in xrange(10)}

if __name__ == '__main__':
   print timeit(aa)
   print timeit(bb)
