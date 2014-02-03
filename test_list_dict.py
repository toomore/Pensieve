from timeit import timeit

t = 'asdasdf;lkjalskdjfalwiefn.zcxn2345o;;adlskf'
tt = dict.fromkeys(t)
print tt
ttt = set(t)

def aa():
    '6' in t

def bb():
    '6' in tt

def cc():
    '6' in ttt

print 'aa'
print timeit(aa, number=10)
# 8.10623168945e-06

print 'bb'
print timeit(bb, number=10)
# 5.00679016113e-06

print 'cc'
print timeit(cc, number=10)
# 5.00679016113e-06
