from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
import models

class MainPage(webapp.RequestHandler):
    def get(self):
        self.redirect("/static/map.html")

class MemberScript(webapp.RequestHandler):
    def get(self):
        q = models.Member.all()
        members = q.fetch(200)
        template_values = { 'members' : members }
        path = os.path.join(os.path.dirname(__file__), 'templates', "ceg.js.tmpl")
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage), ('/ceg.js', MemberScript)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
