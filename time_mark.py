# -*- coding: utf-8 -*-
from timeit import timeit


class timemark(object):

    def __init__(self, target):
        self.target = target
        self._type = type(target)
        self.time = self._time()

    def __repr__(self):
        return '%s %s(%s)' % (self.time, self.target.__name__,
                              self._type.__name__)

    def _time(self):
        return timeit(self.target)

if __name__ == '__main__':
    def aa():
        [i for i in xrange(10)]

    print timemark(aa)
