#-*- encoding: utf-8 -*-

import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

from db_stuff import db_session
from db_stuff.models import User

def query_twitter(user_name):
    url_request = 'https://twitter.com/' + str(user_name)
    r = requests.get(url_request)
    if '404' in r.headers['status']:
        return None

    r = r.text
    soup = BeautifulSoup(r,"html.parser")

    data = soup.find("input", attrs={"class":"json-data"})
    data = json.loads(data["value"])
    profile_data = data["profile_user"]
    name = profile_data["name"]
    bio = profile_data["description"]
    location = profile_data["location"]
    time = datetime.now()
    query_date = time.strftime('%m/%d/%Y %I:%M%p')

    return {"username": user_name,
            "name": name,
            "bio": bio,
            "location": location,
            "query_date": query_date}
    

def mine_user(user_name, refresh):
    '''
    Miner used to gather information from a twitter accout defined as user_name.
    Returns dictionary with:
    - username;
    - name;
    - bio;
    - location.
    '''
    user = User.query.filter(User.username==user_name).first()
    if (not user) or refresh:
        user_dict = query_twitter(user_name)
        if not user_dict:
            return None
        user = User(**user_dict)
        if refresh:
            db_session.query(User).filter_by(username=user_name).update(user_dict)
        else:
            db_session.add(user)
        db_session.commit()
        user_dict['fresh'] = True
    else:
        user_dict = user.get_dict()
        user_dict['fresh'] = False

    return user_dict
