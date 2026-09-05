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


