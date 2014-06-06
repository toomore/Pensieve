# -*- coding: utf-8 -*-
from cStringIO import StringIO
from contextlib import closing
import csv
import urllib3


conn = urllib3.connection_from_url('http://s3.toomore.net/')
result = conn.request('GET', '/test.csv')

with closing(StringIO(result.data)) as files:
    csv_files = csv.reader(files)
    for i in csv_files:
        print i
