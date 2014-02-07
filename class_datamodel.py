# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/datamodel.html
# TODO: implement it.

class base(object):
    pass

class aaa(object):
    def __init__(self, feed):
        self.feed = feed
        print 'in init.'

    '''
    def __new__(self, feed):
        print 'in new.'
        return 'r in new.'
    '''

    def __repr__(self):
        return "<aaa type: 'object'>"

    def __nonzero__(self):
        return False

    def __cmp__(self, other):
        print 'in cmp', other
        print self.feed, other.feed
        return cmp(self.feed, other.feed)

    def __lt__(self, other):
        print 'in lt', other
        return self.feed < other.feed

    def __le__(self, other):
        print 'in le', other
        return self.feed <= other.feed

    def __eq__(self, other):
        print 'in eq', other
        return self.feed == other.feed

    def __ne__(self, other):
        print 'in ne', other
        return not self.feed == other.feed

    def __gt__(self, other):
        print 'in gt', other
        return self.feed > other.feed

    def __ge__(self, other):
        print 'in ge', other
        return self.feed >= other.feed

    #def __hash__(self):
    #    ''' must define __cmp__() '''
    #    print 'in hash'
    #    return None

if __name__ == '__main__':
    a = aaa(123)
    b = aaa(323)
    print a
    print 'bool:', bool(a)
    print a, id(a), b, id(b)
    print 'cmp:', a >= b
    help(a)
