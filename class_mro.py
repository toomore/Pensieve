# -*- coding: utf-8 -*-
# http://www.artima.com/weblogs/viewpost.jsp?thread=236275
# http://www.python.org/download/releases/2.3/mro/
# http://python-history.blogspot.tw/2010/06/method-resolution-order.html

class T(object):
    a = 0

class A(T):
    pass

class B(T):
    a = 2

class C(A, B):
    pass

# L[C]: C A T O B T O
# merge
# L[C]: C A B T O

c = C()

print super(C, c).a == 2
print super(A, c).a == 2
print super(B, c).a == 0
