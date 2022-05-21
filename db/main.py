import sqlite3
from entities.Comment import Comment
from flask import Flask, g,current_app
from flask.cli import with_appcontext
import click
from entities.Movie import Movie
from entities.User import User


def init_db_app(app:Flask):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db)
    app.cli.add_command(add_test)
    app.cli.add_command(delete_all)
    app.cli.add_command(delete_people)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    if 'db' in g:
        db = g.pop('db')
        db.close()


@click.command('init_db')
@with_appcontext
def init_db():
    """
        инициализация бд
    """
    db = get_db()
    with current_app.open_resource('db/schema.sql') as file:
        db.executescript(file.read().decode('utf-8'))
    click.echo('все работает')



def add_entities(movie:Movie):
    db = get_db()
    db.execute("INSERT INTO movie (title,url_,text_) VALUES (?,?,?)",(movie.get()))
    db.commit()
    click.echo('You added new entity')

def delete_entitie(id_movie):
    db = get_db()
    db.execute("DELETE FROM movie WHERE id=?",(id_movie,))
    db.commit()

@click.command('delete_all')
@with_appcontext
def delete_all():
    """
        удалить всю базу movie
    """
    db = get_db()
    db.execute("DELETE FROM comment")
    db.commit()

@click.command('delete_people')
@with_appcontext
def delete_people():
    """
        удалить всю базу movie
    """
    db = get_db()
    db.execute("DELETE FROM user_")
    db.commit()

@click.command('add_test')
@with_appcontext
def add_test(movie:Movie = Movie("test","asd","ыыы")):
    """
        добавить новый тест
    """
    db = get_db()
    db.execute("INSERT INTO movie (title,url_,text_) VALUES (?,?,?)", (movie.get()))
    db.commit()


def get_User():
    return(get_db().execute("SELECT * FROM user_").fetchall())


def check_password(user:User):
    db = get_db()
    password = db.execute("SELECT password_ FROM user_ WHERE name_ = ?", (user.name,)).fetchone()
    returned = None
    if password:
        returned = password[0]
    return returned==user.password


def add_User(user:User):
    db = get_db()
    db.execute("INSERT INTO user_ (name_,password_) VALUES (?,?)",(user.get()))
    db.commit()

def add_coment(com):
    db = get_db()
    db.execute("INSERT INTO comment (UserName,text_,movie_id) VALUES (?,?,?)",(com))
    db.commit()

# a = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'