# -*- coding: utf-8 -*-
from timeit import timeit


class timemark(object):

    def __init__(self, target):
        self.target = target
        self._type = type(target)

    def _time(self):
        return timeit(self.target)
