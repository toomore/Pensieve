from timeit import timeit

a = [1, 2, 3, 4]
b = set(a)

m = min(a)
x = max(a)

def aa():
    4 in a

def bb():
    m >= 4 >= x

print timeit(aa)
print timeit(bb)
