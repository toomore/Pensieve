# -*- coding: utf-8 -*-
import MySQLdb
import setting


class MariaDB(object):

    def __init__(self):
        conn = MySQLdb.connect('localhost', setting.DBUSER, setting.DBPASS, setting.DBS)
        self.cur = conn.cursor()

    def __enter__(self):
        return self

    def sql(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def __exit__(self, type, value, traceback):
        self.cur.close()

class Userdata(MariaDB):
    pass

##cur.execute("""select * from %s""" % setting.TESTTABLE)

with Userdata() as userdata:
    result = userdata.sql("""select * from %s""" % setting.TESTTABLE)

for i in result:
    print i

#print '>>> print cur', cur, dir(cur)
#columns = [i[0] for i in cur.description]
#print columns
#print cur.description_flags
#cur.close()
