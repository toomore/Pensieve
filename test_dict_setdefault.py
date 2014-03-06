# -*- coding: utf-8 -*-
from timeit import timeit

def aa():
    a = {}
    if not a.get('name'):
        a['name'] = 123

def bb():
    a = {}
    a.setdefault('name', 123)

c = {}
def cc():
    if not c.get('name'):
        c['name'] = 123

d = {}
def dd():
    d.setdefault('name', 123)

if __name__ == '__main__':
    print timeit(aa)
    print timeit(bb)
    print timeit(cc)
    print timeit(dd)
