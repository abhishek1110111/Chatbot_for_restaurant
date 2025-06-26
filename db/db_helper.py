# db/db_helper.py
import mysql.connector

def create_connection():
    
    """Create a database connection to the MySQL database."""
    print('create_connection function called')
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',   
            database='indian_eatery',
            connection_timeout=5 # set a 5 sec timeout for the connection
        )
        if connection.is_connected():
            print("Connection to the database established successfully.")
            return connection   
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 'something went wrong while connecting to the chatbot'

    
def close_connection(connection):
    """Close the database connection."""
    if connection.is_connected():
        connection.close()
        print("Database connection closed.")
    else:
        print("Connection is already closed or was never established.")

def get_order_status_by_id(order_id: int):
    """Track an order by its ID."""
    connection = create_connection()
    print(type(order_id))
    print(order_id)
    if not connection:
        print("Failed to connect to the database. function :get_order_status_by_id")
        return f'something went wrong while connecting to the chatbot'

    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM order_tracking WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        order = cursor.fetchone()
        print(order)
        return order
    except mysql.connector.Error as err:
        print(str(err))
        return {"error": str(err)}
    finally:
        cursor.close()
        close_connection(connection)
        
def save_order(ongoing_order: dict, ongoing_order_address: dict):
    """add a complete order in database."""
     
    connection = create_connection()
    if not connection:
        print("Failed to connect to the database. function :save_order")
        return f'something went wrong while connecting to the chatbot'

    cursor = connection.cursor(dictionary=True)
    try:
        get_food_item_id = get_item_id_by_name(ongoing_order, cursor)
        order_id = generate_order_id(cursor)
        print(get_food_item_id)
        count = 0
        for item in get_food_item_id:
            item_id = item['item_id']
            quantity = int(ongoing_order[item['name']])
            total_price = item['price'] * quantity
            #Insert each item into the orders table
            query = "INSERT INTO orders (order_id, item_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
            result = cursor.execute(query, (order_id, item_id, quantity, total_price))
            rs = connection.commit()
            count += cursor.rowcount
            
        if count == len(get_food_item_id):
            print(f'{count} items have been added to the order')
            add_address = add_adress_to_db(order_id, cursor, connection, ongoing_order_address)
            tracking_status = add_tracking_status(order_id, cursor, connection)
            if tracking_status and add_address:
                print(f'Tracking status for order {order_id} added successfully. function: save_order')
                total_order_price = get_total_price_by_order_id(order_id, cursor)
                return f'Thank you for choosing, Your order has been placed successfully with order ID: {order_id}.\
                    The total price is £ {total_order_price}. To know the order status, write "track order"'
            else:
                print(f'Failed to add tracking status or address for order {order_id}. function: save_order')
        else:
            print(f'Only {count} items have been added to the order, function: save_order')
    except mysql.connector.Error as err:
        print(str(err))
        return f'something went wrong while connecting to the chatbot, function: save_order'
    finally:
        cursor.close()
        close_connection(connection)
        
def get_item_id_by_name(ongoing_order: dict, cursor):
    """Get food item ID by its name."""
    try:
        keys = list(ongoing_order.keys())
        placeholders = ','.join(['%s'] * len(keys))
        query = f"SELECT * FROM food_items WHERE name in ({placeholders})"
        cursor.execute(query, keys)
        items = cursor.fetchall()
        return items
    except mysql.connector.Error as err:
        print(f"Error: {err} , function: get_item_id_by_name")
        return f'something went wrong while connecting to the chatbot, function: get_item_id_by_name' 

def generate_order_id(cursor):
    query = "SELECT MAX(order_id) AS max_order_id FROM orders"
    cursor.execute(query)
    result = cursor.fetchone()
    if result['max_order_id'] is not None:
        return result['max_order_id'] + 1
    else:
        return 1  # Start with order ID 1 if no orders exist

def add_tracking_status(order_id, cursor, connection):
    """Add tracking status for the order."""
    try:
        query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
        cursor.execute(query, (order_id, 'Order Placed'))
        connection.commit()
        print(f"Tracking status for order {order_id} added successfully. function: add_tracking_status")
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err} , function: add_tracking_status, function: add_tracking_status")
        return False

def get_total_price_by_order_id(order_id, cursor):
    """Get total price of an order by its ID."""
    try:
        query = "SELECT get_total_order_price(%s)"
        cursor.execute(query, (order_id,))
        total_price_dict = cursor.fetchone()
        if total_price_dict:
            values  = total_price_dict.values()
            value = list(values)[0]
            price = float(value)
            return price  
    except mysql.connector.Error as err:
        print(f"Error: {err} , function: get_total_price_by_order_id")
        return f'something went wrong while connecting to the chatbot, function: get_total_price_by_order_id'
    
def add_adress_to_db(order_id, cursor, connection, ongoing_order_address: dict):
    """Add address to the database."""
    print(ongoing_order_address)
    try:
        query = "INSERT INTO address (order_id, street_address, city, post_code) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (order_id, ongoing_order_address['address'], ongoing_order_address['city'], ongoing_order_address['postcode']))
        connection.commit()
        print(f"Address for order {order_id} added successfully. function: add_adress_to_db")
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err} , function: add_adress_to_db")
        return False