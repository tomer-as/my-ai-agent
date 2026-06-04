import os
from db_connector import query_order_status

def handle_customer_request(phone_number):
    if not phone_number:
        return "אנא ספק מספר טלפון כדי שאוכל לעזור לך להתאים מידה."
    
    # הפעלת הצינור החי והרשמי שלנו ל-n8n
    return query_order_status(phone_number)

if __name__ == "__main__":
    # הרצת טסט פנימי מהיר לראות שהקוד רץ ללא שגיאות סינטקס
    print(handle_customer_request("052-1234567"))
