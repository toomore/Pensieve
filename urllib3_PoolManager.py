# -*- coding: utf-8 -*-
import urllib3

http = urllib3.PoolManager(5)
result = http.request('GET', 'http://www.pinkoi.com/')
print result.status
print result.headers
