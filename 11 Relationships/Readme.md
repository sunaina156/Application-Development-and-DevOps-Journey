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

```text
Primary Key               | 	Foreign Key
--------------------------|--------------------------------------
Uniquely identifies a row	| Connects to a row in another table
Must be unique	          | Doesn't necessarily need to be unique
Cannot be NULL	          | Can potentially be NULL, depending on constraints
Defined in its own table	| References another table
Example: users.id	        | Example: urls.user_id
```

Important: <br>

users.id <br>

might contain: <br>
```text
1 
2 
3 
 ```
 <br>
while: <br>

urls.user_id  <br>

can contain:  <br>
```text
1
1
1
2
2
3
```

That's completely valid. <br>

Why? <br>

Because many URLs can belong to the same user. <br>

And that brings us to relationship types. <br>

---

# Types of Database Relationships

There are three major relationship types: <br>

1. One-to-One
2. 2. One-to-Many
3. Many-to-Many

## One-to-One Relationship

A one-to-one (1:1) relationship means: <br>

One record in Table A is associated with one record in Table B. <br>

And vice versa. <br>

Example:  <br>
```text
Person → Passport
```
One person has one passport.  <br>

```text
Person
------
id
name
```

 <br>
 ```text
Passport
--------
id
passport_number
person_id
```

Conceptually: <br>
```text
Person 1 ─────── 1 Passport
```

 <br>
Another example:
 <br>
 ```text
User → UserProfile
```
A user may have exactly one profile.
 <br>
 
## One-to-Many Relationship

This is one of the most common relationships in real applications. <br>

A one-to-many relationship means: <br>

One record in Table A can be associated with many records in Table B. <br>

But each record in B belongs to one record in A. <br>

Example:  <br>
```text
User → URLs
```
 <br>
One user can create many URLs. <br>
```text
User 1
  |
  ├── URL 1
  ├── URL 2
  ├── URL 3
  └── URL 4
```

 <br>
 
Database:  <br>

```text
users
----------------
id | name
----------------
1  | Sunaina
2  | Rahul
```

 <br>
 ```text
urls
--------------------------------
id | short_code | user_id
--------------------------------
1  | abc123     | 1
2  | xyz789     | 1
3  | pqr456     | 2
4  | mno111     | 1
```

Here:  <br>
```text
Sunaina
   |
   ├── abc123
   ├── xyz789
   └── mno111

Rahul
   |
   └── pqr456
```

So: <br>

```text
users 1 ─────────── * urls
```

The * means many.  <br>

Where is the foreign key?
 <br>
The foreign key goes on the many side. <br>
```text
users
  |
  | 1
  |
  ↓
urls
  *
```

Therefore: <br>

urls.user_id <br>

references: <br>

users.id <br>

This is a rule worth remembering: <br>

In a one-to-many relationship, the foreign key is normally stored in the "many" table. <br>

## Many-to-Many Relationship

A many-to-many relationship means: <br>

Many records in Table A can be associated with many records in Table B. <br>

Example: <br>
```text
Students ↔ Courses
```

 <br>
A student can take multiple courses. <br>

A course can have multiple students. <br>

```text
Student A ── Course 1
     |    └─ Course 2
     |
Student B ── Course 1
          └─ Course 3
```
 <br>
So: <br>
```text
Students * ───────── * Courses
```
 <br>
But relational databases generally don't represent this by directly putting multiple IDs in one column. <br>

Instead, we create a third table.
 <br>
 
---

# Junction Table

A junction table (also called an associative or bridge table) converts a many-to-many relationship into two one-to-many relationships. <br>

Example: <br>
```text
students
---------
id
name

courses
---------
id
name
```
 <br>
Then: <br>

```text
student_courses
---------------
student_id
course_id
```

 <br>
 
Example: <br>

```text
students
----------------
id | name
----------------
1  | Sunaina
2  | Rahul

courses
----------------
id | name
----------------
1  | Python
2  | AWS
3  | Kubernetes

student_courses
-----------------------
student_id | course_id
-----------------------
1          | 1
1          | 2
2          | 1
2          | 3
```

Meaning: <br>
```text
Sunaina → Python
Sunaina → AWS

Rahul → Python
Rahul → Kubernetes
```

The relationship becomes: <br>
```text
students
   1
   |
   |
   *
student_courses
   *
   |
   |
   1
courses
```

---

# URL Shortener Example

Let's apply relationships to the project you're going to build. <br>

We could have:  <br>
```text
users
urls
clicks
```

Users  <br>
```text
users
---------------------
id
name
email
created_at
```

 <br>
 
URLs  <br>
```text
urls
---------------------
id
short_code
original_url
user_id
created_at
```

Relationship: <br>
```text
users 1 ───────── * urls
```
Meaning: <br>

One user can create many shortened URLs. <br>

---

# URL → Clicks

Suppose we also track every click. <br>
```text
clicks
---------------------
id
url_id
ip_address
clicked_at
```

Relationship:
 <br>
 ```text
urls 1 ───────── * clicks
```
One shortened URL can have many clicks. <br>

So our overall design becomes: <br>
```text
users
   |
   | 1
   |
   | *
  urls
   |
   | 1
   |
   | *
 clicks
```

This is already a realistic relational database design.

---

# Foreign Key Constraints

We can enforce relationships using foreign keys. <br>
```text
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);
```

 <br>
Then:
 <br>

 ```text
CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    short_code VARCHAR(10) UNIQUE,
    original_url TEXT NOT NULL,
    user_id INTEGER NOT NULL,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
);
```

Now PostgreSQL knows: <br>

urls.user_id → users.id  <br>

---

# Referential Integrity

Referential integrity means the relationships between tables remain valid. <br>

Suppose: <br>
```text
users

id
---
1
2
```

And: <br>

```text
urls

user_id
-------
1
2
```

If we try: <br>
```text
INSERT INTO urls (..., user_id)
VALUES (..., 99);
```
 <br>
but user 99 doesn't exist, the database should reject it.
 <br>
Why? <br>

Because: <br>

user_id = 99 <br>

would point to a nonexistent user. <br>

The foreign key prevents this. <br>

That's one major reason relationships are enforced at the database level.

---

# What Happens When a Parent Is Deleted?

Suppose: <br>
```text
users
  ↓
urls
```

User 1 has three URLs. <br>

What should happen if user 1 is deleted? <br>

There are different strategies. <br>

**RESTRICT**  <br>

Don't allow deletion if related records exist. <br>

**ON DELETE RESTRICT**
 <br>
Meaning: <br>
```text
Delete User
     ↓
Related URLs exist
     ↓
Don't allow deletion 
```

---

# CASCADE

With: <br>

ON DELETE CASCADE <br>

deleting the parent automatically deletes related records. <br>
```text
Delete User
     ↓
Delete their URLs
```

 <br>
Example: <br>
```text
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE CASCADE
```

Be careful with cascading deletes.
 <br>
A single deletion can remove many related records.
 <br>
 
---

# SET NULL

Another option: <br>

ON DELETE SET NULL <br>

If the parent is deleted, the foreign key becomes NULL. <br>

Example: <br>
```text
User
  ↓
URL
```

 <br>
 
Delete the user: <br>
```text
user_id
   ↓
NULL
```

But the column must allow NULL. <br>

So this would conflict: <br>

user_id INTEGER NOT NULL <br>

because NULL would not be allowed. <br>

---

# ON DELETE Options

The major ones you should know: <br>

```text
Option	| Meaning
-----------------------------------------------------
CASCADE	     | Delete related rows
RESTRICT	   | Prevent parent deletion
SET NULL	   | Set foreign key to NULL
SET DEFAULT	 | Set foreign key to its default
NO ACTION	   | PostgreSQL's default behavior; checks referential integrity
```
For interviews, definitely understand: <br>
CASCADE vs RESTRICT vs SET NULL <br>

---

# 





















 
