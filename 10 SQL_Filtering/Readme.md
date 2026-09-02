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

























