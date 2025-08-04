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
    cursor.execute("SELECT DISTINCT customer_id FROM table1")
    rows = cursor.fetchall()
    conn.close()
    customers = [dict(row) for row in rows]
    return {"customers": customers}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table1 WHERE customer_id = ?", (customer_id,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer = dict(rows[0])
    customer["order_count"] = len(rows)
    return customer
