from json import loads
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from datetime import datetime
import cvxopt as opt
from get_selic import get_selic
from mock_data import mock_data
from get_graph import get_graph

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return {
        "message": "Projeto Markowitz API",
    }

@app.route('/graph', methods=['POST'])
@cross_origin()
def graph():
    data = request.get_json()
    start_date = data['start']
    end_date = data['end']
    return jsonify(get_graph(start_date, end_date))