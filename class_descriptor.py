# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/datamodel.html#implementing-descriptors
# TODO: implement it.

class aaa(object):
    def __init__(self):
        print 'in init'
        self._x = {}

    def __get__(self, name):
        return name

if __name__ == '__main__':
    a = aaa()
    print a.get('123')
