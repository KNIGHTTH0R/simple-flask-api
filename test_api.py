# coding: utf-8

import os
import requests
from unittest import TestCase

SERVER = 'http://127.0.0.1:5000'
FILE = 'test'


class APITest(TestCase):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json'}

    def tearDown(self):
        file_name = FILE + '.json'
        try:
            os.remove(file_name)
        except Exception:
            pass

    def test_post_new(self):
        # given
        # when
        res = self.post_api('foo', 'bar')
        # then
        self.assertEqual(res.status_code, 200)
        res = self.get_api()
        self.assertEqual(res.json()['foo'], 'bar')
        pass

    def test_post_update(self):
        # given
        res = self.post_api('foo', 'bar')
        self.assertEqual(res.status_code, 200)
        # when
        res = self.post_api('foo', 'hoge')
        # then
        self.assertEqual(res.status_code, 200)
        res = self.get_api()
        self.assertEqual(res.json()['foo'], 'hoge')

    def test_get_no_json(self):
        # given
        # when
        res = self.get_api()
        # then
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.text, basestring)

    def test_get_json(self):
        # given
        res = self.post_api('foo', 'bar')
        self.assertEqual(res.status_code, 200)
        # when
        res = self.get_api()
        # then
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['foo'], 'bar')

    def post_api(self, key, val):
        """POST /api/test"""
        res = requests.post(
            '%s/api/%s' % (SERVER, FILE),
            headers=self.headers,
            data='{"%s":"%s"}' % (key, val)
        )
        return res

    def get_api(self):
        """GET /api/test"""
        res = requests.get(
            '%s/api/%s' % (SERVER, FILE)
        )
        return res
