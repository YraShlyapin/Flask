DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS user_;

CREATE TABLE movie (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url_ TEXT NOT NULL,
    text_ TEXT NOT NULL
);

CREATE TABLE comment (
    id INTEGER PRIMARY KEY,
    UserName TEXT NOT NULL,
    text_ TEXT NOT NULL,
    movie_id INTEGER NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movie(id)
    FOREIGN KEY (UserName) REFERENCES user(name_)
);

CREATE TABLE user_ (
    id INTEGER PRIMARY KEY,
    name_ TEXT NOT NULL,
    password_ TEXT NOT NULL
);