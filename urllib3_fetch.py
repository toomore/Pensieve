# -*- coding: utf-8 -*-
import urllib3


class Urlfetch(object):
    def __init__(self, base_url):
        self.conn = urllib3.connection_from_url(base_url)

    def get(self, path, params=None, headers=None):
        return self._request('GET', path, fields=params, headers=headers)

    def post(self, path, data=None, headers=None):
        return self._request('POST', path, fields=data, headers=headers)

    def _request(self, method, path, fields=None, headers=None):
        return self.conn.request(method, path, fields=fields, headers=headers)

if __name__ == '__main__':
    conn = Urlfetch('http://httpbin.org/')
    print conn.get('/get', {'name': 'Toomore'}).data
    print conn.post('/post', {'name': 'Toomore'}).data
