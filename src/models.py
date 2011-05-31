from google.appengine.ext import db

class Snippet(db.Model):
    code = db.TextProperty()
    created_at = db.DateProperty(auto_now_add=True)
    rank = db.IntegerProperty()
    submitter = db.UserProperty()
    
    def add_tag(self,tag):
        SnippetTag(snippet=self,tag=tag).save()
    
    def number_of_votings(self):
        pass
#        vote_set.count()

class Tag(db.Model):
    created_at = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()

class SnippetTag(db.Model):
    snippet = db.ReferenceProperty(Snippet,required=True,collection_name='snippets')
    tags = db.ReferenceProperty(Tag,required=True,collection_name='tags')

class Vote(db.Model):
    winner = db.ReferenceProperty(Snippet)
    loser = db.ReferenceProperty(Snippet)
    created_at = db.DateTimeProperty(auto_now_add=True)


    