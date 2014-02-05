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

class A(object):
    a = 'A'

class B(object):
    a = 'B'

class C(object):
    a = 'C'

class D(object):
    a = 'D'

class E(object):
    a = 'E'

class K1(A, B, C): pass
class K2(D, B, E): pass
class K3(D, A): pass
class Z(K1, K2, K3): pass

# L[Z]: Z K1 K2 K3 D A B C E O

z = Z()

print super(Z, z).a == 'D'
print super(K1, z).a == 'D'
print super(K2, z).a == 'D'
print super(K3, z).a == 'D'
print super(D, z).a == 'A'
print super(A, z).a == 'B'
print super(B, z).a == 'C'
print super(C, z).a == 'E'
