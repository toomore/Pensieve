from timeit import timeit

def aa():
    a = '%s%s%s' % (1, 2, 3)
    assert a == '123'

def aaa():
    a = '%(a)s%(b)s%(c)s' % ({'a': 1, 'b': 2, 'c': 3})
    assert a == '123'

def bb():
    b = '{0}{1}{2}'.format(1, 2, 3)
    assert b == '123'

def bbb():
    b = '{a}{b}{c}'.format(**{'a': 1, 'b': 2, 'c': 3})
    assert b == '123'

print 'str'
print timeit(aa)
# 0.524276971817
print timeit(aaa)
# 0.849791049957

print 'format'
print timeit(bb)
# 0.865188121796
print timeit(bbb)
# 1.11158490181
