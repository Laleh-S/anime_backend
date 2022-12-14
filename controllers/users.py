from http import HTTPStatus
from flask import Blueprint, request
from models.user import UserModel
from serializers.user import UserSchema
from marshmallow.exceptions import ValidationError

user_schema = UserSchema()

router = Blueprint("users", __name__)

#? Register a User
@router.route('/register', methods=["POST"])
def register():
  
    try:
        user_dictionary = request.json
        print('USER DICTIONARY', user_dictionary)
        if (user_dictionary['password'] != user_dictionary['passwordConfirmation']):
          raise ValidationError('password and password confirmation don\'t match')
        user = user_schema.load({
          'username': user_dictionary['username'],
          'email': user_dictionary['email'],
          'password': user_dictionary['password']
        })
        user.save()
        print('USER', user)
        return user_schema.jsonify(user)
    # Specific error
    except ValidationError as e:
        print('VALIDATION ERROR', e.messages)
        return {"errors": e.messages, "messages": "Something went wrong"}
    # General error
    except Exception as e:
        print('EXCEPTION', e.messages)
        return { "messages": "Something went wrong" }


#? Login a User
@router.route('/login', methods=["POST"])
def login():
    try:
        # Get the credentials for logging in.
        credentials_dictionary = request.json
        # First, grab the user from postgresql by their email
        user = UserModel.query.filter_by(email=credentials_dictionary["email"]).first()
        # Of there's no user, return
        if not user:
            return {"message": "No user found for this email"}
        # Check the password matches the hashed one stored.
        if not user.validate_password(credentials_dictionary["password"]):
            return {"message": "You are not authorized"}, HTTPStatus.UNAUTHORIZED
        # Make a token
        token = user.generate_token()
        # Send it back
        return {"user_id": user.id, "token": token, "message": "Welcome back!"}
    
    except Exception as e:
        return { "messages": "Something went wrong" }