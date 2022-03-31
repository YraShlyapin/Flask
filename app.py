import os
from unittest import result
from flask import Flask, redirect, render_template, url_for, request
from db.main import check_password, get_User, init_db_app, get_db, add_entities, delete_entitie,add_User
from entities.Movie import Movie
from entities.User import User


app = Flask(__name__)
app.config.from_mapping(DATABASE = os.path.join(app.root_path,"db\db.sqlite"))
init_db_app(app)


# @app.route("/")
# def main_page():
#     with open("static/index.html", "r", encoding='utf-8') as file:
#         return file.read()


@app.route("/")
def main():
    db = get_db()
    return render_template("card.html", all = db.execute("SELECT * FROM movie"),ban_reg=False)


@app.route("/add_movie",methods=["POST"])
def add_movie():
    newMovie = Movie(request.form.get('title'),request.form.get('url'),request.form.get('text'))
    add_entities(newMovie)
    return redirect(url_for('main'))

@app.route("/delete_movie",methods=["POST"])
def delete_movie():
    delete_entitie(request.form.get('id'))
    return redirect(url_for('main'))

@app.route("/add_user",methods=["POST"])
def add_user():
    newUser = User(request.form.get('name'),request.form.get('password'))
    add_User(newUser)
    return redirect(url_for('main'))

@app.route("/log_in",methods=["POST"])
def log_in():
    result = check_password(User(request.form.get("name"),request.form.get("password")))
    print(result)
    if not result:
        return redirect(url_for('main'))
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
