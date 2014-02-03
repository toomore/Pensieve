from timeit import timeit

t = 'toomore'
upper = str.upper

def aa():
    t = 'toomore'
    upper = str.upper
    a = map(upper, t)

def aaa():
    a = map(upper, t)

def bb():
    a = [ i.upper() for i in t ]

def cc():
    a = ( i.upper() for i in t )

print 'aa'
print timeit(aa)

print 'aaa'
print timeit(aaa)

print 'bb'
print timeit(bb)

print 'cc'
print timeit(cc)
