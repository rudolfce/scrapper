from sqlalchemy_utils import create_database, drop_database, database_exists

from .__init__ import engine, db_url, Base
from .models import User


def initdb():
    '''
    Initialize the database according to db_url, built from config/db_data.json.
    Returns 0 if no error is found and 1 if database already exists.
    '''
    if not database_exists(db_url):
        create_database(db_url)
        Base.metadata.create_all(engine)
        return 0
    else:
        return 1

def dropdb():
    '''
    Drops the database according to db_url, built from config/db_data.json.
    Returns 0 if no error is found and 1 if database doesn't exist.
    '''
    if database_exists(db_url):
        drop_database(db_url)
        return 0
    else:
        return 1
