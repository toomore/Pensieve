# -*- coding: utf-8 -*-
from timeit import timeit
from collections import deque

n = 100

AA_SAMPLE = deque(range(n))
def aa():
    get_one = AA_SAMPLE.pop()
    AA_SAMPLE.appendleft(get_one)

BB_SAMPLE = range(n)
def bb():
    get_one = BB_SAMPLE.pop()
    BB_SAMPLE.insert(0, get_one)

CC_SAMPLE = deque(range(n))
def cc():
    get_one = CC_SAMPLE[-1]
    CC_SAMPLE.rotate(1)

if __name__ == '__main__':
    print timeit(aa), len(AA_SAMPLE)
    # 0.431893110275
    print timeit(bb), len(BB_SAMPLE)
    # 0.762758016586
    print timeit(cc), len(CC_SAMPLE)
    # 0.561318159103
