# What Is Authentication?

Authentication means verifying who the user is. <br>

For example: <br>

A user enters their email and password. The application checks whether the credentials are correct. <br>

If they are correct, the user is authenticated. <br> <br>

## Authentication vs Authorization

```text
Concept                    Meaning                            Example
Authentication       Who are you?                    Login with email and password
Authorization          What can you access?     Only logged-in users can create URLS
```

<br>

## Real-world analogy

Think about your college portal: <br>

Authentication: You log in using your student credentials. <br>

Authorization: After logging in, you can access your marks, but you cannot modify another student's marks. <br>

---

# Authentication Flow

A common API authentication flow looks like this: <br>

**Authentication Flow** <br>

```text
User registers
The password is securely hashed and stored in the database.

User logs in
The server verifies the email and password.

Server creates a JWT token
The token represents the authenticated user.

Client sends the token
The client includes the token in the Authorization header.

Server validates the token
If valid, the protected endpoint is executed.
```

<br>
<br>
Example request header:  <br>

Authorization: Bearer eyJhbGciOiJIUzI1NiIs... <br>

The word Bearer indicates that the client is presenting a bearer token. <br>

---

# Why Should We Never Store Plain Passwords?

Never store passwords like this: <br>

```text
email: sunaina@example.com
password: sunaina123
```

 <br>
If your database is compromised, the passwords are immediately exposed. <br> <br>

Instead, store a password hash: <br>

```text
email: sunaina@example.com
password_hash: $2b$12$...
```

 <br>
A password hash is produced using a password-hashing algorithm such as bcrypt. <br>

**Hashing vs Encryption** <br>

```text
Hashing                                        Encryption
One-way operation                          Reversible with a key
Used for passwords                         Used for protecting data
Original password is not recovered         Original data can be decrypted
```

<br>

---

# What Is JWT?

JWT stands for JSON Web Token. <br>

It is commonly used to represent claims about an authenticated user. <br>

A JWT generally consists of three parts: <br>

```text
Header.Payload.Signature
```

 <br>

```text
Part          Purpose
Header      Algorithm and token type
Payload     Claims such as user ID and expiry
Signature   Helps verify token integrity
```

<br>

Example payload: <br>

```text
{
  "sub": "1",
  "exp": 1790000000
}
```

<br>
sub: Subject, commonly the user ID.
<br>
exp: Token expiration time.

<br><br>

Important security points <br>

- Do not store passwords inside JWT payloads.

- JWT payloads are encoded, not automatically encrypted.

- Use an appropriate expiration time.

- Keep the signing secret private.

- Always use HTTPS in production.

<br>

---

# Install Authentication Dependencies

Activate your virtual environment: <br>

cd C:\Users\sunaina\Desktop\Python_URL_Shortener\Python_URL_Shortener <br>

.\venv\Scripts\Activate.ps1 <br> <br> <br>

Install the packages: <br>

pip install "python-jose[cryptography]" "passlib[bcrypt]" <br> <br> <br>

Update requirements.txt: <br>

pip freeze > requirements.txt <br> <br>

Note: For a modern production project, you should also evaluate actively maintained password-hashing libraries and pin compatible versions. This lesson uses the traditional FastAPI learning approach. <br>

---

# Create a JWT Secret Key

Your JWT signing key must be private. <br> <br>

Generate a secure random key using Python: <br>

python -c "import secrets; print(secrets.token_urlsafe(32))" <br> <br>

Example output: <br>

generated-secret-key <br> <br>

Do not copy the example above as your actual secret. <br>

Add the generated value to .env: <br>

```text
JWT_SECRET_KEY=your_generated_secret_key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
```

 <br> <br>
 
Your .env should now contain: <br>

```text
DB_HOST=localhost
DB_NAME=url_shortener
DB_USER=postgres
DB_PASSWORD=your_database_password
DB_PORT=5432

JWT_SECRET_KEY=your_generated_secret_key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
```


Never commit .env to GitHub. <br>

---

# Update app/config.py

Add the JWT configuration to your existing file. <br>

```text
import os

from dotenv import load_dotenv


load_dotenv()


def get_required_environment_variable(name):
    value = os.getenv(name)

    if value is None or value.strip() == "":
        raise RuntimeError(
            f"Required environment variable '{name}' is missing"
        )

    return value


DB_HOST = get_required_environment_variable("DB_HOST")
DB_NAME = get_required_environment_variable("DB_NAME")
DB_USER = get_required_environment_variable("DB_USER")
DB_PASSWORD = get_required_environment_variable("DB_PASSWORD")
DB_PORT = int(
    get_required_environment_variable("DB_PORT")
)

JWT_SECRET_KEY = get_required_environment_variable(
    "JWT_SECRET_KEY"
)

JWT_ALGORITHM = get_required_environment_variable(
    "JWT_ALGORITHM"
)

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    get_required_environment_variable(
        "JWT_ACCESS_TOKEN_EXPIRE_MINUTES"
    )
)

```

<br>

Why use environment variables? <br>

Instead of hardcoding: <br>

JWT_SECRET_KEY = "my-secret" <br>

You load it from .env. <br> <br> <br>

This allows different values for: <br>

Local development <br>

Testing <br>

Production <br>

---

# Add Password and JWT Security Module

Create a new file: <br>

app/security.py <br>

Add the following code: <br>

```text
from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import (
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_ALGORITHM,
    JWT_SECRET_KEY
)


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Convert a plain password into a secure hash.
    """

    return password_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Check whether a plain password matches its hash.
    """

    return password_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(user_id: int) -> str:
    """
    Create a JWT access token for a user.
    """

    expire_time = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": str(user_id),
        "exp": expire_time
    }

    token = jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )

    return token


def decode_access_token(token: str) -> int:
    """
    Decode and validate a JWT token.

    Returns:
        int: Authenticated user ID.
    """

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        subject = payload.get("sub")

        if subject is None:
            raise ValueError("Token subject is missing")

        return int(subject)

    except (JWTError, ValueError, TypeError) as error:
        raise ValueError(
            "Invalid or expired access token"
        ) from error

```

<br>

 ---

 # Understand the Security Functions
 
**hash_password()** <br>
hashed_password = hash_password("sunaina123") <br>

It returns a password hash. <br>

The same password can produce different hashes because a random salt is used. <br> <br>

**verify_password()** <br>

```text
is_valid = verify_password(
    "sunaina123",
    stored_password_hash
)
```

<br>
Returns: <br>
True or False <br>

<br>

**create_access_token()** <br>

token = create_access_token(user_id=1) <br>

The token contains: <br>

```text
{
  "sub": "1",
  "exp": "expiration time"
}
```

<br>
The token is signed using your secret key. <br> <br>

**decode_access_token()** <br>

```text
user_id = decode_access_token(token)
```

<br>
This function: <br>

Verifies the signature. <br>

Checks token validity. <br>

Checks the expiration claim. <br>

Extracts the user ID. <br>

---

# Important Database Limitation

Your current users table contains: <br>

```text
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

 <br>
It does not contain a password hash. <br>

For authentication, add a new column. <br> <br>

**Option A: Add the column using SQL** <br>

Connect to PostgreSQL: <br>

psql -U postgres <br>

Select your database: <br>

\c url_shortener <br>

Run: <br>

ALTER TABLE users <br>
ADD COLUMN password_hash TEXT; <br>

Check the table: <br>

\d users <br> <br> <br>

Why is the column nullable? <br>

Your existing seed users do not have passwords yet. Making it nullable allows the migration to succeed without immediately breaking those existing rows. <br>

For a production application, you should establish a proper migration and password-setting process. <br>

---

# Create a Registration Endpoint

For this lesson, we will create a simple registration endpoint. <br>

Update app/models.py: <br>

```text
from pydantic import BaseModel, EmailStr, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class ErrorResponse(BaseModel):
    detail: str
```

 <br>
Install email validation support: <br>

pip install email-validator <br> <br>

Update requirements: <br>

pip freeze > requirements.txt <br> <br>
Password validation <br>

For now, we will add basic validation directly in the route. Later, you can move it into a dedicated Pydantic validator. <br>

---

# Create Authentication Routes

Create: <br>

app/routes/auth.py <br>

Add: <br>

```text
import logging

from fastapi import APIRouter, HTTPException, status

from app.db import get_connection
from app.models import UserCreate
from app.security import hash_password


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register_user(user: UserCreate):
    """
    Register a new user.
    """

    if len(user.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must contain at least 8 characters"
        )

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        password_hash = hash_password(user.password)

        cursor.execute(
            """
            INSERT INTO users (
                name,
                email,
                password_hash
            )
            VALUES (%s, %s, %s)
            RETURNING id, name, email
            """,
            (
                user.name,
                user.email,
                password_hash
            )
        )

        created_user = cursor.fetchone()

        connection.commit()

        return {
            "id": created_user[0],
            "name": created_user[1],
            "email": created_user[2]
        }

    except Exception as error:
        if connection:
            connection.rollback()

        logger.exception(
            "User registration failed"
        )

        if "duplicate key" in str(error).lower():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email is already registered"
            ) from error

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to register user"
        ) from error

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
```

<br>

---

# Add the Login Model

Add this model to app/models.py: <br>

```text
class UserLogin(BaseModel):
    username: EmailStr
    password: str
```

<br>
FastAPI's OAuth2 password flow commonly uses the field name username, even when your application actually logs users in using an email address. <br>

---

# Add Login Endpoint

Update app/routes/auth.py. <br>

Add these imports: <br>

```text
from fastapi.security import OAuth2PasswordRequestForm

from app.models import UserCreate, UserLogin
from app.security import (
    create_access_token,
    hash_password,
    verify_password
)
```

 <br>
You can remove UserLogin if you use OAuth2PasswordRequestForm; the form is used below. <br> <br>

**Add the endpoint:** <br>

```text
@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    Authenticate a user and return a JWT token.
    """

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, password_hash
            FROM users
            WHERE email = %s
            """,
            (form_data.username,)
        )

        user = cursor.fetchone()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
                headers={
                    "WWW-Authenticate": "Bearer"
                }
            )

        user_id, stored_password_hash = user

        if stored_password_hash is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User password is not configured",
                headers={
                    "WWW-Authenticate": "Bearer"
                }
            )

        if not verify_password(
            form_data.password,
            stored_password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
                headers={
                    "WWW-Authenticate": "Bearer"
                }
            )

        access_token = create_access_token(user_id)

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise

    except Exception as error:
        logger.exception(
            "Login failed"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to process login"
        ) from error

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
```

 <br>
**Important: Add the missing import** <br>

At the top of auth.py, include: <br>

```text
from fastapi import APIRouter, Depends, HTTPException, status
```

 <br>
The complete imports should include: <br>

```text
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from fastapi.security import OAuth2PasswordRequestForm
```

<br>

---

# Register the Authentication Router

Update app/main.py. <br>

Add: <br>

```text
from app.routes.auth import router as auth_router

Then include the router:

app.include_router(auth_router)

Your relevant main.py structure:

from fastapi import FastAPI

from app.routes.auth import router as auth_router
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


app.include_router(auth_router)
app.include_router(urls_router)
```

 <br>
Keep your existing exception handler if you already have one. Do not accidentally remove it while adding the authentication router.
 <br>

 ---

 # Create an Authentication Dependency

Now we need a reusable function that checks whether a request contains a valid JWT. <br>

Create: <br>

app/dependencies.py <br>

Add: <br>

```text
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.security import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user_id(
    token: str = Depends(oauth2_scheme)
) -> int:
    """
    Extract and validate the current user's ID.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    try:
        user_id = decode_access_token(token)

        return user_id

    except ValueError as error:
        raise credentials_exception from error

```

 <br> <br>
What does OAuth2PasswordBearer do? <br>

It reads the token from: <br>

Authorization: Bearer <token> <br>

It does not itself verify the token. Your decode_access_token() function performs the validation. <br>

---

# Protect URL Creation

Open: <br>

app/routes/urls.py <br>

Find your URL creation endpoint. <br>

Add this import: <br>

```text
from fastapi import Depends

Also import the dependency:

from app.dependencies import get_current_user_id

Change your endpoint from:

@router.post("/urls", status_code=status.HTTP_201_CREATED)
def create_short_url(url_data: URLCreate):

To:

@router.post(
    "/urls",
    status_code=status.HTTP_201_CREATED
)
def create_short_url(
    url_data: URLCreate,
    current_user_id: int = Depends(
        get_current_user_id
    )
):

Then replace the hardcoded user ID:

user_id = 1

with:

user_id = current_user_id

Your SQL insert should use:

cursor.execute(
    """
    INSERT INTO urls (
        short_code,
        original_url,
        user_id
    )
    VALUES (%s, %s, %s)
    RETURNING short_code
    """,
    (
        short_code,
        str(url_data.original_url),
        current_user_id
    )
)
```

 <br> <br>
Why is this important? <br>

Previously: <br>

user_id = 1 <br>

Every URL was assigned to the same user. <br> <br>

Now: <br>

current_user_id <br>

The user ID is taken from the validated token. <br>

This is the foundation for user-specific resources. <br>

---

# Updated Project Structure

Your project should now look like this: <br>

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

---

# Test the Authentication Flow

Start the application: <br>

uvicorn app.main:app --reload <br>

Open: <br>

http://localhost:8000/docs  <br> <br>

**Test 1: Register** <br>

Open: <br>

```text
POST /auth/register
```

 <br>
Request body: <br>

```text
{
  "name": "Test User",
  "email": "test@example.com",
  "password": "TestPassword123"
}
```

 <br>
Expected response: <br>

```text
{
  "id": 4,
  "name": "Test User",
  "email": "test@example.com"
}
```

 <br>
The password should not be included in the response. <br>

<br>

**Test 2: Login**  <br>

Open: <br>

```text
POST /auth/login
```

 <br>
Click Try it out. <br>

Use form values: <br>

```text
username: test@example.com
password: TestPassword123
```

 <br>
Expected response: <br>

```text
{
  "access_token":
```

---
  








