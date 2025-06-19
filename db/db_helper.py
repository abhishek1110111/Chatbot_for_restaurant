# db/db_helper.py
import mysql.connector




def create_connection():
    """Create a database connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',   
            database='indian_eatery'
        )
        
        if connection.is_connected():
            print("Connection to the database established successfully.")
            return connection   
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
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
        return {"error": "Failed to connect to the database."}

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