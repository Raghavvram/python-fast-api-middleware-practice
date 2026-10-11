from pydantic import BaseModel

conn_str = "host=localhost port=15432 dbname=auth_db user=admin password=admin@007"

class authusers(BaseModel):
    name: str
    email: str
    password: str
