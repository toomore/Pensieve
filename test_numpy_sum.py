# -*- coding: utf-8 -*-
from numpy import array
from numpy import sum as numpy_sum
from timeit import timeit

SAMPLE = range(1, 100)
SAMPLE_2 = array(SAMPLE)
def aa():
    sum(SAMPLE)

def bb():
    numpy_sum(SAMPLE_2)

if __name__ == '__main__':
    print timeit(aa)
    # 1.12759184837
    print timeit(bb)
    # 9.14239001274
