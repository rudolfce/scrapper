from scrapper.tests import testBase


class twitterTest(testBase):
    def test_root(self):
        response = self.client.get('/twitter/')
        assert response.status_code == 200
        response_data = response.get_data(as_text = True)
        assert "You should really" in response_data

    def test_user_request(self):
        response = self.client.get('/twitter/flubbercwb')
        assert response.status_code == 200
        response_data = response.get_data(as_text = True)
        assert "Fresh" in response_data
        response = self.client.get('/twitter/flubbercwb')
        assert response.status_code == 200
        response_data = response.get_data(as_text = True)
        assert not ("Fresh" in response_data)

    def test_no_user_found(self):
        response = self.client.get('/twitter/ababalubaba')
        assert response.status_code == 200
        response_data = response.get_data(as_text = True)
        assert "User not found" in response_data        

