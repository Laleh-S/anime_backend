
#* this is controller for animeFilms (also the views.)
# * Flask's router is called Blueprint

# from typing_extensions import Self
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from models.animeFilm import AnimeFilmModel

from serializers.animeFilm import AnimeFilmSchema
from serializers.comment import CommentSchema

animeFilm_schema = AnimeFilmSchema()
comment_schema = CommentSchema()

router = Blueprint("animeFilms", __name__)
STATUS_NOT_FOUND = 404
STATUS_CREATED = 201



#? Get all Anime Films
@router.route("/animeFilms", methods=["GET"])
def get_animeFilms():
    animeFilms = AnimeFilmModel.query.all()
    return animeFilm_schema.jsonify(animeFilms, many=True)



@router.route("/animeFilms/<int:animeFilm_id>", methods=["GET"])
def get_single_animeFilm(animeFilm_id):
    animeFilm = AnimeFilmModel.query.get(animeFilm_id)
    if not animeFilm:
      return { "message": "Anime film not found" }, STATUS_NOT_FOUND

    return animeFilm_schema.jsonify(animeFilm)
    

#? POST An Anime Film!
@router.route("/animeFilms", methods=["POST"])
def create_animeFilm():
    animeFilm_dictionary = request.json
    try:
      animeFilm = animeFilm_schema.load(animeFilm_dictionary)
    
    except ValidationError as e:
      return { "errors": e.messages, "message": "Something went wrong" }

    animeFilm.save()   # save animeFilm , using the methods defined in BaseModel

    return animeFilm_schema.jsonify(animeFilm), STATUS_CREATED   



#? POST A Comment
@router.route('/animeFilms/<int:animeFilm_id>/comments', methods=['POST'])
def create_comment(animeFilm_id):

  comment_dictionary = request.json
  print(comment_dictionary)
  
  try:
    comment = comment_schema.load(comment_dictionary)

  except ValidationError as e:
    return { "errors": e.messages, "message": "Something went wrong" }

  comment.animeFilm_id = animeFilm_id
  comment.save()
  print(comment)

  return comment_schema.jsonify(comment), STATUS_CREATED
    