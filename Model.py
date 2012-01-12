#!/usr/bin/env python

from google.appengine.ext import db
import urllib2

  
class Description(db.Model):
  text = db.StringProperty(required=True)
  added = db.DateProperty(auto_now_add=True)

class Experience(db.Model):
  added = db.DateProperty(auto_now_add=True)
  date_start = db.DateProperty()
  date_end = db.DateProperty()
  organization = db.StringProperty()
  description = db.ListProperty(db.Key)

class Title(db.Model):
  category = db.StringProperty(required=True, choices=set(['Work', 'Education', 'Volunteer', 'Awards', 'Publication', 'Other']))
  title = db.StringProperty(required=True)
  added = db.DateProperty(auto_now_add=True)
  experiences = db.ListProperty(db.Key)
    

#Key for a Resume is the key of the user it belongs to
class Resume(db.Model):
  phones = db.ListProperty(db.PhoneNumber)
  address = db.ListProperty(db.PostalAddress)
  emails = db.ListProperty(db.Email)
  g_user = db.UserProperty()
  titles = db.ListProperty(db.Key)
    
