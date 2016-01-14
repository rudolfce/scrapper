#!/usr/bin/env python3

from flask.ext.script import Manager
from sqlalchemy_utils import create_database, drop_database, database_exists

from scrapper.models import db_url, engine
from scrapper.models.user import Base
from scrapper.controllers import app


manager = Manager(app)

@manager.command
def init_db():
    '''
    Initialize database. Should be run before runserver command. Database details
    can be found (and changed) on scrapper/config/server.py
    '''
    if not database_exists(db_url):
        create_database(db_url)
        Base.metadata.create_all(engine)
        print("Done")
    else:
        print("Database already exists")
        exit(1)

@manager.command
def drop_db():
    '''
    Drops database according to scrapper/config/server.py.
    '''
    if database_exists(db_url):
        drop_database(db_url)
        print("Done")
    else:
        print("Database doesn't exist")
        exit(1)

if __name__=="__main__":
    manager.run()
