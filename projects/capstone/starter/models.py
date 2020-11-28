import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Ourhome

'''
class Ourhome(db.Model):  
  __tablename__ = 'ourhome'

  id = Column(Integer, primary_key=True)
  menu = Column(String)
  description = Column(String)
  cuisine = Column(String)
  preference = Column(Integer)

  def __init__(self, menu, description, cuisine, preference):
    self.menu = menu
    self.description = description
    self.cuisine = cuisine
    self.preference = preference

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'menu': self.menu,
      'description': self.description,
      'cuisine': self.cuisine,
      'preference': self.preference
    }

'''
Cuisine

'''
class Cuisine(db.Model):  
  __tablename__ = 'cuisine'

  id = Column(Integer, primary_key=True)
  type = Column(String)

  def __init__(self, type):
    self.type = type

  def format(self):
    return {
      'id': self.id,
      'type': self.type
    }