
class aa(object):

    def p(self):
        print 'self'

    @classmethod
    def pp(cls):
        print 'cls'

    @classmethod
    def ppp(cls):
        cls.pp()
        print '--'
        #self.pp()

aa().ppp()
aa.ppp()
