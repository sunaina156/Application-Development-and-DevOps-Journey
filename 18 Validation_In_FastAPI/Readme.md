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

FastAPI itself doesn't magically know every business rule about email addresses just because you write: <br>
email: str <br>
That's only a string. <br> <br>

For actual email-format validation, Pydantic provides an email-specific type. <br>

```text
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
```

 <br>
Now: <br>

sunaina@example.com <br>

is valid-looking email syntax. <br> <br>

While something like: <br>

hello <br>

will fail email validation. <br> <br>

You may need the email validation dependency: <br>

```text
pip install email-validator
```

 <br>
Your requirements.txt should then include the required dependency if your project uses it.

---

# Practical User Model

```text
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class User(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=18, le=100)


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User is valid",
        "user": user
    }
```

<br>
Now your API expects: <br>

```text
name
→ string
→ 2–100 characters

email
→ valid email format

age
→ 18–100
```

<br>

## Test Valid Data

at http://localhost:8000/docs <br>


Send: <br>

```text
{
    "name": "Sunaina",
    "email": "sunaina@example.com",
    "age": 21
}
```

 <br>
Expected: <br>

```text
{
    "message": "User is valid",
    "user": {
        "name": "Sunaina",
        "email": "sunaina@example.com",
        "age": 21
    }
}
```

## Test Missing Data

Send: <br>

```text
{
    "name": "Sunaina",
    "age": 21
}
```

 <br>
email is missing. <br> <br>

Result: <br>

```text
Validation error
```

 <br>
Your endpoint function won't process it as a valid User. <br>

## Test Invalid Age

Send: <br>

```text
{
    "name": "Sunaina",
    "email": "sunaina@example.com",
    "age": 15
}
```

 <br>
Your rule says: <br>

age: int = Field(ge=18, le=100) <br>

Therefore: <br>

15 < 18 <br>

Validation fails <br> <br>

## Test Invalid Email

Send: <br>

```text
{
    "name": "Sunaina",
    "email": "hello",
    "age": 21
}
```

<br>
The email validation fails. <br>

## Test Short Name

Send: <br>

```text
{
    "name": "S",
    "email": "sunaina@example.com",
    "age": 21
}
```

 <br>
Your rule: <br>

min_length=2 <br>

is violated. <br>

Validation fails <br>

---

# Validation Error Response

FastAPI gives structured validation information. <br>

A response can look conceptually like: <br>

```text
{
    "detail": [
        {
            "loc": ["body", "age"],
            "msg": "Input should be greater than or equal to 18",
            "type": "greater_than_equal"
        }
    ]
}
```

 <br>
Don't memorize the exact wording. <br>

Understand the structure: <br>

```text
detail
 └── validation errors
      ├── location
      ├── message
      └── error type
```

---

# What Does loc Mean?

Suppose you see: <br>

```text
"loc": ["body", "age"]
```

 <br> 
It means the invalid value was found in: <br>

```text
request body
    ↓
   age
```

 <br> <br>
For a path parameter you might see something conceptually like: <br>

```text
["path", "user_id"]
```

 <br>
For a query parameter: <br>

```text
["query", "limit"]
```

 <br>
This becomes very useful when debugging APIs.

---

# Validating Path Parameters

```text
@app.get("/users/{user_id}")
def get_user(user_id: int):
    ...
```

<br>
You've already got basic validation: <br>

```text
user_id must be an integer
```

 <br>
But we can add constraints. <br>

```text
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(ge=1)
):
    return {
        "user_id": user_id
    }
```

 <br>
Now: <br>

```text
/users/10
```

 <br>
valid. <br>

But: <br>

```text
/users/0
```

 <br>
invalid. <br>

# Path Parameter Description

You can also add metadata: <br>

```text
user_id: int = Path(
    ge=1,
    description="The ID of the user"
)
```

 <br>
This information can appear in the generated API documentation. <br>

That means validation isn't only about rejecting bad requests. <br>

It also helps describe your API contract. <br>

---

# Validating Query Parameters

Day 17 introduced: <br>

```text
limit: int | None = None
```

 <br>
Now we can make it safer. <br>

```text
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/products")
def get_products(
    limit: int = Query(default=10, ge=1, le=100)
):
    return {
        "limit": limit
    }
```

This means: <br>

default = 10 <br>
minimum = 1 <br>
maximum = 100 <br>

# Test Query Validation

```text
Valid:
/products?limit=20
```

```text
Invalid:
/products?limit=0
```

```text
Invalid:
/products?limit=101
```

```text
Invalid:
/products?limit=hello
```

<br>
The validation layer catches these before your function gets a valid limit. <br>

# Query String Length Validation

Suppose you're building: <br>

```text
GET /search?q=python
```

 <br>
You want: <br>

```text
q must contain at least 2 characters
```

 <br> <br>
Use: <br>

```text
@app.get("/search")
def search(
    q: str = Query(min_length=2, max_length=50)
):
    return {
        "query": q
    }
```

 <br>
Now: <br>

```text
/search?q=p

fails.
```

While: <br>

```text
/search?q=python

works.
```

---

# Validation vs Database Constraints

This is very important for your DevOps/backend understanding. <br>

You might have: <br>

```text
FastAPI validation
+
PostgreSQL constraints
```

 <br>
They are not duplicates. <br>

They protect different layers. <br> <br>

For example: <br>

**FastAPI** <br>
```text
email: EmailStr
```

 <br>
checks incoming API data. <br>

**PostgreSQL** <br>
```text
email VARCHAR(255) UNIQUE NOT NULL
```

protects the database itself. <br> <br>

Think: <br>

```text
Client
 ↓
FastAPI validation
 ↓
Business logic
 ↓
PostgreSQL constraints
 ↓
Stored data
```

 <br>
You want protection at multiple layers. <br>

# Validation vs Business Logic

This distinction is also extremely important. <br>

Suppose: <br>

```text
age must be an integer
```

 <br>
That's a validation rule. <br> <br>

But: <br>

```text
user must be at least 18 to purchase alcohol
```

 <br>
is a business rule. <br>

Or: <br>

```text
a user can create maximum 10 active URLs
```

 <br>
is a business rule. <br> <br>

These may require database queries and application logic. <br>

So don't try to put every possible application rule into Pydantic. <br>

---

# Example: URL Shortener

This connects directly to your project. <br>

Your URL shortening API might eventually receive: <br>

```text
{
    "original_url": "https://github.com"
}
```

 <br>
You don't want: <br>

```text
{
    "original_url": ""
}
```

 <br>
You could define: <br>

```text
from pydantic import BaseModel, Field


class URLCreate(BaseModel):
    original_url: str = Field(min_length=1)
```

 <br>
Later, you can use stronger URL-specific validation. <br>

The flow becomes: <br>

```text
POST /urls
      ↓
Request body
      ↓
Pydantic validation
      ↓
Is original_url valid?
      ↓
Business logic
      ↓
Generate short code
      ↓
PostgreSQL
```

Think: <br>

```text
Validation
→ Is the input shaped correctly?

Business logic
→ Is this operation allowed?

Database constraints
→ Is the data allowed to exist consistently?
```

# Pydantic Model as an API Contract

This is a powerful concept. <br>

When you write: <br>

```text
class User(BaseModel):
    name: str
    email: EmailStr
```

 <br>
you're establishing a contract: <br>

Client must provide: <br>

name → string <br>
email → valid email <br> <br>

So your model becomes a kind of agreement between: <br>

```text
Client ↔ API
```

 <br>
This makes APIs predictable. <br> <br>

---

# Request Model vs Response Model

You might have: <br>

```text
class UserCreate(BaseModel):
    name: str
    email: EmailStr
```

 <br>
for incoming data. <br> <br>

But your response might be: <br>

```text
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
```

 <br>
Why? <br>

Because the client shouldn't necessarily provide: <br>

**id** <br>

The database creates it. <br>

So: <br>

```text
Request
→ name + email

Database
→ creates id

Response
→ id + name + email
```

 <br>
This pattern becomes very important once we connect FastAPI to PostgreSQL. <br>
<br>

# Example

```text
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr


@app.post("/users")
def create_user(user: UserCreate):
    # Database operation will come on Day 19
    return {
        "id": 1,
        "name": user.name,
        "email": user.email
    }
```

<br>

The client sends: <br>

```text
{
    "name": "Sunaina",
    "email": "sunaina@example.com"
}
```

<br>
The API returns: <br>

```text
{
    "id": 1,
    "name": "Sunaina",
    "email": "sunaina@example.com"
}
```

# Why Separate Models?

Imagine: <br>

**UserCreate** <br>

means: <br>

Data required to create a user. <br> <br>

While: <br>

**UserResponse** <br>

means: <br>

Data returned after creating a user. <br>

They have different responsibilities. <br>

This becomes extremely useful in real applications. <br>

You'll eventually see models such as: <br>

```text
UserCreate
UserUpdate
UserResponse
LoginRequest
TokenResponse
URLCreate
URLResponse
```

 <br> <br>

 ---

 # Nested Validation


Pydantic models can contain other models. <br>

Example: <br>

```text
class Address(BaseModel):
    city: str
    country: str


class User(BaseModel):
    name: str
    email: EmailStr
    address: Address
```

 <br>
Request: <br>

```text
{
    "name": "Sunaina",
    "email": "sunaina@example.com",
    "address": {
        "city": "Bhopal",
        "country": "India"
    }
}
```

 <br>
FastAPI/Pydantic validates the nested structure too. <br>

This becomes useful for more complex APIs.  <br>

# Validation of Lists

You can also validate collections. <br>

Example: <br>

```text
from pydantic import BaseModel, Field


class Order(BaseModel):
    product_ids: list[int] = Field(min_length=1)
```

 <br>
This means: <br>

product_ids <br>
→ must be a list of integers <br>
→ at least one item <br> <br>

Valid: <br>

```text
{
    "product_ids": [1, 2, 3]
}
```

 <br>
 
Invalid: <br>

```text
{
    "product_ids": []
}
```

<br>

# Extra Fields

Suppose your model is: <br>

```text
class User(BaseModel):
    name: str
    email: str
```

 <br>
Client sends: <br>

```text
{
    "name": "Sunaina",
    "email": "sunaina@example.com",
    "password": "secret"
}
```

 <br>
What happens to the extra field depends on the Pydantic model configuration/version and how you've configured it. <br>

The important production lesson is: <br>

Decide intentionally how your API handles unexpected fields, especially for security-sensitive models. <br>

For example, you may choose to forbid unexpected fields for certain request models. <br>

# Don't Trust Frontend Validation

This is a major production principle. <br>

A frontend might validate: <br>

```text
email
password
age
```

But the backend must validate again. <br>

Why? <br>

Because a client can send requests without using your frontend. <br>
 
For example: <br>

```text
Browser
Mobile app
curl
Postman
Another service
Malicious client
```

 <br>
All can call your API. <br>

Therefore: <br>

```text
Frontend validation
→ good user experience

Backend validation
→ actual security/data protection
```

Never assume the frontend is trustworthy. <br>

# Validation Is Not Authentication

Don't confuse Validation with Authentication. <br>

```text
Validation asks:
Is this input correctly formatted?

Authentication asks:
Who are you?

Authorization asks:
Are you allowed to do this?
```

<br>
Example: <br>
email = valid  doesnot means user is authenticated <br>

And: <br>

age = 25 doesn't mean user is authorized
 <br>
These are different security concepts.
 <br>

 ---

 # Full Request Flow

 Your mental model should now become: <br>

```text
Client
   ↓
HTTP Request
   ↓
Uvicorn
   ↓
FastAPI
   ↓
Route Matching
   ↓
Extract Path / Query / Body
   ↓
Validation
   ↓
 ┌───────────────┐
 │ Valid?        │
 └───────┬───────┘
     Yes ↓       No
         ↓        ↓
 Business Logic   Validation Error
         ↓
      Database
         ↓
      Response
```

<br>

---















      
