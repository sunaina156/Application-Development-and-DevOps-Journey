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

Example: <br>

```text
class Product(BaseModel):
    name: str
    price: float
    quantity: int
```

 <br> <br>
This communicates: <br>

```text
name     → string
price    → number
quantity → integer
```

 <br> <br>
Valid: <br>

```text
{
    "name": "Laptop",
    "price": 55000,
    "quantity": 2
}
 <br> <br>

Invalid: <br>

```text
{
    "name": "Laptop",
    "price": "very expensive",
    "quantity": "many"
}
```

 <br>
Pydantic validates the incoming data before your endpoint logic proceeds <br>


# Validation Happens Before Your Function

This is a very important concept. <br>

Consider: <br>

```text
@app.post("/products")
def create_product(product: Product):
    print("Function executed")
    return product
```

 <br>
Client sends invalid data. <br> <br>

FastAPI doesn't simply do: <br>

```text
request
 ↓
function
 ↓
validation
```

 <br> <br>
Conceptually, the process is: <br>

```text
Request
   ↓
Parse request data
   ↓
Validate against Product
   ↓
Valid?
 ┌───┴────┐
Yes       No
 ↓         ↓
Function   Error Response
 ↓
Response
```

 <br>
So your business logic isn't supposed to receive data that failed the declared request-model validation. <br>

# Required vs Optional Fields


**Required** <br>

```text
class User(BaseModel):
    name: str
    email: str
```

 <br>
Both are required. <br> <br>

**Optional** <br>

```text
class User(BaseModel):
    name: str
    email: str | None = None
```

 <br>
Now email can be omitted. <br> <br>

Example: <br>

```text
{
    "name": "Sunaina"
}
```

 <br>
is valid. <br>

The value becomes: <br>

None <br>

# Optional Does Not Mean "Any Value"

This is a common misunderstanding. <br>

```text
email: str | None = None
```

 <br>
means: <br>

```text
email can be:
    string
    OR
    None
```

 <br>
It does not mean: <br>

email can be anything <br>

For example, your model still describes the expected type. <br>

# Default Values

You can provide defaults. <br>

```text
class Product(BaseModel):
    name: str
    price: float
    quantity: int = 1
```

 <br>
If the client sends: <br>

```text
{
    "name": "Keyboard",
    "price": 1000
}
```

 <br>
then: <br>

quantity = 1
 <br>
will be used. <br> <br>

This is useful for optional settings with sensible defaults <br>

# String Constraints

Now we move beyond basic types. <br>

Suppose: <br>

```text
username:
minimum 3 characters
maximum 20 characters
```

 <br> <br>
You can use Field. <br> 

```text
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: str
```

 <br>
Now: <br>

ab <br>

is too short. <br>

And a username longer than 20 characters is rejected. <br> <br>

# Numeric Constraints

Suppose: <br>

```text
age must be >= 18
```

 <br>
Use: <br>

```text
class User(BaseModel):
    name: str
    age: int = Field(ge=18)
```

 <br>
ge means: <br>

greater than or equal to <br>

So: <br>

```text
age = 18 ✅
age = 20 ✅
age = 17 ❌
```

 <br> <br>

 # Important Numeric Constraint Options

You'll commonly see: <br>

```text
gt → greater than
ge → greater than or equal to
lt → less than
le → less than or equal to
```

 <br>
Examples: <br>

```text
price: float = Field(gt=0)
```

 <br>
means: <br>
price > 0 <br> <br>

While: <br>

```text
age: int = Field(ge=18)
```

 <br>
means: <br>

age >= 18 <br> <br>

And: <br>

```text
quantity: int = Field(ge=1, le=100)
```

 <br>
means: <br>

1 <= quantity <= 100 <br>

---

# Why Validation Rules Matter

Imagine an e-commerce application: <br>

```text
class Product(BaseModel):
    name: str
    price: float
    quantity: int
```

 <br> <br>
Without constraints: <br>

```text
price = -5000
quantity = -100
```

 <br>
could potentially enter your application. <br> <br>

But: <br>

```text
class Product(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity: int = Field(ge=1)
```

 <br>
creates much stronger boundaries. <br>

---

# Email Validation


