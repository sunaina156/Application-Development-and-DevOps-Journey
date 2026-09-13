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



