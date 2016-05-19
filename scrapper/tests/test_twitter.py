import json
from scrapper.tests import testBase


class twitterTest(testBase):
    def test_root(self):
        response = self.client.get('/twitter/')
        assert response.status_code == 400

    def test_user_request(self):
        response = self.client.get('/twitter/flubbercwb')
        assert response.status_code == 202

    def test_user_found(self):
        from scrapper.models.user import User

        in_found = User()
        in_found.username="adabalubaba"
        in_found.exists = True
        in_found.save()

        response = self.client.get('/twitter/adabalubaba')
        assert response.status_code == 200

    def test_no_user_found(self):
        from scrapper.models.user import User

        in_found = User()
        in_found.username="adabalubaba"
        in_found.exists = False
        in_found.save()

        response = self.client.get('/twitter/adabalubaba')
        assert response.status_code == 404
