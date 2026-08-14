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

