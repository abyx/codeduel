import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp

class DuelPage(webapp.RequestHandler):
    def get(self):
        template_values = {
            'greetings': 'hello',
            'url': 'http://www.google.com',
            'url_linktext': 'google',
        }

        path = os.path.join(os.path.dirname(__file__), 'duel.html')
        self.response.out.write(template.render(path, template_values))
