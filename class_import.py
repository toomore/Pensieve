# -*- coding: utf-8 -*-
from timeit import timeit
from datetime import datetime

class o(object):
    def __init__(self):
        pass

    def get_time(self):
        return datetime.now()

    @staticmethod
    def get_timei_b():
        return datetime.now()

class oo(object):
    @staticmethod
    def get_time():
        return datetime.now()

def aa():
    o().get_time()

def bb():
    oo.get_time()

def cc():
    o.get_timei_b()

print timeit(aa)
# 2.22908782959
print timeit(bb)
# 1.61138892174
print timeit(cc)
# 1.58323502541
