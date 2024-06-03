from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Animal, Treatment
from datetime import datetime


#bp = Blueprint('treatments',__name__)

#@bp.route('/')
#


bp = Blueprint('treatments', __name__)
@bp.route('/')
def index():
    return render_template('treatments.html')
@bp.route('/treatments')
def list_treatments():
    treatments = Treatment.query.all()
    return render_template('list_treatments.html', treatments=treatments)

@bp.route('/treatments/add', methods=['GET', 'POST'])
def add_treatment():
    if request.method == 'POST':
        animal_id = request.form['animal_id']
        treatment_type = request.form['treatment_type']
        date = request.form['date']
        notes = request.form['notes']

        # Convert date string to date object
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        
        new_treatment = Treatment(animal_id=animal_id, treatment_type=treatment_type, date=date_obj, notes=notes)
        db.session.add(new_treatment)
        db.session.commit()
        flash('Treatment added successfully!')
        return redirect(url_for('treatments.list_treatments'))
    
    animals = Animal.query.all()
    return render_template('add_treatment.html', animals=animals)
    

@bp.route('/treatments/edit/<int:id>', methods=['GET', 'POST'])
def edit_treatment(id):
    treatment = Treatment.query.get_or_404(id)
    
    if request.method == 'POST':
        treatment.animal_id = request.form['animal_id']
        treatment.treatment_type = request.form['treatment_type']
        date = request.form['date']
        notes = request.form['notes']
        
        # Convert date string to date object
        treatment.date = datetime.strptime(date, '%Y-%m-%d').date()
        
        db.session.commit()
        flash('Treatment updated successfully!')
        return redirect(url_for('treatments.list_treatments'))
    
    animals = Animal.query.all()
    return render_template('edit_treatment.html', treatment=treatment, animals=animals)

@bp.route('/treatments/delete/<int:id>')
def delete_treatment(id):
    treatment = Treatment.query.get_or_404(id)
    db.session.delete(treatment)
    db.session.commit()
    flash('Treatment deleted successfully!')
    return redirect(url_for('treatments.list_treatments'))