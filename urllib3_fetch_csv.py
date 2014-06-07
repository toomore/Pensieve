# -*- coding: utf-8 -*-
import csv
import urllib3
from cStringIO import StringIO
from contextlib import closing
from urllib3.util.request import make_headers


conn = urllib3.connection_from_url('http://s3.toomore.net/')
result = conn.request('GET', '/test.csv')

print result.getheaders()

with closing(StringIO(result.data)) as files:
    csv_files = csv.reader(files)
    for i in csv_files:
        print i

print make_headers(keep_alive=True)
