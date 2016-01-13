#-*- encoding: utf-8 -*-
import os
from flask import Flask, render_template, request, redirect, send_from_directory

from scrapper.controller.miner import mine_user


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        page_output="index"
        user = None
        return render_template("index.html", user=user, page_output=page_output)
    else:
        return redirect(request.form['user_name'])

@app.route('/<user_name>')
def show_user(user_name=None):
    refresh = request.args.get('refresh', '')
    page_output = "user"
    user = mine_user(user_name, refresh)
    return render_template("index.html", user=user, page_output=page_output)

if __name__ == "__main__":
    app.run(debug=True)
