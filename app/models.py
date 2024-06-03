from . import db
from datetime import datetime
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(64), index=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    health_status = db.Column(db.String(64), nullable=False)
    treatments = db.relationship('Treatment', backref='animal', lazy=True)
    feedings = db.relationship('Feed', backref='animal', lazy=True)  # Add this line to establish the relationship

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Float, nullable=False)

class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    treatment_type = db.Column(db.String(64), nullable=False)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text, nullable=True)

class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    notes = db.Column(db.String(200))

class Revenue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    notes = db.Column(db.String(200))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(64), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(64), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    customer_name = db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
