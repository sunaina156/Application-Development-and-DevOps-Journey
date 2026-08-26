# Database

Organized collection of data that allows applicatons to store, retrieve, modify, and manage information efficiently. <br>
Ex: Imagine your URL shortener  have URLS, and store them in json but json won't work for 10 millon URLS, 1 million users, millions of requests per day, multiple application servers etc. <br>

**A database gives mechanism for:** <br>
- efficient searching
- Updating data
- Deleting data
- Handling many users
- Maintaining data consistency
- Managing relationships
- Controlling access
- Handling concurrent operations
- Recovering from failures

---

# Why we need Databases?
Suppose we have a application for company. <br>
It needs to store: <br>

```text
Users
Products
Orders
Payments
URLs
Comments
Messages
Logs
```

We need more than just a place to put data. <br>
We need to answer questions such as: <br>

```text
Find this user
Find all orders belonging to this user
Delete this product
Find all orders from today
Find the most popular URLs
Make sure two users don't get the same username
```

A database provides tools to perform these operations efficiently and reliably.

---

# Database vs File

**File-based storage**  <br>
Python Application
    ⬇
urls.json

**Database-based storage** <br>
Python Application
    ⬇
Database
    ⬇
urls table

---

# Types of Databases

```text
                    Databases
                       |
              +--------+--------+
              |                 |
           SQL              NoSQL
        Relational       Non-relational
```

**Relational / SQL databases** <br>
- PostgreSQL
- MySQL
- MariaDB
- Oracle Database
- Microsoft SQL Server

**NoSQL databases** <br>
Different NoSQL databases use different models
- MongoDB  ->  Document
- Redis  ->  key-value
- Cassandra  ->  Wide-column
- Neo4j  ->  Graph

---

# SQL
SQL = Structured Query Language  <br>
SQL is a language used to communicate with relational databases. <br>
<br>
Ex: <br>
```text
SELECT * FROM users'
```

Use SQL to: 
- create data structures
- Insert data
- Read data
- Update data
- Delete data
- Ceate indexes
- Create relationships
- Control transactions

---

# Relational Database
A relational database stores structed data in tables and allows relationships between those tables.

```text
users
| id | name    | email                                             |
| -: | ------- | ------------------------------------------------- |
|  1 | Sunaina | [sunaina@example.com](mailto:sunaina@example.com) |
|  2 | Rahul   | [rahul@example.com](mailto:rahul@example.com)     |

```


```text
urls
| id | user_id | short_code | original_url                               |
| -: | ------: | ---------- | ------------------------------------------ |
|  1 |       1 | aB92x7     | [https://github.com](https://github.com)   |
|  2 |       1 | Xy81pQ     | [https://google.com](https://google.com)   |
|  3 |       2 | K91Lm2     | [https://youtube.com](https://youtube.com) |

```

The database understand that
```text
urls.user_id
     ↓
users.id
```
creates a relationship

---

# Database -> Table -> Row -> Column

Suppose: <br>

```text
users
| id | name    | email                                             | age |
| -: | ------- | ------------------------------------------------- | --: |
|  1 | Sunaina | [sunaina@example.com](mailto:sunaina@example.com) |  21 |
|  2 | Rahul   | [rahul@example.com](mailto:rahul@example.com)     |  22 |
```

**Database** <br>
the overall database might be ```text url_shortener ```  <br>

**Table**<br>
users<br>

**Column**<br>
id<br>
name<br>
email<br>
age<br>

**Row**<br>
1 | Sunaina | sunaina@example.com | 21<br>

A row represents one record/entity<br>
A column represents a particular attribute/entity<br>

---

# Schema

Schema = logical representation of database  <br>
A database schema describes the structure of your database.<br>

Ex:<br>
```text
users
├── id
├── name
├── email
└── created_at

urls
├── id
├── user_id
├── short_code
├── original_url
└── created_at
```

The schema defines things such as:
- Tables
- Columns
- Data types
- Constraints
- Relationships
- Indexes

Schema = blueprint / structure of the database<br>

---

# Data Types
Columns have data types.   <br>

Ex:
```text
CREATE TABLE users (
  id INTEGER,
  name VARCHAR(100),
  email VARCHAR(255),
  age INTEGER
);
```

Common SQL data types include:   <br>
INTEGER, BIGINT, DECIMAL, VARCHAR, TEXT, BOOLEAN, DATE, TIMESTAMP   <br>

Choosing appropriate data types matters for correctness and storage efficiency.   <br>

---

# Primary Key

# Primary Key

A primary key uniquely identifies each row in a table.   <br>

Ex:   <br>
id | name 
------------------
1 | Sunaina
2 | Rahul 
3 | Aman
   <br>
Here, **id** is a primary key.   <br>

Ex:   <br>
```text
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name VARCHAR(100)
);
```

We can't have id as 1 for two bcoz then the database couldn't use id to uniquely identify a row.   <br>

# Why Do We Need Primary Keys?

```text
users
--------------------------------
id | name | email
1  | A    | a@example.com
2  | B    | b@example.com
3  | C    | c@example.com
```

To update user B   <br>

```text
UPDATE users
SET name = 'Rahul'
WHERE id = 2;
```

The primary key gives each record a stable identity.   <br>

---

# Natural Key vs Surrogate Key

There are two common approaches.  <br>

**Natural Key**
A value that already has real-world meaning.  <br>
ex:  <br>
```text
email
ISBN
phone number
```

**Surrogate Key**
A generated identifier with no business meaning.
  <br>
ex:  <br>
```text
1
2
3
4
```

---

# Foreign Key
A foreign key creates a relationship between tables.
  <br>
Suppose:  <br>

users  <br>
| id | name    |
| -: | ------- |
|  1 | Sunaina |
|  2 | Rahul   |

urls  <br>
| id | user_id | short_code |
| -: | ------: | ---------- |
|  1 |       1 | aB92x7     |
|  2 |       1 | Xy81pQ     |
|  3 |       2 | K91Lm2     |

Here,  <br> 
urls.user_id -> users.id  <br>
urls.user_id is a foreign key referencing users.id
  <br>

SQL:  <br>
```text
CREATE TABLE urls (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  short_code VARCHAR(10),
  FOREIGN KEY (user_id) REFERENCES users(id)
)
```

---

# Why Foregin Keys Matter

Suppose user 999 doesn't exist.
  <br>
Without proper constraints, you might accidentally insert:
  <br>
urls  <br>
id | user_id | short_code
1  | 999     | aB92x7

Now your URL belongs to a nonexistent user.
  <br>
A foreign key can prevent this kind of invalid relationship.
  <br>
This is called referential integrity.
  <br>

---

# CRUD

```text
C -> Create
R -> Read
U -> Update
D -> Delete
```

**Create** <br>
Add data: <br>
```text
INSERT into users (name)
VALUES ('Sunaina');
```

**Read**  <br>
Retrieve data: <br>
```text
SELECT * FROM users;
```

**Update** <br>
Modify data:
```text
UPDATE users
SET name = 'Sunaina Lodha'
WHERE id = 1;
```

**Delete** <br>
Remove data: <br>
```text
DELETE FROM users
WHERE id = 1;
```

---

# INSERT 
INSERT adds records. <br>

```text
INSERT INTO urls
(short_code, original_url, clicks)
VALUES
('aB92x7', 'https://github.com', 0);
```

Multiple records:<br>
```text
INSERT INTO urls
(short_code, original_url, clicks)
VALUES
('aB92x7', 'https://github.com', 0),
('Xy81pQ', 'https://google.com', 0);
```

---

# SELECT
SELECT retrieves data.<br>

All columns:<br>
```text
SELECT *
FROM urls;
```

Specific columns:<br>
```text
SELECT short_code, original_url
FROM urls;
```

This is better when you don't actually need every column

---

# WHERE
WHERE filters records. <br>

```text
SELECT *
FROM urls
WHERE short_code = 'aB92x7';
```

Another: <br>
```text
SELECT *
FROM urls
WHERE clicks > 10;
```

Multiple conditions: <br>
```text
SELECT *
FROM urls
WHERE clicks > 10
AND original_url LIKE 'https%';
```

Common operators:  <br>
```text
=   !=  >   <  <=  >=
```

Logical operators: <br>
```text
AND   OR   NOT
```

---

# LIKE
LIKE performs pattern matching.  <br>

```text
SELECT *
FROM users
WHERE name LIKE 'Sun%';
```

% means zero or more characters.  <br>

Ex:  <br>

```text
SELECT *
FROM users
WHERE email LIKE '%gmail.com';
```

---

# ORDER BY

Sort results.  <br>

```text
SELECT *
FROM urls 
ORDER BY clicks DESC;
```

DESC:  <br>
```text
10
8
5
2
```

ASC:  <br>
```text
2
5
8
10
```

---

# LIMIT

Limits the number of results.  <br>

```text
SELECT *
FROM urls
ORDER BY clicks DESC
LIMIT 10;
```

This is useful when you have millions of records but only want the first few.  <br>

---

# UPDATE
Modify existing data.   <br>

```text
UPDATE urls
SET clicks = clicks + 1
WHERE short_code = 'aB92x7';
```
WHERE is important   <br>

```text
UPDATE urls
SET clicks = clicks + 1;
```
This will update it everywhere bcoz WHERE not mentioned.   <br>
Always understand which records your query affects.   <br>

---

# DELETE
Delete records.   <br>

```text
DELETE FROM urls
WHERE short_code = 'aB92x7';
```

Be careful with WHERE   <br>

```text
DELETE FROM urls;
```
deletes all rows from the table.   <br>

---

# NULL
NULL means the value is missing/unknown/not provided.   <br>
   <br>
It is not the same as:   <br>
```text
0
""
False
```

Ex:   <br>
```text
phone_number = NULL
```
means no phone number value is stored.   <br>

To check for NULL:   <br>
```text
SELECT *
FROM users
WHERE phone_number IS NULL;
```

Not:   <br>
```text
WHERE phone_number = NULL;
```

---

# Constraints

Constraints are rules enforced by the database.  <br>

constraints:  <br>
```text
PRIMARY KEY
FOREIGN KEY
NOT NULL
UNIQUE
DEFAULT
CHECK
```

**NOT NULL**   <br>
The column must have a value  <br>
```text
name VARCHAR(100) NOT NULL
```

**UNIQUE**  <br>
Values cannot be duplicate  <br>
```text
email VARCHAR(255) UNIQUE
```

For URL Shortener:
```text
short_code VARCHAR(10) UNIQUE
```

**DEFAULT**
Provides value automatically.  <br>
```text
clicks INTEGER DEFAULT 0
```

When you insert:  <br>
```text
INSERT INTO urls(short_code, original_url)
VALUES ('aB92x7', 'https://github.com');
```
the database can automatically set:  <br>
```text
clicks = 0
```

---

# CHECK
Enforces a condition  <br>
```text
clicks INTEGER CHECK (clicks >= 0)
```
Now negative clicks are not allowed.  <br>

---

#Relationships Between Tables

There are 3 major relationships types.  <br>

**One-to-One**  <br>
Once record relates to one record.  <br>
```text
Person
  │
  │
  └── Passport
```
One person has one passport <br>

**One-to-Many** <br>
Once record relates to many records.
```text
User
 |- URL
 |- URL
 |- URL
```
One user can create many shortened URLs  <br>
Use in URL shortener  <br>

**Many-to-Many**  <br>
Many records relate to many records  <br>
Ex:  <br>
```text
Students <-> Courses
```
Once student can take many courses  <br>
One course can have many students.  <br>
  <br>
Usually a third/junction table is used:  <br>
```text
students
courses
student_courses
``` 

---

# JOINS
A JOIN allows you to retrieve related data from multiple tables.
  <br>
users:  
id | name
1  | Sunaina
2  | Rahul
  <br>
urls:
id | user_id | short_code
1  | 1           | aB92x7
2  | 1           | Xy81pQ
3  | 2           | K91Lm2
  <br>
You can join them:  <br>
```text
SELECT users.name, urls.short_code
FROM users
JOIN urls
ON users.id = urls.user_id;
```

Result:  <br>
Sunaina | aB92x7
Sunaina | Xy81pQ
Rahul     | K91Lm2

JOIN connect related records from different tables.  <br>

--- 

# Types of JOINs

**INNER JOIN**  <br>
Returns matching records from both tables.  <br>
```text
A ∩ B
```

**LEFT JOIN**  <br>
Returns all records from the left tables plus matching records from the right.  <br>

**RIGHT JOIN**  <br>
THe opposite direction.  <br>

**FULL OUTER JOIN**   <br>
Returns matching and non-matching records from both sides where supported.  <br>

--- 

# Normalization
Normalization is the process of organizing relational data to reduce unnecessary duplication and improve consistency.  <br>

Imagine:  <br>
**Bad Design**  <br>
orders

|order_id | customer_name | customer_email | product
|----------------------------------------------------
|1        | Sunaina       | s@example.com  | Laptop
|2        | Sunaina       | s@example.com  | Mouse
|3        | Sunaina       | s@example.com  | Keyboard

Customer information is repeated.  <br>
Instead:  <br>

customers  <br>
id | name | email
--------------------
|1 | Sunaina | s@exmaple.com

orders

```text
id | customer_id | product
1 | 1 | Laptop
2 | 1 | Mouse
3 | 1 | Keyboard
```

Now the customer information is stored once.  <br>

---

# Why Normalization?

It helps reduce problems such as:

- Update anomaly
you change an email in one row but forget another
- Insert anomaly
You cannot add certain information without unrelated information
- Delete anomaly
Deleting one record accidentally removes information you still need.

Normalization helps organize the data to avoid these problems.

---

# 1NF, 2NF, 3NF

## 1NF - First Normal Form
Data should have atomic values rather than repeating groups.
<br>

Bad:
```text
skills = "Python, Docker, AWS"
```
<br>
Better in a relational design:
```text
user_skills
user_id | skill
1           | Python
1           | Docker
1           | AWS
```

## 2NF - Second Normal Form
The table should already be in 1NF, and non-key attributes should depend on the whole primary key. <br>

## 3NF - Third Normal Form
The table should be in 2NF and non-key attributes should not depend on other non-key attributes.
<br>
The simplified idea: <br>
```text
Non-key data
      ↓
Should depend on
      ↓
The key
```

---

# Indexes

Imagine:
```text
urls table
10,000,000 rows
```
<br>
You frequently execute:
```text
SELECT *
FROM urls
WHERE short_code = 'aB92x7';
```
Without an appropriate index, the database may need to examine many rows. <br>
<br>
An index provides a separate data structure that helps the database locate records more efficiently. <br>

Conceptually: <br>
```text
Table
10 million rows
       ↓
       ↓
Index on short_code
       ↓
Locate matching row
```

<br>
Create an index: <br>
```text
CREATE INDEX idx_urls_short_code
ON urls(short_code);
```

# Why Not Index Everything ?

Indexes improve certain reads, but they have costs. <br>
When you: <br>
```text
INSERT
UPDATE
DELETE
```

the database may also need to maintain indexes. <br>
Indexes also consume storage. <br>
Therefore, Index columns based on actual query patterns rather than blindly indexing every column. <br>
For URL Shortener, short_code is a strong candidate bcoz lookup by short code is a core operation. <br>

---

# Composite Index

You can create an index using multiple columns. <br>
```text
CREATE INDEX idx_urls_user_created
ON urls(user_id, created_at);
```

The order of column matters. <br>

---

# Transactions

Suppose a banking application transfers: 
₹100
from Account A to Account B
You need:
```text
A: -₹100
B: +₹100
```

What if first operation succeeds but second fails?
you dont wantthe money to disappear.
A **transaction** groups operations into a logical unit.

<br>
Conceptually:
```text
BEGIN
   ↓
Operation 1
   ↓
Operation 2
   ↓
COMMIT
```

If something fails: 
```text
BEGIN
   ↓
Operation 1
   ↓
Operation 2 ❌
   ↓
ROLLBACK
```


---

# Commit
COMMIT permanently applies the transaction's changes. <br>
Conceptually:
```text
Transaction
     ↓
COMMIT
     ↓
Changes accepted
```

---

# ROLLBACK
ROLLBACK cancels changes made within a transaction that has not been comitted. <br>
```text
Transaction
     ↓
Something fails
     ↓
ROLLBACK
     ↓
Undo transaction changes
```

---

# ACID
Transactions are commonly described using ACID properties. <br>

```text
A -> Atomicity
C -> Consistency
I -> Isolation
D -> Durability
```

## Atomicity
A transaction is treated as one unit. <br>
Either: Everything succeeds <br>
Or: Everything is rolled back <br>
Not half-successful <br>

## Consistency
A transaction should take the database from one valid state to another valid state while respecting defined rules and constraints.  <br>
Ex: <br>
clicks >= 0 <br>
should remain valid. <br>

## Isolation
when multiple transactions happen at the same time, one transaction should not incorrectly interfere with another. <br>
Think:
Transaction A <-> Transaction B <br>
The database provides mechanisms to control how concurrent transactions interact. <br>

## Durability
Once a transaction has been successfully committed, its changes should survive failures such as a database/server restart, subject to the database's durability mechanisms. <br>

---

 # Concurrency



























