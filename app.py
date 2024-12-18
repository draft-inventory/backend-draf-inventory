import sys
import os

from flask import Flask
from flasgger import Swagger
from config.config import Config
from common.db.db import db, ma

# Routes
from inventory.infrastructure.http.category_routes import category_urls
from iam.infrastructure.http.user_routes import user_urls

app = Flask(__name__)
app.config.from_object(Config)

# Init SQLAlchemy & Marshmallow
db.init_app(app)
ma.init_app(app)

# Add the path to the current file to the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


# Configuration Swagger
app.config['SWAGGER'] = {
    'title': 'Draft Inventory API',
    'uiversion': 3
}
swagger = Swagger(app)

# Routes
app.register_blueprint(category_urls,url_prefix = '/categories')
app.register_blueprint(user_urls,url_prefix = '/users')