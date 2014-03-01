# -*- coding: utf-8 -*-

class aa(object):
    def __init__(self):
        print 'in aa init'

    def name(self):
        return 'toomore'


class tt(object):
    def __new__(self, *args, **kwargs):
        print 'in new'
        print args, kwargs
        return type('toomore', (aa,), {'age': 123})()

    def __init__(self):
        print 'in init'

if __name__ == '__main__':
    t = tt(1, 2)
    help(t)
    print t.name()
    print t.age
