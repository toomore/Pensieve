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
# 2.60321593285

print 'bb'
tb = timeit(bb)
print tb
# 2.2162270546

print ta / tb - 1
# 0.174616078911

print 'cc'
tc = timeit(cc)
print tc
# 1.51776909828

print 'dd'
td = timeit(dd)
print td
# 1.71133208275

print tc / td - 1
# -0.113106618182
