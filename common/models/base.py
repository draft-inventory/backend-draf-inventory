import datetime
from common.db import db

class MVCModel(db.Model):
    __abstract__ = True  # Doesn't map as a table

    usuarioCreacion = db.Column(db.Integer, nullable=True)
    usuarioEdicion = db.Column(db.Integer, nullable=True)
    ipCreacion = db.Column(db.String(50), nullable=True)
    ipEdicion = db.Column(db.String(50), nullable=True)
    fechaCreacion = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    fechaEdicion = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)
