from http import HTTPStatus

from flask import Blueprint, request  #request gives you a dictionary which reperesnts json
from marshmallow.exceptions import ValidationError

from models.genre import GenreModel
from serializers.genre import GenreSchema

genre_schema = GenreSchema()

router = Blueprint("genres", __name__)


#? POST Genre
@router.route("/genres", methods=["POST"])
def create_genre():
    genre_dictionary = request.json

    try:
        genre = genre_schema.load(genre_dictionary)
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}
    genre.save()
    return genre_schema.jsonify(genre)


#? DELETE Genre
@router.route("/genres/<int:genre_id>", methods=["DELETE"])
def remove_genre(genre_id):
    genre = GenreModel.query.get(genre_id)

    if not genre:
        return {"message": "Genre not found"}, HTTPStatus.NOT_FOUND
    genre.remove()
    return '', HTTPStatus.NO_CONTENT