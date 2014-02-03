
class toomore(object):
    ''' Test class toomore '''

    def __init__(self):
        self.l = []

    def __set__(self, value):
        print 'print set:', value
        self.l.append(value)

    def __get__(self):
        return self.l

    # TODO(Toomore)
    x = property(__get__, __set__)

t = toomore()
t.x = 123
t.x = 223
print t.x
#print toomore().__weakref__()
