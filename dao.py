from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)


def add(obj):
    db.session.add(obj)
    db.session.commit()


def delete(obj):
    db.session.delete(obj)
    db.session.commit()


def queryAll(cls):
    return db.session.query(cls).all()


def query(cls):
    return db.session.query(cls)


def get(cls, id):
    return db.session.query(cls).get(id)
