# -*- coding: utf-8 -*-
import urllib3

proxy = urllib3.ProxyManager('http://127.0.0.1:6666/')
r1 = proxy.request('GET', 'http://google.com/')
r2 = proxy.request('GET', 'http://httpbin.org/')
print len(proxy.pools)
