# -*- coding: utf-8 -*-
# http://mysql-python.sourceforge.net/MySQLdb.html#mysqldb
import MySQLdb
import setting

conn = MySQLdb.connect('localhost', setting.DBUSER, setting.DBPASS, setting.DBS)
cur = conn.cursor()
cur.execute("""select * from %s""" % setting.TESTTABLE)

result = cur.fetchall()

for i in result:
    print i

print cur, dir(cur)
columns = [i[0] for i in cur.description]
print columns
print cur.description_flags
cur.close()
