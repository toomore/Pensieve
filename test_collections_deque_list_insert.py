# -*- coding: utf-8 -*-
from timeit import timeit
from collections import deque

AA_SAMPLE = range(100)
def aa():
    d = deque(AA_SAMPLE)
    get_one = d.pop()
    d.appendleft(get_one)

BB_SAMPLE = range(100)
def bb():
    get_one = BB_SAMPLE.pop()
    BB_SAMPLE.insert(0, get_one)

if __name__ == '__main__':
    print timeit(aa), len(AA_SAMPLE)
    # 2.0291929245
    print timeit(bb), len(BB_SAMPLE)
    # 0.714349985123
