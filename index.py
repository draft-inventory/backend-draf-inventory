#Import models
from inventory.domain.models import *

from app import app
from common.db import db

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)