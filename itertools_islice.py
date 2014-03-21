# -*- coding: utf-8 -*-
import itertools

a = itertools.islice('ABCDE', 2)
print list(a)

a = itertools.izip_longest('ABCDE','ABC', fillvalue='x')
print list(a)
