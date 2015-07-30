from flask import jsonify
from flask.ext.restful import Resource
from pymongo import MongoClient

# connect=False for https://jira.mongodb.org/browse/PYTHON-961

class BaseResource(Resource):
    client = None
    def __new__(cls, *args, **kwargs):
        if BaseResource.client is None:
            BaseResource.client = MongoClient('mongodb://localhost:27017/', connect=False)
            BaseResource.collection = BaseResource.client.salt
        object.__new__(cls)
        cls.collection = BaseResource.collection
        return super(BaseResource, cls).__new__(cls)


class Jobs(BaseResource):
    def get(self):
        jobs = self.collection.jobs
        ret = list(jobs.find().sort('jid', -1))
        for x in ret:
            x['_id'] = str(x['_id'])
        return jsonify({'jobs': ret})


class Job(BaseResource):
    def get(self, jid):
        jobs = self.collection.jobs
        ret = jobs.find_one({'jid': jid})
        ret['_id'] = str(ret['_id'])
        return jsonify(ret)


class SaltReturns(BaseResource):
    def get(self):
        returns = self.collection.saltReturns
        ret = list(returns.find())
        for x in ret:
            x['_id'] = str(x['_id'])
        return jsonify({'results': ret})


class SaltReturn(BaseResource):
    def get(self, jid):
        returns = self.collection.saltReturns
        ret = list(returns.find({'jid': jid}).sort('_id'))
        for x in ret:
            x['_id'] = str(x['_id'])
        return jsonify({'results': ret})
