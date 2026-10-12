import logging
from fastapi import FastAPI
from root import router as root_router
from db import router as db_router
from singup import router as singup_router
from signin import router as signin_router
from config import conn_str
import psycopg

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
logging.getLogger("psycopg").setLevel(logging.DEBUG)

conn = psycopg.connect(conn_str)

try:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        """)

    conn.commit()
    print("Users table created successfully.")

finally:
    conn.close()

app = FastAPI()

app.include_router(root_router)
app.include_router(db_router)
app.include_router(singup_router)
app.include_router(signin_router)
