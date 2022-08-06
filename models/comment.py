
from app import db
from models.base import BaseModel

class CommentModel(db.Model, BaseModel):

    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)

    # ForeignKey tells which column to point at so that every comments point to a specific anime. We give it the Primary Key of the anime table: animes.id

    anime_id = db.Column(db.Integer, db.ForeignKey("animes.id", ondelete='CASCADE'), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)

    user = db.relationship('UserModel', backref='user')

  
