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

# Single-Column Index

An index can be created on one column: <br>
```text
CREATE INDEX idx_users_name
ON users(name);
```

This is a: <br>

Single-column index. <br>

---

# Composite Index

You can also create an index on multiple columns. <br>

```text
CREATE INDEX idx_users_city_age
ON users(city, age);
```

This is called a: <br>

Composite index <br>

or: <br>

Multi-column index. <br>

It can help queries that filter or sort using those columns in useful ways.
<br>

---

# The Order of Columns Matters

Suppose: <br>
```text
CREATE INDEX idx_users_city_age
ON users(city, age);
```

The index is ordered conceptually by: <br>

```text
city
  ↓
age
```
So a query like: <br>

```text
SELECT *
FROM users
WHERE city = 'Bhopal'
AND age = 21;
```

can potentially benefit strongly. <br>

A query using: <br>

```text
WHERE city = 'Bhopal'
```

can also potentially benefit. <br>

But a query using only: <br>

```text
WHERE age = 21;
```

may not benefit nearly as much from this particular index. <br>

This is related to the leftmost-prefix principle for B-tree composite indexes. <br>

---

# Example of Composite Index

Suppose you frequently run: <br>

```text
SELECT *
FROM urls
WHERE user_id = 10
AND created_at >= '2026-09-01';
```

You might consider: <br>

```text
CREATE INDEX idx_urls_user_created
ON urls(user_id, created_at);
```

Now the database has an index organized around: <br>

```text
user_id
    ↓
created_at
```

This can be useful for queries that commonly use that access pattern. <br>

But don't blindly create composite indexes. Their usefulness depends on your actual queries and data distribution. <br>

---

# Index + ORDER BY

Indexes can also help with sorting in appropriate situations. <br>

Suppose: <br>
```text
SELECT *
FROM users
ORDER BY created_at DESC;
```

You might create: <br>

```text
CREATE INDEX idx_users_created_at
ON users(created_at);
```

Depending on the query and planner, PostgreSQL may use the index to help produce the required ordering. <br>

This becomes especially useful when combined with: <br>

```text
LIMIT
```

For example: <br>

```text
SELECT *
FROM users
ORDER BY created_at DESC
LIMIT 10;
```

---

# Unique Index

You can explicitly create a unique index: <br>

```text
CREATE UNIQUE INDEX idx_users_email
ON users(email);
```

Now duplicate emails aren't allowed. <br>

For example: <br>

```text
sunaina@gmail.com
rahul@gmail.com
```

are valid. <br>

But: <br>

```text
sunaina@gmail.com
sunaina@gmail.com
```

would violate the unique index. <br>

However, when the business rule is uniqueness, prefer expressing that rule as a UNIQUE constraint when appropriate: <br>

```text
email VARCHAR(255) UNIQUE
```

rather than thinking of a unique index only as a performance feature. <br>

---

# Partial Index

PostgreSQL has a powerful feature called a partial index. <br>

It indexes only rows satisfying a condition. <br>

Example: <br>

```text
CREATE INDEX idx_active_users
ON users(email)
WHERE is_active = TRUE;
```

Instead of indexing every user, it indexes only active users. <br>

Then: <br>

```text
SELECT *
FROM users
WHERE is_active = TRUE
AND email = 'sunaina@gmail.com';
```

can potentially benefit from the partial index. <br>

Partial indexes can be very useful when the condition matches common query patterns  <br>

---

# Index on Expressions

PostgreSQL can also index an expression. <br>

Example: <br>

```text
CREATE INDEX idx_users_lower_email
ON users(LOWER(email));
```

Then: <br>

```text
SELECT *
FROM users
WHERE LOWER(email) = 'sunaina@gmail.com';
```

can potentially use that expression index. <br>

This is useful when applications need case-insensitive searches. <br>

---

# What Columns Should You Index?

Good candidates often include columns frequently used in: <br>

```text
WHERE
JOIN
ORDER BY
```

and sometimes: <br>

```text
GROUP BY
```

depending on the query. <br>

Common examples: <br>

```text
users.email
users.username
urls.short_code
urls.user_id
clicks.url_id
clicks.clicked_at
```

But whether an index is beneficial depends on: <br>

```text
table size
query frequency
selectivity
data distribution
write frequency
query shape
```

---

# Selectivity

Selectivity describes how effectively a condition narrows down rows. <br>

Suppose: <br>

1,000,000 users  <br>

and: <br>

gender = 'Male' <br>

returns: <br>

500,000 rows <br>

That's not very selective. <br>

But:  <br>

email = 'sunaina@gmail.com' <br>

might return: <br>

1 row <br>

That's highly selective <br>.

Indexes are often particularly valuable for selective lookups. <br>

---

# Why Indexes Can Slow Down Writes

Suppose you have: <br>

```text
Table
+
5 indexes
```

When inserting a row: <br>

```text
INSERT
  ↓
Update table
  ↓
Update index 1
  ↓
Update index 2
  ↓
Update index 3
  ↓
Update index 4
  ↓
Update index 5
```

Therefore: <br>

More indexes can mean more write overhead. <br>

This is why database design is always a trade-off between: <br>

```text
Read performance
        vs
Write performance
        vs
Storage
```

---

# Too Many Indexes

Creating: <br>
```text
index on name
index on email
index on age
index on city
index on phone
index on country
index on created_at
...
```

just because you can is bad practice. <br>

Some indexes may:  <br>

```text
never be used
consume storage
slow down writes
increase maintenance overhead
```

Good database design asks: <br>

Which queries actually need to be fast? <br>

Then indexes are designed around those queries. <br>

---

# Index Doesn't Always Mean Faster

This is an important interview point.
 <br>
Suppose a table has: <br>

100 rows <br>

Using an index might not provide meaningful benefit. <br>

Or suppose: <br>

```text
SELECT *
FROM users;
```

You are requesting every row. <br>

An index doesn't magically make retrieving the entire table faster. <br>

The query planner may choose a sequential scan. <br>

So: <br>
 <br>
An index is a tool for efficient access, not a guarantee of faster execution. <br>

---

# How to Delete an Index

Use: <br>

```text
DROP INDEX index_name;
```

Example: <br>

```text
DROP INDEX idx_users_email; 
```

Be careful when dropping indexes in production because queries may become slower. <br>

---

# Indexes and Disk Space

Indexes consume storage. <br>

Conceptually: <br>

```text
Database
├── Tables
│
└── Indexes
```

A large table with several large indexes can consume substantial disk space. <br>

Therefore, database administrators and developers need to consider index size as part of database capacity planning. <br>

---

# Indexes in Your URL Shortener

Let's design some realistic indexes. <br>

**users** <br>

```text
users
-------------------
id
email
name
created_at
```

Potential: <br>

```text
CREATE UNIQUE INDEX idx_users_email
ON users(email);
```

<br>
But if email is declared UNIQUE, PostgreSQL already creates the supporting unique index.
<br>
<br>

**urls** <br>

```text
urls
-------------------
id
short_code
original_url
user_id
created_at
```

Potential: <br>

```text
CREATE UNIQUE INDEX idx_urls_short_code
ON urls(short_code);
```

Again, if short_code is declared UNIQUE, you don't need a separate duplicate index.
<br>
And: <br>

```text
CREATE INDEX idx_urls_user_id
ON urls(user_id);
```

<br> <br>
**clicks** <br>

```text
clicks
-------------------
id
url_id
clicked_at
ip_address
```

Potential: <br>

```text
CREATE INDEX idx_clicks_url_id
ON clicks(url_id);
```

And if analytics frequently query clicks by URL and time:
<br>

```text
CREATE INDEX idx_clicks_url_time
ON clicks(url_id, clicked_at);
```

The exact index design should ultimately be based on your actual query patterns.

---

# A Practical Example

Imagine your URL shortener receives: <br>

10 million URL redirects <br>

per day. <br>

Every redirect needs: <br>

```text
SELECT original_url
FROM urls
WHERE short_code = 'aB92xK';
```

If short_code is indexed: <br>

```text
Request
   ↓
short_code index
   ↓
Find URL
   ↓
Return original_url
```

This is exactly the kind of high-frequency lookup where indexing can be important.

---


















