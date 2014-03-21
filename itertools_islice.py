# -*- coding: utf-8 -*-
import itertools

a = itertools.islice('ABCDE', 2)
print list(a)

# groups
sample = [iter('ABCDE')] * 3
a = itertools.izip_longest(*sample, fillvalue='x')
print list(a)
# ABC, DEx
