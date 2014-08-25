# -*- coding: utf-8 -*-
# http://mysql-python.sourceforge.net/MySQLdb.html#mysqldb
import MySQLdb
import setting

conn = MySQLdb.connect('localhost', setting.DBUSER, setting.DBPASS, setting.DBS)
cur = conn.cursor()
cur.execute('select * from pootlecache26 order by expires desc limit 10')
print cur, dir(cur)

result = cur.fetchall()

for i in result:
    print i
