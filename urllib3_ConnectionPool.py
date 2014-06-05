# -*- coding: utf-8 -*-
import urllib3

conn = urllib3.connection_from_url('http://www.pinkoi.com/')
result = conn.request('GET', '/user/toomore')
print result.getheaders()
print result.data.split('\n')
