# -*- coding: utf-8 -*-
from timeit import timeit

AA = {'name': 'toomore', 'age': 123}
def aa():
    AA['age']

BB = ['toomore', 'age']

def bb():
    BB[1]

if __name__ == '__main__':
    print timeit(aa)
    print timeit(bb)
