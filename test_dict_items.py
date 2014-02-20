# -*- coding: utf-8 -*-
from time_mark import Timemark
from timeit import timeit

sample = {str(i):i for i in range(20)}

def aa():
    for i in sample:
        c = sample[i]

def bb():
    for key, c in sample.items():
        c

def cc():
    for key, c in sample.iteritems():
        c

if __name__ == '__main__':
    print Timemark(aa)
    # 1.63503289223

    print Timemark(bb)
    # 2.37659788132

    print Timemark(cc)
    # 1.85569500923

    print timeit(aa)
    print timeit(bb)
    print timeit(cc)
