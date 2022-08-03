
#* this is controller for animeFilms (also the views.)
# * Flask's router is called Blueprint

# from typing_extensions import Self
from http import HTTPStatus
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from models.animeFilm import AnimeFilmModel
from models.comment import CommentModel

from serializers.animeFilm import AnimeFilmSchema
from serializers.comment import CommentSchema

animeFilm_schema = AnimeFilmSchema()
comment_schema = CommentSchema()

router = Blueprint("animeFilms", __name__)
STATUS_NOT_FOUND = 404
STATUS_CREATED = 201



#? GET all Anime Films
@router.route("/animeFilms", methods=["GET"])
def get_animeFilms():
    animeFilms = AnimeFilmModel.query.all()
    return animeFilm_schema.jsonify(animeFilms, many=True)



#? GET a Single Anime Film
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




#? PUT a Comment
@router.route("/animeFilms/<int:animeFilm_id>/comments/<int:comment_id>", methods=["PUT"])
def update_comment(animeFilm_id, comment_id):

    comment_dictionary = request.json
    existing_comment = CommentModel.query.get(comment_id)

    if not existing_comment:
        return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND

    try:
        comment = comment_schema.load(
            comment_dictionary,  # <-  This ia all the filed we are changing
            instance=existing_comment,  # <- This is the existing comment we are updating
            partial=True  # <- This allows us to only provide the filels you're changing. if you don't include this part it expects you to change the whole thing.
        )

    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}
    comment.save()
    animeFilm = AnimeFilmModel.query.get(animeFilm_id)

    if not animeFilm:
        return {"message": "Anime Film not found"}, HTTPStatus.NOT_FOUND

    return animeFilm_schema.jsonify(animeFilm), HTTPStatus.OK




#? DELETE a Comment
@router.route("/animeFilms/<int:animeFilm_id>/comments/<int:comment_id>", methods=["DELETE"])
def remove_comment(animeFilm_id, comment_id):

    comment = CommentModel.query.get(comment_id)

    if not comment:
        return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND

    comment.remove()

    animeFilm = AnimeFilmModel.query.get(animeFilm_id)

    if not animeFilm:
        return {"message": "AnimeFilm not found"}, HTTPStatus.NOT_FOUND

    return animeFilm_schema.jsonify(animeFilm), HTTPStatus.OK