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






















