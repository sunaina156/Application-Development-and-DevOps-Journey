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

# Required Query Parameters

If you write: <br>
@app.get("/products") <br>
def get_products(limit: int):  <br> <br>

then: <br>
/products?limit=10 works. <br> <br>
But: /products does not provide limit. <br>
FastAPI will return a validation error because limit is required. <br>

# Optional Query Parameters

Often query parameters should be optional. <br>

Ex: <br>
GET /products  <br>
should return products. <br> <br>

But: <br>
GET /products?limit=10 <br>
should return only 10. <br> <br>

We can use **None**: <br>

```text
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products(limit: int | None = None):
  return {
    "limit": limit
  }
```

 <br>
Now: /products <br>
returns: <br>

```text
{
  "limit": null
}
```

And: <br>
/products?limit=10 <br>
returns: <br>

```text
{
  "limit": 10
}
```

# Why None?

This: <br>
limit: int | None = None <br> 
means: <br>
limit can be int or None <br> <br>

And: <br>
= None <br>
means it is optional. <br> <br>

So: /products <br>
is valid <br> <br>

# Multiple query Parameters

Ex: <br>
GET /products?category=laptop&limit=10 <br> <br>

FastAPI: <br>

```text
@app.get("/products")
def get_products(
    category: str | None = None,
    limit: int | None = None
  ):
    return {
      "category": catgory,
      "limit": limit
    }
``` 

Response: <br>

```text
{
  "category": "laptop",
  "limit": 10
}
```

 <br>
The query parameters are separated by: <br>
& <br> <br>

Ex: <br>
?category=laptop&limit=10&sort=price <br> <br>

# Query Parameter Order

The order generally doesn't matter. <br>

/products?category=laptop&limit=10 <br>
and: <br>
/products?limit=10&category=laptop <br> <br>

are equivalent. <br>
FastAPI identifies parameters by their names. <br> <br>

# Query Parameters with Boolean Values

We cal also use: <br>

```text
@app.get("/products")
def get_products(available: bool = True):
  return {
    "available": available
  }
```

Ex: <br>
/products?available=true <br> <br>

or: <br>
/products?available=false <br> <br>
FastAPI converts the value according to the declared type. <br>

# Query Parameters with Strings

Ex: <br>

```text
@app.get("/search")
def search(q: str):
  return {
    "search_query": q
  }
```

Request: <br>
/search?q=python <br> <br>

Response: <br>
```text
{
  "search_query": "python"
}
```

This is common for search APIs

# Real-world Query Parameters

In an online shopping API. <br>

We might have: <br>
GET /products <br>
All products <br> <br>

Then: <br>
GET /products?category=laptop <br>
Products in the laptop category. <br> <br>

Then:  <br>
GET /products?category=laptop&limit=20 <br>
Laptop products, maximum 20 <br> <br>

Then: <br>
GET /products?category=laptop&limit=20&sort=price <br>
Laptop products, maximum 20, sorted by price. <br> <br>

We are still talking about the /products collection. <br>
The query parameters simply change how we retrieve it. <br> <br>


---

# Path + Query Parameters Together

Ex: <br>
GET /users/10/orders?limit=5 <br> <br>

Here: <br>

```text
/users/10/orders
      ↑
   path parameter

?limit=5
 ↑
query parameter
```

<br>

FastAPI: <br>

```text
@app.get("/users/{user_id}/orders")
def get_user_orders(
    user_id: int,
    limit: int | None = None
  ):
    return {
      "user_id": user_id,
      "limit": limit
    }
```

<br> <br>

Request: <br>
/users/10/orders?limit=5 <br> <br>

Response: <br>

```text
{
  "user_id": 10,
  "limit": 5
}
```

---

# Path Parameters and Resource Identity

Consider: <br>
GET /users/10 <br> <br>

The 10 identifies a particular resource. <br>
Therefore, /users/{user_id} can be thought of as /users/{resource_identifier} <br>
whereas, /users?limit=10 still refers to the users collection. <br> <br>

# Query Parameter Validation Preview
We can also impose rules. <br>

Ex: <br>
limit must be between 1 and 100 <br>
FastAPI supportes this through Query. <br> <br>

Ex: <br>

```text
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products(
  limit: int = Query(default=10, ge=1, le=100)
):
  return {
    "limit": limit
  }
```

 <br>
Now: <br>
/products?limit=50 works <br>
But, /products?limit=0 fails. <br>

 <br> <br>

# Path Parameter Validation Preview

You can also use Path. <br>

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
Now, /users/10 is valid. <br>
But, /users/0 is invalid bcoz user_id >= 1

 <br> <br>

# Important Route Ordering Problem

Suppose we write: <br>

```text
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/users/me")
def get_current_user():
    return {"user": "current user"}
```

<br> 

You might expect: <br>
/users/me to call get_current_user() <br>
But /users/{user_id} can also look like user_id = "me" <br>
Route ordering can therefore matter. <br>
 <br>

A safe approach is to declare the fixed route before the dynamic route.: <br>

```text
@app.get("/users/me")
def get_current_user():
    return {"user": "current user"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

<br>
Now /users/me matches the specific route first. 
<br>

# URL Encoding
Query parameters can contain characters that have special meanings in URLs. <br>

Ex: <br>
/search?q=hello world <br>
Browser/clients encode spaces appropriately. <br> <br>

You will often see: <br>
hello%20world <br> <br>

This is called URL encoding or percent encoding. <br>
You don't normally need to manually encode simple values when using Swagger, Postman, frontend code or HTTP libraries bcoz the client handles it. <br> <br>

# Query String Is Not Request Body

**Query parameter** <br>
GET /products?limit=10 <br>
Information is in the URL. <br> <br>

**Request body** <br>

```text
POST /products
Content-Type: application/json

{
  "name": "Laptop",
  "price": 50000
}
```

 <br>
Information is in the HTTP body. <br>

# Why GET Usually Uses Query Parameters

Suppose you are searching products. <br>
You could theoretically send: <br>
GET /products <br>
with a body. <br> <br>

But the normal API design is: <br>
GET /products?category=laptop&limit=20 <br> <br>

GET requests commony use: <br>
- path parameters
- query parameters

 <br>

POST/PUT/PATCH commonly use: <br>
- path parameters
- query parameters
- request body

depending on the API design. <br>

---



























