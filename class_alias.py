# -*- coding: utf-8 -*-

class AA(object):
    def __init__(self, *args):
        self.aliases = set(args)

    def __call__(self, f):
        print f
        return f

class BB(object):
    @AA('mm')
    def mmmmmmmm(self):
        return 123

if __name__ == '__main__':
    print BB().mmmmmmmm()
