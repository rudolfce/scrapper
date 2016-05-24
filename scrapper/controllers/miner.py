#-*- encoding: utf-8 -*-
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from flask import current_app

from scrapper import make_celery
from scrapper.models.user import User

celery = make_celery(current_app)

@celery.task
def scrape_twitter(user_name):
    user = User()
    user.username = user_name
    url_request = 'https://twitter.com/' + str(user_name)
    response = requests.get(url_request)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        data = soup.find("input", attrs={"class":"json-data"})
        data = json.loads(data["value"])
        profile_data = data["profile_user"]
        user.name = profile_data["name"]
        user.bio = profile_data["description"]
        user.location = profile_data["location"]
        user.exists = True
        time = datetime.now()
        user.query_date = time.strftime('%m/%d/%Y %I:%M%p')

        user.save()

def query_database(user_name):
    '''
    Miner used to gather information from a twitter accout defined as user_name.
    Returns dictionary with:
    - username;
    - name;
    - bio;
    - location.
    '''
    user = User.query.filter(User.username==user_name).first()
    if not user:
        return None
    else:
        user_dict = user.get_dict()

        return user_dict
