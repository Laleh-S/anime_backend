

from app import db
from models.base import BaseModel

ANIME_FILM_TABLE_NAME = "AnimeFilms"

# AnimeModel EXTENDS BaseModel and db.Model. Extending db.Model lets Flask-SQLAlchemy KNOW about our model, so it can use it.
class AnimeFilmModel(db.Model, BaseModel):

  # This will be used DIRECTLY to make a TABLE in Postgresql
  __tablename__ = ANIME_FILM_TABLE_NAME

  # Specific columns for our Anime Table.
  title = db.Column(db.Text, nullable=False, unique=True)
  original_title = db.Column(db.Text, nullable=False)
  image = db.Column(db.Text, nullable=False)
  director = db.Column(db.Text, nullable=False)
  producer = db.Column(db.Text, nullable=False)
  release_date = db.Column(db.Integer, nullable=False)
  description = db.Column(db.Text, nullable=False)
