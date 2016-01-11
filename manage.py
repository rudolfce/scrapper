#!/usr/bin/env python

from flask.ext.script import Manager

from scrapper import app

manager = Manager(app)
#Still no custom commands

@manager.command
def debug_server():
    '''
    Run server in debug mode - allows code injection!!! Don't use on a production
    server.
    '''
    app.run(debug=True)

if __name__=="__main__":
    manager.run()
