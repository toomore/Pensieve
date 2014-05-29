# -*- coding: utf-8 -*-
# http://stackoverflow.com/questions/308999/what-does-functools-wraps-do
from functools import wraps

def aa(func):
    @wraps(func)
    def rr(*args, **kwargs):
        print func.__name__, '<<<'
        return func(*args, **kwargs)
    return rr

@aa
def pp(*args, **kwargs):
    return args, kwargs

if __name__ == '__main__':
    # with wraps return pp
    # with out wraps return rr
    print pp.__name__

    print dir(pp)
    print pp.func_dict
    print pp(123)
