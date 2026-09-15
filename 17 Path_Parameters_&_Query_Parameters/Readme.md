# First understand the problem

Imagine you have 1000 users. <br>
 <br>

You have: <br>
GET /users <br>
 <br>

This could return all users. <br>
But what if you want only user 25? <br>
 <br>
You could theoretically create: <br>
GET /get-user-25 <br>
But this is poor API design. <br>
 <br>

Instead: <br>
**GET /users/25** <br>
Here: <br>

```text
/users/25
           ↑
   dynamic value
```

25 is a path parameter.

---

# What is a Path Parameter?

A path parameter is a value placed directly inside the URL path. <br>

Ex: <br>
GET /users/25 <br>
 <br>
Here: <br>
/users/{user_id} <br>
 <br>
The {user_id} means: <br>
This part of the URL will be provided dynamically by the client. <br>

---

# Basic FastAPI Path Parameter

Create: <br>

```text
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }
```

<br>

Run: <br>

```text
uvicorn main:app --reload
```

Then open:  <br>

```text
http://localhost:8000/users/10
```

Response:  <br>

```text
{
  "user_id": 10
}
```

Try: <br>

```text
http://localhost:8000/users/25
```

Response: <br>

```text
{
  "user_id": 25
}
```

<br> <br>

## What exactly happens internally?

Suppose the client sends: <br>
GET /users/25 <br> <br>

FastAPI sees this route: <br>
@app.get("/users/{route_id}") <br> <br>

It recognizes: <br>
{user_id} = 25 <br> <br>

Then FastAPI calls: <br>
get_user(user_id=25) <br> <br>

Bcoz you wrote: <br>
user_id: int <br>
FastAPI converts the value to an integer. <br> <br>

The flow is: <br>

```text
Client
  ↓
GET /users/25
  ↓
FastAPI route matching
  ↓
/users/{user_id}
  ↓
user_id = 25
  ↓
Python function
  ↓
get_user(25)
  ↓
JSON response
```

## Why do we write user_id: int?

Consider: <br>
def get_user(user_id: int):
The : int tells FastAPI, I expect this value to be an integer. <br> <br>

So, /users/25 is valid. <br>
But, /users/abc is not valid for an integer parameter. <br> 
FastAPI will return a validation error. <br>


---

# Path Parameters are required

Suppose you have: <br>

```text
@app.get("/users/{user_id}")
def get_user(user_id: int):
  ...
```

The URL must contain: <br>
/users/25 <br> <br>

You cannot call /users/ <br>
and expect user_id to be available. <br> <br>

Because the parameter is part of the route itself. <br>

```text
/users/{user_id}
            ↑
       required
```

## Multiple Path Parameters

You can have more than one. <br> <br>

Ex: <br>
GET /users/10/orders/500 <br> <br>

FastAPI: <br>

```text
@app.get("/users/{user_id}/orders/{order_id}")
def get_order(user_id: int, order_id: int):
  return {
    "user_id": user_id,
    "order_id": order_id
  }
```

Request: <br>
/users/10/orders/500 <br> <br>

Response: <br>

```text
{
  "user_id": 10,
  "order_id": 500
}
```

 <br> <br>

FastAPI extracts: <br>
user_id = 10
order_id = 500

## Real-world meaning

Let an e-commerce application. <br>

GET /products/101 <br>
means Give me product 101 <br> <br>

or: <br>
GET /users/15 <br>
means give me user 15 <br> <br>

or: <br>
GET /orders/5001 <br>
means give me order 5001 <br> <br>

or: <br>
GET /users/15/orders/5001 <br>
Give me order 5001 belonging to user 15 <br> <br>

Path parameters usually identify which specific resource you are talking about. <br>

---

# Query Parameters

Ex: <br>
GET /products?limit=10 <br>
Here, /products is the path <br>
and limit=10 is a query parameter. <br> <br>

The ? separates the path from the query string.

# Basic Query Parameter

FastAPI makes query parameters very easy. <br>

```text
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products(limit: int):
  return {
    "limit": limit
  }
```

Request: <br>
http://localhost:8000/products?limit=10 <br> <br>

Response: <br>

```text
{
  "limit": 10
}
```

 <br> <br>

FastAPI understands that: <br>
?limit=10 <br> 
should be passed to: <br>
limit  <br> <br>


## How FastAPI knows it is a Query Parameter

```text
@app.get("/products")
def get_products(limit: int):
```

<br> <br>

There is no: <br>
{limit} <br>
inside the path. <br>
Therefore FastAPI treats limit as a query parameter. <br> <br>

**Path parameter** <br>
@app.get("/products/{product_id}") <br>
def get_product(product_id: int):  <br> <br>

URL: <br>
/products/10 <br> <br>

**Query parameter** <br>
@app.get("/products") <br>
def get_products(limit: int):  <br> <br>

URL: <br>
/products?limit=10 <br> <br>

# The Most Important Difference

Remember this: <br>

```text
PATH PARAMETER
/users/25
       ↑
 identifies a specific resource
```

 <br>

```text
QUERY PARAMETER
/users?limit=25
       ↑
 modifies/filter/sorts the request
```

A useful rule: <br>

Path parameter = Which resource? <br>

Query parameter = How do I want the resource/data? <br>

---

























