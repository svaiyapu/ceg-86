from google.appengine.ext import db

class Member(db.Model):
    fn = db.StringProperty()
    ln = db.StringProperty()
    dpt = db.StringProperty()
    sec = db.StringProperty() 
    loc = db.StringProperty() 
    faddr = db.StringProperty() 
    lat = db.FloatProperty() 
    lng = db.FloatProperty() 
