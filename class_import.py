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
# 0.956517934799
print timeit(bb)
# 0.951417922974
