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
    print timeit(ab)
    print timeit(ba)
    print timeit(bb)

