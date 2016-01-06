#!/usr/bin/env python

from flask.ext.script import Manager

from scrapper import app

manager = Manager(app)
#Still no custom commands

if __name__=="__main__":
    manager.run()
