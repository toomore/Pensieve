# -*- coding: utf-8 -*-

class aaa(object):
    def __init__(self, feed):
        self.feed = feed
        print 'in init.'

    def __new__(self, feed):
        print 'in new.'


if __name__ == '__main__':
    a = aaa(123)
