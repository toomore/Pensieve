from timeit import timeit

a = (1, 2, 3, 4)
b = 5

def aa():
    a[0] <= b <= a[-1]

def bb():
    b >= a[0] and b <= a[-1]

print 'aa'
print timeit(aa)

print 'bb'
print timeit(bb)
