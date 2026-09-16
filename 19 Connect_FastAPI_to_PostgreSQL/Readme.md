FastAPI does not replace PostgreSQL. <br>

FastAPI is responsible for handling HTTP/API requests. <br>

PostgreSQL is responsible for persistent relational data. <br>

Python code connects the two. <br>

# Three Different Responsibilities

Keep these separate in your mind. <br>

**FastAPI** Handles: <br>

```text
HTTP
Routes
Requests
Responses
Validation
Status codes
API documentation
```

<br>
**Python**

Handles: <br>

```text
Application logic
Database connection
SQL execution
Processing results
```

**PostgreSQL** Handles: <br>

```text
Persistent data
Tables
Relationships
Constraints
Indexes
Transactions
SQL queries
```

<br>
So: <br>

```text
FastAPI ≠ Database
Python ≠ Database
PostgreSQL ≠ API framework
```

They work together

---

# Create a virtual Environemnt

```text
python -m venv venv
```

Activate it: <br>

```text
.\venv\Scripts\Activate.ps1
```

## requirements.txt

```text
fastapi
uvicorn
psycopg2-binary
python-dotenv
email-validator
```

Install the packages: <br>

```text
pip install -r requirements.txt
```

<br>

Verify installation: <br>

```text
pip list
```

```text
Package                 Purpose

fastapi             Creates the API

uvicorn             Runs the FastAPI application

psycopg2-binary     Connects Python to PostgreSQL

python-dotenv       Loads variables from .env

email-validator     Supports Pydantic's EmailStr
```

---

# Create PostgreSQL Database

We will use database named fastapi_practice  <br>

Open PostgreSQL using <br>

```text
psql -U postgres
```

Enter your PostgreSQL password. <br>
 <br>

Create the Database: <br>

```text
CREATE DATABASE fastapi_practice;
```

 <br>
Connect to it: <br>

```text
\c fastapi_practice
```

 <br>
Create users table <br>

```text
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

 <br>
Insert sample data: <br>

```text
INSERT INTO users (name, email)
VALUES
    ('Sunaina', 'sunaina.practice@example.com'),
    ('Rahul', 'rahul.practice@example.com'),
    ('Aman', 'aman.practice@example.com');
```

Verify the records: <br>

```text
SELECT * FROM users;
```

 <br>
You should see three users. <br>

Exit PostgreSQL: <br>

```text
\q
```

This database is separate from your url_shortener database. <br>

---

# .env

```text
DB_HOST=localhost
DB_NAME=fastapi_practice
DB_USER=postgres
DB_PASSWORD=postgres123@!#
DB_PORT=5432
```


Do not upload .env to GitHub.

---

# db.py

This file will contain the PostgreSQL connection function.

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

<br>
The flow is: <br>

```text
Python
   ↓
psycopg2
   ↓
PostgreSQL
```

---

# Test the Database Connection

Before connecting FastAPI, test the connection separately. <br>

Create a temporary file: <br>

test_db.py <br> <br>

```text
from db import get_connection


connection = get_connection()

print("Database connection successful!")

connection.close()
```

Run: <br>

```text
python test_db.py
```

 <br>
Expected output: <br>

Database connection successful! <br> <br>

After testing, you can delete test_db.py. <br> <br>

---

# Create the models.py File

This file will contain the Pydantic models used for request validation. <br>

```text
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
```

FastAPI automatically validates the request using Pydantic. <br>

---

# Create main.py

This file will contain the FastAPI application and API routes.

```text
# Add imports and create the app
from fastapi import FastAPI, HTTPException, status

from db import get_connection
from models import UserCreate


app = FastAPI()

# Create the GET /users API

@app.get("/users")
def get_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email
        FROM users
        ORDER BY id;
    """)

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    result = []

    for user in users:
        result.append({
            "id": user[0],
            "name": user[1],
            "email": user[2]
        })

    return result

# Create the GET /users/{user_id} API

@app.get("/users/{user_id}")
def get_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, email
        FROM users
        WHERE id = %s;
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user[0],
        "name": user[1],
        "email": user[2]
    }

Create the POST /users API

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (name, email)
            VALUES (%s, %s)
            RETURNING id, name, email;
            """,
            (user.name, user.email)
        )

        created_user = cursor.fetchone()

        connection.commit()

        return {
            "id": created_user[0],
            "name": created_user[1],
            "email": created_user[2]
        }

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()
```


Complete flow: <br>

```text
GET /users
     ↓
FastAPI route
     ↓
get_connection()
     ↓
cursor.execute()
     ↓
SELECT query
     ↓
PostgreSQL returns rows
     ↓
fetchall()
     ↓
Convert tuples to dictionaries
     ↓
JSON response
```

---

# .gitignore

```text
venv/
.env
__pycache__/
*.pyc
```

---

# Run the FastAPI application

Make sure the virtual environment is activated. <br>

Run: <br>

```text
uvicorn main:app --reload
```

Test it : <br>

```text
http://localhost:8000/docs
```


<br>
```text
psql -U postgres
\c fastapi_practice
SELECT * FROM users;
```

---








