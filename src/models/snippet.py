from google.appengine.ext import db

class Snippet(db.Model):
    code = db.TextProperty()
    created_at = db.DateProperty(auto_now_add=True)
    rank = db.IntegerProperty()
    submitter = db.UserProperty()
    
    
    def number_of_votings(self):
        pass
#        vote_set.count()
    