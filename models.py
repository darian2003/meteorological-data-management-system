from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class Tara(db.Model):
    __tablename__ = 'Tari'
    id = db.Column(db.Integer, primary_key=True)
    nume_tara = db.Column(db.String(255), unique=True, nullable=False)
    latitudine = db.Column(db.Float, nullable=False)
    longitudine = db.Column(db.Float, nullable=False)

class Oras(db.Model):
    __tablename__ = 'Orase'
    id = db.Column(db.Integer, primary_key=True)
    id_tara = db.Column(db.Integer, db.ForeignKey('Tari.id'), nullable=False)
    nume_oras = db.Column(db.String(255), nullable=False)
    latitudine = db.Column(db.Float, nullable=False)
    longitudine = db.Column(db.Float, nullable=False)

    __table_args__ = (UniqueConstraint('id_tara', 'nume_oras', name='unique_id_tara_nume_oras'),)

class Temperatura(db.Model):
    __tablename__ = 'Temperaturi'
    id = db.Column(db.Integer, primary_key=True)
    valoare = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    id_oras = db.Column(db.Integer, db.ForeignKey('Orase.id'), nullable=False)

    __table_args__ = (UniqueConstraint('id_oras', 'timestamp', name='unique_id_oras_timestamp'),)
