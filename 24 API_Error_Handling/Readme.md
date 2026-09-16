# What Is Error Handling?

An error occurs when an application cannot complete a requested operation. <br>

For example: <br>

- User requests a URL that does not exist.
- User sends invalid data.
- Database connection fails.
- User does not have permission.
- A required resource is missing.

 <br>
Error handling means detecting these situations and returning a meaningful response instead of allowing the application to fail unexpectedly. <br>

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























