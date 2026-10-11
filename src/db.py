import psycopg
from fastapi import APIRouter

# Initialize the router
router = APIRouter()

@router.get("/db")
def return_db():
    with psycopg.connect(
                host="localhost",
                port=15432,
                dbname="auth_db",
                user="admin",
                password="admin@007"
            ) as conn:
        with conn.cursor() as curr:
            curr.execute("SELECT * FROM users")
            output = curr.fetchall()
        conn.close()
        return {"Output" : output}
