#-*- encoding: utf-8 -*-
import os
from flask import render_template, request, redirect, Blueprint

from scrapper.controllers.miner import mine_user


twitter = Blueprint('twitter', __name__, url_prefix = '/twitter')

@twitter.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        page_output="index"
        user = None
        return render_template("index.html", user=user, page_output=page_output)
    else:
        return redirect('/twitter/{}'.format(request.form['user_name']))

@twitter.route('/<user_name>')
def show_user(user_name=None):
    refresh = request.args.get('refresh', '')
    page_output = "user"
    user = miner.mine_user(user_name, refresh)
    return render_template("index.html", user=user, page_output=page_output)

if __name__ == "__main__":
    app.run()
