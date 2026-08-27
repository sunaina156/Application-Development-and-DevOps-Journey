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


