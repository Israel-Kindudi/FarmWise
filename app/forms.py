# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class AddAnimalForm(FlaskForm):
    species = SelectField('Species', choices=[('cow', 'Cow'), ('pig', 'Pig'), ('chicken', 'Chicken'), ('fish', 'Fish')], validators=[DataRequired()])
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])
    health_status = StringField('Health Status', validators=[DataRequired()])
    submit = SubmitField('Add Animal')

class LogFeedingForm(FlaskForm):
    animal_id = StringField('Animal ID', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    quantity = FloatField('Quantity (kg)', validators=[DataRequired()])
    submit = SubmitField('Log Feeding')

class CreateReportForm(FlaskForm):
    report_type = SelectField('Report Type', choices=[('weekly', 'Weekly'), ('monthly', 'Monthly')], validators=[DataRequired()])
    submit = SubmitField('Create Report')
