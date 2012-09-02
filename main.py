#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py
IP(REMOTE_ADDR) viewer on Google App Engine

"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import os

class IndexPage(webapp.RequestHandler):
    def get(self):
        host = os.environ['HTTP_HOST']
        self.response.out.write("""
<!DOCTYPE html>
<html>
<body>
<a href="http://%s/ip">ip</a><br />
<br />
<a href="http://twitter.com/wataken44">@wataken44</a>
</body>
</html>
""" % host)

    def head(self):
        pass

class IPPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        addr = os.environ['REMOTE_ADDR']
        self.response.out.write(addr)

    def head(self):
        pass

def main():
    application = webapp.WSGIApplication(
        [('/', IndexPage),
         ('/ip', IPPage)]
        )
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
