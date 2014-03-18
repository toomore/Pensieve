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
    # 0.49315905571
    print timeit(bb)
    # 7.44000315666
