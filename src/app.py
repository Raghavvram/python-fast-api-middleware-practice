import logging

from fastapi import FastAPI, HTTPException, status
import psycopg
from pydantic import BaseModel


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
logging.getLogger("psycopg").setLevel(logging.DEBUG)

conn_str = "host=localhost port=15432 dbname=auth_db user=admin password=admin@007"

app = FastAPI()

class authusers(BaseModel):
    name: str
    email: str
    password: str


@app.get("/")
def return_root():
    return {"Message": "Backend is Running ...."}


@app.get("/db")
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


@app.post("/sign-up")
async def create_user(user: authusers):
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as curr:
            query = """
                INSERT INTO users ("name", "email", "password")
                VALUES (%(name)s, %(email)s, %(password)s)
                RETURNING id;
            """
            curr.execute(query, user.model_dump())
            conn.commit()
    return {"messgae": "Iteam Created Successfully"}

@app.post("/sign-in")
def auth_user(user: authusers):
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as curr:
            query = """
                SELECT "name", "password"
                FROM users
                WHERE email = %(email)s
            """
            curr.execute(query, {"email" : user.email})
            db_user = curr.fetchone()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    db_name, db_password = db_user

    if (user.password != db_password): raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

    return {
            "status": "success",
            "message": "Logged in successfully",
            "user": {"name": db_name}
        }
