from fastapi.responses import JSONResponse
from db import db_helper
import generic_helper

in_progress_orders = {}
in_progress_orders_address = {}

def track_order(parameters: dict,):
    """Track an order by its ID."""
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
    """Add items to the ongoing order."""
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
        
        return f' {extract_message} has been added to your order. you want to add more items? or add your address for delivery?'
    else:
        return f"Sorry! Can you please Specify item and quantities clearly. like one pizza, 2 lassi, two chole bhature, etc"

def complete_order(session_id: str):
    """Complete the order and save it to the database."""
    ongoing_order = in_progress_orders.get(session_id)
    ongoing_order_address = in_progress_orders_address.get(session_id)
    response =db_helper.save_order(ongoing_order, ongoing_order_address)
    in_progress_orders.pop(session_id)
    return response

def remove_order(parameters: dict, session_id: str):
        """Remove items from the ongoing order."""
        food_items = parameters["food-item"]
       
        if session_id in in_progress_orders:
            ongoing_order_dict = in_progress_orders[session_id]
            for item in food_items:
                if item in ongoing_order_dict:
                    del ongoing_order_dict[item]
            in_progress_orders[session_id] = ongoing_order_dict
            if len(in_progress_orders[session_id]) == 0:
                return "Your order cart is now empty. please add items to your order."
            else:
                extract_message = generic_helper.get_str_from_food_dict(in_progress_orders[session_id])
                result = ', '.join(food_items)
                return f' {result} has been removed from your order and {extract_message} is left in you cart. you want to add more items? or add your address for delivery?'
        else:
            return "No ongoing order found to remove items from."            

def add_address(parameters: dict, session_id: str):
    """Add address to the ongoing order."""
    if session_id in in_progress_orders_address:
        address =  parameters['street-address']['street-address']
        if address:
            in_progress_orders_address[session_id] = {'address': address, 'city': parameters['geo-city-gb'], 'postcode': parameters['zip-code']}
            return f'Address: {address}, {parameters['geo-city-gb']}, {parameters['zip-code']} has been added to your order. you want to finish your order or add some more items?'
        else:
            return "Please provide a valid address."
    else:
        address =  parameters['street-address']['street-address']
        if address:
            in_progress_orders_address[session_id] = {'address': address, 'city': parameters['geo-city-gb'], 'postcode': parameters['zip-code']}
            return f'Address: {address}, {parameters['geo-city-gb']}, {parameters['zip-code']} has been added to your order. you want to finish your order or add some more items?'
        else:
            return "Please provide a valid address."