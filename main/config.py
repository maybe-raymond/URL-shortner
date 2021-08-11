
class Config(object):
    SECRET_KEY = '65446464566g6d4651c66s461c6v651v'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    JSON_SORT_KEYS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    DEBUG = True
    Domain = "http://127.0.0.1:5000/"

class Deployment(Config):
    Domain =  "http://iika-env.eba-cabvyiip.us-east-2.elasticbeanstalk.com/"