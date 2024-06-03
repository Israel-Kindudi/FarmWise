from flask import Blueprint,render_template
from datetime import datetime, timedelta
from app.models import Order, Revenue, Expense
from app import db
bp = Blueprint('dashboard',__name__)

@bp.route('/')
def index():
    # Calculate the number of new orders in the last 30 days
    today = datetime.utcnow()
    thirty_days_ago = today - timedelta(days=30)
    sixty_days_ago = today - timedelta(days=60)

    # Orders in the last 30 days
    current_period_orders_count = Order.query.filter(Order.order_date >= thirty_days_ago).count()

    # Orders in the previous 30 days
    previous_period_orders_count = Order.query.filter(Order.order_date.between(sixty_days_ago, thirty_days_ago)).count()

    # Calculate the percentage change
    if previous_period_orders_count == 0:
        orders_percentage_change = 0
    else:
        orders_percentage_change = ((current_period_orders_count - previous_period_orders_count) / previous_period_orders_count) * 100
 # # Revenues
    current_period_revenue = Revenue.query.with_entities(db.func.sum(Revenue.amount)).filter(Revenue.date >= thirty_days_ago).scalar() or 0
    previous_period_revenue = Revenue.query.with_entities(db.func.sum(Revenue.amount)).filter(Revenue.date.between(sixty_days_ago, thirty_days_ago)).scalar() or 0

    if previous_period_revenue == 0:
        revenue_percentage_change = 0
    else:
        revenue_percentage_change = ((current_period_revenue - previous_period_revenue) / previous_period_revenue) * 100

    # Expenses
    current_period_expense = Expense.query.with_entities(db.func.sum(Expense.amount)).filter(Expense.date >= thirty_days_ago).scalar() or 0
    previous_period_expense = Expense.query.with_entities(db.func.sum(Expense.amount)).filter(Expense.date.between(sixty_days_ago, thirty_days_ago)).scalar() or 0

    if previous_period_expense == 0:
        expense_percentage_change = 0
    else:
        expense_percentage_change = ((current_period_expense - previous_period_expense) / previous_period_expense) * 100

    return render_template(
        'dashboard.html',
        new_orders_count=current_period_orders_count,
        orders_percentage_change=orders_percentage_change,
        current_period_revenue=current_period_revenue,
        revenue_percentage_change=revenue_percentage_change,
        current_period_expense=current_period_expense,
        expense_percentage_change=expense_percentage_change
    )