
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request
from models.user import UserModel
from serializers.user import UserSchema
# from marshmallow.exceptions import ValidationError

user_schema = UserSchema()

router = Blueprint("users", __name__)

@router.route('/register', methods=["POST"])
def register():
  

    try:
        user_dictionary = request.json
        user = user_schema.load(user_dictionary)
        user.save()
        return user_schema.jsonify(user)
    # Specific error
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}
    # General error
    except Exception as e:
        return { "messages": "Something went wrong" }