from fastapi.responses import JSONResponse
from db import db_helper

in_progress_orders = {}

def track_order(parameters: dict,):
    order_id = int(parameters['order_id'])
    status = db_helper.get_order_status_by_id(order_id)
    print(status)
    print(type(status))
    if status == None:
        print(f"No order found with ID: {order_id}")
        message = f"We did not found any order with this id: {order_id}"
    elif status['status']:
        print(f"Order found: {status}")
        message =  f" your order status is {status['status']}"
    else:
        message = f"something went wrong"
    return message

def add_order(parameters: dict, session_id: str):
    food_items = parameters["food-item"]
    quantity = parameters["quantity"]
    if len(food_items) == len(quantity):
        in_progress_orders[session_id] = dict(zip(food_items, quantity))
        print(in_progress_orders)
        return f"All clear"
    else:
        return f"Sorry! Can you please Specify item and quantities clearly. like one piza, 2 lassi, two chole bhature, etc"
        