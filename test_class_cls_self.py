# -*- coding: utf-8 -*-
from timeit import timeit

class aa(object):
    def a(self):
        return 1

    def b(self):
        return 2

    def c(self):
        c = self.a() + self.b()

class bb(object):
    @classmethod
    def a(cls):
        return 1

    @classmethod
    def b(cls):
        return 2

    @classmethod
    def c(cls):
        c = cls.a() + cls.b()

if __name__ == '__main__':
    print aa().c() == bb.c()
    print timeit(aa().c)
    print timeit(bb.c)
