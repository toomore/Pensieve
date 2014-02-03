import requests
from timeit import timeit

def aa():
    d = {
            '1': requests,
            '2': requests,
            '3': requests,
            '4': requests,
            '5': requests
        }

def bb():
    d = {
            '1': requests,
        }

print 'timeit a'
print timeit(aa)

print 'timeit b'
print timeit(bb)
