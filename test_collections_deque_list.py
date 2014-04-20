# -*- coding: utf-8 -*-
from timeit import timeit
from collections import deque

n = 100

AA_SAMPLE = range(n)
def aa():
    POINT = 0
    AA_SAMPLE[POINT]
    POINT += 1
    if POINT > n:
        POINT = 0

CC_SAMPLE = deque(range(n))
def cc():
    get_one = CC_SAMPLE[-1]
    CC_SAMPLE.rotate(1)

if __name__ == '__main__':
    print timeit(aa), len(AA_SAMPLE)
    # 0.388238191605
    print timeit(cc), len(CC_SAMPLE)
    # 0.700126171112
