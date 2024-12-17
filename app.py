from flask import Flask
from config.config import Config
from common.db import db, ma

# Routes
from inventory.infrastructure.http.category_routes import category_urls

app = Flask(__name__)
app.config.from_object(Config)

# Init SQLAlchemy & Flask-Migrate
db.init_app(app)
ma.init_app(app)

# Routes
app.register_blueprint(category_urls,url_prefix = '/categories')