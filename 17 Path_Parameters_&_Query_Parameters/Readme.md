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























