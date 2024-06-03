# app/routes/animals.py
from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Animal
from app.forms import AddAnimalForm

bp = Blueprint('animals', __name__)

@bp.route('/animals', methods=['GET', 'POST'])
def index():
    form = AddAnimalForm()
    if form.validate_on_submit():
        animal = Animal(species=form.species.data, birth_date=form.birth_date.data, health_status=form.health_status.data)
        db.session.add(animal)
        db.session.commit()
        flash('New animal added successfully!')
        return redirect(url_for('animals.index'))
    return render_template('animals.html', form=form)
