import logging
from fastapi import FastAPI
from root import router as root_router
from db import router as db_router
from singup import router as singup_router
from signin import router as signin_router

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
logging.getLogger("psycopg").setLevel(logging.DEBUG)

app = FastAPI()

app.include_router(root_router)
app.include_router(db_router)
app.include_router(singup_router)
app.include_router(signin_router)
