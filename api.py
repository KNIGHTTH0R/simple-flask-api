# coding: utf-8

import json
from flask import Flask, request, jsonify, abort

FILE = 'status.json'
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'hello:)'


@app.route('/api/<status>', methods=['POST', 'GET'])
def status(status):
    if request.method == 'POST':
        return post_status(status, request)
    elif request.method == 'GET':
        return get_status(status)
    else:
        return abort(405)


@app.route('/api/<status>/<key>', methods=['DELETE'])
def del_status(status, key):
    if request.method == 'DELETE':
        return delete_status(status, key)
    else:
        return abort(405)


def get_status(status):
    file_name = status + '.json'
    try:
        f = open(file_name, 'r')
        data = json.load(f)
        f.close()
    except Exception:
        return "NOT FOUND"
    return json.dumps(data)


def post_status(status, request):
    file_name = status + '.json'
    req = json.loads(request.data)
    try:
        f = open(file_name, 'r')
        data = json.load(f)
    except Exception:
        data = {}
    for item in req.keys():
        if item in set(data.keys()):
            data.update(req)
        else:
            val = req[item]
            data[item] = val
    f = open(file_name, 'w')
    json.dump(data, f, sort_keys=True, indent=4)
    f.close()
    return jsonify(data)


def delete_status(status, key):
    file_name = status + '.json'
    req = key
    try:
        f = open(file_name, 'r')
        data = json.load(f)
    except Exception:
        return "NOT FOUND"
    for item in data.keys():
        if req in set(data.keys()):
            data.pop(req)

    f = open(file_name, 'w')
    json.dump(data, f, sort_keys=True, indent=4)
    f.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
