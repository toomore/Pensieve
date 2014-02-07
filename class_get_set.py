# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/datamodel.html
# TODO: implement it.

class base(object):
    pass

class aaa(base):
    def __init__(self, feed):
        self.feed = feed
        print 'in init.'

    def __new__(self, feed):
        print 'in new.'
        return 'r in new.'

    def __repr__(self):
        return 'r repr'

    def __nonzero__(self):
        return False

    def __cmp__(self, other):
        print 'in cmp', other
        return 1

    def __eq__(self, other):
        print 'in eq', other
        return 0

    def __ne__(self, other):
        print 'in ne', other
        return 0

    def __hash__(self):
        ''' must define __cmp__() '''
        print 'in hash'
        return None

if __name__ == '__main__':
    a = aaa(123)
    b = aaa(333)
    print a
    print 'bool:', bool(a)
    print 'cmp:', cmp(a, b)
