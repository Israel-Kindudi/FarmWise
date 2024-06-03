# app/routes/order.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import db
from app.models import Order

bp = Blueprint('order', __name__)

@bp.route('/orders')
def list_orders():
    orders = Order.query.all()
    return render_template('list_orders.html', orders=orders)

@bp.route('/orders/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        product = request.form['product']
        quantity = request.form['quantity']
        status = request.form['status']
        date = request.form['date']
        customer_name = request.form['customer_name']
        order_date = request.form['order_date']

        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        order_date_obj = datetime.strptime(order_date, '%Y-%m-%d').date()
        
        new_order = Order(product=product, quantity=quantity, status=status, date=date_obj, customer_name=customer_name, order_date=order_date_obj)
        db.session.add(new_order)
        db.session.commit()
        flash('Order added successfully!')
        return redirect(url_for('order.list_orders'))
    
    return render_template('add_order.html')

@bp.route('/orders/edit/<int:id>', methods=['GET', 'POST'])
def edit_order(id):
    order = Order.query.get_or_404(id)
    
    if request.method == 'POST':
        order.product = request.form['product']
        order.quantity = request.form['quantity']
        order.status = request.form['status']
        order.date = request.form['date']
        order.customer_name = request.form['customer_name']
        order.order_date = request.form['order_date']

        order.date = datetime.strptime(order.date, '%Y-%m-%d').date()
        order.order_date = datetime.strptime(order.order_date, '%Y-%m-%d').date()
        
        db.session.commit()
        flash('Order updated successfully!')
        return redirect(url_for('order.list_orders'))
    
    return render_template('edit_order.html', order=order)

@bp.route('/orders/delete/<int:id>')
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    flash('Order deleted successfully!')
    return redirect(url_for('order.list_orders'))
