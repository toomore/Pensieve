# -*- coding: utf-8 -*-
from collections import deque

SAMPLE = deque(range(10))

def aa():
    q = SAMPLE.pop()
    SAMPLE.appendleft(q)
    return q

def bb():
    q = SAMPLE.pop()
    SAMPLE.appendleft(q)
    return q

for i in range(10):
    print u'aa', aa()
    print u'bb', bb()
