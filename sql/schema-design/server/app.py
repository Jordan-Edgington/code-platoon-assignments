from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
# this URI may or may not be complete, francisco used postgresql+pscypg, i may need to install psycopg
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://jordanedgington@localhost/5432/store_db'

db = SQLAlchemy(app)

# START MAKING MODELS


class Genres(db.Model):
    genre_id = db.Column(db.Integer(), primary_key=True)
    genre_name = db.Column(db.String(20))


class Gaming_engine(db.Model):
    gaming_engine_id = db.Column(db.Integer(), primary_key=True)
    engine = db.Column(db.String(20))


class Games(db.Model):
    game_id = db.Column(db.Integer(), primary_key=True)
    engine_id = db.Column(db.Integer())
    game_title = db.Column(db.String(255))
    quantity = db.Column(db.Integer())
    price = db.Column(db.types.DECIMAL(5, 2))


class Game_genres(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    game_id = db.Column(db.Integer())
    genre_id = db.Column(db.Integer())


class Action_figures(db.Model):
    action_figure_id = db.Column(db.Integer(), primary_key=True)
    action_figure_title = db.Column(db.String(255))
    quantity = db.Column(db.Integer())
    price = db.Column(db.types.DECIMAL(4, 2))


class Posters(db.Model):
    poster_id = db.Column(db.Integer,  primary_key=True)
    poster_title = db.Column(db.String(50))
    quantity = db.Column(db.Integer())
    price = db.Column(db.types.DECIMAL(4, 2))


''' 
just like react-router, we need to specify a route to display at index ('/')
@app.route() decorator takes the path to the route and provides the function output at that route
'''


@app.route('/', methods=['GET'])
def home():
    return 'Hello Whiskey'


app.run(debug=True, port=8000)
