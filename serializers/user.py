from marshmallow import fields

from app import ma
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        # New capabilities of marshmallow! Must add the comma for it to be a TUPPLE
        exclude = ("password_hash",)
        # ONLY INCLUDE THESE FIELDS IN DESERIALIZATION (.load method)
        load_only = ('email', 'password')

    # Tells serializer to expect a password field
    # (in other words, because it's a column in User)
    password = fields.String(required=True)
