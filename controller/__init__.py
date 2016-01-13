#-*- encoding: utf-8 -*-
from flask import Flask, render_template, request, redirect

import model.miner


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        page_output="index"
        user = None
        return render_template("index.html", user=user, page_output=page_output)
    else:
        return redirect(request.form['user_name'])

@app.route('/favicon.ico')
def return_favicon():
    return 404

@app.route('/<user_name>')
def show_user(user_name=None):
    refresh = request.args.get('refresh', '')
    page_output = "user"
    user = model.miner.mine_user(user_name, refresh)
    return render_template("index.html", user=user, page_output=page_output)

if __name__ == "__main__":
    app.run(debug=True)
