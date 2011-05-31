from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from src.models import Snippet
import os

class UserDisplay(object):
    
    def __init__(self, nickname, snippets):
        self._nickname = nickname
        self._snippets = snippets
        
    @property
    def nickname(self):
        return self._nickname

    @property
    def snippets(self):
        return self._snippets
    
    @property
    def rank(self):
        if len(self._snippets) > 0:
            return sum([s.rank for s in self._snippets]) / len(self._snippets)
        
        return 0

    @property
    def tags(self):
        tags = set()
        for s in self._snippets:
            tags.update(s.tags)
        
        return tags 

class UserPage(webapp.RequestHandler):
    def get(self):
        template_values = {
                           'user': self._get_user(),
                           }

        path = os.path.join(os.path.dirname(__file__), 'snippet.html')
        self.response.out.write(template.render(path, template_values))


    def _get_all_users(self):
        all_snips = Snippet.all()
        return dict((s.submitter.nickname, s.submitter) for s in all_snips)
    
    def _get_snippets_for_nick(self, nickname):
        all_snips = Snippet.all()
        return [s for s in all_snips if s.submitter.nickname == nickname]

    def _get_user(self):
        users = self._get_all_users()
        nickname = users[self.request.get("nickname")]
        return UserDisplay(nickname, self._get_snippets_for_nick(nickname))
