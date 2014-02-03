from timeit import timeit

def aa():
    a = '%s%s%s' % (1, 2, 3)

def aaa():
    a = '%(a)s%(b)s%(c)s' % ({'a': 1, 'b': 2, 'c': 3})
    assert a == '123'

def bb():
    b = '{0}{1}{2}'.format(1, 2, 3)

def bbb():
    b = '{a}{b}{c}'.format(**{'a': 1, 'b': 2, 'c': 3})
    assert b == '123'

print 'str'
print timeit(aa)
print timeit(aaa)

print 'format'
print timeit(bb)
print timeit(bbb)
