# -*- coding: utf-8 -*-

import json

from flask import Flask, request, jsonify


app = Flask(__name__)


"""Routing: リクエストの URI とメソッドに応じた処理を呼び出し、結果を返す。"""
@app.route('/', methods=['GET'])
def hello():
    return 'hello:)'


@app.route('/api/<key>', methods=['GET'])
def get(key):
    model = get_model(key)
    if model is None:
        return "NOT FOUND"
    else:
        return jsonify(model)


@app.route('/api/<key>', methods=['POST'])
def post(key):
    print request.data
    result = set_property(key, json.loads(request.data))
    return jsonify(result)


@app.route('/api/<key>/<property_name>', methods=['DELETE'])
def delete(key, property_name):
    result = delete_property(key, property_name)
    if result is None:
        return "NOT FOUND"
    else:
        return jsonify(result)


"""モデルに対する操作"""
def get_model(key):
    return read_model(key)


def set_property(key, properties):
    data = read_model(key)
    if data is None:
        data = {}
    data.update(properties)
    result = write_model(key, data)
    return result


def delete_property(key, property_name):
    data = read_model(key)
    if data is None:
        return None
    if property_name not in data:
        return None
    del data[property_name]
    result = write_model(key, data)
    return result


"""永続化層アクセス"""
def read_model(key):
    file_name = key + '.json'
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except IOError as e:
        print e
        return None


def write_model(key, data):
    file_name = key + '.json'
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4)
            return data
    except IOError as e:
        print e
        return None


if __name__ == '__main__':
    app.run(debug=True)
