

from app import db
from models.base import BaseModel

from models.anime_genre import anime_genre
from models.genre import GenreModel
from models.comment import CommentModel
from models.user import UserModel



# AnimeModel EXTENDS BaseModel and db.Model. Extending db.Model lets Flask-SQLAlchemy KNOW about our model, so it can use it.
class animeModel(db.Model, BaseModel):

  # This will be used DIRECTLY to make a TABLE in Postgresql
  __tablename__ = "animes"

  # Specific columns for our Anime Table.
  title = db.Column(db.Text, nullable=False, unique=True)
  original_title = db.Column(db.Text, nullable=False)
  image = db.Column(db.Text, nullable=False)
  director = db.Column(db.Text, nullable=False)
  producer = db.Column(db.Text, nullable=False)
  release_date = db.Column(db.Integer, nullable=False)
  description = db.Column(db.Text, nullable=False)

  user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
# Letting flask-sqlalchemy know about my new table for tea_note
    # This is similar to relatinonship for comments, but we tell 
    # it about the JOIN TABLE.
  genres = db.relationship('GenreModel', backref='genres', secondary=anime_genre)
  comments = db.relationship('CommentModel', backref='comments', cascade="all, delete")

  user = db.relationship('UserModel', backref='users')
