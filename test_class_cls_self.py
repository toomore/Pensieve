# -*- coding: utf-8 -*-
from timeit import timeit

class oaa(object):
    def a(self):
        return 1

    def b(self):
        return 2

    def c(self):
        c = self.a() + self.b()

class obb(object):
    @classmethod
    def a(cls):
        return 1

    @classmethod
    def b(cls):
        return 2

    @classmethod
    def c(cls):
        c = cls.a() + cls.b()

def aa():
    result = oaa().c()

def bb():
    result = obb.c()

if __name__ == '__main__':
    print oaa().c() == obb.c()
    print timeit(aa)
    # 0.80507516861
    print timeit(bb)
    # 0.670232057571
