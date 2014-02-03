from timeit import timeit

class offers(object):
    def offers_11(self):
        print 'offers_11'

    def offers_12(self):
        print 'offers_12'

    def offers_13(self):
        print 'offers_13'

    def get_offers(self, issues):
        gm = getattr(self, 'offers_{0}'.format(issues))
        gm()


def aa():
    d = {11: offers().offers_11,
         12: offers().offers_12,
         13: offers().offers_13}

    gm = d[13]

def bb():
    gm = getattr(offers, 'offers_{0}'.format(13))

print 'aa'
print timeit(aa)

print 'bb'
print timeit(bb)
