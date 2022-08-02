from app import db  # <- this means we are importing the object we created -> db = SQLAlchemy(app) from app.py file.
from datetime import *

#  - Flask SQLAlchemy will create tables based on these models.
# below class will have all the COMMON fields that EVERY model will use.
class BaseModel:

  id = db.Column(db.Integer, primary_key=True)  # column means it creates a column with an id

  created_at = db.Column(db.DateTime, default=datetime.utcnow)  # when it created
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) #when is updated

  # Add a methods here to save and delete our model to the database
  def save(self):
    db.session.add(self)
    db.session.commit()


  def remove(self):
    db.session.delete(self)
    db.session.commit()