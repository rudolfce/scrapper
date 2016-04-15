from flask import Flask, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from celery import Celery


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('scrapper.config.server')
    db.init_app(app)

    from scrapper.controllers import twitter_bp

    app.register_blueprint(twitter_bp)

    # Only one app so far, so why not?
    @app.route('/')
    def index():
       return redirect('/twitter/')

    return app

def make_celery():
    app = create_app()
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
