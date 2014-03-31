# -*- coding: utf-8 -*-
from timeit import timeit

AA_SAMPLE = {'name': 'toomore', 'age': 23, 'zxc': 'zxc', 'asd': 'asd'}
def aa():
    AA_SAMPLE.get('name')

def ab():
    'name' in AA_SAMPLE

def ba():
    AA_SAMPLE.get('name2')

def bb():
    'name2' in AA_SAMPLE

if __name__ == '__main__':
    print timeit(aa)
    # 0.293436050415
    print timeit(ab)
    # 0.1987388134
    print timeit(ba)
    # 0.301844835281
    print timeit(bb)
    # 0.22206902504
