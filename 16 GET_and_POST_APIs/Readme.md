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






















