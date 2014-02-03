from timeit import timeit


def aa():
    a = [i for i in range(1000)]
    for i in a:
        i

def bb():
    b = (i for i in range(1000))
    for i in b:
        i

print 'aa'
print timeit(aa, number=10)*1000000
# 900.030136108

print 'bb'
print timeit(bb, number=10)*1000000
# 1386.1656189
