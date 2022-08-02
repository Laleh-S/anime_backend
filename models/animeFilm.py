

from app import db
from models.base import BaseModel

from models.animeFilm_genre import animeFilm_genre
# ! Gotta import NoteModel in here, for like 18 to create the relationship.
from models.genre import GenreModel

ANIME_FILM_TABLE_NAME = "animeFilms"

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


# Letting flask-sqlalchemy know about my new table for tea_note
    # This is similar to relatinonship for comments, but we tell 
    # it about the JOIN TABLE.
  genres = db.relationship('GenreModel', backref='genres', secondary=animeFilm_genre)