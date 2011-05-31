from google.appengine.ext import db

class Snippet(db.Model):
    code = db.TextProperty()
    title = db.StringProperty()
    created_at = db.DateProperty(auto_now_add=True)
    rank = db.IntegerProperty()
    submitter = db.UserProperty()
    
    def add_tag(self,tag):
        SnippetTag(snippet=self,tag=tag).put()
    
    def number_of_votings(self):
        pass
#        vote_set.count()

class Tag(db.Model):
    created_at = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()

class SnippetTag(db.Model):
    tag = db.ReferenceProperty(Tag,required=True,collection_name='snippets')
    snippet = db.ReferenceProperty(Snippet,required=True,collection_name='tags')

class Vote(db.Model):
    winner = db.ReferenceProperty(Snippet,collection_name="winning_votes")
    loser = db.ReferenceProperty(Snippet,collection_name="losing_votes")
    created_at = db.DateTimeProperty(auto_now_add=True)


    