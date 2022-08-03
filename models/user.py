
from sqlalchemy.ext.hybrid import hybrid_property

from app import db, bcrypt
from models.base import BaseModel


class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)

    # We want to set a password field that doens't get saved to the db, because we don't want to save original passswrod.
    # this will ensure you can provide a password field to this model when you try to create a User.
    # This password will not be saved to db.
    @hybrid_property
    def password(self):
        print("inside password hash method")
        pass # <- means don't do anything
    # We then use this password function as a decorator. It'll get called by Flask SQLAlchemy when pipenv the model gets created, BEFORE saving to the DB.
    @password.setter
    def password(self, password_plaintext):
        print("inside password hash method")

        # Write our code to hash the password. It will give us back an encoded pw
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)


        # The decoded password, that we actually want to store.
        self.password_hash = encoded_pw.decode('utf-8')
