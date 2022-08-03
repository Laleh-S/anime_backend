
# Our seed file, knows about flask, and SQLAlchemy
from app import app, db
from models.animeFilm_data import animeFilms_list, comments_list
from models.user_data import user_list

# This ensures app and db are ready for use, and it provide 'scope' where we can access the app/db.
with app.app_context():
  try:
    print('Recreating database')
    db.drop_all() # Removing everything from the DB
    db.create_all() # This creates the TABLES in the database.

    print("seeding our database")
    db.session.add_all(user_list)
    db.session.commit()

    db.session.add_all(animeFilms_list) # Add a list of things to DB
    db.session.commit() # have to Add and commit. Similar to git.

    #This has to come after making animeFilms. Because you need animeFilms to comment.
    db.session.add_all(comments_list)
    db.session.commit()

    print("Done ✅")
  except Exception as e:
    print(e)
