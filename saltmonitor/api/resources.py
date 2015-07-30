from flask import jsonify
from flask.ext.restful import Resource
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
collection = client.salt


class Jobs(Resource):
    def get(self):
        jobs = collection.jobs
        ret = list(jobs.find({'fun': 'state.highstate'}).sort('jid'))
        for x in ret:
            x['_id'] = str(x['_id'])
        return jsonify({'jobs': ret})


class Job(Resource):
    def get(self, jid):
        jobs = collection.jobs
        ret = jobs.find_one({'jid': jid})
        ret['_id'] = str(ret['_id'])
        return jsonify(ret)


class SaltReturns(Resource):
    def get(self):
        returns = collection.saltReturns
        ret = list(returns.find())
        for x in ret:
            x['_id'] = str(x['_id'])
        return jsonify({'results': ret})


class SaltReturn(Resource):
    def get(self, jid):
        returns = collection.saltReturns
        ret = list(returns.find({'jid': jid}).sort('return.__run_num__'))
        for x in ret:
            x['_id'] = str(x['_id'])
        return jsonify({'results': ret})