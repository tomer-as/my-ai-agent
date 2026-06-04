import os
import requests

def query_order_status(phone_number):
    # כתובת ה-Production Webhook הרשמית שלך
    N8N_WEBHOOK_URL = "https://tomeras.app.n8n.cloud/webhook/customer-lookup"
    
    # אריזת מספר הטלפון של הלקוח שנכנס לצ'אט
    payload = {
        "phone": phone_number
    }
    
    try:
        # שליחת הפנייה ל-n8n והמתנה לעיבוד הנתונים
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=15)
        
        if response.status_code == 200:
            # מחזיר את מחרוזת ה-JSON המלאה (בזכות ה-JSON.stringify שעשית ב-n8n)
            return response.text 
        else:
            return '{"status": "error", "message": "המערכת נתקלה בשגיאה בקבלת הנתונים."}'
            
    except Exception as e:
        return f'{{"status": "error", "message": "{str(e)}"}}'
