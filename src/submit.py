import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from src.models import Snippet
from google.appengine.api import users

class SubmitPage(webapp.RequestHandler):
  def get(self):
    template_values = {
        'greetings': 'hello',
        'url': 'http://www.google.com',
        'url_linktext': 'google',
	'user': users.get_current_user(),
        }

    path = os.path.join(os.path.dirname(__file__), 'submit.html')
    self.response.out.write(template.render(path, template_values))

  def post(self):
#	print self.request.POST
   submitter = users.get_current_user()
   code = self.request.POST.get(u"code")
   title = self.request.POST.get(u"title")
   snippet = Snippet(code=code, submitter=submitter, title=title)
#   snippet.addTag(
   snippet.put()
