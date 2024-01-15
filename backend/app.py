from json import loads
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime
import cvxopt as opt
from get_selic import get_selic
from mock_data import mock_data

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return {
        "message": "Projeto Markowitz API",
    }

data = mock_data()
data = loads(data)

@app.route('/graph')
@cross_origin()
def graph():
    return jsonify(data)