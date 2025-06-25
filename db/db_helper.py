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
            database='indian_eatery'
        )
        print('connection created')
        print(connection)
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
        
def save_order(ongoing_order: dict):
    """add a complete order in database."""
    print('okkkkkkkkkkkkkkkk')
    print(ongoing_order)
    connection = create_connection()
    print(connection)
    
    if not connection:
        print("Failed to connect to the database. function :save_order")
        return f'something went wrong while connecting to the chatbot'

    cursor = connection.cursor(dictionary=True)
    print('cursor test')
    print(cursor)
    try:
        
        # query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        # cursor.execute(query, (order_id,))
        # order = cursor.fetchone()
        # print(order)
        
        return f'complete order has been saved successfully'
    except mysql.connector.Error as err:
        print(str(err))
        return f'something went wrong while connecting to the chatbot'
    finally:
        cursor.close()
        close_connection(connection)