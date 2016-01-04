from flask import Flask, render_template, request, redirect

import miner

app = Flask(__name__)

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
    page_output = "user"
    user = miner.mine_user(user_name)
    return render_template("index.html", user=user, page_output=page_output)

if __name__ == "__main__":
    app.run()
