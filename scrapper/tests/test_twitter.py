import unittest
from flask.ext.testing import TestCase

from scrapper import db, create_app


class scrapperTest(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://rudolf:somepassword@127.0.0.1/scrapper_temp"
        return app

    def setUp(self):
        self.db = db
        self.db.init_app(self.app)
        self.db.drop_all(app=self.app)
        self.db.create_all(app=self.app)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all(app=self.app)

    def test_root_request(self):
        response = self.client.get('/')
        assert response.status_code == 302
        assert 'twitter' in response.location

    def test_twitterApp_root(self):
        response = self.client.get('/twitter/')
        assert response.status_code == 200
        response_data = response.get_data(as_text = True)
        assert "You should really" in response_data

    def test_twitterApp_userRequest(self):
        response = self.client.get('/twitter/flubbercwb')
        assert response.status_code == 200
        response_data = response.get_data(as_text = True)
        assert "Fresh" in response_data
        response = self.client.get('/twitter/flubbercwb')
        assert response.status_code == 200
        response_data = response.get_data(as_text = True)
        assert not ("Fresh" in response_data)

    def test_twitterApp_noUserFound(self):
        response = self.client.get('/twitter/ababalubaba')
        assert response.status_code == 200
        response_data = response.get_data(as_text = True)
        assert "User not found" in response_data        

if __name__ == "__main__":
    unittest.main()
