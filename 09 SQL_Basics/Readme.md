# SQL
SQL is a language used to communicate with relational databases. <br>

Ex: if application stores users: <br>
```text
id | name    | email
---+---------+-------------------
1  | Sunaina | sunaina@gmail.com
2  | Rahul   | rahul@gmail.com
3  | Aman    | aman@gmail.com
```
<br>
You can use SQL to ask database:<br>
Give me all users.
<br>

```text
SELECT * FROM users;
```

Or:<br>
Give me Sunaina's email.<br>

```text
SELECT email
FROM users
WHERE name = 'Sunaina';
```

Or:<br>
Change Sunaina's email.<br>
```text
UPDATE users
SET email = 'sunaina@example.com'
WHERE id = 1;
```
<br>
So SQL allows applications to create, read, update, and delete data.

---

# SQL vs Database

**Database**  <br>
A database is where the data is stored. <br>
Ex: <br>
```text
url_shortener
```

**SQL** <br>
SQL is the language used to communicate with the database. <br>
```text
Python Application
       ↓
      SQL
       ↓
PostgreSQL Database
```
Think of it like:  <br>
```text
Database = Storage
SQL          = Language used to communicate with it
```

---

# SQL and Relational Databases
SQL is primarily associated with relational database systems such as:
- PostgreSQL
- MySQL
- MariaDB
- Microsoft SQL Server
- Oracle Database

---

# Basic Structure of a Relational Database

A relational database contains tables.  <br>
```text
Database
 |
 |- users
 |- urls
 |- analytics
```

A table contains: rows and columns. <br>

Ex: <br>
```text
users

id | name    | email
---+---------+-------------------
1  | Sunaina | sunaina@gmail.com
2  | Rahul   | rahul@gmail.com
3  | Aman    | aman@gmail.com
```

Here, <br>
users -> table <br>
id, name, email -> columns <br>
Each horizontal record -> row <br>

---

# SQL Syntax
A basic SQL statement looks like: <br>

```text
SELECT column
FROM table;
```
 <br>
Ex: <br>

```text
SELECT name
FROM users;
```

 <br>
SQL statements usually ends with: <br>

```text
;
```
The semicolon indicates the end of a SQL statement.

---

# SQL Keywords

SQL has keywords such as:  <br>

```text
SELECT
FROM
WHERE
INSERT
UPDATE
DELETE
CREATE
DROP
ORDER BY
GROUP BY
```

Ex: <br>

```text
SELECT name
FROM users
WHERE id = 1;
```

SQL keywords are generally written in uppercase for readability. <br>

 <br>
This: <br>
SELECT name FROM users; <br>
and: <br>
select name from users; <br>
are generally equivalent in PostgreSQL. <br>
 <br>
But using uppercase keywords makes SQL easier to read: <br>
```text
SELECT name
FROM users
WHERE id = 1;
```

---

# Creating a Database

In PostgreSQL: <br>
```text
CREATE DATABASE url_shortener;
```

You would then connect to that database before creating application tables inside it.

# CREATE TABLE
```text
CREATE TABLE users (
  id INTEGER,
  name VARCHAR(100),
  email VARCHAR(255)
);
```

# SQL Data Types
Every column generally has a data type. <br>
Common data types include:
- INTEGER <br>
Whole numbers:<br>
```text
age INTEGER
```
- BIGINT
Gor larger integer values:<br>
```text
id BIGINT
```
- VARCHAR
Variable length text with a maximum length<br>
```text
name VARCHAR(100)
```
- TEXT
Text without specifying a fixed maximum length<br>
```text
description TEXT
```
- BOOLEAN
True/False:
```text
is_active BOOLEAN
```
Values:<br>
```text
TRUE
FALSE
```
- DECIMAL/NUMERIC
Useful for exact numeric values:<br>
```text
price DECIMAL(10, 2)
```
Ex:<br>
```text
999.99
```
For financial applications exact numeric types are generally preferred over floating-point types for monetary amounts.
- DATE
```text
birth_date DATE
```
ex:<br>
2004-08-15
- TIMESTAMP
Stores date and time:<br>
```text
created_at TIMESTAMP
```

---

# Creating a Better Users Table

```text
CREATE TABLE users (
    id INTEGER,
    name VARCHAR(100),
    email VARCHAR(255),
    age INTEGER,
    is_active BOOLEAN,
    created_at TIMESTAMP
);
```

---

# INSERT
INSERT adds data to a table. <br>

```text
INSERT INTO users
(name, email, age)
VALUES
('Sunaina', 'sunaina@gmail.com', 21);
```
Now the table contains a row.

---

# Insert Multiple Rows

You can insert multiple records:
<br>

```text
INSERT INTO users
(name, email, age)
VALUES
('Sunaina', 'sunaina@gmail.com', 21),
('Rahul', 'rahul@gmail.com', 22),
('Aman', 'aman@gmail.com', 20);
```

Result:
<br>
```text
id | name    | email              | age
---+---------+--------------------+----
1  | Sunaina | sunaina@gmail.com  | 21
2  | Rahul   | rahul@gmail.com    | 22
3  | Aman    | aman@gmail.com     | 20
```

---

# INSERT Without Specifying Columns

You may see: <br>

```text
INSERT INTO users
VALUES (1, 'Sunaina', 'sunaina@gmail.com', 21);
```

But this approach is generally less explicit and more fragile because it depends on the exact column order.
<br>
Prefer:
<br>
```text
INSERT INTO users
(name, email, age)
VALUES
('Sunaina', 'sunaina@gmail.com', 21);
```
This makes your query clearer and safer when the schema evolves.

---

# SELECT

SELECT retrieves data. <br>
```text
SELECT *
FROM users;
```

* means:
<br>
All columns.

---

# Selecting Specific Columns

Instead of: <br>
```text
SELECT *
FROM users;
```
you can write: <br>
```text
SELECT name, email
FROM users;
```

Result: <br>
```text
name    | email
--------+-------------------
Sunaina | sunaina@gmail.com
Rahul   | rahul@gmail.com
```
In real applications, selecting only the columns you need is often preferable

---

# WHERE

WHERE filters rows. <br>
```text
SELECT *
FROM users
WHERE age = 21;
```
Only users whose age is 21 are returned.

---

# Comparison Operators

SQL provides comparison operators. <br>
```text
=
<>
!=
>
<
>=
<=
```

Examples: <br>

**Equal** <br>
```text
SELECT *
FROM users
WHERE age = 21;
```

**Not equal** <br>
```text
SELECT *
FROM users
WHERE age != 21;
```

<> is also commonly used for "not equal": <br>
```text
WHERE age <> 21;
```
<br>
**Greater than** <br>
```text
SELECT *
FROM users
WHERE age > 20;
```
<br>

**Less than** <br>
```text
SELECT *
FROM users
WHERE age < 25;
```
<br>
**Greater than or equal** <br>
```text
WHERE age >= 21;
```

<br>
**Less than or equal** <br>
```text
WHERE age <= 21;
```

---

# AND

AND means all conditions must be true. <br>
```text
SELECT *
FROM users
WHERE age >= 18
AND is_active = TRUE;
```

Both conditions must match.

---

# OR

OR means at least one condition must be true. <br>
```text
SELECT *
FROM users
WHERE age = 20
OR age = 21;
```

---

# NOT

NOT reverses a condition. <br>

```text
SELECT *
FROM users
WHERE NOT is_active = TRUE;
```
You may also commonly write: <br>
WHERE is_active = FALSE;

---

# Combining AND and OR

This is where SQL can become tricky.
<br><br>
Consider: <br>

```text
SELECT *
FROM users
WHERE age = 20
OR age = 21
AND is_active = TRUE;
```
You should not blindly assume the expression is evaluated left-to-right. <br>

Use parentheses when you want the logic to be explicit: <br>
```text
SELECT *
FROM users
WHERE (age = 20 OR age = 21)
AND is_active = TRUE;
```
This means: <br>

(age is 20 OR age is 21)<br>
        AND <br>
     active <br>

Good SQL uses parentheses when they make logical intent clearer. <br>

---

















