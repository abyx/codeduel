from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from src.models import Snippet, Tag
import os

class SubmitPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        login_url = None
        logout_url = users.create_logout_url("/submit")
        if user is None:
            login_url = users.create_login_url("/submit")

        template_values = {
                         'user': user,
                         'login_url': login_url,
                         'logout_url': logout_url
                        }

        path = os.path.join(os.path.dirname(__file__), 'submit.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        #	print self.request.POST
        submitter = users.get_current_user()
        code = self.request.POST.get(u"code")
        title = self.request.POST.get(u"title")
        snippet = Snippet(code=code, submitter=submitter, title=title)
        snippet.put()
        
        tags = self.request.POST.get(u"tags")
        
        if tags is not None and len(tags.strip()) > 0:
            for tag in tags.split():
                tag_obj = Tag(name=tag)
                tag_obj.put()
                snippet.add_tag(tag_obj)
            
