import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from models import *

class DuelPage(webapp.RequestHandler):
    def get(self):
        template_values = {
            'snippet_one': Snippet.all()[0],
            'snippet_two': Snippet.all()[1],
            'url': 'http://www.google.com',
            'url_linktext': 'google',
        }

        path = os.path.join(os.path.dirname(__file__), 'duel.html')
        self.response.out.write(template.render(path, template_values))
