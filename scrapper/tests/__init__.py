from flask.ext.testing import TestCase
from sqlalchemy_utils import database_exists, create_database, drop_database
from celery.task.control import inspect

from scrapper import db, create_app


i = inspect()
session = list(i.active().keys())[0]

class testBase(TestCase):
    def create_app(self):
        app = create_app('scrapper.config.testing')
        db.init_app(app)
        db.drop_all(app=app)
        return app

    def setUp(self):
        self.db = db
        if not database_exists(self.app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(self.app.config["SQLALCHEMY_DATABASE_URI"])
        self.db.create_all()
        self.db.init_app(self.app)

    def tearDown(self):
        while len(i.active()[session]):
            pass # Wait for task to be complete
        self.db.session.remove()
        self.db.drop_all(app=self.app)
