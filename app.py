import sys
import os

from flask import Flask
from config.config import Config
from common.db.db import db, ma

# Routes
from inventory.infrastructure.http.category_routes import category_urls

app = Flask(__name__)
app.config.from_object(Config)

# Init SQLAlchemy & Marshmallow
db.init_app(app)
ma.init_app(app)

# Add the path to the current file to the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


# Routes
app.register_blueprint(category_urls,url_prefix = '/categories')