# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/datamodel.html
# TODO: implement it.


class aaa(object):
    def __init__(self):
        print 'in init'

    def __getattr__(self, name):
        print 'in getattr'
        return self.__dict__.get(name)

    def __setattr__(self, name, value):
        print 'in setattr'
        self.__dict__[name] = value

    def __delattr__(self, name):
        print 'in delattr'
        del self.__dict__[name]

if __name__ == '__main__':
    a = aaa()
    print a.__dict__
    print a.x
    a.x = 'Toomore'
    print a.x
    print a.__dict__
