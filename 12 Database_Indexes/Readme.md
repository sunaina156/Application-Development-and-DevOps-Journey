# What Is a Database Index?

A database index is a data structure that helps the database find rows faster. <br>

Think about a physical book. <br>

Suppose you want to find information about:
 <br>
Kubernetes
 <br>
You could read every page from beginning to end.
 <br>
That works, but it's slow.
 <br> <br>
Instead, you look at the index at the back of the book, find "Kubernetes", and it tells you where to go.
 <br>
A database index works similarly.
 <br>
Without Index:
 <br>
 ```text
Database
   ↓
Check row 1
Check row 2
Check row 3
Check row 4
...
Check row 1,000,000
```
 <br>
With an index:
 <br>
 ```text
Query
  ↓
Index
  ↓
Find matching location
  ↓
Retrieve row
```
 <br>
So:
 <br>
An index is used to make data retrieval faster.
 <br>

---

# Simple Example

Suppose we have: <br>

users <br>

with 1 million users:  <br>
```text
id | name     | email
---+----------+---------------------
1  | Sunaina  | sunaina@gmail.com
2  | Rahul    | rahul@gmail.com
3  | Aman     | aman@gmail.com
...
1000000 | ...
```

Now we execute:
 <br>
 ```text
SELECT *
FROM users
WHERE email = 'sunaina@gmail.com';
```
 <br>
If email doesn't have an index, the database may need to examine many rows to find the matching email.
 <br>
If we create:
 <br>
 ```text
CREATE INDEX idx_users_email
ON users(email);
```
the database can use the index to locate matching rows much more efficiently.
 <br>

 ---

 # Why Do We Need Indexes?

Imagine: <br>

10 rows <br>

Searching without an index is usually not a big problem.
 <br> <br>
But imagine: <br>

10 million rows <br>

or: <br>

500 million rows
 <br> <br>
Repeatedly scanning a huge table can become expensive.
 <br>
Indexes can dramatically improve queries that frequently search, sort, or join using indexed columns. <br>

---

# Important Trade-Off

Indexes are not free.

This is one of the most important concepts.

An index provides:

Faster reads

but generally costs:

More storage
More work during INSERT
More work during UPDATE
More work during DELETE

Why?

Because when data changes, the corresponding index also needs to be maintained.

Think:

INSERT row
   ↓
Update table
   +
Update indexes

Therefore:

Don't create an index on every column just because indexes make queries faster.

---

# How Does an Index Work?

The exact implementation depends on the database and index type. <br>

In PostgreSQL, the default index type is generally B-tree. <br>

A B-tree keeps indexed values organized in a structure that allows efficient searching.
 <br>
Conceptually: <br>
```text

                 50
               /    \
             /        \
           25          75
          /  \        /  \
        10   40      60   90
```

If you're looking for: <br>

60 <br>

you don't necessarily inspect every value.
 <br>
You follow the appropriate path.
 <br>
 ```text
50
 ↓
75
 ↓
60
```
This is why indexes can make lookups much faster than scanning the whole table. <br>

You don't need to memorize the internal implementation yet. The important idea is:
 <br>
The index organizes information so the database can locate relevant rows efficiently.
 <br>

 ---
 
# Creating an Index

Basic syntax: <br>
```text
CREATE INDEX index_name
ON table_name(column_name);
```
<br>
Example:
<br>
```text
CREATE INDEX idx_users_email
ON users(email);
```

Let's break it down: <br>
```text
CREATE INDEX
     ↓
idx_users_email
     ↓
ON users
     ↓
(email)
```

---

# Naming Indexes

A common naming convention is: <br>
```text
idx_<table>_<column>  
```

Examples: <br>
```text
idx_users_email
idx_users_name
idx_urls_short_code
idx_urls_user_id
idx_clicks_url_id
```

This makes indexes easier to identify. <br>

---

# Finding Data With an Index

Suppose: <br>
```text
CREATE INDEX idx_users_email
ON users(email);
```
Then: <br>
```text
SELECT *
FROM users
WHERE email = 'sunaina@gmail.com';
```
may use that index.
 <br>
But remember: <br>

Creating an index does not guarantee that PostgreSQL will use it for every query. <br>

PostgreSQL's query planner decides whether using the index is actually cheaper than another execution strategy.
 <br>

 ---

 # Query Planner

This is an important concept for becoming a strong developer. <br>

When you execute: <br>
```text
SELECT *
FROM users
WHERE email = 'sunaina@gmail.com';
```
 <br>
PostgreSQL doesn't blindly say: <br>

"There is an index, so I'll use it." <br> <br>

Instead, the query planner evaluates possible execution plans.
 <br>
Conceptually:
 <br>
 ```text
SQL Query
   ↓
Query Planner
   ↓
Choose execution plan
   ↓
Execute
```
 <br>
Possible strategies include:
 <br>
 ```text
Sequential Scan
Index Scan
Bitmap Index Scan
...
```


## Sequential Scan

A sequential scan means PostgreSQL reads the table sequentially. <br>

Conceptually: <br>
```text
Row 1
 ↓
Row 2
 ↓
Row 3
 ↓
Row 4
 ↓
...
```

 <br>
This is often called:

Seq Scan
 <br> <br>
A sequential scan is not automatically bad.
 <br>
If a table contains only 20 rows, using an index might provide little benefit. <br>

If PostgreSQL needs a large percentage of the table, a sequential scan can sometimes be faster.   
 <br>

  <br>

## Index Scan

An index scan uses the index to find relevant rows. <br>

Conceptually: <br>
```text
Query
 ↓
Index
 ↓
Find matching row locations
 ↓
Table
 ↓
Retrieve rows
```

For selective queries on large tables, this can be very efficient. <br>

---

# EXPLAIN

One of the most important tools for understanding indexes is: <br>

EXPLAIN <br>

Example: <br>
```text
EXPLAIN
SELECT *
FROM users
WHERE email = 'sunaina@gmail.com';
```

PostgreSQL will show the execution plan it expects to use. <br>

## EXPLAIN ANALYZE

Even more useful: <br>

```text
EXPLAIN ANALYZE
SELECT *
FROM users
WHERE email = 'sunaina@gmail.com';
```

<br>

```text
EXPLAIN shows the planned execution. 

EXPLAIN ANALYZE actually executes the query and reports what happened. 
```

<br>
For example, you might see something conceptually like: <br>

Index Scan using idx_users_email on users <br>

That tells you PostgreSQL used the index. <br>

---

# Before and After Index

Suppose: <br>
```text
SELECT *
FROM urls
WHERE short_code = 'abc123';
```

Without index: <br>
```text
Query
 ↓
Sequential scan
 ↓
Many rows examined
```

<br>

Create: <br>
```text
CREATE INDEX idx_urls_short_code
ON urls(short_code);
```

<br>

Then PostgreSQL may use:
<br>

```text
Query
 ↓
Index
 ↓
Find abc123
 ↓
Retrieve URL
```

This is particularly relevant to your URL shortener.
<br>

---

# URL Shortener Example

Your URL shortener will eventually have something like: <br>

```text
urls
--------------------------------
id
short_code
original_url
user_id
created_at
```

<br>
When somebody visits: <br>

https://example.com/abc123 <br>

your backend needs to find: <br>
```text
SELECT original_url
FROM urls
WHERE short_code = 'abc123';
```

This query will potentially execute very frequently. <br>

Therefore: <br>

```text
CREATE INDEX idx_urls_short_code
ON urls(short_code);
```

 <br>
is a very reasonable design. <br>
 <br> <br>
In fact, if short_code must be unique, you can use a UNIQUE constraint, which also creates a unique index in PostgreSQL. <br>

For example: <br>
```text
CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    short_code VARCHAR(20) UNIQUE,
    original_url TEXT NOT NULL
);
```
 <br>
The UNIQUE constraint is enforcing uniqueness, while the underlying unique index also supports efficient lookup. <br>

---

# Primary Keys and Indexes

When you define: <br>
```text
id INTEGER PRIMARY KEY
```
 <br>
PostgreSQL automatically creates a unique index to enforce the primary key. <br>

So you generally don't need to manually create another index on the primary key. <br>


Conceptually:  <br>
```text
PRIMARY KEY
     ↓
Unique index
```

---

# UNIQUE Constraints and Indexes

Consider: <br>
```text
email VARCHAR(255) UNIQUE
```
PostgreSQL creates a unique index to enforce the uniqueness requirement. <br>

Therefore: <br>

```text
UNIQUE
  ↓
No duplicate values
  +
Unique index
```
 <br>
Don't create another normal index on exactly the same column unless you have a specific reason.

---

# Indexing Foreign Keys

Consider our URL shortener: <br>
```text
users
   1
   |
   *
urls
```

 <br>
The urls table has: <br>
```text
user_id
```
 <br>
which is a foreign key. <br>

A useful index can be: <br>
```text
CREATE INDEX idx_urls_user_id
ON urls(user_id);
```

 <br>
Why? <br>

Because we may frequently ask: <br>
```text
SELECT *
FROM urls
WHERE user_id = 1;
```
 <br>
This means: <br>

Find all URLs created by user 1. <br>

An index on user_id can make such queries much more efficient, especially when the urls table becomes large. <br>

Important: PostgreSQL does not automatically create an index on the referencing side of a foreign key merely because you declared the foreign key. <br>

---

# 

