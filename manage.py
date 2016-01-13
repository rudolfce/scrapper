#!/usr/bin/env python

from flask.ext.script import Manager

from controller import app
from model.management import initdb, dropdb

manager = Manager(app)

@manager.command
def init_db():
    '''
    Initialize database. Should be run before runserver command. Database details
    can be found (and changed) on config/db_data.json.
    '''
    if initdb():
        print("Database already exists")
        exit(1)
    else:
        print("Done")

@manager.command
def drop_db():
    '''
    Drops database according to config/db_data.json.
    '''
    if dropdb():
        print("Database doesn't exist")
        exit(1)
    else:
        print("Done")

if __name__=="__main__":
    manager.run()
