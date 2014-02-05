# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/datamodel.html
# TODO: implement it.

class aaa(object):
    def __init__(self, feed):
        self.feed = feed
        print 'in init.'

    def __new__(self, feed):
        print 'in new.'
        return 'r in new.'

    def __repr__(self):
        return 'r repr'

    def __nonzero__(self):
        #print 'in __nonzero__'
        return False

if __name__ == '__main__':
    a = aaa(123)
    print a
