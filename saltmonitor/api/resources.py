from flask.ext.restful import Resource
from pymongo import MongoClient

from saltmonitor.utils import jsonify


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
        return jsonify(ret)


class SaltReturns(BaseResource):
    def get(self):
        returns = self.collection.saltReturns
        ret = list(returns.find())
        return jsonify({'results': ret})


class SaltReturn(BaseResource):
    def get(self, jid):
        returns = self.collection.saltReturns
        ret = list(returns.find({'jid': jid}).sort('_id'))
        return jsonify({'results': ret})
