# we will convert your existing URL-shortening logic into a FastAPI endpoint.

The API will: <br>

Accept a long URL. <br>

Validate the URL. <br>

Generate a six-character short code. <br>

Check whether the short code already exists. <br>

Save the URL in PostgreSQL. <br>

Return the created short code. <br>

Use database transactions. <br>

Return HTTP 201 Created. <br>

---

# Application flow

```text
Client / Swagger
       |
       | POST /urls
       ↓
FastAPI
       |
       ↓
Validate original_url
       |
       ↓
Generate unique short code
       |
       ↓
Insert into PostgreSQL
       |
       ↓
Commit transaction
       |
       ↓
Return response
```

---

# Final Project Structure

Your repository will look like this: <br>

```text
Python_URL_Shortener/
│
├── venv/
├── main.py
├── api_main.py          # New FastAPI application
├── db.py                # New database connection file
├── models.py            # New Pydantic models
├── database.sql
├── seed.sql
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

#  Why create separate files?

```text
File           Responsibility
main.py          Existing CLI application
api_main.py      FastAPI routes
db.py            Database connection
models.py        Request and response validation
database.sql     Database schema
seed.sql         Sample data
```

---

# In Requirements.txt 

appended <br>

```text
fastapi
uvicorn
pydantic
```

Activate the virutal Environment <br>
**.\venv\Scripts\Activate.ps1** <br> <br>

Install the updated packages: <br>
**pip install -r requirements.txt** <br> <br>

Verify FastAPI is installed: <br>
**python -c "import fastapi; print('FastAPI installed successfully')"**  <br>

---

# Verify your database

```text
psql -U postgres
\c url_shortener

\dt
SELECT id, name, email FROM users ORDER BY id;

SELECT id, short_code, original_url, user_id
FROM urls
ORDER BY id;

```

---

# Create db.py

```text
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    return connection
```

It provides one reusable function: <br>

```text
get_connection()
```


Whenever your FastAPI application needs to access PostgreSQL, it can import this function. <br>

```text
from db import get_connection
```

Architecture: <br>

```text
api_main.py
     |
     | imports
     ↓
db.py
     |
     ↓
psycopg2
     |
     ↓
PostgreSQL
```

---

# Create models.py

```text
from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl
```

original_url: HttpUrl <br>

This tells Pydantic that the input should be a valid HTTP or HTTPS URL. <br> <br>

FastAPI will reject invalid input before your database query runs. <br>

Without validation, your database could receive incorrect values such as: <br>

hello <br>
abc <br>
not a website <br>

Validation protects the API input layer. PostgreSQL still protects database integrity. <br>

---

# Create api_main.py

```text
# Add the imports
import random
import string

from fastapi import FastAPI, HTTPException, status

from db import get_connection
from models import URLCreate

# Create the FastAPI application:

app = FastAPI(
    title="URL Shortener API",
    description="A practice URL shortening API using FastAPI and PostgreSQL",
    version="1.0.0"
)

# Add the short_cod_generator
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    code = ""

    for _ in range(length):
        code += random.choice(characters)

    return code

# Create a function to generate a unique short code

def generate_unique_short_code(cursor):
    while True:
        short_code = generate_short_code()

        cursor.execute(
            """
            SELECT id
            FROM urls
            WHERE short_code = %s;
            """,
            (short_code,)
        )

        existing_url = cursor.fetchone()

        if existing_url is None:
            return short_code

# Add a Root Endpoint
@app.get("/")
def home():
    return {
        "message": "URL Shortener API is running"
    }


# Create the POST /urls Endpoint

@app.post("/urls", status_code=status.HTTP_201_CREATED)
def create_short_url(url_data: URLCreate):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        short_code = generate_unique_short_code(cursor)

        cursor.execute(
            """
            INSERT INTO urls (
                short_code,
                original_url,
                user_id
            )
            VALUES (%s, %s, %s)
            RETURNING id, short_code, original_url, user_id, created_at;
            """,
            (
                short_code,
                str(url_data.original_url),
                1
            )
        )

        created_url = cursor.fetchone()

        connection.commit()

        return {
            "id": created_url[0],
            "short_code": created_url[1],
            "original_url": created_url[2],
            "user_id": created_url[3],
            "created_at": created_url[4]
        }

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()



```

---

# Run the FastAPI Application

```text
uvicorn api_main:app --reload
```

Open Swagger UI <br>

```text
http://localhost:8000/docs
```

## Test the Root Endpoint

In Swagger: <br>

Open GET /. <br>
Click Try it out. <br>
Click Execute. <br>

Expected response: <br>

```text
{
    "message": "URL Shortener API is running"
}
```

This confirms that your FastAPI application is running <br>



## Test POST /urls

In Swagger: <br>

Open POST /urls. <br>

Click Try it out. <br>

Enter the following request: <br>

```text
{
    "original_url": "https://github.com"
}
```

Click Execute.
 <br>
Expected status: <br>

201 Created
 <br>
Example response: <br>

```text
{
    "id": 5,
    "short_code": "aB12xY",
    "original_url": "https://github.com",
    "user_id": 1,
    "created_at": "2026-09-16T..."
}
```

Your ID, short code, and timestamp will be different. <br>

## Verify the Record in PostgreSQL

Open a second terminal while FastAPI continues running in the first terminal. <br>

```text
psql -U postgres

\c url_shortener
```

 <br>
Run: <br>

```text
SELECT
    id,
    short_code,
    original_url,
    user_id,
    created_at
FROM urls
ORDER BY id DESC;
```

 <br>
You should see the URL created through Swagger. <br>

Verify a specific short code <br>

Replace aB12xY with the code returned by your API: <br>

```text
SELECT *
FROM urls
WHERE short_code = 'aB12xY';
```

This proves the complete connection: <br>

```text
Swagger
   ↓
FastAPI
   ↓
Python
   ↓
psycopg2
   ↓
PostgreSQL
   ↓
urls table
```

---

# main.py vs app_main.py

main.py <br>
User → Terminal → Python → PostgreSQL <br> <br>

app_main.py <br>
Client → FastAPI → Python → PostgreSQL <br>


```text
Python_URL_Shortener/
│
├── main.py       → CLI application
└── api_main.py   → FastAPI application
```

<br>
They can use the same PostgreSQL database, but they are separate programs. <br> <br>

### Why keep main.py along with app_main.py

- It contains your original Python practice.

- You can compare CLI logic with FastAPI logic.

- You can preserve your original implementation.

- It helps you understand how the same business logic can be exposed through different interfaces.

### Having both files does not mean both applications run simultaneously. You choose which one to start.

- CLI: python main.py

- API: uvicorn api_main:app --reload
















