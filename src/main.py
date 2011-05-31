from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from src.snippet import SnippetPage
from src.duel_page import DuelPage
from src.submit import SubmitPage
from src.top import TopPage
import os

class MainPage(webapp.RequestHandler):
  def get(self):
    template_values = {
        'greetings': 'hello',
        'url': 'http://www.google.com',
        'url_linktext': 'google',
        }

    path = os.path.join(os.path.dirname(__file__), 'main.html')
    self.response.out.write(template.render(path, template_values))


application = webapp.WSGIApplication(
                                     [('/', DuelPage),
                                      ('/submit', SubmitPage),
                                      ('/snippet', SnippetPage),
                                      ('/top', TopPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
