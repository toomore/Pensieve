from timeit import timeit

t = 10
l = []
l_append = l.append
s = 'str'


def aa():
    l = []
    for i in xrange(t):
        l.append(i)

def bb():
    l = []
    l_append = l.append
    for i in xrange(t):
        l_append(i)

def cc():
    ss = ''
    for i in xrange(t):
        ss+=s

    #return ss

ll = []
ll_append = ll.append
def dd():
    ll = []

    for i in xrange(t):
        ll_append(s)

    #return ''.join(ll)

print 'aa'
ta = timeit(aa)
print ta

print 'bb'
tb = timeit(bb)
print tb

print ta / tb - 1

print 'cc'
tc = timeit(cc)
print tc

print 'dd'
td = timeit(dd)
print td

print tc / td - 1
