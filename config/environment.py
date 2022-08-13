# postgresql: is our database driver which a protocol that a database uses.
# localhost:5432: is postgress's port
# db_URI = "postgresql://postgres:laleh@localhost:5432/animes_db"
# secret = "thisismyverysecretsecret"

db_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:laleh@localhost:5432/animes_db')
secret = os.getenv('SECRET', 'thisismyverysecretsecret')