from flask import Flask, render_template

app = Flask(__name__)
app.testing = True


@app.route("/<username>")
def hello_world(username=None):
    return render_template("index.html", name=username)


@app.route("/blog/2020/dogs")
def blog():
    return "this is a dog!"


@app.route("/<username>/<int:post_id:>")
def params(username=None, post_id=None):
    return render_template("index.html", name=username, post_id=post_id)
