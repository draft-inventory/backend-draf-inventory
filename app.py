import sys
import os

from flask import Flask
from flasgger import Swagger
from config.config import Config
from common.db.db import db, ma

# Routes
from inventory.infrastructure.http.category_routes import category_urls
from inventory.infrastructure.http.price_routes import price_urls
from inventory.infrastructure.http.quantity_routes import quantity_urls
from inventory.infrastructure.http.quantity_history_routes import quantity_history_urls
from inventory.infrastructure.http.product_routes import product_urls

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
    'uiversion': 3,
    'openapi': '3.0.0',
    'produces': ['application/json'],
}
swagger = Swagger(app)

# Routes
app.register_blueprint(category_urls, url_prefix='/categories')
app.register_blueprint(price_urls, url_prefix='/prices')
app.register_blueprint(quantity_urls, url_prefix='/quantities')
app.register_blueprint(quantity_history_urls, url_prefix='/quantity_histories')
app.register_blueprint(product_urls, url_prefix='/products')
