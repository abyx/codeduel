import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from src.models import Snippet

class SnippetPage(webapp.RequestHandler):
    def get(self):
        template_values = {
                           'snippet': self._get_snippet(),
                           }

        path = os.path.join(os.path.dirname(__file__), 'snippet.html')
        self.response.out.write(template.render(path, template_values))

    def _get_snippet(self):
        return Snippet.get(self.request.get("id"))
