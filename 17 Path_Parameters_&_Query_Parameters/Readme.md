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


