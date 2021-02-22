import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# The owner of my local database is postgres , the password is 'admin' , replace this connection string info with yours.
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:admin@localhost:5432/fyyur'
