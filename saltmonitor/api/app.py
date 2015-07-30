from flask import Blueprint
from flask.ext.restful import Api

def create_app():
    app = Blueprint('backend', __name__)
    app.debug=True
    api = Api(app)

    from saltmonitor.api.resources import (
        Jobs,
        Job,
        SaltReturns,
        SaltReturn,
    )
    resources = {
        Jobs: '/jobs',
        Job: '/jobs/<jid>',
        SaltReturns: '/returns',
        SaltReturn: '/returns/<jid>',
    }

    for resource, route in resources.items():
        api.add_resource(resource, route)
    return app
