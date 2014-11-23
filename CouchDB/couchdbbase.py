# -*- coding: utf-8 -*-
import couchdb

COUCHDB = couchdb.Server()

class CouchDBBase(dict):

    def __init__(self, db_name, _id):
        self.db_name = db_name
        self._id = _id
        self.db = COUCHDB[db_name]

    def get_data(self):
        self.update(self.db.get(self._id, {}))

    def save(self):
        data = self.db.get(self._id, {'_id': self._id})
        data.update(self)
        self.db.save(data)


class Test(CouchDBBase):
    db_name = 'toomoretest'

    def __init__(self, _id):
        super(Test, self).__init__(self.db_name, _id)


if __name__ == '__main__':
    test = Test('opppp')
    test.get_data()
    print 'test: ', test
    #test['name'] = 'toomore2'
    #test.save()
