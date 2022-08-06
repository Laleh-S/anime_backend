from app import db

anime_genre = db.Table ('animes_genres',
    db.Column('anime_id', db.Integer, db.ForeignKey('animes.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)