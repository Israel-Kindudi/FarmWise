# app/routes/reports.py
from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import CreateReportForm

bp = Blueprint('reports', __name__)

@bp.route('/reports', methods=['GET', 'POST'])
def index():
    form = CreateReportForm()
    if form.validate_on_submit():
        # Logic to generate the report
        flash('Report created successfully!')
        return redirect(url_for('reports.index'))
    return render_template('reports.html', form=form)
