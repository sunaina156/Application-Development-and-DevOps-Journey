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

```text
CREATE INDEX idx_urls_user_id
ON urls(user_id);
```

<br>

```text
CREATE INDEX idx_clicks_url_id
ON clicks(url_id);
```

---

# Insert Some Users Manually
Before connecting Python, let's test the database manually. <br>

```text
INSERT INTO users (name, email)
VALUES
    ('Sunaina', 'sunaina@example.com'),
    ('Rahul', 'rahul@example.com'),
    ('Aman', 'aman@example.com');
```

<br>
Check: <br>

```text
SELECT * FROM users;
```

---

# Understand the Difference From Your Current Python Code

Currently you have: <br>

url_storage = {} <br>
<br><br>
When you do:<br>

url_storage["abc123"] = "https://github.com" <br>

the data exists only inside your Python program. <br><br>

If you stop the program: <br>

```text
Python program stopped
       ↓
dictionary destroyed
       ↓
data lost
```

 <br>
That's the major problem.
 <br> <br>

With PostgreSQL: <br>
```text
INSERT INTO urls (...)
```

 <br>
the data is stored in the database. <br>

You can stop Python and start it again: <br>
```text
Python stops
     ↓
PostgreSQL still has data
     ↓
Python starts again
     ↓
Data still exists
```

That's what you are building now.

---
---

# Install PostgreSQL Python Driver

Your Python application needs a library to communicate with PostgreSQL. <br>

Since you're using a virtual environment, activate it first. <br>


```text
C:\Users\sunaina\Desktop\Python_URL_Shortener>cd Python_URL_Shortener

C:\Users\sunaina\Desktop\Python_URL_Shortener\Python_URL_Shortener>dir

C:\Users\sunaina\Desktop\Python_URL_Shortener\Python_URL_Shortener>venv\Scripts\activate

(venv) C:\Users\sunaina\Desktop\Python_URL_Shortener\Python_URL_Shortener>
```

<br>

psycopg2-binary is a Python package that allows your Python program to connect to and communicate with PostgreSQL. <br>

```text
pip install psycopg2-binary
```

Check: <br>
pip show command is used to check information about an installed Python package <br>

```text
pip show psycopg2-binary
```

---

# Add It to requirements.txt

Run: <br>

```text
pip freeze > requirements.txt 
```

You should now have the PostgreSQL dependency in your requirements file. <br>

pip freeze means: <br>
 
Show me everything installed in this Python environment <br>

**OR** <br>

```text
psycopg2-binary==2.9.12
python-dotenv
```

 <br>
 
Then someone can install them with:  <br>

pip install -r requirements.txt <br>

---

# Create Database Connection

Now our Python application needs to connect to PostgreSQL Database. <br>

In **main.py** add, <br>
```text
import psycopg2

def get_connection():
     return psycopg2.connect(
          host="localhost",
          database="url_shortener",
          user="postgres",
          password="postgres123@!#",
          port = "5432"
     )


```

<br>

## Test the Python → PostgreSQL Connection

Before changing your whole application, test the connection. <br>

Temporarily add: <br>

```text
connection = get_connection()

print("Connected to PostgreSQL successfully!")

connection.close()
```

<br>

Run: <br>
```text
python main.py
```

If everything is correct: <br>
```text
Connected to PostgreSQL successfully!
```
<br>
If this works, your Python application can communicate with PostgreSQL. <br>

---

# Now Remove the Dictionary

Now from main.py <br>
remove <br>
```text
url_storage = {}
```
<br>
Because PostgreSQL is going to store your URLs. <br> <br>

## Modify store_url()

we dont want: <br>
```text
url_storage[short_code] = original_url
```
anymore. <br>

Instead, we want: <br>
```text
generate short code
       ↓
INSERT into PostgreSQL
       ↓
return short code
```

<br> <br>
For now, let's assume user 1 is creating the URL. <br>

**main.py** <br>

```text
def store_url(original_url, user_id):

    connection = get_connection()
    cursor = connection.cursor()

    short_code = generate_short_code()

    cursor.execute(
        """
        INSERT INTO urls (short_code, original_url, user_id)
        VALUES (%s, %s, %s)
        RETURNING short_code;
        """,
        (short_code, original_url, user_id)
    )

    short_code = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return short_code
```

# Modify get_original_url()

Now PostgreSQL should find the URL. <br>

**main.py** <br>
```text
def get_original_url(short_code):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT original_url
        FROM urls
        WHERE short_code = %s;
        """,
        (short_code,)
    )

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return result[0]
    else:
        return "Short code not found!"
```

<br>

Now your lookup is: <br>

```text
short code
    ↓
Python
    ↓
PostgreSQL
    ↓
urls table
    ↓
original URL
```

---

# Your Application Can Now Work With PostgreSQL

Your menu can remain almost the same. <br>

But change: <br>
```text
short_code = store_url(original_url)
```

<br>

to: <br>

```text
short_code = store_url(original_url, 1)
```

<br>
For now, user 1 means Sunaina.
<br>

So your flow becomes: <br>

```text
1. Shorten URL
       ↓
Enter URL
       ↓
Generate short code
       ↓
INSERT into urls
       ↓
PostgreSQL
       ↓
Return short code
```

<br> And:

```text
2. Retrieve Original URL
       ↓
Enter short code
       ↓
SELECT from urls
       ↓
PostgreSQL
       ↓
Original URL
```

## Test It

Start your application: <br>

```text
python main.py
```

 <br>
Choose: <br>

```text
1. Shorten URL
```

 <br>
Enter: <br>

```text
https://github.com
```

 <br>
You might get: <br>

Short Code: LJRm4h <br>

Now go to PostgreSQL: <br>

```text
> psql -U postgress
> \c url_shortener
```

<br>
You are now connected to database "url_shortener" as user "postgres".
<br>

Check the tables: <br>
```text
\dt
```

<br>

```text
SELECT * FROM urls;
```

 <br>
You should see something like: <br>

 ```text
 id | short_code |    original_url     | user_id
----+------------+---------------------+---------
  1 | LJRm4h     | https://github.com  |    1
```

 <br>

## Test Retrieval


Run your Python application again. <br>

Choose: <br>

```text
2. Retrieve Original URL
```

<br>
Enter: <br>

```text
LJRm4h
```

<br>
You should get: <br>

```text
Original URL: https://github.com
```

<br>
Then verify directly in PostgreSQL: <br>

```text
SELECT original_url
FROM urls
WHERE short_code = 'LJRm4h';
```

---

# Add Click Tracking




