from fastapi import FastAPI, HTTPException
from database import get_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer API is working"}

@app.get("/customers")
def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT user_id FROM table1")
    rows = cursor.fetchall()
    conn.close()
    customers = [row[0] for row in rows]
    return {"customers": customers}

@app.get("/customers/{user_id}")
def get_customer(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table1 WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="Customer not found")

    first_order = dict(zip([col[0] for col in cursor.description], rows[0]))
    first_order["order_count"] = len(rows)
    return first_order
