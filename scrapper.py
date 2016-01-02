from flask import Flask, render_template

import miner

app = Flask(__name__)

@app.route('/')
@app.route('/<user_name>')
def index(user_name=None):
    if user_name:
        page_output = "user"
        user = miner.mine_user(user_name)
    else:
        page_output = "index"
        user = None
    return render_template("index.html", user=user, page_output=page_output)

if __name__ == "__main__":
    app.run()
