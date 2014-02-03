from timeit import timeit


def aa():
    a = [i for i in range(10)]
    for i in a:
        i

def bb():
    b = (i for i in range(10))
    for i in b:
        i

print 'aa'
print timeit(aa, number=10)*1000000

print 'bb'
print timeit(bb, number=10)*1000000
