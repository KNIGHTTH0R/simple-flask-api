# coding: utf-8

import json


def get_item(key):
    file_name = key + '.json'
    try:
        f = open(file_name, 'r')
        data = json.load(f)
        f.close()
        return data
    except Exception:
        return None


def set_item(key, obj):
    file_name = key + '.json'
    res = get_item(key)
    if res is None:
        data = {}
    else:
        data = res
    data.update(obj)
    f = open(file_name, 'w')
    json.dump(data, f, sort_keys=True, indent=4)
    f.close()
    return data


def remove_item(key, dict_key):
    file_name = key + '.json'
    try:
        f = open(file_name, 'r')
        data = json.load(f)
    except Exception:
        return None
    if dict_key in set(data.keys()):
        data.pop(dict_key)
    else:
        return None
    f = open(file_name, 'w')
    json.dump(data, f, sort_keys=True, indent=4)
    f.close()
    return data
