# -*- coding: utf-8 -*-
from timeit import timeit

a = {'name': 'toomore', 'age': 30, 'boy': True}
b = {'data': a}

def aa():
    if 'data' in b and b['data'].get('boy', True):
        pass

def bb():
    if 'data' in b and 'boy' in b['data'] and b['data']['boy']:
        pass

def cc():
    if b.get('data', {}).get('boy', True):
        pass

if __name__ == '__main__':
    print timeit(aa)
    # 0.411198854446
    print timeit(bb)
    # 0.406551122665
    print timeit(cc)
    # 0.496109008789
