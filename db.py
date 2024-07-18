import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={os.getenv("DB_SERVER")};'
    f'DATABASE={os.getenv("DB_NAME")};'
    f'UID={os.getenv("DB_USER")};'
    f'PWD={os.getenv("DB_PASSWORD")}'
)
conn = pyodbc.connect(conn_str)