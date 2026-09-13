# What is a backend?

A backend is the part of an application responsible for things such as: <br>

- business logic
- data processing
- authentication
- database interaction
- authorization
- APIs
- background processing
- communicating with other services

<br>

For example, in a shopping application: <br>

```text
Frontend:
"Buy this product"

Backend:
"Is the user logged in?"
"Is the product available?"
"How much does it cost?"
"Can this user buy it?"
"Create the order"
"Update inventory"
"Save order in database"
```

---

# What is an API?

API = Application Programming Interface <br>

In our context, think of it as a controlled interface through which one application communicates with another. <br>

Example: <br>

```text
Mobile App
     ↓
   API
     ↓
Backend
```

 <br>
The mobile app doesn't need to know how the backend internally works. <br>

It only needs to know: <br>

Which URL? <br>
Which HTTP method? <br>
What data should I send? <br>
What response will I receive? <br>

---

# What is a Web API?

A Web API is an API accessible over a network using web technologies, primarily HTTP. <br>

For example: <br>

```text
GET https://example.com/users

or:

POST https://example.com/users
```

 <br>
The client sends an HTTP request. <br>

The server sends an HTTP response. <br>

---

# What is HTTP?

HTTP = HyperText Transfer Protocol <br>

It's the protocol used for communication between clients and web servers. <br>

Basic flow: <br>

```text
Client
  │
  │ HTTP Request
  ▼
Server
  │
  │ HTTP Response
  ▼
Client
```

 <br>
 
 For example: <br>

 ```text
 GET /users
```

 <br>
 
The server might respond: <br>

```text
{
    "users": 100
}
```

---

# HTTP methods

```text
Method	| General purpose
GET     |	Retrieve data
POST	  | Create/send data
PUT	    | Replace/update data
PATCH	  | Partially update data
DELETE	| Delete data
```

<br>
Example: <br>

GET /users <br>

means Give me users. <br>

POST /users <br>

means Create a user. <br>

---

# What is a URL?

Consider: <br>

http://localhost:8000/users <br>

Break it down: <br>

```text
http://
   ↓
Protocol

localhost
   ↓
Host

8000
   ↓
Port

/users
   ↓
Path

So:

http://localhost:8000/users
│       │         │    │
│       │         │    └── Path
│       │         └─────── Port
│       └───────────────── Host
└───────────────────────── Protocol

```

---

# What is localhost?

localhost means this computer. <br>

Usually localhost resolves to 127.0.0.1 <br>

So these normally refer to your own machine: <br>

http://localhost:8000  <br>

and: <br>

http://127.0.0.1:8000 <br>

---

# What is a port?

A port identifies a network endpoint where a service is listening. <br>

For example: <br>

FastAPI → 8000 <br>
PostgreSQL → 5432 <br>

So: <br>

localhost:8000 means connect to port 8080 on my computer. <br>


Later you might have: <br>

```text
Browser
   ↓
localhost:8000
   ↓
FastAPI

FastAPI
   ↓
localhost:5432
   ↓
PostgreSQL
```

<br>

---

# What is a server?

At a high level, a server is a program/system that listens for requests and responds to them. <br>

When you run: <br>

```text
uvicorn main:app
```

 <br>
Uvicorn starts listening for requests. <br>

For example: <br>

127.0.0.1:8000 <br>

is now accepting HTTP connections. <br>

---
---

# So what exactly is FastAPI?

FastAPI is a Python web framework for building APIs. <br>

It provides mechanisms for: <br>

- defining routes
- receiving HTTP requests
- handling requests
- returning responses
- validation
- serialization
- error handling
- API documentation
- asynchronous programming

---

# Python vs FastAPI


Python: Programming language <br>

FastAPI: Framework built using Python <br>

You can write: <br>

print("Hello") <br>

without FastAPI. <br> <br>

But to create an HTTP API easily, FastAPI provides the necessary framework.
 <br>
Think: <br>

```text
Python
   ↓
Language

FastAPI
   ↓
Framework using Python
```

---

# What is a framework?

A framework provides a structure and tools for building applications. <br>

Without a web framework, you'd have to deal with many low-level web concerns yourself. <br>

With FastAPI: <br>

```text
@app.get("/")
def home():
    return {"message": "Hello"}
```

 <br>
FastAPI handles much of the HTTP-related plumbing around your function. <br>

The framework essentially says: <br>

You define what should happen when a request arrives; I'll handle much of the web machinery around it. <br>

---

# FastAPI is not the server

FastAPI and Uvicorn are not the same thing.  <br>

FastAPI defines your web application. <br>
Uvicorn runs that application using an ASGI server. <br>

Simplified: <br>

```text
Client
  ↓
Uvicorn
  ↓
FastAPI
  ↓
Your function
```

---

# What is Uvicorn?

Uvicorn is an ASGI web server implementation. <br>

Its job is to run your FastAPI application and communicate with clients over HTTP. <br>

When you run: <br>

```text
uvicorn main:app
```

 <br>
Uvicorn essentially says: <br>

Find the app application inside main.py and serve it. <br>

---

# Understanding main:app

command: <br>

```text
uvicorn main:app
```

<br>
contains main:app <br>
main means main.py <br>
app means app = FastAPI() <br>
So main:app means import the app object from main.py <br>

---

# What is ASGI?

ASGI = Asynchronous Server Gateway Interface <br>

understand the architecture: <br>

```text
HTTP Client
     ↓
ASGI Server
     ↓
ASGI Application
```

Uvicorn is an ASGI server. <br>
FastAPI provides an ASGI-compatible application. <br>


Conceptually: <br>

```text
Browser
   ↓
HTTP
   ↓
Uvicorn
   ↓
FastAPI
   ↓
Your Python code
```

<br>

---

# What about WSGI?

WSGI is the older/common Python web-server interface. <br>

ASGI was designed to support modern asynchronous capabilities and protocols beyond traditional synchronous HTTP handling. <br>

Framework examples: <br>

```text
Flask → traditionally WSGI
FastAPI → ASGI
```

 <br>

```text
FastAPI
   ↓
ASGI application

Uvicorn
   ↓
ASGI server

```

 <br>
 
---
---


# Install FastAPI

Create your project: Application_Development/ <br>
Open it in VS Code. <br>

Create virtual environment: <br>

python -m venv venv <br>
 <br>
Activate: <br>

.\venv\Scripts\Activate.ps1 <br> <br>

Install: <br>

```text
pip install fastapi uvicorn
```

 <br>
Verify: <br>

pip list <br>

---

# Why use a virtual environment?

Suppose project A needs: <br>

FastAPI version X <br> <br>

and project B needs: <br>

FastAPI version Y <br>

Installing everything globally can create conflicts. <br>

A virtual environment isolates dependencies. <br>

```text
Computer
│
├── Project A
│    └── venv
│
├── Project B
│    └── venv
│
└── Project C
     └── venv
```

Your project dependencies stay isolated. <br>

This is why you have already been using: <br>

venv/ <br>

with your Python projects. <br>

---

#  Create your first FastAPI application

main.py <br><br>

```text
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Helo, FastAPI!"}
```

 <br>

**from fastapi import FastAPI** <br>
we import FastAPI class. <br>
Without importing it, Python doesn't know what FastAPI means.  <br> <br>

**app = FastAPI()** <br>
This creates your FastAPI application object.  <br>
Think of **app** as the central object representing our web application. <br> <br>

**@app.get("/")** <br>
The @ syntax is a Python decorator. <br>
At a general Python level, a decorator modifies or registers behaviour around a function. <br>
In FastAPI, decorators are used to register path operations. <br>
 <br>
ex: <br>

```text
@app.get("/")
def home():
  ...
```

 <br>
means Register home() as the function that handles GET requests for / <br>

---

# What is a path operation?
FastAPI documentation commonly calls: <br>

```text
@app.get("/")
```

 <br>
a path operation decorator. <br> <br>

The combination: <br>

```text
HTTP method + path
```

 <br>
defines the operation. <br> <br>

Ex: <br>

```text
GET /
```

 <br>
or: <br>

```text
GET /users
```

---

# Route vs endpoint

A **route/path** is the URL path: <br>

```text
/users
```

 <br> <br>
An **endpoint** usually refers to the accessible API operation: <br>

```text
GET /users
```

 <br> <br>
The HTTP method matters. <br>

These are different operations: <br>

```text
GET /users
POST /users
```

 <br>
even though they have the same path. <br>

---

# The function

```text
def home():
```

<br>
This is a normal Python function. <br>
FastAPI will call it when a matching request arrives. <br>
The function is your application for that endpoint. <br>

---

# The response

```text
return {"message": "Hello, FastAPI"}
```

 <br>
You're returning a Python dictionary. <br>
FastAPI converts it into an HTTP response containing JSON. <br>
 <br>
 
Conceptually: <br>

```text
Python dict
     ↓
FastAPI serialization
     ↓
JSON
     ↓
HTTP response
```

---

# Run the application

Run: <br>

```text
uvicorn main:app --reload
```

 <br>
You should see something similar to: <br>

```text
Uvicorn running on http://127.0.0.1:8000
```

 <br>
Now your application is running. <br>

---

# # Understand --reload

You ran: <br>

```text
uvicorn main:app --reload
```

 <br>
--reload means: <br>
Watch your source files and restart/reload the application when code changes during development. <br>
 <br>
Ex: <br>

```text
You modify main.py
        ↓
Uvicorn notices
        ↓
Application reloads
```

 <br>
This is convenient during development. <br>
Don't think of --reload as something you normally want in production. <br>

---

# Your first request

Open: <br>

```text
http://127.0.0.1:8000/
```

 <br> <br>
Your browser sends approximately: <br>
GET / <br> <br>

FastAPI sees: <br>
@app.get("/") <br> <br>

and calls: <br>
home() <br> <br>

The function returns: <br>
{"message": "Hello, FastAPI!"} <br> <br>

FastAPI produces a response. <br>

---

# The complete request lifecycle

```text
                CLIENT
          Browser / Mobile App
                    │
                    │ HTTP Request
                    │
                    ▼
             ┌─────────────┐
             │   Uvicorn   │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │   FastAPI   │
             └──────┬──────┘
                    │
              Match route
                    │
                    ▼
             ┌─────────────┐
             │ Python      │
             │ function    │
             └──────┬──────┘
                    │
                    ▼
                 Result
                    │
                    ▼
             FastAPI creates
             HTTP response
                    │
                    ▼
                  Client
```

---

# Add another route

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

```

<br> <br>

GET / calls home() <br>
and <br>
GET /about calls about() <br>

---

# Route matching

Suppose someone requests: <br>

**GET /about** <br>
FastAPI checks its registered routes. <br>
It finds **@app.get("/about")** <br>
Then it executes **about()** <br> <br>

But if the client requests **GET /something** <br>
FastAPI won't find a matching route. <br>
Usually the cient receives: <br>

```text
404 NOT Found
```

---

# # What is 404?

HTTP status codes communicate result of a request. <br>

Ex: <br>

```text
200 → Success
201 → Created
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Internal Server Error
```

---

# FastAPI automatic documentation

Go to: <br>

```text
http://127.0.0.1:8000/docs
```

 <br>
You'll see your API. <br>
This is Swagger UI. <br>

 <br>
It automatically displays your available endpoints. <br>

Ex: <br>

```text
GET /
GET /about
```

 <br>
You can interact with them directly. <br>
This is extremly useful when developing APIs. <br>

---

# Where did /docs come from?

You didn't write: <br>

```text
@app.get("/docs")
```

 <br>
FastAPI provides it automatically. <br>
FastAPI automatically generates API documentation based on the application's API definitions. <br>
It uses the OpenAPI specification. <br>

---

# What is OpenAPI?

OpenAPI is a standardized specification for describing HTTP APIs. <br>

It can describe things like: <br>

- available endpoints
- HTTP methods
- parameters
- request bodies
- responses
- schemas

 <br>
FastAPI generates an OpenAPI schema for your application. <br>

You can normally access the raw schema at: <br>

```text
http://127.0.0.1:8000/openapi.json
```

 <br>
You don't need to manually write that JSON.
 <br>
FastAPI generates it.

---

# Swagger UI vs OpenAPI vs ReDoc

**OpenAPI** <br>

The specification/documentation description of your API. <br>
 <br>
 
**Swagger UI** <br>

An interactive interface that displays the API documentation. <br> <br>

**ReDoc**  <br>

Another interface for displaying OpenAPI documentation. <br>

So: <br>

```text
FastAPI
   ↓
Generates OpenAPI schema
   ↓
Swagger UI / ReDoc
   ↓
Human-friendly documentation
```

---

# /docs

Interactive Swagger UI: <br>

```text
/docs
```

Useful for: 

- testing endpoints
- seeing parameters
- seeing request schemas
- seeing responses

---

# /redoc

Alternative documentation interface: <br>

```text
/redoc
```

<br>
It's generally more documentation-oriented and less focused on interactive testing.

---

# Why automatic documentation matters in real companies

Imagine a company has: <br>

```text
Frontend Team
Backend Team
Mobile Team
QA Team
DevOps Team
```

 <br> <br>
Backend developers create APIs. <br>

Other teams need to know: <br>

```text
Which endpoints exist?
What data do I send?
What response do I receive?
What parameters are required?
```

 <br>
Good API documentation makes this much easier. <br>

FastAPI automatically generating OpenAPI documentation is therefore more than a beginner convenience.

---

# Add a health endpoint

A common pattern in real services is a health endpoint. <br>

```text
@app.get("/health")
def health():
  return {
    "status": "healthy"
}
```

<br>
Now: <br>

```text
GET /health
```

 <br>

returns:  <br>

```text
{
  "status": "healthy"
}
```

Later, infrastructure tools can use health endpoints for service checks. <br>

Ex:  <br>

```text
Load Balancer
      ↓
GET /health
      ↓
Application
```

---

```text
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to my application"
    }


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

---

# FastAPI does NOT automatically mean REST

FastAPI is a framework. <br>

REST is an architectural style for designing APIs. <br>

You can use FastAPI to build REST-style APIs, but: <br>

```text
FastAPI ≠ REST
```

 <br>
Similarly: <br>

JSON ≠ API <br>

and: <br>

Uvicorn ≠ FastAPI <br>

---

## Understand

```text
Python -> programming language
FastAPI -> Python framework
```

<br>

```text
Uvicorn -> ASGI server
FastAPI -> web framework  application
```

<br>
JSON is not an API <br>
JSON is a data format <br>

<br>

/users is not an API <br>
More precisely: **GET /users** is an API operation/endpoint. <br>
The method matters. <br> <br>

The database is not part of FastAPI. <br>
You can use FastAPI without a database <br>

----

# What happens if FastAPI isn't running?

If you stop <br>
```text
Uvicorn
```

and then open:  <br>
```text
http://localhost:8000
```

TH browser won't receive a FastAPI response.  <br>
Because nothing is listening on that port.  <br>

We may see:  <br>

```text
ERR_CONNECTION_REFUSED
```
or a similar browser error.  <br>

---

# Troubleshooting FastAPI

Problem: uvicorn not recognised <br>
You might see: <br>

```text
'uvicorn' is not recognized...
```

 <br>
First check if virtual environment is active: <br>

```text
.\venv\Scripts\Activate.ps1
```

Then: <br>

```text
pip install fastapi uvicorn
```

Check: <br>

```text
uvicorn --version
```

---

# Problem: ModuleNotFoundError: No module named 'fastapi'

Usually means FastAPI isn't installed in the Python environment you're currently using. <br>

Check: <br>

```text
pip show fastapi
```

 <br> <br>
Also: <br>

```text
python -m pip show fastapi
```

 <br> <br>

If missing: <br>

```text
python -m pip install fastapi uvicorn
```

 <br> <br>
Using: <br>

```text
python -m pip
```

can help ensure pip belongs to the Python interpreter you're using.

---

# Problem: Error loading ASGI app

For example: <br>

Error loading ASGI app. Could not import module "main" <br>

Check: <br>

1. Are you in the correct folder? <br>

Run: <br>

```text
dir
```

 <br> 
 
You should see: <br>

```text
main.py
```

 <br> <br>
2. Is the filename actually main.py?

Not: <br>

main.py.txt <br> <br>

3. Is your command correct? <br>

```text
uvicorn main:app --reload
```

 <br> <br>
 
4. Does your code contain: <br>

```text
app = FastAPI()
```

---

# Problem: 404 Not Found

Suppose you defines <br>
@app.get("/about") <br>
but open /about-us <br>
You will get 404. <br>
Because /about-us doesnot match /about <br> <br> 
Routes need to match. <br>

---

#  Problem: port already in use

You may see something indicating: <br>
Address already in use <br> <br>

This usually means another process is already using port 8000 <br> <br>

You can run FastAPI on another port: <br>

```text
uvicorn main:app --reload --port 8001
```

 <br> <br>
Then use: <br>

```text
http://localhost:8001
```

---

# Development vs Production

During development: <br>

```text
uvicorn main:app --reload
```
 is convenient. <br> <br>

Production deployment requires thinking about: <br>

- process management
- multiple workers/instances
- reverse proxy/load balancer
- containers
- environment variables
- logging
- health checks
- monitoring
- resource limits
- TLS/HTTPS
- security

<br>
A command that is convenient for local development is not automatically a complete production deployment strategy.

---

# Why FastAPI is popular

Some important reasons: <br>

- Python

You already know Python.

- Type hints

FastAPI makes heavy use of Python type hints.

- Validation

FastAPI works closely with Pydantic for data validation.

- Automatic documentation

OpenAPI documentation is generated automatically.

- Async support

FastAPI supports asynchronous Python.

- Developer experience

It's relatively concise while still providing powerful features.

---

# Type hints - preview

FastAPI makes extensive use of Python type hints. <br>

Ex:  <br>

```text
def add(a: int, b: int):
  return a + b
```

<br>

The:  <br>

```text
: int
```

is a type hint. <br>

Later we will use type hints in API models and validation. <br>

Ex: <br>

```text
name: str
age: int
```

---

# Sync vs async — understand the idea

You may see: <br>

```text
def home():
```

 <br>
and: <br>

```text
async def home():
```

Today we're using: <br>
```text
def
```

because we're learning fundamentals. <br>

async def is used for asynchronous functions and becomes particularly useful when dealing with I/O-bound operations. <br> <br>

For example: <br>

```text
Waiting for database
Waiting for another API
Waiting for network
```

---

# Why not make everything async?

Because: <br>

```text
async ≠ automatically faster
```

Async programming is useful for particular workloads and requires understanding how asynchronous execution works. <br>

For now: <br>

```text
def
```

is completely fine for our basic endpoints. <br>

---

# FastAPI and your existing URL Shortener

Your current project is: <br>

```text
Python
   ↓
PostgreSQL
   ↓
CLI
```

<br> <br>
Eventually we're going to transform the application into something like: <br>

```text
Frontend / Browser
       ↓
HTTP
       ↓
FastAPI
       ↓
Python logic
       ↓
PostgreSQL
```

<br> <br>
Then eventually: <br>

```text
POST /urls
       ↓
Create short code
       ↓
Store in PostgreSQL
       ↓
Return short URL
```

<br> 
and: <br>

```text
GET /abc123
       ↓
Find original URL
       ↓
Record click
       ↓
Redirect
```

---








