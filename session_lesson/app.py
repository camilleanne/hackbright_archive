from flask import Flask, render_template, request, redirect, session, url_for, flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators

import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")

    user_id = model.authenticate(username, password)
    if user_id != None:
        flash("User authenticated!")
        session['user_id'] = user_id
        return redirect(url_for("view_user", username = username))
    else:
        flash('Username or password incorrect!')
        return redirect(url_for("index"))

@app.route("/register")
def register():
    if session.get("user_id"):
        username = model.get_user_by_id(session.get("user_id"))
        return redirect(url_for("view_user", username = username))
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def create_account():
    username = request.form.get("username")
    password = request.form.get("password")
    if model.get_user_by_name(username):
        flash("There is already a user by that name")
        return redirect(url_for("create_account"))
    else:
        flash("User created, please log in")
        model.add_user_to_db(username, password)
        return redirect(url_for("index"))

@app.route("/user/<username>", methods = ["GET"])
def view_user(username):
    user_id = model.get_user_by_name(username)
    wall_posts = model.return_wall_posts(user_id)
    return render_template("wall.html", username = username, wall_posts = wall_posts)

@app.route("/user/<username>", methods = ["POST"])
def post_to_wall(username):
    user_id = model.get_user_by_name(username)
    content = request.form.get("post_text")
    author_id = session.get("user_id")
    model.add_wall_post_to_db(user_id, author_id, content)
    return redirect(url_for("view_user", username = username))


@app.route("/clear")
def session_clear():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
