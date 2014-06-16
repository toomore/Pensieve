# -*- coding: utf-8 -*-
import ujson as json
import urllib3
from urllib3.util import get_host


##class UrlFetch(object):
##    def __init__(self, base_url):
##        self.conn = urllib3.connection_from_url(base_url)
##
##    def get(self, path, params=None, headers=None):
##        return self._request('GET', path, fields=params, headers=headers)
##
##    def post(self, path, data=None, headers=None):
##        return self._request('POST', path, fields=data, headers=headers)
##
##    def _request(self, method, path, fields=None, headers=None):
##        return self.conn.request(method, path, fields=fields, headers=headers)
##
##if __name__ == '__main__':
##    conn = UrlFetch('http://httpbin.org/')
##    print conn.get('/get', {'name': 'Toomore'}).data
##    result = conn.post('/post', {'name': 'Toomore'})
##    print result.data

class UrlFetch(urllib3.HTTPConnectionPool):
    def __init__(self, url):
        scheme, host, port = get_host(url)
        super(UrlFetch, self).__init__(host, port=port)

    def get(self, path, params=None, headers=None):
        return self.request('GET', path, fields=params, headers=headers)

    def post(self, path, data=None, headers=None):
        return self.request('POST', path, fields=data, headers=headers)

if __name__ == '__main__':
    conn = UrlFetch('http://httpbin.org/')
    print conn.get('/get', {'name': 'Toomore'}).data
    print conn.post('/post', {'name': 'Toomore'}).data
