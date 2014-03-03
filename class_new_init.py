# -*- coding: utf-8 -*-
# http://stackoverflow.com/questions/7057019/python-dynamic-inheritance-how-to-choose-base-class-upon-instance-creation
import requests

class aa(object):
    def __init__(self, *args, **kwargs):
        self.ok = 1
        r = requests.get('http://www.google.com/')
        print r.status_code
        print 'in aa init'

    def name(self):
        return 'toomore'


class tt(object):
    def __new__(cls, *args, **kwargs):
        print 'in tt new'
        print args, kwargs
        if cls is tt:
            print '123'
            return type('toomore', (aa,), {'age': 123})(*args, **kwargs)
        else:
            return object.__new__(cls)

if __name__ == '__main__':
    t = tt(1)
    #help(t)
    print t.name()
    print t.age
    print t.ok
