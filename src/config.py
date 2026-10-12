from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

port = os.getenv("PORT")
localhost = os.getenv("LOCALHOST")
dbname = os.getenv("DBNAME")
user = os.getenv("DB_USER")
passs = os.getenv("DB_PASS")

conn_str = f"host={localhost} port={port} dbname={dbname} user={user} password={passs}"

class authusers(BaseModel):
    name: str
    email: str
    password: str
