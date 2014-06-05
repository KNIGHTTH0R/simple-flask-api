Simple Flask API
=======================

Create `<name>.json` by requesting to `http://127.0.0.1:5000/api/<name>` and create and update, get parameters.

========
Install
========

if you use vertualenv,

.. sourcecode:: sh

   $ virtualenv -p python2.7 --no-site-packages --clear --distribute venv
   $ source venv/bin/activate; pip install -r requirements.txt

========
Usage
========

Run Server
-------------

.. sourcecode:: sh

   $ python api.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

Use Curl
----------

.. sourcecode:: sh
    
   ## create 
   $ curl http://127.0.0.1:5000/api/status -D - -X POST --data '{"mode": 1}' -H "Content-type: application/json"
   HTTP/1.0 200 OK
   Content-Type: application/json
   Content-Length: 15
   Server: Werkzeug/0.9.4 Python/2.7.6
   Date: Thu, 05 Jun 2014 00:41:27 GMT

   {
     "mode": 1
   }

   ## get
   $ curl http://127.0.0.1:5000/api/status -D - -X GET
   HTTP/1.0 200 OK
   Content-Type: text/html; charset=utf-8

   {"mode": 1}

   ## update
   $ curl http://127.0.0.1:5000/api/status -D - -X POST --data '{"mode": 2}' -H "Content-type: application/json"
   HTTP/1.0 200 OK
   Content-Type: application/json

   {
     "mode": 2
   }

   ## add another key
   $ curl http://127.0.0.1:5000/api/status -D - -X POST --data '{"guest": true}' -H "Content-type: application/json"
   HTTP/1.0 200 OK
   Content-Type: application/json

   {
     "guest": true,
     "mode": 2
   }

   ## delete key
   $ curl http://127.0.0.1:5000/api/status/mode -D - -X DELETE
   HTTP/1.0 200 OK
   Content-Type: application/json

   {
     "guest": true
   }

Use $.ajax
------------

.. sourcecode:: javascript

   // GET
   $.ajax({
     type: 'GET'
     url:'http://localhost:5000/api/status'
   }).done(function(res){
     // success
   });

   // POST
   $.ajax({
     type: 'POST',
     url:'http://localhost:5000/api/status',
     data: '{"bar":"hoge"}',
     headers: {
       'Content-Type': 'application/json'
     }
   }).done(function(res){
     // success
   });

   // DELETE
   $.ajax({
     type: 'DELETE',
     url:'http://localhost:5000/api/status/bar'
   }).done(function(res){
     // success
   });

========
Test
========

.. sourcecode:: sh
    
   $ py.test test_api.py -v -s
