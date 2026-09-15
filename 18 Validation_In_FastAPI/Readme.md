# What is Validation?

Validation means checking whether incoming data follows the rules that your application expects. <br>
 <br>
Suppose your API creates a user. <br>
You expect: <br>

```text
{
  "name": "Sunaina",
  "email": "sunaina@example.com",
  "age": 21
}
```

 <br>
But a client sends: <br>

```text
{
  "name": "",
  "email": "hello",
  "age": -50
}
```

So our should application should not accept this. <br>
 <br>
So we need rules such as : <br>

```text
name -> required, cannot be empty
email -> must be a valid email
age -> must be positive
```

This is validation. <br>

# Why Validation Is Necessary

Imagine your application has: <br>

```text
Frontend
   ↓
FastAPI
   ↓
Business Logic
   ↓
PostgreSQL
```

 <br>
If the frontend sends bad data: <br>

```text
Frontend
   ↓
BAD DATA
   ↓
FastAPI
   ↓
Business Logic
   ↓
Database
```

 <br> 
You don't want bad data reaching the database. <br>

Instead: <br>

```text
Frontend
   ↓
Incoming Request
   ↓
FastAPI Validation
   ↓
 ┌───────────────┐
 │ Valid?        │
 └───────┬───────┘
       Yes ↓       No
           ↓        ↓
   Business Logic   4xx response
           ↓
       Database
```

 <br>
Validation acts as a gatekeeper.


# There Are Different Types of Validation

In FastAPI, you'll commonly validate: <br>

**Request body**  <br>

```text
{
    "name": "Sunaina",
    "email": "sunaina@example.com"
}
```

 <br> <br>
**Path parameters** <br>

```text
/users/10
       ↑
Query parameters
/users?limit=10
       ↑
```

 <br> <br>
 
**Headers**  <br>
For example: <br>

```text
Authorization: Bearer ...
```

 <br> <br>
**Business rules**  <br>

For example: <br>

A user cannot purchase more than 10 items. <br>

This last category is particularly important. <br>

Not every rule is simply a Pydantic type check. <br>

---

# Pydantic — The Main Tool

FastAPI uses Pydantic heavily for data validation and parsing. <br>

You've already seen: <br>

```text
from pydantic import BaseModel 
```

<br>

and: <br>

```text
class User(BaseModel):
    name: str
    email: str
```

 <br>
This isn't just defining a Python class. <br>

You're effectively telling FastAPI: <br>

"When this model is used for incoming data, these are the fields and types I expect." <br>

# Basic Pydantic Validation

Create: <br>

```text
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str


@app.post("/users")
def create_user(user: User):
    return {
        "name": user.name,
        "email": user.email
    }
```

<br>
Now send: <br>

```text
{
    "name": "Sunaina",
    "email": "sunaina@example.com"
}
```

<br>
Valid.

<br>

# What If a Field Is Missing?

Suppose the client sends: <br>

```text
{
    "name": "Sunaina"
}
```

 <br> <br>
But your model says: <br>

```text
class User(BaseModel):
    name: str
    email: str
```

 <br>
email is required. <br>

FastAPI/Pydantic rejects the request. <br>

You'll receive a validation response rather than your function executing normally. <br>

Typically the HTTP status is: <br>

**422 Unprocessable Entity**  <br>

In newer FastAPI versions, the exact validation status/details can depend on the validation situation, but for request validation failures, 422 is the standard response you'll commonly encounter. <br>

# Why This Is Powerful

Without validation, you might have to manually write: <br>

```text
if "name" not in data:
    ...

if "email" not in data:
    ...

if not isinstance(data["age"], int):
    ...

if data["age"] < 0:
    ...
```

For every endpoint. <br>

Pydantic gives you a structured way to declare these rules <br>

---

# Basic Type Validation



