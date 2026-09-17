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

The token contains:

{
  "sub": "1",
  "exp": "expiration time"
}

The token is signed using your secret key.











