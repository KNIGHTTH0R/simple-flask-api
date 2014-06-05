# coding: utf-8

import json
from flask import Flask, request, jsonify, abort
from db import get_item, set_item, remove_item


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'hello:)'


@app.route('/api/<key>', methods=['POST', 'GET'])
def api(key):
    if request.method == 'POST':
        return post_api(key, request)
    elif request.method == 'GET':
        return get_api(key)
    else:
        return abort(405)


@app.route('/api/<key>/<dict_key>', methods=['DELETE'])
def del_api(key, dict_key):
    if request.method == 'DELETE':
        return delete_api(key, dict_key)
    else:
        return abort(405)


def get_api(key):
    res = get_item(key)
    if res is None:
        return "NOT FOUND"
    else:
        return jsonify(res)


def post_api(key, request):
    req = json.loads(request.data)
    res = set_item(key, req)
    return jsonify(res)


def delete_api(key, dict_key):
    res = remove_item(key, dict_key)
    if res is None:
        return "NOT FOUND"
    else:
        return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
