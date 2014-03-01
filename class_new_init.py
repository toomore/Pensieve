# -*- coding: utf-8 -*-

class aa(object):
    pass

class tt(object):
    def __new__(self, *args, **kwargs):
        print 'in new'
        return type('toomore', (int,), {'name': 123})

    def __init__(self):
        print 'in init'

if __name__ == '__main__':
    t = tt()
    help(t)
