import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="pfe-data.database.windows.net",
        user="admin_pfe",
        password="password_24",
        database="PFE-database"
    )
    if conn.is_connected():
        print("Connected to the database")
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if conn.is_connected():
        conn.close()