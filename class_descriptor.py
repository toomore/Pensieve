# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/datamodel.html#implementing-descriptors
# TODO: implement it.


class aaa(object):
    def __init__(self):
        print 'in init'
        self._x = 0

    def __get__(self):
        return self._x

    def __set__(self, value):
        self._x = value

    x = property(__get__, __set__)

if __name__ == '__main__':
    a = aaa()
    print a.x
    a.x = 123
    print a.x
