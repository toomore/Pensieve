from timeit import timeit

t = 10
l = []
l_append = l.append
s = [1, 2, 3]


def aa():
    return ','.join([str(i) for i in s])

def bb():
    return ''.join(str(s)[1:-1])

print aa()
print bb()

print 'aa'
ta = timeit(aa)
print ta

print 'bb'
tb = timeit(bb)
print tb

print ta / tb - 1
