# -*- coding: utf-8 -*-
from timeit import timeit


STR_SAMPLE = '國'

def aa():
    STR_SAMPLE.decode('UTF-8')

def bb():
    STR_SAMPLE.decode('utf-8')

def cc():
    STR_SAMPLE.decode('UTF8')

def dd():
    STR_SAMPLE.decode('utf8')

if __name__ == '__main__':
    print timeit(aa)
    print timeit(bb)
    print timeit(cc)
    print timeit(dd)
