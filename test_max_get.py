from timeit import timeit

a = [1, 2, 3, 4, 5]

def aa():
    assert 5 == a[-1]

def bb():
    assert 5 == max(a)

print 'aa'
print timeit(aa)
# 0.212356090546

print 'bb'
print timeit(bb)
# 0.523684978485
