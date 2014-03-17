# -*- coding: utf-8 -*-
from collections import deque
from timeit import timeit

SAMPLE = deque(range(10))

class aa(object):
    @staticmethod
    def get_queue():
        q = SAMPLE.pop()
        SAMPLE.appendleft(q)
        return q

class bb(object):
    @staticmethod
    def get_queue():
        q = SAMPLE.pop()
        SAMPLE.appendleft(q)
        return q

for i in range(10):
    #print u'aa', aa.get_queue()
    #print u'bb', bb.get_queue()
    print timeit(aa.get_queue)
    print timeit(bb.get_queue)
