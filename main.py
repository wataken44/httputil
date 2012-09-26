#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py
IP(REMOTE_ADDR) viewer on Google App Engine

"""

import webapp2
import os

class IndexPage(webapp2.RequestHandler):
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

class IPPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        addr = os.environ['REMOTE_ADDR']
        self.response.out.write(addr)

    def head(self):
        pass

application = webapp2.WSGIApplication(
    [('/', IndexPage),
     ('/ip', IPPage)]
    )

if __name__ == "__main__":
    main()
