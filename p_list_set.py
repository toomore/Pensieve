from timeit import timeit

a = range(100)
b = set(a)

m = min(a)
x = max(a)

def aa():
    100 in a

def bb():
    100 in b

def cc():
    m >= 100 >= x

print timeit(aa)
# 2.40269112587

print timeit(bb)
# 0.211581945419

print timeit(cc)
# 0.235991001129
