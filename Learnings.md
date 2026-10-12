Never using common names USER, PASS, etc...; use only not comman words as env variables.

In docker compose yaml
```yaml
- "${PORT}"
- ${DB_USER}
```
both with in strings or without string use `$` and `{}` for env variables

For python, use

```py
from dotenv import load_dotenv
import os

load_dotenv()

port = os.getenv("PORT")

```

For creating table in postgres using psycopg use the below syntax

```py
import psycopg
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

```
