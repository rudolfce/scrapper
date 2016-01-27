from flask import Flask, redirect
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('scrapper.config.server')
    db.init_app(app)

    from scrapper.controllers import twitter
    
    app.register_blueprint(twitter)

    # Only one app so far, so why not?
    @app.route('/')
    def index():
       return redirect('/twitter/')

    return app
