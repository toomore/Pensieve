# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/datamodel.html#implementing-descriptors
# TODO: implement it.
from timeit import timeit


class aaa(object):
    def __init__(self, initval=0, name=''):
        #print 'in init'
        self.value = initval
        self.name = name

    def __get__(self, obj, objtype):
        #print 'in get', self.name, obj, objtype, obj.y
        return self.value

    def __set__(self, obj, value):
        #print 'in set', self.name
        self.value = value

class bbb(object):
    x = aaa(10, 'x')
    y = 'abc'

class ccc(object):
    __slots__ = ['x', 'y']
    x = aaa(10, 'x')
    y = 'abc'

def test1():
    b = bbb()
    b.x = 12

def test2():
    b = ccc()
    b.x = 12

if __name__ == '__main__':
    print timeit(test1)
    # 0.768654823303
    print timeit(test2)
    # 0.74841594696
