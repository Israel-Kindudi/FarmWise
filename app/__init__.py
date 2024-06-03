# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import models
        from .routes import dashboard, animals, feed, treatments, finances, orders, reports
        app.register_blueprint(dashboard.bp)
        app.register_blueprint(animals.bp)
        app.register_blueprint(feed.bp)
        app.register_blueprint(treatments.bp)
        app.register_blueprint(finances.bp)
        app.register_blueprint(orders.bp)
        app.register_blueprint(reports.bp)

        db.create_all()

    return app
