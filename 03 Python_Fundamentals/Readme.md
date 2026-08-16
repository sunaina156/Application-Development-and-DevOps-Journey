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

Python is dynamically typed, so we don't need to specify the data type while declaring a variable.

```Python
x = 10
x = "Hello"
```

The typpe of x can change bcoz the name can refer to a different object.


---

# Python Data Types

| Type | Meaning | Example |
|----------|----------------|----------------|
| str | String/text | "Hello"|
| int | Integer | 21|
| float | Decimal number | 10.5 |
| bool | Boolean value (True/False) | True | 
| list | ordered, mutable collection | [1, 2, 3] | 
| tuple | Ordered, immutable collection |  (1, 2, 3) |
| set | unordered collection of unique values | {1, 2, 3} | 
| dict | key-value data | {"name": "Sunaina"} |
| None | Absence of a value | None | 
 

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
# Mutable vs Immutable

## Immutable
An immutable object cannot be changed after it is created.

Ex:
```text
int
float
bool
str
tuple
```

Ex:
```python
name = "Python"
#name[0] = "J"  # error
```
A new string must be created instead

## Mutable
A mutable object can be changed after creation.

Ex:
```text
list
dict
set
```

Ex:
```python
skills = ["Python", "Docker"]
skills.append("kubernetes")

print(skills)
```

output:
```text
['Python', 'Docker', 'kubernetes']
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

Strings are ordered sequences of characters. <br>

**Access characters**
```python
language = "Python"

print(language[0])
print(language[-1])
```

output:
```text
p
n
```

**String slicing**
```python
language = "Python"

print(language[0:3])
```

output:
```text
Pyt
```

General Syntax:
```text
string[start:stop:step]
```
stop index is not included


## Common String Methods

```text
text = "  Hello Python  "

text.lower()
text.upper()
text.strip()
text.replace("Python", "World")
text.startswith("Hello")
text.endswith("Python")
text.split()
```

# Lists

A list is an ordered and mutable collection.

```python
skills = ["Python", "Docker", "Kubernetes"]

# Access elements
print(skills[0])

# Modify an element
skills[0] = "Java"
print(skills)

# Add an element
skills.append("Terraform")
print(skills)

# Remove an element
skills.remove("Java")
print(skills)
```

output:
```text
Python
['Java', 'Docker', 'Kubernetes']
['Java', 'Docker', 'Kubernetes', 'Terraform']
['Docker', 'Kubernetes', 'Terraform']
```


# Tuples

A tuple is an ordered and immutable collection.

```python
coordinates = (10, 20)

# Access
print(coordinates[0])    # Output: 10

# but we cannot modify the tuple
# coordinates[0] = 30    
```

Use a tuple when the collection should not be changed.


# Sets
A set is a collection  of unique elements.

```python
skills = {"Python", "Docker", "Python", "Kubernetes"}
print(skills)

# duplicate "Python" is removed
```

Sets are useful when we need:
- unique values
- fast membership checking
- Set operations such as union and intersection


# Dictionaries

A dictionary stores data as key-value pairs.

```python
user = {
    "name": "Sunaina",
    "age": 21,
    "role": "student"
}

# Access a value
print(user["name"])

# Modify
user["age"] = 22

# Add a new key-value pair
user["city"] = "Guna"
```

Dictionaries importance:
Dictionaires are heavily used in backend development bcoz API data  is commonly represented in JSON.

```text
{
    "long_url": "https://example.com",
    "short_code": aB92x
}
```


# None
It represents the absence of a value

```text
user = None
```

Ex: if database search doesn't find a user:
```python
user = find_user(10)

if user is None:
  print("User not found")
```

Use:
```text
is None
```

rather than:
```text
== None
```

---
# Type Conversion

Type conversion means converting a value from one data type to another.

```python
age = "21"
age = int(age)
# now age is an integer
```

```text
int("10")
float("10.5")
str(100)
list("ABC")
```

---

# Input and Output

## output
print() displays information
```text
print('Hello Python")
```

## Input
input() takes input from the user
```python
name = input("Enter your name: ")
print(name)
```

input() always returns a string <br>


```text
age = int(input("Enter age: "))
# therefore  int is reqired when an integer is needed
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

# Operators

# Arithmetic Operators
```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
//   Floor Division
%    Modulus
**   Power
```

Ex:
```python
a = 10
b = 3
print(a + b)
print(a % b)

## Comparison Operators

```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
//   Floor Division
%    Modulus
**   Power
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


## Logical Operators
```text
and
or
not
```

Ex:
```python
age = 21
has_id = True

if age >= 18 and has_id:
  print("Allowed")
```

---

# == vs is


**=**
Checks whether two objects have the same value

```python
a = [1, 2]
b = [1, 2]
print(a == b)
```

output:
```text
True
```

**is**
Checks whether two variables refers to the same object.

```text
print(a is b)
```

```text
output:
False
# bcoz a and v are separate list objects
```

---

# Conditional Statements

Conditonal statements allow a program to make decisions.

```python
age = 21

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

```python
#Multiple conditions:

marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

---

# Truthy and Falsy Values
Python evaluates certain values as Fase when used in a condition

```text
# Common falsy values:
False
None
0
""
[]
{}
set()
```

Ex:
```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")
```

output:
```text
Name is empty
```

--- 

# Loops

Loops are used to execute code repeatedly.

**for loop**
```python
skills = ["Python", "Docker", "Kubernetes"]

for skill in skills:
    print(skill)
```

**while loop**
```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---
# range()

range() generates a sequence of numbers

```python
for i in range(5):
  print(i)
```

output:
```text
0 
1
2
3
4
```

syntax: <br>
range(start, stop, step)  <br>

Ex:
















