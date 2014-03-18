# -*- coding: utf-8 -*-
import time
from datetime import datetime
from timeit import timeit

def aa():
    int(time.time())

def bb():
    time.mktime(datetime.now().utctimetuple())

print aa() == bb()

if __name__ == '__main__':
    print timeit(aa)
    print timeit(bb)
