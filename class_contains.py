# -*- coding: utf-8 -*-

class a(object):
    def __init__(self):
        self.sample = dict.fromkeys(range(10))
        print 'in init'

    def __contains__(self, key):
        print 'in contains.'
        return key in self.sample

if __name__ == '__main__':
    print 1 in a()
