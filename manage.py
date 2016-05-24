#!/usr/bin/env python3
from flask.ext.script import Manager
from sqlalchemy_utils import create_database, database_exists, drop_database

from scrapper import create_app

manager = Manager(create_app)

@manager.command
def init_db():
    '''
    Initialize database. Should be run before runserver command. Database details
    can be found (and changed) on scrapper/config/server.py
    '''
    from scrapper.config.default import SQLALCHEMY_DATABASE_URI as db_url
    from scrapper import db

    if not database_exists(db_url):
        create_database(db_url)
        db.create_all()
        print("Done")
    else:
        print("Database already exists")
        exit(1)

@manager.command
def drop_db():
    '''
    Drops database according to scrapper/config/server.py.
    '''
    from scrapper.config.default import SQLALCHEMY_DATABASE_URI as db_url

    if database_exists(db_url):
        drop_database(db_url)
        print("Done")
    else:
        print("Database doesn't exist")
        exit(1)

if __name__=="__main__":
    manager.run()
