
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.environment import db_URI
from flask_marshmallow import Marshmallow 


app = Flask(__name__)

# Configuring it with flask. Telling flask-sqlalchemy where the database lives in our machine.
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI 
# Removes a warning for a part of the library that we are not using.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Plugging in Flask SQLAlchemy. it means: 
# "SQLAlchemy" is a class and "app" is an object that we are passing through
# we are telling SQLalchemy about flask so we can use it in diffrent ways.
db = SQLAlchemy(app) 

ma = Marshmallow(app)

from controllers import animeFilms, genres

app.register_blueprint(animeFilms.router, url_prefix="/api")
app.register_blueprint(genres.router, url_prefix="/api")
