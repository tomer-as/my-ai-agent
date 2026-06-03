import os
import mysql.connector
from urllib.parse import urlparse

def get_db_connection():
    # מושך את ה-URL שהמערכת הגדירה אוטומטית
    db_url = os.getenv("DATABASE_URL")
    
    if not db_url:
        raise Exception("DATABASE_URL environment variable is not set!")

    # ניתוח ה-URL כדי לחלץ את הפרטים
    url = urlparse(db_url)
    
    return mysql.connector.connect(
        host=url.hostname,
        port=url.port,
        user=url.username,
        password=url.password,
        database=url.path[1:] # הסרת ה-/ מהתחלת שם בסיס הנתונים
    )

def query_order_status(order_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # שאילתה לדוגמה (תלוי במבנה הטבלאות שלך)
    query = "SELECT * FROM orders WHERE order_id = %s"
    cursor.execute(query, (order_id,))
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()
    return result
