from fastapi.responses import JSONResponse
from db import db_helper
import generic_helper

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
        if session_id not in in_progress_orders:
            in_progress_orders[session_id] = dict(zip(food_items, quantity))
        else:
            ongoing_order_dict = in_progress_orders[session_id]
            ongoing_order_dict.update(dict(zip(food_items, quantity)))
            in_progress_orders[session_id] = ongoing_order_dict
            
        extract_message = generic_helper.get_str_from_food_dict(in_progress_orders[session_id])
        print(extract_message)
        
        return f' {extract_message} has been added to your order. you want to add more items? or finish your order?'
    else:
        return f"Sorry! Can you please Specify item and quantities clearly. like one piza, 2 lassi, two chole bhature, etc"

def complete_order(session_id: str):
    ongoing_order = in_progress_orders.get(session_id)
    print('************')
    print(in_progress_orders)
    print('&&&&&&&')
    print(session_id)
    print('#############')
    print(ongoing_order)
    print('*************')
    response =db_helper.save_order(ongoing_order)
    return response
            