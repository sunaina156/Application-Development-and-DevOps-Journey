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














