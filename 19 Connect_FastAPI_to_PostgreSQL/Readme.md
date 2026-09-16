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




