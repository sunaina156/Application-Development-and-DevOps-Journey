# What Is Project Structure?

Project structure means how we organize files and folders inside an application. <br>

Imagine you keep everything in one file: <br>

```text
main.py
├── Database connection
├── API routes
├── Validation
├── Authentication
├── Business logic
└── Error handling
```

 <br>
This may work for a small project, but as the application grows, the file becomes difficult to understand and maintain. <br>

A professional application separates responsibilities into different files.
 <br>

 ```text
Example: E-commerce Application
ecommerce/
├── main.py
├── database.py
├── models.py
├── auth.py
├── products.py
├── orders.py
└── payments.py
```

 <br>
Each file has a specific responsibility. <br>

The same principle applies to your URL Shortener. <br>

---

# Why Separate Files?

Imagine your application has these responsibilities: <br>

```text
Responsibility           Suitable file
Start FastAPI             main.py
Database connection       db.py
Request validation        models.py
URL API routes          routes/urls.py
Authentication           auth.py
Configuration           config.py
```

**Main benefit: Separation of concerns** <br>

Each part of the application should focus on a particular responsibility. <br>

For example: <br>

 #db.py <br>

 ```text
def get_connection():
    ...
```

 <br>
The database connection code should not need to know how the URL redirect endpoint works. <br>

Similarly: <br>

#routes/urls.py <br>

```text
@app.post("/urls")
def create_short_url():
    ...
```

 <br>
The route should use the database connection without duplicating all database configuration.  <br>

---

# Current vs Professional Structure
Your Current Structure <br>

Your project currently resembles: <br>

```text
Python_URL_Shortener/
│
├── main.py
├── api_main.py
├── db.py
├── models.py
├── database.sql
├── seed.sql
├── requirements.txt
├── .env
├── .gitignore
└── venv/
```

 <br>
This structure is fine for early practice. <br>

However, as you add authentication, testing, and more routes, a dedicated app package will make the project easier to maintain <br>

---

# Structure We Will Create

We will use the following structure: <br>

```text
Python_URL_Shortener/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   │
│   └── routes/
│       ├── __init__.py
│       └── urls.py
│
├── legacy/
│   └── cli_main.py
│
├── database.sql
├── seed.sql
├── requirements.txt
├── .env
├── .gitignore
└── venv/
```

 <br>

**Folder responsibilities** <br>

```text
app/
Main application package.

app/main.py
Creates the FastAPI application and registers routes.

app/db.py
Database connection logic.

app/models.py
Pydantic request models.

app/routes/
API endpoint modules.

legacy/
Your original CLI application, preserved separately.
```

---

# Create the Folders in VS Code

Open your project in VS Code. <br>

From the project root, create these folders: <br>

```text
app
app/routes
legacy
```

 <br>
Create these files: <br>

```text
app/__init__.py
app/main.py
app/db.py
app/models.py
app/routes/__init__.py
app/routes/urls.py
legacy/cli_main.py
```

 <br>
You can create them directly in VS Code's Explorer. <br>

---

# Move Your Existing Files

Do not delete your code. Move it carefully.

Current file      New location
api_main.py        app/main.py
db.py              app/db.py
models.py          app/models.py
Old CLI main.py    legacy/cli_main.py

You can use VS Code drag-and-drop.

Important: Your old CLI application is not being deleted. We are preserving it in the legacy folder.

After moving, your root folder should no longer contain the old main.py, assuming you moved it successfully.

---

# Update Imports

Moving files into a package changes how Python imports them. <br>

Previous app_main.py imports <br>

Your previous file used: <br>

```text
from db import get_connection
from models import URLCreate
```

<br>
After moving the files into the app package, use: <br>

```text
from app.db import get_connection
from app.models import URLCreate
```

However, because we will move the routes into a separate module, we will organize the imports further. <br>

---

# Update app/db.py

Move your existing database connection code into: <br>

app/db.py <br>

Use: <br>

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
What does this file do? <br>

It provides a reusable function: <br>

connection = get_connection() <br>

Any route that needs PostgreSQL can import this function. <br>

---

# Update app/models.py

Move your existing Pydantic model into: <br>

app/models.py <br>

```text
from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl
```

 <br>
This file is responsible for request validation. <br>

For example: <br>

```text
{
  "original_url": "https://github.com"
}
```

 <br>
FastAPI uses URLCreate to validate the incoming request. <br>

---

# Create app/routes/urls.py

Now we separate the URL-related endpoints from the application startup file. <br>

Create: <br>

app/routes/urls.py <br>

Add the following code: <br>

```text
import random
import string

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from app.db import get_connection
from app.models import URLCreate


router = APIRouter()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    code = ""

    for _ in range(length):
        code += random.choice(characters)

    return code


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


@router.post("/urls", status_code=status.HTTP_201_CREATED)
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


@router.get("/{short_code}")
def redirect_to_original_url(
    short_code: str,
    request: Request
):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT id, original_url
            FROM urls
            WHERE short_code = %s;
            """,
            (short_code,)
        )

        result = cursor.fetchone()

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Short URL not found"
            )

        url_id = result[0]
        original_url = result[1]

        visitor_ip = None

        if request.client is not None:
            visitor_ip = request.client.host

        cursor.execute(
            """
            INSERT INTO clicks (
                url_id,
                ip_address
            )
            VALUES (%s, %s);
            """,
            (url_id, visitor_ip)
        )

        connection.commit()

        return RedirectResponse(
            url=original_url,
            status_code=status.HTTP_307_TEMPORARY_REDIRECT
        )

    except HTTPException:
        connection.rollback()
        raise

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()
```

 <br>
What changed? <br>

Previously, you used: <br>

@app.post("/urls") <br>

Now you use: <br>

@router.post("/urls") <br>

Why? <br>

Because this file uses an APIRouter, which allows us to group related endpoints and register them in the main application. <br>

---

# Create app/main.py

This file will be the entry point for your FastAPI application. <br>

Create: <br>

app/main.py <br>

Add: <br>

```text

from fastapi import FastAPI

from app.routes.urls import router as urls_router


app = FastAPI(
    title="URL Shortener API",
    description="A practice URL shortening API using FastAPI and PostgreSQL",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "URL Shortener API is running"
    }


app.include_router(urls_router)
```

 <br>
Understand include_router() <br>
app.include_router(urls_router)
 <br>
This connects the routes from urls.py to the main FastAPI application. <br> <br>

Think of it like: <br>

```text
app/main.py
    |
    └── Includes routes from urls.py
            |
            ├── POST /urls
            └── GET /{short_code}
```


This allows you to add more route files later: <br> <br>

```text
routes/
├── urls.py
├── users.py
├── auth.py
└── analytics.py
```

---

---

# Move the CLI Application

Move your old CLI main.py into: <br>

legacy/cli_main.py <br>

Because your CLI uses imports such as: <br>

from dotenv import load_dotenv <br>

and: <br>
 
import psycopg2 <br>

it may still work from the project root if you run: <br>

python -m legacy.cli_main <br>

However, your CLI is now legacy practice code, while FastAPI is the main application. <br>

You do not need to run the CLI today. Preserve it for reference. <br>

---

# Run the New Structure

Make sure your PowerShell is opened in the project root: <br>

cd C:\Users\sunaina\Desktop\Python_URL_Shortener\Python_URL_Shortener
 <br>
Activate the virtual environment: <br>

.\venv\Scripts\Activate.ps1 <br>

Start FastAPI using the new module path: <br>

uvicorn app.main:app --reload <br> <br>


Understand the command <br>

```text
app.main:app
│   │    │
│   │    └── FastAPI object named app
│   └────── main.py
└────────── app package
```

 <br>
Previously: <br>

uvicorn api_main:app --reload <br>

Now: <br>

uvicorn app.main:app --reload
 <br>

 ---

 # Test Your Application

Open: <br>

http://localhost:8000/

---
