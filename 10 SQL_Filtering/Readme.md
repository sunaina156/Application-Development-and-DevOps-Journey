Filtering: <br>
Filtering means selecting only the rows that satisfy a particular condition. <br>

Suppose we have: <br>
```text
users

id | name    | age | city
---+---------+-----+--------
1  | Sunaina | 21  | Guna
2  | Rahul   | 25  | Delhi
3  | Aman    | 19  | Bhopal
4  | Priya   | 30  | Indore
5  | Riya    | 21  | Delhi
```

If we want  only users whose age is 21: <br>
```text
SELECT *
FROM users
WHERE age = 21;
```

Result: <br>
1 | Sunaina | 21 | Guna
5 | Riya    | 21 | Delhi

---

# WHERE Clause
The primary SQL filtering tool is: <br>
```text
WHERE
```

Basic Syntax: <br>
```text
SELECT column1, column2
FROM table 
WHERE condition;
```

Ex: <br>
```text
SELECT name, age
FROM users
WHERE age > 20;
```

---

# Comparison Operators
The main comparison operators are: <br>
```text
Operator	Meaning
=	Equal
<>	Not equal
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
```

**Equal** <br>
```text
SELECT *
FROM users
WHERE city = 'Delhi';
```

<br>

**Not Equal** <br>
```text
SELECT *
FROM users
WHERE city <> 'Delhi';
```
<br>

**Greater Than** <br>
```text
SELECT *
FROM users
WHERE age > 21;
```
<br>

**Less Than** <br>
```text
SELECT *
FROM users
WHERE age < 21;
```
<br>

**Greater Than or Equal** <br>
```text
SELECT *
FROM users
WHERE age >= 21;
```
<br>

**Less Than or Equal** <br>
```text
SELECT *
FROM users
WHERE age <= 21;
```
<br>

---

# Filtering Text
Text values are normally written inside single quotes: <br>
```text
WHERE name = 'Sunaina'
```

Correct: <br>
```text
SELECT *
FROM users
WHERE name = 'Sunaina';
```

Don't confuse: <br>
```text
name = 'Sunaina'
```

with: <br>
```text
name = Sunaina
```

The second form treats Sunaina as an identifier rather than a string value. <br>

---

# Filtering Numbers

Numbers don't require quotes. <br>

Correct: <br>
```text
SELECT *
FROM users
WHERE age = 21;
```

Not: <br>
```text
WHERE age = '21'
```

Although some database systems may perform implicit type conversion in certain circumstances, you should write queries using the appropriate data type.

---

# AND
AND combines conditions. <br>
Every condition must be true: <br>
<br>
Ex: <br>
```text
SELECT *
FROM users
WHERE age >= 18
AND city = 'Delhi';
```

Only rows satisfying both conditions are returned.

---

# Multiple AND Conditions

You can have more than two: <br>
```text
SELECT *
FROM users
WHERE age >= 18
AND city = 'Delhi'
AND is_active = TRUE;
```

---

# OR
OR means At least one confition must be true. <br>

Ex: <br>
```text
SELECT *
FROM users
WHERE city = 'Delhi'
OR city = 'Bhopal';
```
This returns users from either city. 

---

# AND + OR

Consider: <br>
```text
SELECT *
FROM users
WHERE city = 'Delhi'
OR city = 'Bhopal'
AND age >= 18;
```

Use parenthese when your intended logic is important: <br>
```text
SELECT *
FROM users
WHERE (city = 'Delhi' OR city = 'Bhopal')
AND age >= 18;
```

---

# Operator Precedence

A simplified order for boolean operators is: <br>
```text
NOT
 ↓
AND
 ↓
OR
```
Therefore: <br>

A OR B AND C <br>

is interpreted roughly as: <br>

A OR (B AND C) <br>

not: <br>

(A OR B) AND C <br>
Important rule <br>

When combining AND and OR, use parentheses if you want a specific grouping.
<br>
This prevents logical mistakes.
<br>

---

# NOT

NOT reverses a condition. <br>

Example: <br>
```text
SELECT *
FROM users
WHERE NOT city = 'Delhi';
```

This means: <br>

Users whose city is not Delhi.
<br>
You can also write:
<br>
```text
SELECT *
FROM users
WHERE city <> 'Delhi';
```

---

# IN

Suppose you want users from: <br>
```text
Delhi
Bhopal
Indore
```
You could write: <br>
```text
SELECT *
FROM users
WHERE city = 'Delhi'
OR city = 'Bhopal'
OR city = 'Indore';
```
But this is easier:
<br>
```text
SELECT *
FROM users
WHERE city IN ('Delhi', 'Bhopal', 'Indore');
```
IN checks whether a value belongs to a specified set.

---

# NOT IN

Opposite of IN. <br>
```text
SELECT *
FROM users
WHERE city NOT IN ('Delhi', 'Bhopal');
```
Meaning: <br>

Return users whose city isn't Delhi or Bhopal. <br>

⚠️ Important NULL issue <br>

NOT IN can behave unexpectedly when the list contains NULL, because SQL uses three-valued logic.
<br>
For now remember:
<br>
Be careful with NULL when using NOT IN.
<br>

---

# BETWEEN

Used to filter a range. <br>
```text
SELECT *
FROM users
WHERE age BETWEEN 18 AND 25;
```

This is equivalent conceptually to: <br>
```text
age >= 18
AND
age <= 25
```
Important <br>

BETWEEN is inclusive.
<br>
So: <br>
```text
18 → included
25 → included
```

---

# NOT BETWEEN
```text
SELECT *
FROM users
WHERE age NOT BETWEEN 18 AND 25;
```

Returns values outside that range.


---

# LIKE

LIKE is used for pattern matching. <br>

Suppose: <br>
```text
Sunaina
Sunil
Suresh
Rahul
Aman
```

Find names beginning with Su: <br>
```text
SELECT *
FROM users
WHERE name LIKE 'Su%';
```

Result: <br>
```text
Sunaina
Sunil
Suresh
```

---

# % Wildcard

% means: <br>

Zero or more characters. <br>

Starts with S <br>
```text
WHERE name LIKE 'S%';
```

Ends with a <br>
```text
WHERE name LIKE '%a';
```

Contains "ain" <br>
```text
WHERE name LIKE '%ain%';
```

Exactly starts and ends with specific text <br>
```text
WHERE name LIKE 'Su%a';
```

---

# _ Wildcard

_ means: <br>

Exactly one character.  <br>

Example: <br>

WHERE name LIKE 'A_an'; <br>

The _ represents one character. <br>

So values such as: <br>

Aman <br>
Alan <br>

can match the pattern.
<br>

---

# LIKE vs =

This is important. <br>

WHERE name = 'Sunaina' <br>

means: <br>

Exact value. <br>
<br>
While: <br>

WHERE name LIKE 'Sun%' <br>

means: <br>

Any value beginning with Sun. <br>

So:
<br>
=       → exact comparison <br>
LIKE    → pattern matching <br>

---


# NOT LIKE

You can exclude patterns: <br>
```text
SELECT *
FROM users
WHERE name NOT LIKE 'S%';
```

Meaning: <br>

Names that don't start with S. <br>

---


# ILIKE in PostgreSQL

PostgreSQL provides: <br>

ILIKE <br>

for case-insensitive pattern matching.
 <br>
Example: <br>
```text
SELECT *
FROM users
WHERE name ILIKE 'sun%';
```

This can match different capitalization such as: <br>

Sunaina <br>
sunaina <br>
SUNAINA <br>

ILIKE is PostgreSQL-specific rather than standard SQL.
<br>

---

# NULL Filtering

Suppose: <br>
```text
users 

id | name    | phone
---+---------+-------------
1  | Sunaina | 9876543210
2  | Rahul   | NULL
3  | Aman    | 9123456789
```

To find users without phone numbers: <br>
```text
SELECT *
FROM users
WHERE phone IS NULL;
```

---

# IS NOT NULL

To find users who have a phone number: <br>
```text
SELECT *
FROM users
WHERE phone IS NOT NULL;
```

---

# Why = NULL Doesn't Work

Don't write: <br>

WHERE phone = NULL; <br>

Use: <br>

WHERE phone IS NULL;
<br>
Why? <br>

Because NULL means:
<br>
Unknown / missing value.
<br>
SQL doesn't treat it like an ordinary value.
<br>

---

# SQL Three-Valued Logic

This is useful for difficult questions. <br>

Normal programming often thinks in: <br>
```text
TRUE 
FALSE 
```

SQL has:
<br>
```text
TRUE
FALSE
UNKNOWN
```

For example: <br>

NULL = 5 <br>

doesn't produce ordinary TRUE or FALSE; it evaluates to UNKNOWN. <br>

Similarly: <br>

NULL = NULL <br>

is not TRUE. <br>

That's why: <br>

IS NULL <br>

is used instead. <br>

---

# Filtering Dates

Suppose: <br>
```text
orders

id | order_date
---+-------------------
1  | 2026-08-01
2  | 2026-08-15
3  | 2026-09-01
```

Find orders after August 10: <br>
```text
SELECT *
FROM orders
WHERE order_date > '2026-08-10';
```

Find orders on or after August 15: <br>
```text
SELECT *
FROM orders
WHERE order_date >= '2026-08-15';
```

---

# Date Range Filtering

```text
SELECT *
FROM orders
WHERE order_date BETWEEN '2026-08-01' AND '2026-08-31';
```

This works straightforwardly when order_date is a DATE. <br>

Important with timestamps <br>

If the column is a TIMESTAMP, blindly using: <br>

BETWEEN '2026-08-01' AND '2026-08-31' <br>

can exclude much of August 31 because the upper bound may represent midnight at the start of that date. <br>

A safer half-open range is often: <br>
```text
WHERE created_at >= '2026-08-01'
AND created_at < '2026-09-01'; 
```

This is an important real-world SQL habit.

---

# Filtering with Multiple Conditions

Suppose your products table is: <br>
```text
id | name | price | category | stock
```

Find electronics under ₹50,000 that are in stock: <br>
```text
SELECT *
FROM products
WHERE category = 'Electronics'
AND price < 50000
AND stock > 0;
```

This is how real application filtering starts to look.

---

# Filtering + ORDER BY

You can combine filtering and sorting:

SELECT *
FROM products
WHERE price < 50000
ORDER BY price DESC;

Logical idea:

All products
    ↓
price < 50000
    ↓
Sort remaining products
    ↓
Highest price first

# Filtering + LIMIT
SELECT *
FROM products
WHERE category = 'Electronics'
ORDER BY price DESC
LIMIT 5;

Meaning:

Find electronics, sort by highest price, return the top 5.

# Filtering + DISTINCT
SELECT DISTINCT city
FROM users
WHERE age >= 18;

Meaning:

Find unique cities among users aged 18 or older.

# Filtering Your URL Shortener

Now connect Day 10 to the application you'll eventually build.

Suppose:

urls

id | short_code | original_url | clicks | user_id
Find a particular short URL
SELECT *
FROM urls
WHERE short_code = 'abc123';
Find popular URLs
SELECT *
FROM urls
WHERE clicks > 100;
Find URLs with no clicks
SELECT *
FROM urls
WHERE clicks = 0;
Find highly popular URLs
SELECT *
FROM urls
WHERE clicks >= 1000
ORDER BY clicks DESC;
Find URLs belonging to specific users
SELECT *
FROM urls
WHERE user_id IN (1, 3, 5);
Search URLs containing a word
SELECT *
FROM urls
WHERE original_url LIKE '%github%';

# Combining Conditions for URL Shortener

Suppose you want:

URLs belonging to user 1 that have received more than 100 clicks.

SELECT *
FROM urls
WHERE user_id = 1
AND clicks > 100;

Another:

URLs belonging to user 1 or 2 that have more than 500 clicks.

SELECT *
FROM urls
WHERE user_id IN (1, 2)
AND clicks > 500;

# A More Difficult Query

Suppose the requirement is:

Find URLs that belong to user 1 or user 2, have more than 100 clicks, and whose original URL contains "github".

SELECT *
FROM urls
WHERE user_id IN (1, 2)
AND clicks > 100
AND original_url LIKE '%github%';

Break it down:

user_id IN (1,2)
       ↓
     AND
       ↓
clicks > 100
       ↓
     AND
       ↓
URL contains github

This is the kind of query you should become comfortable reading.

# Filtering and Logical Thinking

Don't memorize SQL syntax only.

Translate requirements into logical conditions.

Requirement:

Find active users from Delhi who are at least 18.

Think:

active
AND
Delhi
AND
age >= 18

Then:

SELECT *
FROM users
WHERE is_active = TRUE
AND city = 'Delhi'
AND age >= 18;

This habit will make SQL much easier.

# A Useful Mental Model

Whenever you see:

SELECT ...
FROM ...
WHERE ...

think:

FROM
 ↓
Choose the table

WHERE
 ↓
Filter the rows

SELECT
 ↓
Choose what to display

For example:

SELECT name, email
FROM users
WHERE age >= 18;

Think:

users
 ↓
keep age >= 18
 ↓
show name + email

# Common Filtering Mistakes
Mistake 1

Using = with NULL:

WHERE email = NULL;

❌ Wrong.

Use:

WHERE email IS NULL;
Mistake 2

Forgetting quotes around strings:

WHERE city = Delhi;

❌ Wrong.

Use:

WHERE city = 'Delhi';
Mistake 3

Using quotes unnecessarily around numbers:

WHERE age = '21';

Prefer:

WHERE age = 21;
Mistake 4

Incorrect AND/OR logic:

WHERE city = 'Delhi'
OR city = 'Bhopal'
AND age >= 18;

If you mean both cities and age ≥ 18:

WHERE (city = 'Delhi' OR city = 'Bhopal')
AND age >= 18;
Mistake 5

Using LIKE for exact matching

If you need exactly:

Sunaina

use:

WHERE name = 'Sunaina';

rather than:

WHERE name LIKE '%Sunaina%';

unless pattern matching is actually what you want.


















