#-*- encoding: utf-8 -*-
import os
import json
from flask import render_template, request, redirect, Blueprint, abort
from flask.ext.api import status

from scrapper.controllers.twitter import twitter_bp
from scrapper.controllers.miner import mine_user


@twitter_bp.route('/', methods=['GET', 'POST'])
def index():
    abort(400)

@twitter_bp.route('/<user_name>')
def show_user(user_name=None):
    refresh = request.args.get('refresh', '')
    user = miner.mine_user.delay(user_name, refresh)
    user = json.dumps(user.get())
    return user, status.HTTP_200_OK
