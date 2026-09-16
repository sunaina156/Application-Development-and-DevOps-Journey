# What Are Environment Variables?

An environment variable is a value stored outside your application code that your program can read when it runs. <br>

For example, your database connection requires: <br>

```text
Database host
Database name
Database username
Database password
Database port
```

Instead of writing these values directly in Python: <br>

```text
connection = psycopg2.connect(
    host="localhost",
    database="url_shortener",
    user="postgres",
    password="your_password",
    port="5432"
)
```

 <br>
We store them in a configuration file: <br>

```text
DB_HOST=localhost
DB_NAME=url_shortener
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

 <br>
Then Python reads them. <br> <br>

Why is this important? <br>

The same application may run in different environments: <br>

```text
Environment        Database
Development     Local PostgreSQL
Testing         Test database
Production      Cloud database
```

 <br>
You should not modify your Python code every time the database changes. <br>

Instead, you change the configuration. <br>

----

# Why Hardcoding Is a Problem

❌ Hardcoded configuration <br>

```text
DB_PASSWORD = "my_secret_password"
```

 <br>
Problems: <br>

- Password may accidentally be uploaded to GitHub. 
- Different environments require code changes. 
- Team members may need different configurations. 
- Rotating credentials becomes inconvenient. <br> <br>

✅ Environment variables <br>

```text
import os

password = os.getenv("DB_PASSWORD")
```

 <br>
Benefits: <br>

- Configuration is separated from application code.
- Secrets are less likely to be committed to Git.
- Different environments can use different values.
- Configuration can be supplied by deployment platforms.
- <br>

Important: A .env file is not automatically secure. It must be protected and excluded from Git.<br>

---

# How .env Works

Your project uses the python-dotenv package. <br>

The flow is: <br>

```text
  .env file
DB_HOST, DB_USER, DB_PASSWORD
     ⬇
  load_dotenv()
     ⬇
  os.getenv("DB_HOST")
     ⬇
  Database connection
```

 <br>
Important distinction <br>

- .env is a file containing configuration values.

- An environment variable is a value available to the running process.

- load_dotenv() loads values from .env into the process environment.

  <br>
In production, configuration is often provided directly by the hosting platform rather than using a .env file.<br>

---

# Practice Environment Variables Separately

**.env**  <br>

```text
APP_NAME=URL Shortener
APP_ENVIRONMENT=development
DEBUG=true
```

<br>

**main.py** <br>

```text
import os

from dotenv import load_dotenv

app_name = os.getenv("APP_NAME")
app_environment = os.getenv("APP_ENVIRONMENT")
debug_mode = os.getenv("DEBUG")

print("Application:", app_name)
print("Environment:", app_environment)
print("Debug mode:", debug_mode)
```

<br>

```text
 python main.py
```

<br>

---

# Understand os.getenv()

```text
os.getenv("DB_HOST")
```

<br>
This retrieves the value of DB_HOST. <br>

If the variable exists <br>
DB_HOST=localhost <br>

Python receives: <br>

"localhost" <br> <br>
If the variable does not exist <br>
os.getenv("UNKNOWN_VARIABLE") <br>

The result is: <br>

None <br> <br>

**You can provide a default value:** <br>

```text
os.getenv("DB_PORT", "5432")
```

 <br>
This means: <br>

Use the DB_PORT environment variable. If it doesn't exist, use "5432". <br>

**Why defaults can be risky** <br>

Defaults are useful for non-sensitive values, but silently defaulting a missing production password or database name can hide configuration problems. <br>

For important settings, explicit validation is better
 <br>

---
 
# Improve Your Project Structure

Currently, your database configuration is read directly inside app/db.py. <br>

```text
app/
├── __init__.py
├── main.py
├── config.py
├── db.py
├── models.py
└── routes/
    ├── __init__.py
    └── urls.py
```

 <br>
Responsibility of each file <br>

```text
File                  Responsibility
config.py         Load and validate configuration
db.py             Create database connections
models.py         Validate request data
urls.py           Handle URL endpoints
main.py           Start and configure FastAPI
```

 <br>
This is a basic configuration layer. Later, you can learn more advanced settings management using Pydantic Settings. <br>

---

# Create app/config.py

Create this file: <br>

app/config.py <br>

Add: <br>

```text
import os

from dotenv import load_dotenv


load_dotenv()


def get_required_environment_variable(name):
    value = os.getenv(name)

    if value is None or value.strip() == "":
        raise RuntimeError(
            f"Required environment variable '{name}' is missing"
        )

    return value


DB_HOST = get_required_environment_variable("DB_HOST")
DB_NAME = get_required_environment_variable("DB_NAME")
DB_USER = get_required_environment_variable("DB_USER")
DB_PASSWORD = get_required_environment_variable("DB_PASSWORD")
DB_PORT = get_required_environment_variable("DB_PORT")
```

<br>

**Understand the helper function** <br>
def get_required_environment_variable(name): <br>

This function receives a variable name. <br>

For example: <br>

get_required_environment_variable("DB_HOST") <br>

It checks whether the value exists. <br>

If the value is missing: <br>

raise RuntimeError(...) <br>

The application will show a clear error instead of failing later with an unclear database error. <br> <br>

Why is this reusable? <br>

You can use the same helper for: <br>

- API keys

- Database credentials

- JWT secret keys

- Cloud configuration

- External service URLs

---

# Update app/db.py

Open: <br>

app/db.py <br>

Replace its content with: <br>

```text
import psycopg2

from app.config import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER
)


def get_connection():
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    return connection
```

 <br>

 What changed? <br>
Before <br>

db.py loaded environment variables itself: <br>

```text
load_dotenv()
os.getenv("DB_HOST")
```

 <br> <br>
Now <br>

config.py handles configuration: <br>

```text
from app.config import DB_HOST
```

 <br>
db.py only handles the database connection. <br>

This is separation of responsibilities. <br>

---

# Understand the Import Flow

Your application now works like this: <br>

```text
app/routes/urls.py
        |
        └── imports get_connection()
                    |
                    └── app/db.py
                              |
                              └── imports configuration
                                        |
                                        └── app/config.py
                                                  |
                                                  └── reads .env
```

<br>
The route does not need to know:  <br>

- Where the password is stored.

- How .env is loaded. 

- How configuration is validated.

<br>
It only requests a database connectio.. <br>

---

# Improve Configuration Further

The current config.py validates that values exist, but it does not validate their types. <br>

For example, environment variables are strings: <br>

DB_PORT = "5432" <br> <br>

You can convert the port to an integer: <br>

```text
DB_PORT = int(
    get_required_environment_variable("DB_PORT")
)
```

 <br>
Then your configuration contains: <br>

DB_PORT = 5432 <br> <br>
Why does type conversion matter? <br>

A port should represent a number. Type validation helps catch invalid values early. <br>

For now, update only the DB_PORT line in app/config.py: <br>

```text
DB_PORT = int(
    get_required_environment_variable("DB_PORT")
)
```

 <br>
If someone writes: <br>

DB_PORT=wrong <br>

the application will fail during configuration loading instead of producing a less direct database connection error. <br>

---

# Test Your Updated Application
1. Check the project root
2.  <br>

Your .env should contain the database configuration. <br>

Do not paste your password into GitHub or chat messages. <br>

2. Start FastAPI
 <br>
From the project root: <br>

uvicorn app.main:app --reload <br>
3. Test the home endpoint
 <br>
Open: <br>

http://localhost:8000/ <br>

Expected: <br>

```text
{
  "message": "URL Shortener API is running"
}
```


4. Test creating a short URL
 <br>
Open: <br>

http://localhost:8000/docs <br>

Use POST /urls: <br>

```text
{
  "original_url": "https://github.com"
}
```

 <br>
If the response is successful, your new configuration system is working with the database. <br>

---

# .gitignore and Security

Your .gitignore should contain: <br>

```text
venv/
.env
__pycache__/
*.pyc
```

 <br>
Check Git's tracking status: <br>

git status <br> <br>

If .env has already been committed to Git, adding it to .gitignore alone does not remove it from Git history. <br>

You would need to remove it from tracking and handle any exposed credentials appropriately. <br>

**Security reminder** <br>

If the database password you previously shared is a real and still-active password, change it in PostgreSQL and update your .env. Avoid reusing exposed credentials. <br>

---

# Development vs Production

```text
Development                                   Production
Local .env file                        Deployment-managed configuration
Local PostgreSQL                       Managed or secured database
Local credentials                      Restricted credentials
Debugging enabled as needed            Debugging configured carefully
Developer machine                      Cloud server/container
```

<br>
The application code can remain mostly the same while the configuration changes. <br>

This is one of the main advantages of environment-based configuration. <br>

---













