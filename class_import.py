# -*- coding: utf-8 -*-
from timeit import timeit
import requests

def aa():
    r = requests.post
    str(r)

rr = requests
def bb():
    str(rr.post)

print timeit(aa)
print timeit(bb)
