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

# IN

IN is useful when checking against multiple values. <br>

Instead of: <br>

WHERE age = 20 <br>
OR age = 21 <br>
OR age = 22 <br>
<br><br>
write: <br>

WHERE age IN (20, 21, 22); <br>
<br>
For your URL Shortener: <br>
```text
SELECT *
FROM urls
WHERE short_code IN ('abc123', 'xyz789');
```

---

# NOT IN

Opposite of IN. <br>
```text
SELECT *
FROM users
WHERE age NOT IN (18, 19, 20);
```
This returns users whose age is not one of those values. <br>

⚠️ NULL makes NOT IN behavior surprising in SQL's three-valued logic.

---

# BETWEEN

BETWEEN checks whether a value falls within a range. <br>
```text
SELECT *
FROM users
WHERE age BETWEEN 18 AND 25;
```

Conceptually: <br>

18 ≤ age ≤ 25 <br> <br>

The boundaries are included. <br>

So: <br>

18 → included <br>
25 → included

---

# NOT BETWEEN
```text
SELECT *
FROM users
WHERE age NOT BETWEEN 18 AND 25;
```

---

# LIKE

LIKE is used for pattern matching. <br>

Suppose: <br>
```text
Sunaina
Sunil
Rahul
Aman
```
Find names beginning with S: <br>
```text
SELECT *
FROM users
WHERE name LIKE 'S%';
```
Result: <br>
```text
Sunaina
Sunil
```

---

# % Wildcard

% represents zero or more characters. <br>
<br>
```text
LIKE 'S%' 
```
means: <br>
Starts with S

<br><br>
```text
LIKE '%a'
```
means: <br>

Ends with a   <br><br>

```text
LIKE '%ain%'
```
means: <br>

Contains "ain"

---

# _ Wildcard

_ represents exactly one character. <br>

Example: <br>
```text
WHERE name LIKE 'A_an';
```
Could match: <br>

Alan  <br>
Aman  <br>

because _ represents one character.

---

# LIKE vs =

These are different. <br>

WHERE name = 'Sunaina'; <br>

checks for an exact value. <br><br>

Whereas: <br>

WHERE name LIKE 'Sun%';
<br>
checks for a pattern.

---

# Case Sensitivity in PostgreSQL

In PostgreSQL, LIKE is case-sensitive. <br>

You can use: <br>
```text
ILIKE
```
for case-insensitive pattern matching. <br>

Example: <br>
```text
SELECT *
FROM users
WHERE name ILIKE 'sun%';
```
This can match names such as: <br>

Sunaina <br>
sunaina <br>
SUNAINA <br>

---

# NULL

NULL represents an absent/unknown value.
<br>
For example: <br>
```text
id | name    | phone
---+---------+----------
1  | Sunaina | 9876543210
2  | Rahul   | NULL
```
Rahul doesn't have a phone value stored. <br>

Important: <br>

NULL is not: <br>
0 <br>
"" <br>
FALSE <br>

---

# IS NULL

To find missing values: <br>
```text
SELECT *
FROM users
WHERE phone IS NULL;
```

---

# IS NOT NULL
```text
SELECT *
FROM users
WHERE phone IS NOT NULL;
```

---

# Why = NULL Doesn't Work

This is wrong: <br>

WHERE phone = NULL; <br> <br>

Use: <br>

WHERE phone IS NULL; <br> <br>

Why? <br>

Because NULL represents an unknown/missing value, and SQL uses three-valued logic: <br>

TRUE <br>
FALSE <br>
UNKNOWN <br>

Comparisons involving NULL generally produce UNKNOWN, rather than ordinary TRUE or FALSE. <br>

---

# DISTINCT

DISTINCT removes duplicate values from the result. <br>

Suppose: <br>

users <br>
```text
city
------
Delhi
Delhi
Bhopal
Indore
Bhopal
```

Query: <br>
```text
SELECT DISTINCT city
FROM users;
```

Result:
<br>

```text
Delhi
Bhopal
Indore
```

---

# DISTINCT on Multiple Columns

You can write:  <br>
```text
SELECT DISTINCT city, age
FROM users;
```

Here, uniqueness is determined by the combination of city and age.

---

# ORDER BY

ORDER BY sorts results. <br>
```text
SELECT *
FROM users
ORDER BY age;
```

Default is generally ascending order: <br>

20 <br>
21 <br>
22 <br>
25 <br>

---

# Multiple Columns in ORDER BY

You can sort using multiple columns: <br>
```text
SELECT *
FROM users
ORDER BY age DESC, name ASC;
```

Meaning: <br>

Sort by age descending. <br>
If two users have the same age, sort those users by name ascending. <br>

---

# LIMIT + ORDER BY

These are commonly used together. <br>
<br>
For example: <br>

Find the 5 users with the highest age. <br>
```text
SELECT *
FROM users
ORDER BY age DESC
LIMIT 5;
```

The order matters conceptually: <br>
```text
All users
   ↓
Sort by age
   ↓
Take top 5
```

---

# OFFSET

OFFSET skips rows. <br>
```text
SELECT *
FROM users
ORDER BY id
LIMIT 10 OFFSET 10;
```

Conceptually: <br>
```text
Rows 1–10
   ↓
skip

Rows 11–20
   ↓
return
```

This is commonly used for basic pagination.

---

# Aliases

Aliases give temporary names to columns or tables. <br>

Column alias <br>
```text
SELECT
    name AS username
FROM users;
```

Result column: <br>

username <br>

instead of: <br>

name <br>

---

# Table Alias

Instead of: <br>
```text
SELECT users.name
FROM users;
```

you can write: <br>
```text
SELECT u.name
FROM users AS u;
```

Now: <br>

u → users <br>

This becomes extremely useful when using joins.

---

# Arithmetic in SQL

SQL can perform calculations. <br>

Suppose: <br>
```text
price
-----
100
200
300
```

You can write: <br>
```text
SELECT price * 2
FROM products;
```

Or: <br>

```text
SELECT price, price * 1.18 AS price_with_tax
FROM products;
```

---

# Aggregate Functions

Aggregate functions perform calculations across multiple rows. <br>

Important ones: <br>

```text
COUNT()
SUM()
AVG()
MIN()
MAX()
```

## COUNT()

Count rows: <br>

```text
SELECT COUNT(*)
FROM users;
```

Suppose there are 100 users: <br>

100 <br>

## COUNT(column)

You can also write: <br>

```text
SELECT COUNT(email)
FROM users;
```

Important distinction: <br>

COUNT(column) generally counts non-NULL values in that column. <br>

Whereas: <br>

COUNT(*) <br>

counts rows.<br>

Example: <br>

```text
id | email
---+----------------
1  | a@gmail.com
2  | NULL
3  | c@gmail.com
```

Then: <br>

COUNT(*)
<br>
→ 3
<br><br>
while: <br>

COUNT(email) <br>

→ 2 <br>

---

## SUM()

Suppose: <br>

```text
sales
-----
100
200
300
```

Query: <br>
```text
SELECT SUM(sales)
FROM orders;
```

Result:
<br>
600

## AVG()

```text
SELECT AVG(age)
FROM users;
```

Returns the average age.

## MIN()

```text
SELECT MIN(age)
FROM users;
```

Returns the smallest age.


## MAX()

```text
SELECT MAX(age)
FROM users;
```

Returns the largest age.


---

# GROUP BY

GROUP BY groups rows that have the same values. <br>

Suppose: <br>

users <br>

```text
name    | city
--------+--------
A       | Delhi
B       | Delhi
C       | Bhopal
D       | Bhopal
E       | Indore
```

Query: <br>

```text
SELECT city, COUNT(*)
FROM users
GROUP BY city;
```

Result: <br>

```text
city    | count
--------+------
Delhi   | 2
Bhopal  | 2
Indore  | 1
```

The database creates groups: <br>

Delhi <br>
 ├── A <br>
 └── B <br>

Bhopal <br>
 ├── C <br>
 └── D <br>

Indore <br>
 └── E <br>

Then COUNT() is calculated for each group.<br>

---

# GROUP BY + SUM

Suppose: <br>

orders <br>

```text
customer | amount
---------+-------
A        | 100
A        | 200
B        | 300
B        | 100
```

Query: <br>
```text
SELECT customer, SUM(amount)
FROM orders
GROUP BY customer;
```

Result: <br>

```text
customer | sum
---------+----
A        | 300
B        | 400
```

---

# GROUP BY + AVG

```text
SELECT city, AVG(age)
FROM users
GROUP BY city;
```

This gives average age per city.

---

# HAVING

HAVING filters groups. <br>

Suppose: <br>

Find cities having more than 5 users. <br>

```text
SELECT city, COUNT(*)
FROM users
GROUP BY city
HAVING COUNT(*) > 5;
```

This is different from WHERE.

---

# WHERE vs HAVING


**WHERE**

Filters rows before grouping. <br>

```text
SELECT city, COUNT(*)
FROM users
WHERE age >= 18
GROUP BY city;
```

Meaning: <br>

```text
Take users
   ↓
Keep users age >= 18
   ↓
Group by city
   ↓
Count
```

**HAVING**

Filters groups after grouping. <br>

```text
SELECT city, COUNT(*)
FROM users
GROUP BY city
HAVING COUNT(*) > 5;
```

Meaning: <br>
```text
Take users
   ↓
Group by city
   ↓
Count users
   ↓
Keep groups with count > 5
```

Remember: <br>

WHERE → filters rows <br>
HAVING → filters groups

---

# Basic JOIN

Suppose you have: <br>

users <br>
```text
id | name
---+--------
1  | Sunaina
2  | Rahul
3  | Aman
```

urls <br>
```text
id | user_id | short_code
---+---------+-----------
1  | 1       | abc123
2  | 1       | xyz789
3  | 2       | pqr456
```

You want: <br>
```text
name | short_code
-----+-----------
Sunaina | abc123
Sunaina | xyz789
Rahul   | pqr456
```

Use: <br>
```text
SELECT u.name, url.short_code
FROM users AS u
JOIN urls AS url
ON u.id = url.user_id;
```

---

# Understanding the JOIN

This part:

FROM users AS u

means:

u = users

This part:

JOIN urls AS url

adds the urls table.

And:

ON u.id = url.user_id

tells the database:

Match a user's id with the URL's user_id.

Conceptually:

users.id
    │
    │ matches
    ↓
urls.user_id







