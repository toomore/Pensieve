# -*- coding: utf-8 -*-
from timeit import timeit


STR_SAMPLE = '國'

def aa():
    return STR_SAMPLE.decode('UTF-8')

def bb():
    return STR_SAMPLE.decode('utf-8')

def cc():
    return STR_SAMPLE.decode('UTF8')

def dd():
    return STR_SAMPLE.decode('utf8')

if __name__ == '__main__':
    if aa() == bb() == cc() == dd():
        print timeit(aa)
        print timeit(bb)
        print timeit(cc)
        print timeit(dd)
