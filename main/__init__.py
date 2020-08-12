from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"]='65446464566g6d4651c66s461c6v651v'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
db = SQLAlchemy(app)

from main import routes
