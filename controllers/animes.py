
#* this is controller for animes (also the views.)
# * Flask's router is called Blueprint

# from typing_extensions import Self
from curses.ascii import HT
from http import HTTPStatus
from flask import Blueprint, request, g
from marshmallow.exceptions import ValidationError

from models.anime import animeModel
from models.comment import CommentModel
from models.genre import GenreModel

from serializers.anime import animeSchema
from serializers.comment import CommentSchema
from serializers.genre import GenreSchema

from middleware.secure_route import secure_route


anime_schema = animeSchema()
comment_schema = CommentSchema()

router = Blueprint("animes", __name__)



#? GET all Anime Films 
@router.route("/animes", methods=["GET"])
def get_animes():
    animes = animeModel.query.all()
    return anime_schema.jsonify(animes, many=True)


#? GET a Single Anime Film
@router.route("/animes/<int:anime_id>", methods=["GET"])
def get_single_anime(anime_id):
    anime = animeModel.query.get(anime_id)
    if not anime:
      return { "message": "Anime film not found" }, HTTPStatus.NOT_FOUND

    return anime_schema.jsonify(anime)


#? POST An Anime Film!
@router.route("/animes", methods=["POST"])
@secure_route
def create_anime():
    anime_dictionary = request.json
    try:
      anime = anime_schema.load(anime_dictionary)
    
    except ValidationError as e:
      return { "errors": e.messages, "message": "Something went wrong" }

    anime.user_id = g.current_user.id
    anime.save()   # save anime , using the methods defined in BaseModel
    return anime_schema.jsonify(anime), HTTPStatus.CREATED 


#? PUT an Anime Film
@router.route("/animes/<int:anime_id>", methods=["PUT"])
@secure_route
def update_anime(anime_id):
    anime_dictionary = request.json
    existing_anime = animeModel.query.get(anime_id)

    if not existing_anime:
        return {"message": "Anime not found"}, HTTPStatus.NOT_FOUND
    
    if not g.current_user.id == existing_anime.user_id:
        return {"message": "Not your anime!"}, HTTPStatus.UNAUTHORIZED

    try:
        anime = anime_schema.load(anime_dictionary, instance=existing_anime, partial=True)
    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}
    anime.save()

    return anime_schema.jsonify(anime), HTTPStatus.OK


#? DELETE an Anime Film
@router.route("/animes/<int:anime_id>", methods=["DELETE"])
@secure_route
def remove_anime(anime_id):
    anime = animeModel.query.get(anime_id)

    if not anime:
        return {"message": "Anime not found"}, HTTPStatus.NOT_FOUND

    anime.remove()

    return '', HTTPStatus.NO_CONTENT




#? POST A Comment 
@router.route('/animes/<int:anime_id>/comments', methods=['POST'])
@secure_route
def create_comment(anime_id):
  comment_dictionary = request.json
  
  try:
    comment = comment_schema.load(comment_dictionary)

  except ValidationError as e:
    return { "errors": e.messages, "message": "Something went wrong" }
    
  comment.anime_id = anime_id
  comment.user_id = g.current_user.id
  
  comment.save()
  return comment_schema.jsonify(comment),  HTTPStatus.CREATED


#? PUT a Comment
@router.route("/animes/<int:anime_id>/comments/<int:comment_id>", methods=["PUT"])
@secure_route
def update_comment(anime_id, comment_id):

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
    anime = animeModel.query.get(anime_id)

    if not anime:
        return {"message": "Anime Film not found"}, HTTPStatus.NOT_FOUND

    return anime_schema.jsonify(anime), HTTPStatus.OK



#? DELETE a Comment
@router.route("/animes/<int:anime_id>/comments/<int:comment_id>", methods=["DELETE"])
@secure_route
def remove_comment(anime_id, comment_id):

    comment = CommentModel.query.get(comment_id)

    if not comment:
        return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND

    comment.remove()

    anime = animeModel.query.get(anime_id)

    if not anime:
        return {"message": "anime not found"}, HTTPStatus.NOT_FOUND

    return anime_schema.jsonify(anime), HTTPStatus.OK




#? Creating a relationship) between anime and Genre *****
@router.route("/animes/<int:anime_id>/genres/<int:genre_id>", methods=["POST"])
@secure_route
def create_anime_genre(anime_id, genre_id):
    
# This assumes both the genre and the anime exists. 
    anime = animeModel.query.get(anime_id)
    genre = GenreModel.query.get(genre_id)

    if not genre or not anime:
        return {"message": "Item not found"}, HTTPStatus.NOT_FOUND

    # ! This is possible cuz of the relationship field in animeModel
    anime.genres.append(genre)    # Add the genre to the anime. This defines the relationship.

    anime.save()

    return anime_schema.jsonify(anime), HTTPStatus.OK  