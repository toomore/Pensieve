# -*- coding: utf-8 -*-
import couchdb


class CouchDBBase(dict):

    def __init__(self, db_name):
        self.db_name = db_name

    def save(self):
        print self


class Test(CouchDBBase):
    db_name = 'toomoretest'

    def __init__(self, _id):
        super(Test, self).__init__(self.db_name)


if __name__ == '__main__':
    test = Test('op')
    test['name'] = 'toomore'
    test.save()
