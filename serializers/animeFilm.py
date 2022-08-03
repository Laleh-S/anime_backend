# sterilizer or schema

from app import ma
from models.animeFilm import AnimeFilmModel
from marshmallow import fields

# ? A schema says how to serialize:
# Python Model -> JSON
# Python Dictionary -> Python Model
class AnimeFilmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
      # A property on this class, where I tell it about my model.
      model = AnimeFilmModel  # This has to be called model
      # need to tell Marshmallow to give back a MODEL when I deserialize, rather than a dictionary
      load_instance = True


# This will nest comments inside of animeFilm First argument is the name of schema to nest. Second argument is if there's a list many=True
    comments = fields.Nested("CommentSchema", many=True)
    
    genres = fields.Nested("GenreSchema", many=True)
