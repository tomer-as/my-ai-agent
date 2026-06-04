import os
from db_connector import query_order_status

def query_customer_by_phone(phone_number: str) -> str:
    """
    הפונקציה הזו מקבלת מספר טלפון של לקוח, פונה למנוע האוטומציה ב-n8n,
    ומחזירה ניתוח מלא של היסטוריית ההחזרות, מוקשי מידות (Product Traps) והמלצת מידה מדויקת.
    יש להשתמש בה מיד כשהלקוח מספק מספר טלפון.
    """
    if not phone_number:
        return "שגיאה: לא סופק מספר טלפון."
    
    # הפעלת הצינור שבנינו ל-n8n
    return query_order_status(phone_number)

if __name__ == "__main__":
    # בדיקה מקומית מהירה
    print(query_customer_by_phone("050-1112267"))
