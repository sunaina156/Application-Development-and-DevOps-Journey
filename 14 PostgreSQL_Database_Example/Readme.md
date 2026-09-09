# Download PostgreSQL
PostgreSQL default port 5432 <br>
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
<br><br>
password: postgres123@!#
<br><br>

open pqAdmin <br> 
see it  <br>
data base visible

-----------

Open Command Prompt: <br>
Add the Path Environment Variable in Windows C:\Program Files\PostgreSQL\18\bin if psql --version not work  <br>
```text
> psql --version
```

<br>
```text
psql -U postgres
```
 <br>
psql starts the PostgreSQL command-line interface and connects you to PostgreSQL. <br>
 Password for user postgres: <br><br>

 psql (17.x) <br>
Type "help" for help. <br>

postgres=# <br>
(Now you are inside psql.) <br>

psql is the command-line tool (terminal program) used to communicate with PostgreSQL. <br>
PostgreSQL is the actual database system that stores, organizes, and manages your data.  <br>


---

# What happens when you install PostgreSQL on Windows?

When you download PostgreSQL for Windows and install it, you are installing a PostgreSQL database server system on your computer. <br>

```text
YOUR WINDOWS COMPUTER
│
└── PostgreSQL
     │
     └── PostgreSQL Server / Instance
          │
          ├── Databases
          │    ├── postgres
          │    ├── url_shortener
          │    └── another_database
          │
          └── Users
               └── postgres
```

<br>

1. **PostgreSQL** is the database management system (DBMS).

It is software. <br>

Just like: <br>

Windows → operating system <br>
Python  → programming language <br>
PostgreSQL → database management system <br>

PostgreSQL provides the software that can: <br>
- create databases
- create tables
- store data
- retrieve data
- update data
- delete data
- manage users and permissions
- handle transactions
- manage connections from applications

Your URL Shortener needs this because you don't want your URLs to disappear every time your Python program stops.
<br>

2. A PostgreSQL server is the running PostgreSQL process/instance that accepts connections and manages databases. <br>

For example:<br>
```text
PostgreSQL Server
       │
       ├── Database A
       ├── Database B
       └── Database C
```

<br>
When you install PostgreSQL on your Windows laptop, the installer normally creates a PostgreSQL server instance and runs it as a Windows service.
<br>
You don't necessarily have to manually create a server just to start using PostgreSQL.<br>

---

# Database Create, Connect to Database, Verify Database

Open CMD <br>
<br>
Connect to default server i.e postgres with username as postgres <br>
```text
psql -U postgres
```

<br>
To check version of server  <br>
```text
SELECT version();
```

 <br> <br>
Create the database.  <br>
```text
CREATE DATABASE url_shortener;
```

Connect to url_shortener database  <br>
```text
\c url_shortener
```

 <br> <br>

 Verify we connect to right database or not.  <br>
 ```text
SELECT current_database();
```

---

# Create the Tables

Now our database url_database is empty. <br>

We need 3 tables: <br>

```text
users
  │
  │ 1:N
  ↓
urls
  │
  │ 1:N
  ↓
clicks
 ```

 <br>

 ## Create users

```text
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

<br>

## Create urls

```text
CREATE TABLE urls (
    id BIGSERIAL PRIMARY KEY,
    short_code VARCHAR(20) NOT NULL UNIQUE,
    original_url TEXT NOT NULL,
    user_id BIGINT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
);
```

<br>

**Clear Screen in psql** <br>
To clear the visible screen in psql  <br>
```text
\! cl
```

<br>

## Create clicks

```text
CREATE TABLE clicks (
    id BIGSERIAL PRIMARY KEY,
    url_id BIGINT NOT NULL,
    ip_address INET,
    clicked_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (url_id)
        REFERENCES urls(id)
        ON DELETE CASCADE
);
```

## To check List of all Tables

```text
\dt
```

## To inspect each table

```text
\d users
```

<br>


```text
\d urls
```

<br>


```text
\d clicks
```

---

# Add Indexes





















