
from app import db
from models.base import BaseModel

class CommentModel(db.Model, BaseModel):

    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)

    # ForeignKey tells which column to point at so that every comments point to a specific animeFilm. We give it the Primary Key of the animeFilm table: animeFilms.id
  
    # animeFilm_id = db.Column(db.Integer, db.ForeignKey('{0}.id'.format(ANIME_FILM_TABLE_NAME), ondelete='CASCADE'), nullable=False)
    animeFilm_id = db.Column(db.Integer, db.ForeignKey("animeFilms.id", ondelete='CASCADE'), nullable=False)

    # #  This line is for serialization. Tells our comment about our animeFilm model. Assosciates 2 models together.
    # #  It won't make a new column, but instead, specifies a relationship between 2 models.
    # # ? backref should be the table name of this current table.
    # animeFilm = db.relationship("AnimeFilmModel", backref="comments", cascade="all, delete")
