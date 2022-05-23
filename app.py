import os
from flask import Flask, redirect, render_template, url_for, request,make_response
from db.main import check_password, add_coment, init_db_app, get_db, add_entities, delete_entitie,add_User,update
from entities.Movie import Movie
from entities.User import User
from entities.Comment import Comment



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
    user = db.execute("SELECT * FROM user_ WHERE name_=?",(request.cookies.get("user"),)).fetchall()
    print(user)
    if user==[]:
        res = make_response(render_template("card.html", all = db.execute("SELECT * FROM movie"),ban_reg=False,register=request.cookies.get("user")))
        res.set_cookie('user', max_age=0)
        return res
    res = make_response(render_template("card.html", all = db.execute("SELECT * FROM movie"),ban_reg=False,register=request.cookies.get("user")))
    return res


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
    db = get_db().execute("SELECT * FROM user_ WHERE name_=?",(request.form.get('name'),)).fetchall()
    if request.form.get('password')==request.form.get('passwordTwo') and db==[]:
        res = make_response('<script>document.location.href = document.referrer</script>')
        res.set_cookie('user', max_age=0)
        newUser = User(request.form.get('name'),request.form.get('password'))
        add_User(newUser)
        res.set_cookie('user', newUser.name)
        return res
    return '<script>document.location.href = document.referrer</script>'

@app.route("/log_in",methods=["POST"])
def log_in():
    nowUser = User(request.form.get("name"),request.form.get("password"))
    result = check_password(nowUser)
    print(result)
    res = make_response('<script>document.location.href = document.referrer</script>')
    res.set_cookie('user', max_age=0)
    if not result:
        return res
    res.set_cookie('user', nowUser.name)
    return res

@app.route("/exit",methods=["POST"])
def exit():
    res = make_response('<script>document.location.href = document.referrer</script>')
    res.set_cookie('user', max_age=0)
    return res

@app.route("/card/<movie>And<id>")
def card(movie,id):
    db = get_db()
    select = db.execute("SELECT * FROM movie where title = ? AND id=?",(str(movie),id,)).fetchall()
    comment = db.execute("SELECT * FROM comment where movie_id = ?",(id,)).fetchall()
    if select==[]:
        return render_template("404.html",url=request.url)
    return render_template("movieSeen.html",all = select[0], ban_reg=False,register=request.cookies.get("user"),comments=comment)

@app.route("/addComment<id>",methods=["POST"])
def add_comment(id):
    Coment = Comment(request.cookies.get("user"),id,request.form.get('text'))
    add_coment(Coment.get())
    return '<script>document.location.href = document.referrer</script>'

@app.route("/edit_movie",methods=["POST","GET"])
def edit_movie():
    db = get_db()
    if request.method=="GET":
        card = db.execute("SELECT * FROM movie WHERE id=?",(request.args.get("id"),)).fetchall()[0]
        print(card)
        all = db.execute("SELECT * FROM movie")
        return render_template("editeMovie.html",register=request.cookies.get("user"),card = card,all=all)
    movie = Movie(request.form.get("title"),request.form.get("url"),request.form.get("text"))
    update(movie,request.form.get("id"))
    return redirect(url_for("main"))
    

if __name__ == "__main__":
    app.run(debug=True)
