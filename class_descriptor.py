# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/datamodel.html#implementing-descriptors
# TODO: implement it.


class aaa(object):
    def __init__(self, initval=0, name=''):
        print 'in init'
        self.value = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'in get', self.name, obj, objtype, obj.y
        return self.value

    def __set__(self, obj, value):
        print 'in set', self.name
        self.value = value

class bbb(object):
    x = aaa(10, 'x')
    y = 'abc'

if __name__ == '__main__':
    b = bbb()
    print b.x
    b.x = 12
    print b.x
