from app import db

animeFilm_genre = db.Table ('animeFilms_genres',
    db.Column('animeFilm_id', db.Integer, db.ForeignKey('animeFilms.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)