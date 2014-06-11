# -*- coding: utf-8 -*-
import urllib3

class Urlfetch(object):
    def __init__(self, base_url):
        self.conn = urllib3.connection_from_url(base_url)

    def get(self, path, params=None):
        return self.conn.request('GET', path)

    def post(self, path, data=None):
        return self.conn.request('POST', path)

if __name__ == '__main__':
    conn = Urlfetch('http://www.pinkoi.com/')
    print conn.get('/offers').data

