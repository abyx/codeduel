from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from src.models import Snippet
import os

LIMIT_TOP_RANKS = 5

class TopPage(webapp.RequestHandler):

    def get(self):
        template_values = {
                           'top_num' : LIMIT_TOP_RANKS,
                           'snippets': self._get_sorted_snippets()
                          }

        path = os.path.join(os.path.dirname(__file__), 'top.html')
        self.response.out.write(template.render(path, template_values))
    
    def _get_sorted_snippets(self):
        query = Snippet.all().order("rank")
        return query.fetch(limit = LIMIT_TOP_RANKS)

