from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models import *
import os
from random import shuffle

class DuelPage(webapp.RequestHandler):
    def get(self):
        
        all_snippets = list(Snippet.all())
        shuffle(all_snippets)
        
        
        template_values = {
            'snippet_one': all_snippets[0],
            'snippet_two': all_snippets[1],
            'url': 'http://www.google.com',
            'url_linktext': 'google',
        }

        path = os.path.join(os.path.dirname(__file__), 'duel.html')
        self.response.out.write(template.render(path, template_values))
        
    def post(self):
        winner = Snippet.get(self.request.get('winning'))
        loser = Snippet.get(self.request.get('losing'))
        Vote(winner=winner,loser=loser).put()
        winner.rank += 1
        winner.put()
        self.redirect("/")
