# -*- coding: utf-8 -*-
# http://docs.python.org/2/reference/expressions.html

print {i:i for i in xrange(10)}
print (i for i in xrange(10))
print {i for i in xrange(10)}

# ----- String conversions ----- #
print `1, 2, 3`

c = '3'
print `1, 2, c`

#print [yield i for i in range(10)]
