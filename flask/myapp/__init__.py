# from config import Config
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from flask_cors import CORS
# from flask_googlemaps import GoogleMaps


app = Flask(__name__)
# app.config.from_object(Config)
# CORS(app)
# db = SQLAlchemy(app)
# map = GoogleMaps(app)
from myapp import routes
# app.config.from_object(Config)

# db = SQLAlchemy(app)
