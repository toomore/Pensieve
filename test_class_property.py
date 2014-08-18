# -*- coding: utf-8 -*-

class ClassProperty (property):
    """Subclass property to make classmethod properties possible"""
    def __get__(self, cls, owner):
        return self.classmethod.__get__(None, owner)()

class People(object):
    names = {'toomore': 30}

    @ClassProperty
    @classmethod
    def names(cls):
        return cls.names

if __name__ == '__main__':
    #print People.names['toomore']
    print People.names['toomore']
