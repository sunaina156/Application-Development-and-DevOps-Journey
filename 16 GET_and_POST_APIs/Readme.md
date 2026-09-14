# GET

GET is generally used when the client wants to retrieve/read data. <br>

Ex: <br>

```text
GET /users
GET /products
GET /orders
GET /urls
```

 <br> <br>
Ex:  <br>
**GET /users** <br>
could return:  <br>

```text
[
  {
    "id": 1,
    "name": "Sunaina"
  },
  {
    "id": 2,
    "name": "Rahul"
  }
]
```

---

# POST

POST is generally used when the client wants to send data to the server, commonly to create a new resource.  <br>

Ex: **POST /users**  <br>

The client might send:  <br>

```text
{
  "name": "Sunaina",
  "email": "sunaina@example.com"
}
```

 <br>
The backend processes it and might respond:  <br>

```text
{
  "id": 3,
  "name": "Sunaina", 
  "email": "sunaina@example.com"
}
```

 <br>
Conceptually:  <br>

```text
POST /users
      ↓
"Please create this user"
```

---


# GET vs POST

## GET
- Usually retrieves data
- Data often represented in URL/query
- Should not normally change server state
- Can be cached in appropriate circumstances
- Usually safe/idempotent

## POST
- Usually creates/submit data
- Data commonly sent in request body
- Often changes server state
- Usually not treated like a chacheable retrieval
- Not generally idempotent

---

# What does "server state" mean?

Suppose your database contains: <br>
**users** <br>
 <br>
If your send: <br>
**GET /users** <br>
you are generally asking show me what is already there.  <br>
You are not asking the server to create something.  <br> <br>

But **POST /users** <br>
might cause <br>

```text
New user
   ↓
Database INSERT
```

<br>
So server state changes.


**POST isn't generally considered idempotent.**

---

# What does idempotent mean?

An operation is idempotent if repeating the same operation has the same intended effect on server state as performing it once. <br>

For example, conceptually: <br>

```text
PUT /users/10
```

 <br>
with the same complete representation repeatedly should leave user 10 in the same final state. <br>

POST doesn't have that guarantee <br>

---

# HTTP Request

Every API interaction starts with a request. <br>

A simplified HTTP request looks like: <br>

```text
POST /users HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "name": "Sunaina",
    "email": "sunaina@example.com"
}
```

# ## Request method

```text
POST
```

<br>
This tells the server what type of operation the client is requesting.

## Request path

```text
/users
```

<br>
This identifies the requested resource/path. <br>

## Request headers

Ex: <br>

```text
Content-Type: application/json
```

Headers provide additional information about the request.  <br>

Ex: <br>

```text
Content-Type
Authorization
Accept
User-Agent
```

## Request body

The request body contains data sent to the server.  <br>

Ex:  <br>

```text
{
  "name": "Sunaina",
  "email": "sunaina@example.com"
}
```


---

# Important: GET can technically have a body, but...

HTTP does not generally prohibit a body on every GET implementation, but using a request body with GET is not the normal API design pattern and has poor interoperability.  <br>

For our applications: <br>

```text
GET
 ↓
retrieve data

POST
 ↓
send/create data in request body
```

## HTTP Response

The server sends a response back. <br>

Simplified: <br>

```text
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 1,
    "name": "Sunaina"
}
```


## Response status code

201 Created - tells the client what happened. <br>

Common examples: <br>

```text
200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
500 Internal Server Error
```

## Response headers

Example: <br>

```text
Content-Type: application/json
```

This tells the client what kind of data is being returned. <br>

## Response body

Example: <br>

```text
{
    "id": 1,
    "name": "Sunaina"
}
```

 <br>
This contains the actual response data.  <br>

## The complete request/response

For POST: <br>

```text
CLIENT
   │
   │ POST /users
   │
   │ JSON body
   ▼
FASTAPI
   │
   │ process request
   ▼
PYTHON LOGIC
   │
   ▼
DATABASE
   │
   │
   ▼
FASTAPI
   │
   │ 201 Created
   │ JSON response
   ▼
CLIENT
```

---

# Let's build a GET API

main.py <br>

```text
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
  return [
    {
      "id": 1,
      "name": "Sunaina"
    },
    {
      "id": 2,
      "name": "Rahul"
    }
  ]
```

 <br>
Run:  <br>
**uvicorn main:app --reload**  <br> <br>

Open:  <br>
**http://localhost:8000/users** <br> <br>

You'll receive:  <br>

```text
[
  {
    "id": 1,
    "name": "Sunaina"
  },
  {
    "id": 2,
    "name": "Rahul"
  }
]
```

 <br> <br>

## What happened here?

The client requested:  <br>
**GET /users**  <br> <br>

FastAPI found:  <br>
**@app.get("/users")**  <br> <br>

Then it called:  <br>
**get_users()** <br> <br>

The function returned a Python list containg dictionaries. <br>
FastAPI converted that result into  a JSON response.  <br>

So: <br>

```text
Python list/dict
      ↓
FastAPI
      ↓
JSON response
```

## GET does not mean "Python GET function"

This: <br>
**@app.get("/users")**  <br>

is FastAPI's way of registering an HTTP GET operation. <br> <br>

The function: <br>

**def get_users():** <br>

is just your Python function. <br> <br>

You could technically call it: <br>

**def hello():** <br>

and it would still work <br>.

The important part is: <br>

**@app.get("/users")**


## GET with a single object

Try: <br>

```text
@app.get("/user")
def get_user():
    return {
        "id": 1,
        "name": "Sunaina",
        "email": "sunaina@example.com"
    }
```

 <br>
Request: <br>

```text
GET /user
```

 <br>
Response: <br>

```text
{
    "id": 1,
    "name": "Sunaina",
    "email": "sunaina@example.com"
}
```

---

# POST

Let's create: <br>

```text
POST /users
```

 <br>
We need to receive information from the client. <br>

For example: <br>

```text
{
    "name": "Aman",
    "email": "aman@example.com"
}
```

 <br>
The backend needs a way to read this request body. <br>

FastAPI provides several ways to do that. <br>

## Using Body

You can write: <br>

```text
from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/users")
def create_user(user: dict = Body(...)):
  return {
    "message": "User received",
    "user": user
  }
```

<br>
Now the endpoint expects a request body. <br>

### What does this mean?

```text
user: dict 
```

means: <br>

user is expected to be a Python dictionary. <br>

And: <br>

```text
Body(...)
```

 <br>
tells FastAPI: <br>

Get this value from the HTTP request body. <br>

The ... means the body is required. <br>

## Test the POST API

Go to: <br>
http://localhost:8000/docs <br> <br>

Find: <br>
POST /users <br> <br>

Try it out <br> <br>

You can enter: <br>

```text
{
    "name": "Aman",
    "email": "aman@example.com"
}
```

 <br> <br>
Then click: <br>

Execute <br> <br>

You should receive something like:  <br>


## But this isn't how we'll build production APIs

This works: <br>

user: dict <br>

but it doesn't tell us exactly what the user data should look like. <br> <br>

What if the client sends: <br>

```text
{
    "banana": "hello"
}

or:

{
    "age": "something"
}

or:

{
    "name": 123
}
```

 <br>
We need proper schemas and validation. <br>

That's where Pydantic models become important.

---

# Pydantic model

```text
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Helo, FastAPI!"}

@app.get("/about")
def about():
    return {
        "application": "URL Shortener",
        "version": "1.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
```


## Understanding BaseModel

```text
class User(BaseModel):
```

<br>
We are creating a Pydantic model called User. <br> <br>

Then: <br>
```text
name: str
email: str
```

<br>
describe the expected data. <br> <br>


## What request should we send?

```text
{
    "name": "Aman",
    "email": "aman@example.com"
}
```

<br>
FastAPI/Pydantic processes it according to the model. <br> <br>

Then inside the function: <br>

```text
user
```

 <br>
is a User model instance rather than an ordinary dictionary. <br> <br>

You can access: <br>

```text
user.name
```

 <br>
and: <br>

```text
user.email
```

## Why models are better

Compare: <br>

user: dict <br> <br>

with: <br>

user: User <br> <br>

The second approach communicates much more clearly: <br>

This endpoint expects a User object containing a name and email. <br> <br>

It also gives FastAPI enough information to generate better API documentation and perform validation. <br>

## What happens if required data is missing?

Suppose your model is: <br>

```text
class User(BaseModel):
    name: str
    email: str
```

 <br> <br>
but the client sends: <br>

```text
{
    "name": "Aman"
}
```

 <br> <br>
The required email is missing. <br>

FastAPI/Pydantic will reject the request instead of simply giving your function an incomplete object. <br> <br>

The client receives a validation error response, typically: <br>

422 Unprocessable Entity <br>

Depending on the exact situation/version and validation semantics, the response contains details describing what failed. <br>

---

# GET and POST side by side

```text
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.get("/users")
def get_users():
    return [
        {
            "id": 1,
            "name": "Sunaina",
            "email": "sunaina@example.com"
        }
    ]

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User received",
        "user": user
    }
```

<br>

Now:  <br>

**GET /users** <br>
means Give me users. <br> <br>

while:  <br>
**POST /users** <br>
means here's user data, process/create it. <br> <br>

Same resource: <br>
**users** <br>
Different operation: <br>
**GET** <br>
**POST** <br>

## This is the beginning of REST-style API design

A common API design pattern is: <br>
**/users** <br> 
represents the user resource.  <br> <br>

Then: <br>
**GET /users**  <br>
retrieve users <br> <br>

**POST /users** <br>
create user <br> <br>

GET /users/10 <br>
retrieve user 10 <br> <br>

PUT /users/10  <br>
replace user 10 <br> <br>

PATCH /users/10 <br>
partially update user 10 <br> <br>

DELETE /users/10 <br>
delete user 10

## Don't create URLs like this unnecessarily

A beginner might write: <br>

```text
/create-user
/get-users
/delete-user
/update-user
```

 <br> <br>
It is possible , but a more resource-oriented API design often uses: <br>

```text
/users
```

with HTTP methods expressing the operation. <br>
 <br>

Ex: <br>

```text
POST /users
```

instead of:  <br>

```text
POST /create-user
```

This is a REST-style design principle.

---

# Another Example: URL Shortener

This is directly related to the application you have already built. <br>
 <br>
Imagine the future API:  <br>

```text
POST /urls
```

 <br> <br>

Client sends:  <br>

```text
{
  "original_url": "https://github.com"
}
```

 <br> <br>
Backend:  <br>

```text
Generate short code
       ↓
Store in PostgreSQL
       ↓
Return result
```

<br> <br>
Response: <br>

```text
{
    "short_code": "abc123",
    "original_url": "https://github.com"
}
```

<br> <br>
Then later: <br>

```text
GET /abc123
```

will retrieve the URL and eventually redirect.

---

# GET request with query data - preview only

You may see URLs like:  <br>
**GET /users?limit=10** <br>

 <br>
The: <br>

**?limit=10** <br>
is a query parameter. <br>


# POST body vs query parameter

POST: <br>
**POST /users** <br> <br>

can receive: <br>

```text
{
  "name": "Sunaina",
  "email": "sunaina@example.com"
}
```

as a request body <br> <br>

Whereas: <br>
**GET /users?limit=10** <br>
has limit=10 <br>
in the URL query string. <br> <br>


# What does /docs do for POST?

Open: <br>
**http://localhost:8000/docs** <br> <br>

FastAPI knows: <br>

```text
class User(BaseModel):
  name: str
  email: str
```

 <br> <br>
So Swagger UI can display an expected request body such as: <br>

```text
{
  "name": "string",
  "email": "string"
}
```

 <br>
This is one of the major benefit of structure API definitions. <br> <br>

---

# Status Codes















