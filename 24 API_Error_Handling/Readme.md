# What Is Error Handling?

An error occurs when an application cannot complete a requested operation. <br>

For example: <br>

- User requests a URL that does not exist.
- User sends invalid data.
- Database connection fails.
- User does not have permission.
- A required resource is missing.

 <br>
Error handling means detecting these situations and returning a meaningful response instead of allowing the application to fail unexpectedly. <br> <br>

❌ Poor error handling <br>

```text
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = find_user(user_id)

    return user["name"]
```

 <br>
If the user does not exist, this could cause an unexpected error such as: <br>

```text
TypeError: 'NoneType' object is not subscriptable
```

 <br>
The client receives an unclear error. <br> <br>

✅ Proper error handling <br>

```text
from fastapi import HTTPException


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = find_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
```

 <br>
Now the API returns a meaningful response: <br>

```text
{
  "detail": "User not found"
}
```

 <br>
---

# HTTP Status Codes

HTTP status codes communicate the result of a request. <br>

```text
Status    Meaning                      Example
200         OK                     Data retrieves successfully
201        Created                 New URL Created
400        Bad Request             Invalid request format or business input
401       Unauthorized             Authentication is required or invalid
403        Forbidden               User is not allowed to access a resource
404       Not Found                Short code does not exist
409       Conflict                 Duplicate resource
422       Validation Error         Invalid Pydantic input
500       Internal Server Error     Unexpected server-side failure          
```

<br>

Important distinction <br>

- 401: The client is not properly authenticated.

- 403: The client is authenticated or identified, but does not have permission.

- 404: The requested resource cannot be found.

 <br>
The exact choice depends on the API's behavior and security requirements. <br>

---

# Learn HTTPException

FastAPI provides HTTPException for returning HTTP errors. <br>

```text
from fastapi import HTTPException
```

 <br>
Basic example: <br>

```text
raise HTTPException(
    status_code=404,
    detail="Resource not found"
)
```

 <br>
**General syntax**  <br>

```text
raise HTTPException(
    status_code=STATUS_CODE,
    detail="Meaningful error message"
)
```

 <br>
Why use raise? <br>

raise immediately stops the current function and sends the exception to FastAPI. <br> <br>

Example: <br>

```text
if user is None:
    raise HTTPException(status_code=404, detail="User not found")

print("This line will not run if user is missing")
```


---

# Practice Error Handling Separately

main.py <br>

```text
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/products/{product_id}")
def get_product(product_id: int):
  
  if product_id <= 0:
    raise HTTPException(
      status_code=400,
      detail="Product ID must be greater than zero"
    )

  if product_id != 1:
    raise HTTPException(
      status_code=404,
      detail="Product not found"
    )

  return {
    "id": 1,
    "name": "Laptop",
    "price": 50000
  }
```

<br>
Run: <br>

```text
uvicorn main:app --reload
```

 <br>

## Test 
**Valid product** <br>
Open: <br>
http://localhost:8000/products/1 <br>
Response: <br>
id, name, price will be shown. <br> <br> <br>

**Missing product** <br>
Open: <br>
http://localhost:8000/products/99 <br>
Response: <br>

```text
{
  "detail": "Product not found"
}
Status:
404 Not Found
```

 <br>

**Invalid product ID** <br>
Open: <br>
http://localhost:8000/products/0 <br>
Response: <br>

```text
{
  "detail": "Product ID must be greater than zero"
}
```

 <br>
Status: <br>

---

# FastAPI Validation Errors

You already use this model in app/models.py: <br>

```text
from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    original_url: HttpUrl
```

<br>
FastAPI automatically validates incoming request data. <br>

For example: <br>

```text
{
  "original_url": "not-a-valid-url"
}
```

 <br>
FastAPI returns a validation error, commonly with status code:
 <br>
422 Unprocessable Entity <br>

You do not need to manually write an if condition for every validation rule.
 <br>
 <br>

Why is automatic validation useful? <br>

The same concept works for: <br>

- Product prices

- User email addresses

- Password fields

- Order quantities

- Date formats

- API request bodies
 <br>

Pydantic validation and business validation are different: <br>

Type                       Example
Input validation        URL must be a valid URL
Business validation     User cannot order more items than available stock
Authorization           User can modify only their own URL

---

# Error Handling in URL Shortener

Your current application has several places where errors can happen. <br>

```text
Operation                          Possible error
Create short URL               Database failure
Find short URL                Short code does not exist
Record click                  Database insertion failure
Validate request              Invalid URL
Connect to PostgreSQL         Database unavailable   
```

<br>
We will improve the API so that : <br>
- Expected client errors return clear HTTP responses.
- Database transactions are rolled back on failure.
- Database connections are closed.
- Unexpected errors are not exposed with sensitive internal details.

 <br>

---

# Add a Custom Error Response Model

We can use a Pydantic model to standardize our error responses. <br>

Open: <br>
app/models.py <br> <br>

Update it to: <br>

```text
from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl


class ErrorResponse(BaseModel):
    detail: str
```

 <br>
 Why use an error model? <br>

It documents the expected error format and helps keep API responses consistent. <br>

For now, FastAPI's built-in validation errors may still use a different structure. We will handle those more comprehensively with exception handlers later.
 <br>

 ---

 # Update app/routes/urls.py

Your existing redirect endpoint already handles a missing short code: <bt>

```text
if result is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Short URL not found"
    )
```

<br>
That is correct.
<br>
Now we will improve the endpoint declarations by adding response documentation. <br> <br> <br>


## Update imports

At the top of app/routes/urls.py, use: <br>

```text
import random
import string

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from app.db import get_connection
from app.models import ErrorResponse, URLCreate
```

## Update the POST endpoint

Find: <br>

```text
@router.post("/urls", status_code=status.HTTP_201_CREATED)
```

<br>
Replace it with: <br>

```text
@router.post(
    "/urls",
    status_code=status.HTTP_201_CREATED,
    responses={
        500: {
            "description": "Internal server error"
        }
    }
)

```

<br>

The endpoint's main logic can remain unchanged for now. <br>
<br>
Important <br>

The responses parameter documents possible responses in Swagger. It does not automatically catch errors or change how exceptions are handled. <br>

---

# Improve Database Error Handling

Your current code uses: <br>

```text
except Exception:
    connection.rollback()
    raise
```

 <br>
This is useful because it: <br>

- Rolls back the transaction.

- Re-raises the original exception.

- Allows FastAPI to handle the unexpected error.


<br><br>
However, exposing raw database errors to users is not appropriate in production.

 <br> 
For example, an error might reveal: <br>

- Database table names

- SQL statements

- Internal infrastructure details

- Connection information

<br>
Instead, we can log the internal error and return a generic message.
 <br>


 ## First, understand the pattern

```text
try:
    # Perform database operation

except Exception:
    connection.rollback()

    # Log the internal error

    raise HTTPException(
        status_code=500,
        detail="An internal server error occurred"
    )

finally:
    cursor.close()
    connection.close()
```

<br>
Important production consideration <br>

Do not blindly replace every exception with a 500 response. <br>

Some exceptions, such as an intentional HTTPException(404), should be preserved. Also, logging should capture useful diagnostic information without exposing secrets. <br> <br>

---

# Add Logging

Python provides a built-in logging module. <br>

Create a logger at the top of: <br>

app/routes/urls.py <br>

Add: <br>

```text
import logging


logger = logging.getLogger(__name__)
```

 <br>
Your imports should now include: <br>

```text
import logging
import random
import string
```

 <br> <br>
Why use logging? <br>

Logging helps developers troubleshoot problems without showing internal details to API users. <br> <br>

Example: <br>

```text
logger.exception("Failed to create short URL")

logger.exception() should be called inside an exception handler. It records the error and traceback.
```

 <br>

## Update the Create URL Endpoint

Replace your existing create_short_url() function with this version: <br>

```text
@router.post(
    "/urls",
    status_code=status.HTTP_201_CREATED
)
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

        logger.exception("Failed to create short URL")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create short URL"
        )

    finally:
        cursor.close()
        connection.close()
```

 <br> <br>
What changed? <br>

Previously: <br>

```text
except Exception:
    connection.rollback()
    raise
```

 <br>
Now: <br>

```text
except Exception:
    connection.rollback()
    logger.exception("Failed to create short URL")

    raise HTTPException(
        status_code=500,
        detail="Unable to create short URL"
    )
```
 <br>

The user receives a generic message, while the internal logs retain diagnostic information. <br>

A limitation in this version <br>

get_connection() is called before the try block. Therefore, if the connection itself fails, this handler will not catch that exception. <br>
  
We will improve centralized error handling later. For now, this teaches the basic pattern. <br>

---

# Improve the Redirect Endpoint

Your redirect endpoint already handles HTTPException separately. Keep that behavior. <br>

Replace the endpoint with: <br>

```text
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

        logger.exception("Failed to redirect short URL")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to process short URL"
        )

    finally:
        cursor.close()
        connection.close()
 ```

<br>

Why is HTTPException handled separately? <br>

Suppose the short code does not exist: <br>

raise HTTPException(status_code=404) <br>

We want to preserve the 404 response.
 <br>
If we caught all exceptions and returned 500, a missing URL would incorrectly appear as a server failure. <br>

This is why exception handling order matters. <br>

---

# Centralized Exception Handling

So far, we have handled errors inside individual endpoints. <br>

But imagine you have 30 endpoints. <br>

Would you want to repeat the same error-handling code 30 times? <br>

Usually, no. <br> <br>

FastAPI supports exception handlers, which allow you to define common behavior for specific exception types. <br>

Example: Global unexpected error handler <br> <br>

Open: <br>

app/main.py <br>

Update it to: <br>

```text
import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routes.urls import router as urls_router


logger = logging.getLogger(__name__)


app = FastAPI(
    title="URL Shortener API",
    description="A practice URL shortening API using FastAPI and PostgreSQL",
    version="1.0.0"
)


@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception
):
    logger.exception(
        "Unhandled exception on %s %s",
        request.method,
        request.url.path
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "An internal server error occurred"
        }
    )


@app.get("/")
def home():
    return {
        "message": "URL Shortener API is running"
    }


app.include_router(urls_router)
```

What does this handler do? <br>

If an unexpected exception reaches the application, this handler: <br>

- Logs the internal exception. 

- Returns status code 500.

- Provides a generic error response.

 <br> <br>
Important <br>

This is a basic educational handler. FastAPI's normal handling of HTTPException and validation errors should be preserved. In production, you should also consider environment-specific logging, monitoring, and avoiding overly broad exception handling that hides useful error information.
 <br>

---

# What Happens During an Error?

Consider this request: <br>

```text
GET /abc123
```

 <br>
The database is temporarily unavailable. <br> <br>

The flow is: <br>

```text
1. Request arrives
2. API tries to connect/query PostgreSQL
3. Database operation fails
4. Exception is raised
5. Transaction is rolled back where applicable
6. Error is logged
7. Client receives a safe error response
```

 <br>
The user should not receive a response such as: <br>

```text
psycopg2.OperationalError:
could not connect to server...
```

 <br>
Instead: <br>

```text
{
  "detail": "An internal server error occurred"
}
```

 <br>
The detailed error should be available through appropriate internal logs. <br>

---

# Test Your Error Handling

## Invalid URL input

Open: <br>

http://localhost:8000/docs <br>

Try: <br>

```text
{
  "original_url": "hello"
}
```

<br>
Expected: Validation error, generally 422.


## Missing short code

Open: <br>

http://localhost:8000/notfound123 <br>

Expected: <br>

```text
{
  "detail": "Short URL not found"
}
```

Status: <br>

404 <br>

## Valid short code

Create a URL: <br>

```text
{
  "original_url": "https://github.com"
}
```

 <br>
Open the generated short URL. <br>
 <br>
Expected: <br>

Browser redirects.
 <br>
Click is recorded.
 <br>
No unexpected error occurs.
 <br>



## Missing configuration

Temporarily remove DB_NAME from .env and restart the application: <br>

DB_NAME= <br>

The configuration validation from Day 23 should raise a clear startup error.
 <br>
Restore the value afterward.
 <br>
 
---

# Production Error Handling Principles

These principles apply to almost every backend application. <br>

1. Return meaningful status codes
 <br>
Do not return 200 OK for every situation. <br>

For example: <br>

```text
Missing resource → 404
Invalid input → 422 or 400
Unauthenticated → 401
Unexpected server error → 500
```

 <br>
2. Do not expose sensitive details
 <br>
Avoid returning:
 <br>

 ```text
Database passwords
Internal SQL statements
Stack traces
Secret keys
Infrastructure details
```

 <br>
3. Log errors internally
 <br>
Logs help with: <br>

```text
Debugging
Monitoring
Incident investigation
Identifying recurring failures
```

 <br>
 
4. Roll back failed transactions
 <br>
If a database operation fails, roll back the transaction when appropriate.

5. Always clean up resources
 <br>
Use finally to close database cursors and connections.

6. Validate inputs
 <br>
Use Pydantic validation and business rules.

7. Handle expected errors separately
 <br>
A missing resource is not the same as an unexpected database failure.

  <br>

 ---

Professional API error handling means: <br>

Detect errors → Return the correct status code → Log useful internal details → Protect sensitive information → Clean up resources.  

<br>


