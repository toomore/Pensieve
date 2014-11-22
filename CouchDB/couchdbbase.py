# -*- coding: utf-8 -*-
import couchdb

COUCHDB = couchdb.Server()

class CouchDBBase(dict):

    def __init__(self, db_name, _id):
        self.db_name = db_name
        self._id = _id

    def save(self):
        data = COUCHDB[self.db_name].get(self._id, {'_id': self._id})
        data.update(self)
        COUCHDB[self.db_name].save(data)


class Test(CouchDBBase):
    db_name = 'toomoretest'

    def __init__(self, _id):
        super(Test, self).__init__(self.db_name, _id)


if __name__ == '__main__':
    test = Test('oppp')
    test['name'] = 'toomore2'
    test.save()
