from flask import Flask
from config.config import Config
from common.db import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Init SQLAlchemy & Flask-Migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Basic Route
    @app.route("/")
    def home():
        return "<h1>All works for now...</h1>"
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
