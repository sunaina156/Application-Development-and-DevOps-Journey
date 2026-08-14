# First Python Program

```python
print("Hello World")
```

print() is used to display something on the screen.

---

# Python Variables

A variable is a name used to store a value.

```python
name = "Sunaina"
age= 21

print(name)
print(age)
```

```python
long_url = "https://example.com"
short_code = "aB92x"

print(long_url)
```

---

# Python Data Types

| Type | Meaning | Example |
|----------|----------------|----------------|
| string | String/text | "Hello"|
| int | Integer | 21|
| float | Decimal | 10.5 |
| bool | True/False | True | 
| list | Collection | [1, 2, 3] | 
| dict | key-value data | {"name": "Sunaina"} | 


Ex:
```python
name = "Sunaina"    # str
age = 21            # int
price = 99.5        # float
is_student = True   # bool
skills = ["Python", "AWS"]   # list
user = {"name": "Sunaina", "age": 21}  # dict

print(user)

```

---

# Checking Data Types

Python provides type()

```python
name = "Sunaina"
print(type(name))

age = 21
print(type(age))
```

output:
```text
<class 'str'>
<class 'int'>
```

--- 

# Strings

A string represents text.

```python
name = "Sunaina"
url = "https://example/com"
```

**We can combine strings.**

```python
name = "Sunaina"
print("Hello " + name)
```

output:
```text
Hello Sunaina
```

**A better way is an f-string**

```python
name = "Sunaina"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

output:
```text
My name is Sunaina and I am 21 years old.
```

---

# Numbers and Operators

Python supports normal mathematical operators:  <br>
+   Addition  <br>
-    Subtraction  <br>
*   Multiplication  <br>
/    Division  <br>
%  Modulus  <br>
//   Floor division  <br>
**  Power  <br>


Ex:
```python
a = 10
b = 3

print(a + b) 
print(a - b)
print(a * b)
print(a / b)
print(a % b)
```

---
# Comparison Operators

These are used to compare values

```text
==   Equal
!=    Not equal
>     Greater than
<     Less than
>=   Greater than or equal
<=   Less than or equal
```

Ex:
```python
age = 21
print(age >= 18)
```

output:
```text
True
```

---

# Boolean Values

Boolean has only two values
```python
True
False
```

Ex:
```text
is_logged_in = True
is_admin = False
```

These are extremely important for application logic.

Ex:
```text
if is_logged_in:
  print("Welcome")
```

---

# Conditional Statements




















