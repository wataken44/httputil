#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py
IP(REMOTE_ADDR) viewer on Google App Engine

"""

from flask import Flask, make_response, request

app=Flask(__name__)

@app.route("/")
def index():
    host = request.environ['HTTP_HOST']
    return """<!DOCTYPE html>
<html>
<body>
<a href="http://%s/ip">ip</a><br />
<br />
<a href="http://twitter.com/wataken44">@wataken44</a>
</body>
</html>
""" % host 


@app.route("/ip")
def ip():
    addr = request.environ['REMOTE_ADDR']
    resp = make_response(addr)

    resp.headers['Content-Type'] = 'text/plain'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
