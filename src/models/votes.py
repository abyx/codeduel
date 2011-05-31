from google.appengine.ext import db
from snippet import Snippet

class Vote(db.Model):
    winner = db.ReferenceProperty(Snippet)
    loser = db.ReferenceProperty(Snippet)
    created_at = db.DateTimeProperty(auto_add_now=True)
    