# -*- coding: utf-8 -*-
from timeit import timeit

sample = {'name': 'toomore', 'age': 23, 'list': None}

def aa():
    sample['list'] or None

def bb():
    sample.get('list')

if __name__ == '__main__':
    print timeit(aa)
    print timeit(bb)
