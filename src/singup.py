import psycopg
from fastapi import APIRouter
from config import conn_str, authusers

# Initialize the router
router = APIRouter()

@router.post("/sign-up")
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
