from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config['DEBUG'] = True

import saltmonitor.api.app
app.register_blueprint(saltmonitor.api.app.create_app())
