#-*- encoding: utf-8 -*-
import os
import json
from flask import render_template, request, redirect, Blueprint, abort
from flask.ext.api import status

from scrapper.controllers.miner import mine_user


twitter = Blueprint('twitter', __name__, url_prefix = '/twitter')

@twitter.route('/', methods=['GET', 'POST'])
def index():
    abort(400)

@twitter.route('/<user_name>')
def show_user(user_name=None):
    refresh = request.args.get('refresh', '')
    user = miner.mine_user(user_name, refresh)
    user = json.dumps(user)
    return user, status.HTTP_200_OK

if __name__ == "__main__":
    app.run()
