from flask.ext.testing import TestCase

from scrapper import db, create_app


class testBase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://rudolf:some_password@127.0.0.1/scrapper_temp"
        return app

    def setUp(self):
        self.db = db
        self.db.init_app(self.app)
        self.db.drop_all(app=self.app)
        self.db.create_all(app=self.app)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all(app=self.app)

