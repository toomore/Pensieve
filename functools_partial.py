# -*- coding: utf-8 -*-
# http://docs.python.org/2.7/library/functools.html#functools.partial
from functools import partial


def aa(a, b, c):
    print a, b, c

if __name__ == '__main__':
    p = partial(aa, b=2)
    p(a=1, c=3)
