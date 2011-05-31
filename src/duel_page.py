from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models import *
import os

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
        
    def post(self):
        winner_key = self.request.get('winner')
        loser_key = self.request.get('loser')
        winner = Snippet.get(winner_key)
        loser = Snippet.get(loser_key)
        Vote(winner=winner,loser=loser).put()
        winner.rank = winner.rank + 1
        winner.put()
