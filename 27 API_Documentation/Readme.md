# What Is API Documentation?

API documentation is a guide that explains how to use your API. <br>

For example, another developer wants to create a short URL using your application. <br> <br>

Without documentation, they may ask: <br>

What URL should I call? What method should I use? What data should I send? Do I need authentication? <br> <br>

With documentation: <br>

```text
POST /urls

Request:
{
    "original_url": "https://github.com"
}

Authentication:
Bearer token required

Response:
{
    "short_code": "aB12xY"
}
```

 <br>
The developer can understand and use your API without reading your entire source code <br>

---

# What Is OpenAPI?

OpenAPI is a standard format for describing APIs. <br>

FastAPI uses OpenAPI to generate documentation automatically. <br>

Your FastAPI application provides: <br>

```text
URL                    Purpose
/docs              Swagger UI
/redoc             ReDoc documentation
/openapi.json      OpenAI schema in JSON
```

<br>

```text
Open:
http://localhost:8000/docs
You will se interactive Swagger UI
```

```text
Open:
http://localhost:8000/redoc
You will see ReDoc
```

```text
Open 
http://localhost:8000/openapi.json
You will se the generated OpenAPI schema.
```

<br>

---

# Start Your Application

```text
Activate your virtual environment:

cd C:\Users\sunaina\Desktop\Python_URL_Shortener\Python_URL_Shortener

.\venv\Scripts\Activate.ps1
```

<br>

```text
Start FastAPI:

uvicorn app.main:app --reload
```

<br>

```text
Now visit:

http://localhost:8000/docs

Your current endpoints should appear automatically.
```

<br>

---

# Configure Application Metadata

Your current app/main.py probably contains: <br>

```text
app = FastAPI(
    title="URL Shortener API",
    description="A practice URL shortening API using FastAPI and PostgreSQL",
    version="1.0.0"
)
```

 <br>
We can improve the documentation by adding: <br>

```text
Contact information
License information
API server information
Tags
Markdown descriptions
```

 <br> <br>
Updated app/main.py <br>

Keep your existing exception handlers and routes. Update the FastAPI() configuration: <br>

```text
from fastapi import FastAPI


app = FastAPI(
    title="URL Shortener API",
    summary="Create, manage, and redirect shortened URLs",
    description="""
# URL Shortener API

This API allows users to:

- Register an account
- Authenticate using JWT tokens
- Create shortened URLs
- Redirect to original URLs
- Record URL clicks

## Authentication

Protected endpoints require a valid JWT access token.

Use the `Authorize` button in Swagger UI to provide your token.
""",
    version="1.0.0",
    contact={
        "name": "Sunaina Lodha",
    },
    license_info={
        "name": "MIT",
    }
)
```

 <br>

 Explanation: <br>

```text
Property             Purpose
title            API name
summary         Short API description
description     Detailed Markdown description
version         API version
contact         Maintainer information
license_info    License details
```

<br>
Only include contact and license information that you actually want to publish.
<br>

---

# What Are API Tags?

Tags group related endpoints in Swagger UI. <br>

For example: <br>

```text
Authentication
    POST /auth/register
    POST /auth/login

URLs
    POST /urls
    GET /{short_code}
```

 <br> <br>
You already added tags to the authentication router: <br>

```text
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
```

 <br>
Add a tag to your URL router in app/routes/urls.py: <br>

```text
router = APIRouter(
    tags=["URLs"]
)
```

 <br>
If your URL router already has an APIRouter() declaration, replace it rather than creating a second router. <br>

---

# Add Endpoint Summaries and Descriptions

Your endpoint may currently look like this: <br>

```text
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
```

 <br>
Improve it: <br>

```text
@router.post(
    "/urls",
    status_code=status.HTTP_201_CREATED,
    summary="Create a shortened URL",
    description="""
    Creates a short URL for the authenticated user.

    The original URL is stored in PostgreSQL,
    and a unique short code is generated.
    """,
    response_description="The newly created shortened URL"
)
def create_short_url(
    url_data: URLCreate,
    current_user_id: int = Depends(
        get_current_user_id
    )
):
```

 <br> <br>
Why is this useful? <br>

Swagger UI will display meaningful information instead of only showing: <br>

```text
POST /urls
```

 <br>
Developers will understand what the endpoint does before calling it. <br>

---

# Document Request Models

Your current model: <br>

```text
class URLCreate(BaseModel):
    original_url: HttpUrl
```

 <br>
can be improved with a field description. <br>

Update app/models.py: <br>

```text
from pydantic import BaseModel, EmailStr, Field, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl = Field(
        ...,
        description="The original URL that should be shortened",
        examples=["https://github.com"]
    )


class UserCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Full name of the user",
        examples=["Sunaina Lodha"]
    )

    email: EmailStr = Field(
        ...,
        description="A valid email address",
        examples=["user@example.com"]
    )

    password: str = Field(
        ...,
        min_length=8,
        description="Account password with at least 8 characters"
    )


class ErrorResponse(BaseModel):
    detail: str
```

 <br>

**Important: ...** <br> <br>

In: <br>

Field(...) <br>

the ... means the field is required. <br>
 <br>
Why use Field()? <br> 

It provides: <br>

```text
Validation constraints
Documentation descriptions
Example values
Better generated OpenAPI schemas
```

 <br>
 
---

# Document Response Models

Currently, your endpoint may return a plain dictionary: <br>

```text
return {
    "short_code": short_code,
    "original_url": str(url_data.original_url)
}
```

 <br>
You can create a response model. <br> <br>

Add to app/models.py: <br>

```text
class URLCreateResponse(BaseModel):
    short_code: str = Field(
        ...,
        description="Generated short code",
        examples=["aB12xY"]
    )

    original_url: HttpUrl = Field(
        ...,
        description="The original URL"
    )
```

 <br>
Then import it in app/routes/urls.py: <br>

```text
from app.models import (
    URLCreate,
    URLCreateResponse
)
```

 <br> <br>
Update the endpoint decorator: <br>

```text
@router.post(
    "/urls",
    status_code=status.HTTP_201_CREATED,
    response_model=URLCreateResponse,
    summary="Create a shortened URL",
    response_description="Created shortened URL"
)
```

 <br> <br>
Why use response_model? <br>

It helps FastAPI: <br>

```text
Document the response schema.
Validate response data.
Filter out unexpected response fields.
Make the API contract clearer.
```

 <br>

Example documented response <br>

```text
{
  "short_code": "aB12xY",
  "original_url": "https://github.com"
}
```

 <br>
 
---

# Create a Login Response Model

Add to app/models.py: <br>

```text
class TokenResponse(BaseModel):
    access_token: str = Field(
        ...,
        description="JWT access token"
    )

    token_type: str = Field(
        ...,
        description="Authentication token type",
        examples=["bearer"]
    )
```

 <br>
In app/routes/auth.py, import it: <br>

```text
from app.models import (
    TokenResponse,
    UserCreate
)
```

 <br> <br>
Update your login endpoint: <br>

```text
@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Authenticate a user",
    description="""
    Verifies user credentials and returns
    a JWT access token.
    """
)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends()
):
```

 <br>
The response will now be documented as: <br>

```text
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

 <br>

---

 # Document Registration Response

Create a response model: <br>

```text
class UserResponse(BaseModel):
    id: int = Field(
        ...,
        description="Unique user ID",
        examples=[1]
    )

    name: str = Field(
        ...,
        description="User's name"
    )

    email: EmailStr = Field(
        ...,
        description="User's email address"
    )
```

<br> <br>
Update the registration endpoint: <br>

```text
@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
    summary="Register a new user",
    response_description="Registered user details"
)
def register_user(user: UserCreate):
```

<br>
Notice that password and password_hash are not included in UserResponse.
<br>
Never return password hashes through your API.
<br>

---

# Document Error Responses

Your API may return errors such as: <br>

```text
{
  "detail": "Invalid email or password"
}
```

 <br>
You can describe possible responses in the route decorator. <br>

Example: <br>

```text
@router.post(
    "/login",
    response_model=TokenResponse,
    responses={
        401: {
            "description": "Invalid email or password"
        },
        500: {
            "description": "Internal server error"
        }
    }
)
```

 <br>
For the registration endpoint: <br>

```text
@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
    responses={
        400: {
            "description": "Invalid registration data"
        },
        409: {
            "description": "Email is already registered"
        },
        500: {
            "description": "Internal server error"
        }
    }
)
```

 <br> <br>
Why document errors? <br>

Consumers should know not only how a successful request looks, but also how failures are represented. <br>

---

# Document the Redirect Endpoint

Your redirect endpoint may look similar to: <br>

```text
@router.get("/{short_code}")
def redirect_to_original_url(short_code: str):
```

 <br>
Improve the documentation: <br>

```text
@router.get(
    "/{short_code}",
    summary="Redirect to the original URL",
    description="""
    Finds the original URL using the short code,
    records a click, and redirects the client.
    """,
    response_description="Temporary redirect to the original URL",
    responses={
        404: {
            "description": "Short code not found"
        },
        307: {
            "description": "Redirect to original URL"
        }
    }
)
def redirect_to_original_url(short_code: str):
```

 <br> <br>
Important <br>

Your redirect endpoint should not require authentication if you want anyone to use shortened links. <br>

Your URL creation endpoint should remain protected. <br>

---

# Add Path Parameter Documentation

You can use Path to describe and validate a path parameter. <br>

In app/routes/urls.py: <br>

```text
from fastapi import Path
```

 <br>
Update the endpoint: <br>

```text
@router.get(
    "/{short_code}",
    summary="Redirect to the original URL"
)
def redirect_to_original_url(
    short_code: str = Path(
        ...,
        min_length=1,
        max_length=20,
        description="Short code assigned to the original URL",
        examples=["abc123"]
    )
):
```

 <br> <br>
This documents the expected short-code format and adds basic length validation. <br>

If your application later uses a stricter short-code format, such as exactly six alphanumeric characters, you can use a regular expression or additional validation. <br>

---

# Add Authentication Documentation

Your dependencies.py contains: <br>

```text
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)
```

 <br>
This allows Swagger UI to understand the OAuth2 password token endpoint. <br> <br>

However, there is an important detail: <br>

OAuth2PasswordBearer defines how the token is extracted. <br>
 
Your login endpoint must return a valid token. <br>

Protected routes must use Depends(get_current_user_id). <br>
 <br>
Example: <br>

```text
@router.post("/urls")
def create_short_url(
    url_data: URLCreate,
    current_user_id: int = Depends(
        get_current_user_id
    )
):
```

 <br>
Swagger UI can then display the Authorize button.
 <br>

---

# Understand OpenAPI JSON





