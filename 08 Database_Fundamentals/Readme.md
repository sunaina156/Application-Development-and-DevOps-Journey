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

CRUD

























