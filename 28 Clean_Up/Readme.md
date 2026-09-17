# What Is Code Cleanup?

Code cleanup means improving existing code without unnecessarily changing its functionality. <br>

For example, this code works: <br>

```text
def create_url(url):
    # 50 lines of mixed logic
    pass
```

 <br> <br>
But it may contain: <br>

```text
Repeated code
Poor naming
Missing error handling
Hardcoded values
Unnecessary imports
Difficult-to-test functions
```

 <br>
Clean code separates responsibilities and makes future changes safer. <br> <br>

Real-world analogy <br>

Imagine your room: <br>

Working code: Everything is present, but items are scattered. <br>

Clean code: Items are organized, labeled, and easy to find. <br>

The application may work in both cases, but maintenance is easier in the second case. <br>

---

# Review Your Current Project Structure

Your intended structure: <br>

```text
Python_URL_Shortener/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   ├── security.py
│   ├── dependencies.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── auth.py
│       └── urls.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_security.py
│   └── test_urls.py
│
├── legacy/
│   └── cli_main.py
│
├── database.sql
├── seed.sql
├── requirements.txt
├── pytest.ini
├── .env
└── .gitignore
```

<br>

Responsibility of each file <br>

```text
File                 Responsibility
main.py           Creates FastAPI application and registers routers
config.py         Loads configuration
db.py             Creates database connections
models.py         Request and response schemas
security.py       Password hashing and JWT functions
dependencies.py   Reusable authentication dependencies
auth.py           Registration and login endpoints
urls.py           URL creation and redirection endpoints
tests/            Automated tests
```

<br>
Goal: Each file should have a clear responsibility.

<br>

---

# Step 1: Remove Unnecessary Imports

Unused imports make code confusing and can trigger linting warnings. <br>

Poor example <br>

```text
import random
import string
import os
import json
import time
```

 <br>
If your file only uses random and string, remove the rest. <br>

Clean example <br>

```text
import random
import string
```

 <br>
Check each file: <br>

```text
main.py
config.py
db.py
models.py
security.py
dependencies.py
auth.py
urls.py
```

Do not remove an import simply because it looks unused without checking whether it is required. <br>

---

# Step 2: Use Meaningful Names

Names should explain the purpose of variables and functions. <br>

**Avoid** <br>

```text
def f(x):
    y = x.fetchone()
    return y
```

<br>

**Prefer** <br>

```text
def get_user(cursor):
    user = cursor.fetchone()
    return user
```

<br>
Examples from your project: <br>

```text
Less clear            Clearer
conn                 connection
cur                    cursor
u                        user
data                  url_data
res                    response
x                       short_code
```

<br>

---

# Step 3: Centralize Configuration

You already created app/config.py. <br>

Your application should read configuration from there instead of repeating environment-variable logic in multiple files. <br>

**Avoid**  <br>

```text
# auth.py
import os

secret = os.getenv("JWT_SECRET_KEY")
```

```text
# another_file.py
import os

secret = os.getenv("JWT_SECRET_KEY")

```

<br>

**Prefer** <br>

```text
from app.config import JWT_SECRET_KEY
```

<br>

**Benefits** <br>

```text
One source of truth
Easier testing
Less duplication
Consistent configuration
```

<br>
Your database and JWT configuration should not be scattered across the project. <br>

---

# Improve Database Connection Handling

Your current app/db.py: <br>

```text
import psycopg2

from app.config import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER
)


def get_connection():
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    return connection
```

 <br>
This is acceptable for a learning project. <br> <br>

However, there are two important production considerations: <br>

A new database connection is created for each request. <br>

Connection failures need to be handled consistently. <br>

For a small application, you can retain this structure while improving the route-level cleanup. <br>

---

# Step 5: Use a Consistent Database Pattern

Your database operations should generally follow this structure: <br>

```text
connection = None
cursor = None

try:
    connection = get_connection()
    cursor = connection.cursor()

    # Execute SQL operations

    connection.commit()

except Exception:
    if connection:
        connection.rollback()

    raise

finally:
    if cursor:
        cursor.close()

    if connection:
        connection.close()
```

 <br>
Why is rollback() important? <br>

Suppose your endpoint performs two database operations: <br>

```text
Insert URL
    |
    v
Insert another record
    |
    v
Second operation fails
```

 <br> <br>

Without rollback, the transaction may be left in an inconsistent state. <br>

With rollback: <br>

```text
Transaction fails
       |
       v
Rollback changes
       |
       v
Database returns to previous transaction state
```

 <br>
Commit successful changes and rollback failed transactions. <br>

---

# Important Improvement: Handle Connection Failures

In your existing urls.py, the following pattern may exist: <br>

```text
connection = get_connection()

try:
    # Database operations
    pass

except Exception:
    # Error handling
    pass
```

 <br>
The problem is that if get_connection() fails, the error occurs before the try block. <br>

Better pattern <br>

```text
connection = None
cursor = None

try:
    connection = get_connection()
    cursor = connection.cursor()

    # Database operations

except Exception as error:
    if connection:
        connection.rollback()

    logger.exception(
        "Database operation failed"
    )

    raise HTTPException(
        status_code=500,
        detail="Database operation failed"
    ) from error

finally:
    if cursor:
        cursor.close()

    if connection:
        connection.close()
```

 <br>
This ensures connection errors can also be handled by the same error-handling flow. <br>

---

# Step 6: Avoid Repeating Short-Code Logic

Your project uses short-code generation. <br>

You may have: <br>

```text
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    return "".join(
        random.choice(characters)
        for _ in range(length)
    )
```

 <br>
And a separate function: <br>

```text
def generate_unique_short_code(cursor):
    while True:
        short_code = generate_short_code()

        cursor.execute(
            "SELECT id FROM urls WHERE short_code = %s",
            (short_code,)
        )

        if cursor.fetchone() is None:
            return short_code
```

 <br>
This is better than duplicating the same logic inside every endpoint. <br> <br>

Why uniqueness checks matter <br>

Random generation does not mathematically guarantee uniqueness. <br> <br>

Your database also has: <br>

short_code VARCHAR(20) NOT NULL UNIQUE <br>

You should retain the database-level unique constraint even if your application checks for collisions. <br>

Application validation and database constraints serve different purposes. <br>

---


# Step 7: Improve Pydantic Models

Your models should define the API contract. <br>

Example: <br>

```text
from pydantic import BaseModel, EmailStr, Field, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl = Field(
        ...,
        description="Original URL to shorten",
        examples=["https://github.com"]
    )


class UserCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8
    )


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
```

 <br>
 
**Cleanup rules** <br>

```text
Use request models for incoming data.
Use response models for outgoing data.
Do not expose password hashes.
Avoid unnecessary fields.
Add validation where appropriate.
```

<br>

---

# Step 8: Improve Authentication Security

Your authentication implementation is suitable for learning, but review these security points. <br>

**Passwords** <br>

```text
Never store plain passwords.
Use a suitable password-hashing algorithm.
Do not log passwords.
Do not return password hashes.
```

 <br>
 
**JWT**  <br>

```text
Keep JWT_SECRET_KEY in environment configuration.
Set an expiration time.
Validate the token signature.
Reject expired tokens.
Use HTTPS in production.
```

 <br>
 
**Login errors**  <br>

```text
Use a generic error message:
detail="Invalid email or password"
Avoid revealing whether an email exists.
```

 <br> <br>
Important <br> 

JWT authentication does not automatically provide: <br>

Logout invalidation <br>

Refresh-token management <br>

Role-based authorization <br>

Account lockout <br>

Multi-factor authentication <br>

These are additional features you may learn later. <br>

---

# Step 9: Review API Routes

Review each endpoint. <br>

```text
Endpoint                          Review
GET /                        Returns health message
POST /auth/register          Hashes password and creates user
POST /auth/login             Verifies credentials and returns JWT
POST /urls                   Requires authentication
GET /{short_code}            Redirects and records click
```

 <br>
Check that: <br>

```text
HTTP methods are correct.
Status codes are meaningful.
Response models are accurate.
Authentication is applied only where needed.
Errors do not expose internal details.
```

 <br>

 ---

 # Step 10: Be Careful With the Redirect Route

Your route: <br>

```text
@router.get("/{short_code}")
```

 <br>
matches many single-segment paths. <br> <br>

For example: <br>

```text
/abc123
/docs
/something
```

 <br>
FastAPI's routing order and mounted documentation routes affect which route handles a request. <br> <br>

Cleanup recommendations <br>

Keep documentation routes working. <br>
Test valid and invalid short codes. <br>
Ensure your redirect route does not accidentally capture an endpoint you intended to add later. <br>

Consider placing URL redirect routes under a deliberate prefix if your API design changes. <br> <br> <br>

For example: <br>

/r/{short_code} <br>

This is an architectural choice. Changing it would break existing shortened links, so do not change it casually. <br>

---

# Step 11: Review Error Handling

You previously added a broad exception handler: <br>

```text
@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception
):
    ...
```

 <br>
Review the following: <br>

**Do** <br>

```text
Log detailed errors on the server.
Return safe messages to clients.
Preserve intentional HTTPException responses.
Avoid exposing SQL queries or credentials.
```

 <br>
 
**Do not**  <br>

```text
return {
    "error": str(exc)
}
```

 <br>
This could reveal internal details such as: <br>

password authentication failed for user "postgres" <br>

A safer response is: <br>

```text
{
  "detail": "An internal server error occurred"
}
```

 <br>
The logger should contain the details needed for debugging. <br>

---

# Step 12: Run Formatting and Linting

Automated formatting helps keep code consistent. <br>

Install tools: <br>

```text
pip install black ruff
```

 <br>
Update requirements: <br>

```text
pip freeze > requirements.txt
```

 <br>
Run Ruff <br>

```text
ruff check app tests
```

 <br> 
Ruff identifies various code-quality problems. <br> <br>

Run Black <br>

```text
black app tests
```

 <br>
Black formats Python files automatically. <br> <br>

Check formatting without changing files <br>

```text
black --check app tests
```

 <br>
Formatting tools can modify your files. Review the changes with Git before committing. <br>

---

# Step 13: Run Tests

First, execute your tests: <br>

```text
pytest -v
```

 <br>
Then run linting: <br>

```text
ruff check app tests
```

 <br>
Then check formatting: <br>

```text
black --check app tests
```

 <br> <br>
A useful local quality sequence: <br>

```text
pytest -v
ruff check app tests
black --check app tests
```

 <br>
Do not claim that the project passes until you have actually run the commands and checked the output. <br>

---

# Step 14: Improve requirements.txt

Your requirements file should contain the dependencies needed by the project. <br>

Example categories: <br>

```text
fastapi
uvicorn
psycopg2-binary
python-dotenv
python-jose
passlib
email-validator
pytest
httpx
ruff
black
```

 <br>
Your actual file may include version pins and transitive dependencies. <br> <br>

Best practices <br>

```text
Use a virtual environment.
Keep dependencies updated carefully.
Review dependency compatibility.
Separate production and development dependencies as your project grows.
Test after dependency changes.
```

 <br>
For a professional project, consider maintaining separate files such as: <br>

requirements.txt <br>
requirements-dev.txt <br>

---

# Step 15: Check .gitignore

Your .gitignore should include: <br>

```text
venv/
.env
__pycache__/
*.pyc
.pytest_cache/
.ruff_cache/
.coverage
```

 <br>
Important security note <br>

If .env was previously committed to Git, adding it to .gitignore does not remove it from Git history. <br> <br>

Check your Git status: <br>

git status <br>

If a real secret was committed or exposed, rotate that secret. <br>

---

# Step 16: Improve Your README

Your README should allow another developer to reproduce the project. <br>

Recommended structure: <br>

```text
# Python URL Shortener

## Overview

## Features

## Technology Stack

## Project Structure

## Prerequisites

## Installation

## Environment Configuration

## Database Setup

## Running the Application

## API Endpoints

## Authentication

## Running Tests

## Troubleshooting

## Future Improvements
```

 <br>
Example README Sections <br>

```text
Installation
git clone <your-repository-url>

cd Python_URL_Shortener

python -m venv venv

Windows PowerShell:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt
Run the API
uvicorn app.main:app --reload
API documentation
http://localhost:8000/docs
Run tests
pytest -v
```

 <br>
Do not include your actual database password or JWT secret in the README. <br>

---

# Step 17: Check Database Reproducibility

Your project contains: <br>

```text
database.sql
seed.sql
```

 <br>
Review whether a new developer can: <br>

```text
Create the database.
Create the tables.
Add indexes.
Add the password hash column if required.
Insert sample data.
Run the application successfully.
```

 <br>
 
**Important schema issue** <br>

Your original database.sql may not include the newer password_hash column. <br>

Update the schema carefully so a fresh database setup supports your current authentication code. <br>

For a fresh database, add the column directly to the users table definition: <br>

```text
password_hash TEXT
```

 <br>
For an existing database, use a migration: <br>

```text
ALTER TABLE users
ADD COLUMN password_hash TEXT;
```

 <br>
Avoid running the CREATE TABLE statements repeatedly on an already-created database unless you intentionally reset it. <br>

---

# Step 18: Test From a Clean Setup

A project may work on your computer but fail on another system because of: <br>

```text
Missing dependencies
Incorrect environment variables
Missing database tables
Hardcoded paths
Untracked files
Incorrect Python version
Missing migration steps
```

 <br>
Try to reproduce your setup using the README instructions. <br>

 <br>
Clean setup checklist <br>

```text
Clone or copy the project into a separate folder
Create a new virtual environment
Install dependencies from requirements.txt
Create a separate test database
Configure environment variables
Run database schema setup
Start FastAPI
Open Swagger documentation
Run automated tests
Confirm README instructions work
```

 <br>
 
---

# Step 19: Git Review

```text
Check your changes: 
git status

View differences:
git diff

Check tracked files:
git ls-files

Check recent commits:
git log --oneline -5
```

<br>  <br>

Before committing, ensure that: <br>

```text
.env is not tracked.
Passwords are not present in source code.
Debug statements are removed.
Tests are included.
README is updated.
Unnecessary files are removed.
```

 <br>
Example commit:
 <br>
git add app tests README.md requirements.txt pytest.ini .gitignore <br>
 
git commit -m "Clean up FastAPI URL shortener project" <br>

Only include files you have reviewed. <br>

---

# Step 20: Basic CI Workflow Preview

You will learn CI/CD more deeply during your DevOps phase. <br>

A basic GitHub Actions workflow could run tests automatically. <br> <br>

Create: <br>

.github/workflows/tests.yml <br>

Example: <br>

```text
name: Run Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest -v
```

 <br> <br>
Important considerations <br>

Your current application loads required database and JWT environment variables during import. <br>

Therefore, the workflow may fail if those variables are not configured. <br> <br>

You will need to: <br>

Configure safe test environment variables. <br>

Use a test database or mocks. <br>

Ensure your test suite does not depend on your personal .env. <br>

Avoid storing secrets directly in the workflow. <br>

This is a preview, not a guarantee that your current tests will pass in GitHub Actions without additional setup. <br>

---

# Code Quality vs Code Functionality

These are different concepts. <br>

```text
Functionality                           Code quality
Does the feature work?               Is the code maintainable?
Returns expected results             Uses clear structure
Meets requirements                   Handles errors properly
Passes functional tests              Is easy to modify
```

<br>
Example: <br>

```text
def create_url():
    # Very long function
    # Repeated SQL
    # Hardcoded values
    # No validation
    pass
```

<br>
It might work today but be difficult to maintain.
<br>
Clean code should make future features easier to add.

---
















