from fastapi import FastAPI, HTTPException
from database import get_connection
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer API is running"}



@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM table1 WHERE user_id = ?", (customer_id,))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            raise HTTPException(status_code=404, detail="Customer not found")

        customer = dict(rows[0])
        customer["order_count"] = len(rows)
        return customer
    except Exception as e:
        return {"error": str(e)}


@app.get("/customers")
def get_all_customers():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT user_id FROM table1")
        rows = cursor.fetchall()
        conn.close()
        customers = [{"user_id": row["user_id"]} for row in rows]
        return {"customers": customers}
    except Exception as e:
        return {"error": str(e)}
