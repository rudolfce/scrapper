#-*- encoding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup

def mine_user(user_name):
    '''
    Miner used to gather information from a twitter accout defined as user_name.
    Returns dictionary with:
    - username;
    - name;
    - bio;
    - location.
    '''
    output_username='@' + str(user_name)
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

    return {"username": output_username,
            "name": name,
            "bio": bio,
            "location": location}
