# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
