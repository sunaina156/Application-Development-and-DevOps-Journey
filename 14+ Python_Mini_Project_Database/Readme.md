# Install Python

```text
> python --version
```

<br>

# Instal PostgreSQL
remember the password

<br>

# Create virtual environment
```text
> python -m venv venv
```

<br>

# Activate Virtual Environmnt 

```text
> .\venv\Scripts\Activate.ps1
```

<br>

# Install Python Dependencies

```text
> pip install -r requirements.txt
```

<br>
Check: <br>

```text
> pip list
```

<br>

# Create the PostgreSQL database

```text
> psql -U postgres
```

<br>

```text
postgres-# CREATE DATABASE url_shortener;
```

# Connect to the database

```text
> \c url_shortener
```

<br>

Verify: <br>

```text
> SELECT current_database():
```

<br>

#  Create all tables

```text
> \i database.sql
```
(This executes everything inside yur database.sql) <br> <br>

Verify: <br>

```text
> \dt
> \d users
```

<br>

# Insert sample data

```text
> \i seed.sql
```

<br>

# Verify the users

```text
> SELECT * FROM users;
```

<br>

# Verify URLs

```text
> SELECT * FROM urls;
```

<br>

# Verify clicks:

```text
> SELECT * FROM clicks;
```

<br>
Practice Indexes, Relationships, Transactions <br>

# Edit .env 
# Run your Python Application
Make sure the virtual environment is active: <br>
(venv) <br>

```text
> python main.py
```

<br>

# Test Shorten URL
Enter: 1 <br>
Then : https://github.com <br>
You get shortcode <br>
Then PostgreSQL <br>
> SELECT * FROM urls; <br>
shoul contain the newly inserted URL <br>
17. Test Retrieve URL <br> 
Run program <br>
choose: 2 <br>
Enter generated code <br>
Expected:  <br>
Original URL: https://github.com <br>
