from flask import Flask
from main.config import Development
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)
application.config.from_object(Development())

db = SQLAlchemy(application )
CORS(application)

from main import routes
