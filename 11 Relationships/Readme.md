# Why Do We Need Relationships?

Imagine we create a users table: <br>
```text
users
--------------------------------
id    name       email
--------------------------------
1     Sunaina    sunaina@gmail.com
2     Rahul      rahul@gmail.com
3     Aman       aman@gmail.com
```
<br>

And a urls table: <br>

```text

urls
---------------------------------------------
id    short_code    original_url       user_id
---------------------------------------------
1     abc123        https://google.com      1
2     xyz789        https://github.com      1
3     pqr456        https://youtube.com     2
```

Here: <br>

User 1 created URL abc123 <br>
User 1 created URL xyz789 <br>
User 2 created URL pqr456 <br>

The user_id in the urls table connects each URL to a user. <br>

This is called a relationship between tables. <br>

```text
users
  |
  | user_id
  ↓
urls

```

---

# What Is a Database Relationship?

A database relationship defines how records in one table are associated with records in another table. <br>

For example:  <br>

User → URL  <br>
 
A user can create URLs.  <br>
 <br>
Customer → Orders  <br> 

A customer can place orders.
 <br> <br>
Student → Course <br>

A student can enroll in courses. <br> <br>

Relationships allow us to store related information in separate tables while still being able to connect that information.  <br>

---

# Why Not Put Everything in One Table?

Suppose we did this: <br>
```text
id | user_name | email | url1 | url2 | url3
```

This creates several problems.
 <br>
- Problem 1 — Repeated data
 <br>
The user's name and email would be repeated for every URL.
 <br>
- Problem 2 — Difficult to maintain
 <br>
If the email changes, we'd need to update it in multiple places.
 <br>
- Problem 3 — Limited URLs
 <br>
What happens when the user creates URL number 4?
 <br>
We would have to add another column.
 <br>
- Problem 4 — Poor database design <br>

A table should generally represent one logical entity.
 <br> <br>
Instead:
 <br>
 ```text
users
urls
```

and connect them through relationships.
 <br>

 ---

# Primary Key

A primary key uniquely identifies each record in a table. <br>

Example: <br>
```text
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);
```
Here:  <br>

id is the primary key. <br>

Example:  <br>
```text
id | name
---+--------
1  | Sunaina
2  | Rahul
3  | Aman
```

Each id is unique. <br>

**Primary key properties**  <br>

A primary key:
 <br>
- uniquely identifies a row
- cannot contain NULL
- should not have duplicate values
- normally remains stable
- can be referenced by another table

---

# Foreign Key
 
A foreign key is a column that references a key in another table. <br>

Example: <br>
```text
CREATE TABLE urls (
    id INTEGER PRIMARY KEY,
    short_code VARCHAR(10),
    original_url TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

Here: <br>
```text
users.id
    ↑
    |
urls.user_id
```

urls.user_id is the foreign key. <br>

It references: users.id <br>

---

# Primary Key vs Foreign Key

Primary Key | 	Foreign Key
----------------------------------------------------------------
Uniquely identifies a row	| Connects to a row in another table
Must be unique	 | Doesn't necessarily need to be unique
Cannot be NULL	| Can potentially be NULL, depending on constraints
Defined in its own table	| References another table
Example: users.id	| Example: urls.user_id

Important:

users.id

might contain:

1
2
3

while:

urls.user_id

can contain:

1
1
1
2
2
3

That's completely valid.

Why?

Because many URLs can belong to the same user.

And that brings us to relationship types.




















 
