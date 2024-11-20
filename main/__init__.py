from flask import Flask
from main.config import Deployment, Development
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)
application.config.from_object(Development())


from main import routes
