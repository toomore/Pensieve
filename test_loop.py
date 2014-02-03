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
# 2.43927001953

print 'aaa'
print timeit(aaa)
# 2.25370001793

print 'bb'
print timeit(bb)
# 2.3753888607

print 'cc'
print timeit(cc)
# 0.780359983444
