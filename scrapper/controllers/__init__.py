#-*- encoding: utf-8 -*-
import os
import json
from flask import render_template, request, redirect, Blueprint, abort, make_response
from flask.ext.api import status

from scrapper.controllers.twitter import twitter_bp
from scrapper.controllers.miner import query_database, scrape_twitter


@twitter_bp.route('/', methods=['GET', 'POST'])
def index():
    abort(status.HTTP_400_BAD_REQUEST)

@twitter_bp.route('/<user_name>')
def show_user(user_name=None):
    refresh = request.args.get('refresh', '')
    user = query_database(user_name)
    if not user or refresh:
        scrape_twitter.delay(user_name)
        return make_response('Processing...', status.HTTP_202_ACCEPTED)
    else:
        if user['exists']:
            user = json.dumps(user)
            return user, status.HTTP_200_OK
        else:
            abort(status.HTTP_404_NOT_FOUND)

if __name__ == "__main__":
    app.run()
