from flask import Flask
from main.config import  Development
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

application = Flask(__name__)
application.config.from_object(Development())

db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(application)

from main import routes
