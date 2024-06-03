# app/routes/finance.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import db
from app.models import Expense, Revenue


bp = Blueprint('finances', __name__)
@bp.route('/finances')
def index():
    expenses = Expense.query.all()
    return render_template('list_expenses.html',exppense=expenses)
# Expenses routes
@bp.route('/expenses')
def list_expenses():
    expenses = Expense.query.all()
    return render_template('list_expenses.html', expenses=expenses)

@bp.route('/expenses/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        notes = request.form['notes']

        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        
        new_expense = Expense(description=description, amount=amount, date=date_obj, notes=notes)
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully!')
        return redirect(url_for('finances.list_expenses'))
    
    return render_template('add_expense.html')

@bp.route('/expenses/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    
    if request.method == 'POST':
        expense.description = request.form['description']
        expense.amount = request.form['amount']
        date = request.form['date']
        expense.notes = request.form['notes']

        expense.date = datetime.strptime(date, '%Y-%m-%d').date()
        
        db.session.commit()
        flash('Expense updated successfully!')
        return redirect(url_for('finances.list_expenses'))
    
    return render_template('edit_expense.html', expense=expense)

@bp.route('/expenses/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!')
    return redirect(url_for('finances.list_expenses'))

# Revenues routes
@bp.route('/revenues')
def list_revenues():
    revenues = Revenue.query.all()
    return render_template('list_revenues.html', revenues=revenues)

@bp.route('/revenues/add', methods=['GET', 'POST'])
def add_revenue():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        notes = request.form['notes']

        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        
        new_revenue = Revenue(description=description, amount=amount, date=date_obj, notes=notes)
        db.session.add(new_revenue)
        db.session.commit()
        flash('Revenue added successfully!')
        return redirect(url_for('finances.list_revenues'))
    
    return render_template('add_revenue.html')

@bp.route('/revenues/edit/<int:id>', methods=['GET', 'POST'])
def edit_revenue(id):
    revenue = Revenue.query.get_or_404(id)
    
    if request.method == 'POST':
        revenue.description = request.form['description']
        revenue.amount = request.form['amount']
        date = request.form['date']
        revenue.notes = request.form['notes']

        revenue.date = datetime.strptime(date, '%Y-%m-%d').date()
        
        db.session.commit()
        flash('Revenue updated successfully!')
        return redirect(url_for('finance.list_revenues'))
    
    return render_template('edit_revenue.html', revenue=revenue)

@bp.route('/revenues/delete/<int:id>')
def delete_revenue(id):
    revenue = Revenue.query.get_or_404(id)
    db.session.delete(revenue)
    db.session.commit()
    flash('Revenue deleted successfully!')
    return redirect(url_for('finance.list_revenues'))

# Financial report route
@bp.route('/finance/report')
def finance_report():
    expenses = Expense.query.all()
    revenues = Revenue.query.all()
    total_expenses = sum(expense.amount for expense in expenses)
    total_revenues = sum(revenue.amount for revenue in revenues)
    net_profit = total_revenues - total_expenses
    return render_template('finance_report.html', total_expenses=total_expenses, total_revenues=total_revenues, net_profit=net_profit)
