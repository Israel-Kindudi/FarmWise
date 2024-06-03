# app/routes/feed.py
from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Feed
from app.forms import LogFeedingForm

bp = Blueprint('feed', __name__)

@bp.route('/feed', methods=['GET', 'POST'])
def index():
    form = LogFeedingForm()
    if form.validate_on_submit():
        feeding = Feed(animal_id=form.animal_id.data, date=form.date.data, quantity=form.quantity.data)
        db.session.add(feeding)
        db.session.commit()
        flash('Feeding logged successfully!')
        return redirect(url_for('feed.index'))
    return render_template('feed.html', form=form)
