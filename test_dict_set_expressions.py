# -*- coding: utf-8 -*-
from timeit import timeit


def aa():
    ''' list '''
    a = [i for i in xrange(10)]
    #a = set(a) # 1.99305200577

def bb():
    ''' set '''
    a = {i for i in xrange(10)}

def cc():
    ''' tuple '''
    a = (i for i in xrange(10))
    #a = set(a) # 1.60462594032

def dd():
    ''' dict'''
    a = {i:i for i in xrange(10)}

if __name__ == '__main__':
   print timeit(aa)
   # 1.09882903099
   print timeit(bb)
   # 1.67259907722
   print timeit(cc)
   # 1.00920009613
   print timeit(dd)
