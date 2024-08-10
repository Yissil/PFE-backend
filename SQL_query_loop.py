import mysql.connector
import time
from mysql.connector import Error

DB_USER = "admin_pfe"
DB_PASSWORD = "password_24"
DB_SERVER = "pfe-data.database.windows.net"
DB_NAME = "PFE-database"

# Function to query the MySQL database
def query_database(cursor):
    try:
        cursor.execute("SELECT * FROM data")  # Replace with your query
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

# Function to connect to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host=DB_SERVER,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            print("Connected to the database")
            return conn
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Main loop
def main():
    conn = connect_to_database()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()

    try:
        while True:
            query_database(cursor)
            time.sleep(10)  # Wait for 10 seconds before querying again
    except KeyboardInterrupt:
        print("Stopping the continuous query.")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
