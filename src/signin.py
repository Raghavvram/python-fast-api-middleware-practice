import psycopg
from fastapi import APIRouter
from fastapi import HTTPException, status
from config import conn_str, authusers

# Initialize the router
router = APIRouter()

@router.post("/sign-in")
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
