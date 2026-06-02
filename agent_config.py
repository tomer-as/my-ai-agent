# Agent Database Config
DB_HOST = "YOUR_AWS_ENDPOINT"
DB_USER = "YOUR_USER"
DB_PASS = "YOUR_PASSWORD"
DB_NAME = "YOUR_DATABASE_NAME"

def fetch_data(query):
    # כאן תבוא הלוגיקה של החיבור ל-MySQL
    print(f"Executing: {query} on {DB_HOST}")
