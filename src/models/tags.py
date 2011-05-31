from google.appengine.ext import db
from snippet import Snippet

class Tag(db.Model):
    created_at = db.DateTimeProperty(auto_add_now=True)
    name = db.StringProperty()

class SnippetTag(db.Model):
    snippet = db.ReferenceProperty(Snippet,required=True,collection_name='snippets')
    tags = db.ReferenceProperty(Tag,required=True,collection_name='tags')
    