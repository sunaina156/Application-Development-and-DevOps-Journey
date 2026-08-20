# Modules in Python

A module is a single Python file (.py) containing Python code. <br>
It can include functions, classes, and variables that you can reuse in other programs.  <br>

**Why use modules**?
- To organize code into smaller, manageable chunks.
- To reuse code across multiple programs.

```python
# Create a module:
# Save the following as mymodule.py

def say_hello(name):
  return print(f"Hello, {name}!")
```

```python
#Use the module:
import mymodule
greetings.say_hello("Madhav")     # Output: Hello, Madhav!
```

---

# Packages in Python

A package is a collction of modules organized in directories (folder) with an __init_.py file .  <br>
It allows you to structure your Python projects logically.

**Why use packages?**
- To group related modules together.
- To create larger applications or libraries.

**#Structure Example:**   <br>
my_package/   <br>
&nbsp;&nbsp;  __init__.py   <br>
&nbsp;&nbsp;  math_utils.py   <br>
&nbsp;&nbsp;  string_utils.py   <br>

**#Use the package:**   <br>
Syntax: **from** my_package **import** <package_name>  <br>
Example: **from** my_package **import** math__utils, string_utils

---

Module Example   <br>

mymodule.py

```python
# def say_hello(name):
#     return print(f"Hello, {name}!, kaise ho?")

# def say_bye(name):
#     return print(f"Bye, {name}!, take care")

#-------

person1 = {'name': 'Keshav', 'age': 23}

#-----------------------
```

main.py

```python
# import mymodule

# mymodule.say_hello("Sunaina")
# mymodule.say_bye('Sunaina')

# -------------------

from mymodule import person1

print(person1['age'])

#-------------------------
```

---

# Libraries in Python

A library is a collection of modules and packages that provide pre-written functionality for your program.  <br>
Libraries are typically larger and more feature-rich than packages or modules.  <br>

**Why use libraries?**  
- To avoid writing common functionality from scratch.
- To leverage powerful tools developed by the community.


**Example:**<br>
Python has many popular libraries, such as:  <br>
- Pandas: For data manipulation
- Matplotlib: For plotting and visualization

**#Using a library (Pandas):**
import pandas as pd

---

# Python PIP

pip stands for "Pip Install Packages". <br>
It is the package manager for Python that allows you to install, update, and manage Python libraries (packages) from the Python Package Index (PyPI).  <br>

Think of pip as an app store for Python libraries. You use it to search, install, and manage Python tools, just like downloading apps on your phone.  <br>

When you use pip install <package_name>, it:
- Connects to PyPI (Python Package Index) online.
- Downloads the specified library or package.
- Installs it into your Python environment.

To install packages, we use: **pip install <library_name>**  <br>
Example:  installing pandas to work on dataframe: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                 **pip install pandas**

---

main.py

```python
# library: collection of modules and packages

# inbuilt library
import math

A = 16
print(math.sqrt(A))

# import specific function from library
from math import factorial
B = 4
print(factorial(B))

```

<img width="1103" height="591" alt="image" src="https://github.com/user-attachments/assets/655c9516-90b0-4e1d-90bc-e4d04e3a57b6" />

<img width="1128" height="582" alt="image" src="https://github.com/user-attachments/assets/15106af4-848a-4b75-80e4-5600c07519c4" />

---
---
---

# Exception Handling

## Why Exception Handling ?
- Exceptions are unexpected events that disrupt your program's normal flow.
- They occur during runtime (e.g., dividing by zero, missing files, type errors).

## Why this is a problem in the real world?
- An ATM that crashes when you enter the wrong PIN.
- A hospital app that stops when a file is missing.
- An exam portal that breaks when the network drops.
<br>
- Every program must handle unexpected situations gracefully.

## What if the program can recover on its own?

```python
try:
  marks = int(input("Enter marks: "))
  percentage = (marks / total) * 100
  print(percentage)
except:
print("Please enter a valid number!")
```

```text
Enter marks: abc
Please enter a valid number!
```

No crash. No red error. This is Exception Handling.

---
## Types of Errors 

There are two types of program errors.
- COMPILE-TIME
Syntax Errors  <br>
Caught before the program runs. <br>
<br>
SYNTAX ERROR - BEFORE RUN

```text
print("Hello"  # missing closing bracket
```

```text
SyntaxError: unexpected EOF
  while parsing
```

- RUN-TIME
Exceptions <br>
Occur while the program is running. <br>
<br>
RUN-TIME ERROR - DURING RUNTIME

```text
print(10 / 0)
```

```text
ZeroDivisionError: division by zero
```

---

**So what exactly is an Exception?**  <br>
An Exception is an anomalous or unexpected event that occurs during runtime and disrupts the normal flow of the program. <br>
<br>
- It is not a syntax error
- It occurs when the program is already runing
- If unhandled -> the program crashes

"Every syntax error is an exception, but every exception is NOT a syntax error."

<img width="949" height="554" alt="image" src="https://github.com/user-attachments/assets/4966989a-5e42-4c08-87cc-36b1716554e5" />

---

# How does Exception Handling Works ?

1. **TRY** <br>
&nbsp;&nbsp;&nbsp;&nbsp;Risky code in a try block
2. **RAISE**  <br>
&nbsp;&nbsp;&nbsp;&nbsp; Python raises an exception.
3. **CATCH** <br>
&nbsp;&nbsp;&nbsp;&nbsp; The except block catches & handles it. <br>


<img width="896" height="265" alt="image" src="https://github.com/user-attachments/assets/3a9a928d-98b3-4dbd-8a48-9945f19b439d" />

---

# try ... except

### The basic shape

```python
try:
  # code that might cause an exception
except:
  # what to do when it occurs
```

**Example 1: Division** <br>

```python
try:
    print("result of 10/5 =", (10/5))
    print("result of 10/0 =", (10/0))
except:
    print("Divide by Zero! Denominator", "must not be zero!")
    
```

**Example 1: Type Conversion** <br>

```python
try:
    x = int("XII")
except:
    print("Error converting 'XII' to a number")
```

---

## Built-in Exceptions <br>

Python has a name for every common error. <br>

<img width="908" height="661" alt="image" src="https://github.com/user-attachments/assets/2f9e37a4-9fbc-421b-bdb0-4b9fa497808a" />
<br>

<img width="1120" height="379" alt="image" src="https://github.com/user-attachments/assets/47280f35-a242-46a5-9e2b-dba6516ef5a4" />
<br>

<img width="938" height="226" alt="image" src="https://github.com/user-attachments/assets/75ae05a8-2806-4f29-8275-57dbe9b30cea" />

<img width="608" height="561" alt="image" src="https://github.com/user-attachments/assets/8ad6de1f-3a3c-4e3e-aa24-e945e0c4ae2e" />
<br>

<img width="615" height="215" alt="image" src="https://github.com/user-attachments/assets/6a1d532b-2d42-4461-9ae2-830bd8e035a4" />

<br>

---

## Multiple except - else

<img width="1076" height="610" alt="image" src="https://github.com/user-attachments/assets/da7d4aee-0e6c-4b20-bf88-faef38f5fa3f" />
<br>

```python
try:
    my_file = open("myfile.txt")
    my_line = my__file.readline()
    my_int = int(my_line.strip())
    value = 101 / my_int

except IOError:
    print("I/O error occured")
except ValueError:
    print("Could not convert to an integer.")
except ZeroDivisionError:
    print("Division by zero error")
except:
    print("Unexpected error")
else:
    print("Hurray! No exceptions!")
```

- Only one except block runs - the first one that matches.
- else only runs if try completed with zero exceptions

---

# THE FINALLY BLOCK

- The block that always runs.
- **finally** runs whether or not an exception occured
- Used for cleanup: closing files, releasing resources, logging

```python
try:

# statements that may raise an 
exception except:

# handle exception finally:

# THIS ALWAYS RUNS - exception or not
```


**Example 1** <br>

```python
# No Error
text = "78"

try:
    marks = int(text)
except ValueError:
    print("Not a number")
else:
    print("Marks: ", marks)
finally:
    print("Done checking")
```

```python
# ERROR Raised
text = "abc"

try: 
    marks = int(text)
except ValueError:
    print("Not a number")
else:
    print("Marks: ", marks)
finally:
    print("Done checking")
```

**finally** runs in BOTH cases - error or no error  <br>

<img width="1066" height="449" alt="image" src="https://github.com/user-attachments/assets/3d283a8b-fbf0-4ca8-97e1-b24fce4979d0" />
 <br>

<img width="1221" height="587" alt="image" src="https://github.com/user-attachments/assets/1f60156c-e6a0-4363-98c3-94c88449da43" />
<br>

---

### RAISE - FORCING AN EXCEPTION

**You can force an exception too** <br>
- So far Python raises exceptions automatically.
- With raise: you can force an exception to occur
- Useful when you want to enforce your own rules

```text
raise ExceptionName("your custom message")
```

**Example:** <br>

```python
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    if b == 0:
        raise ZeroDivisionError(str(a) + "/0 not possible")
    print(a/b)
except ZeroDivisionError as e:
    print("Exception", str(e))
```

output: <br>

```text
Enter numerator: 7
Enter denominator: 0
Exception 7/0 not possible
```

- We manually raised the exception before reaching the division.
- The message "7/0 not possible" is our own, printed via str(e)
 

---

### ASSERT STATEMENT

A built-in debugging tool.  <br>

```text
assert condition [, error_message]
```

- If the condition is **True** -> nothing happens, program continues
- If the condition is **False** -> raises AssertionError with the optional message
<br>
- Use a assert statement when you know what a value should be, and want to catch it early if it's wrong.

**Example:** <br>

```python
n = int(input("Enter Numerator: "))
d = int(input("Enter Denominator: "))

assert d != 0, "Denominator must not be 0"

print("n/d =", int(n/d))
```

output:

```text
Enter Numerator: 10
Enter Denominator: 10
n/d = 1
```

```text
    assert d != 0, "Denominator must not be 0"
           ^^^^^^
AssertionError: Denominator must not be 0
```

<img width="1098" height="409" alt="image" src="https://github.com/user-attachments/assets/687d4b60-3c7b-430c-a334-80d1a46ef583" />
<br>

**Example 1:** <br>

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

# divide(2, 1)
# divide(2, 0)
# divide("2", "1")
```

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
```
output:

```text
# divide(2, 1)
result is 2.0
executing finally clause
```

```text
# divide(2, 0)
division by zero!
executing finally clause
```

```text
# divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "C:\Users\sunaina\Desktop\py\main.py", line 13, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
```

**finally** runs in all three cases - even when an unhandled exception crashes the program.

<br>
<br>

**Example 2:** <br>

```python
print("Learning Exceptions...")

try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    quotient = (num1 / num2)
    print("Both numbers were correct")

except ValueError:   # only integers
    print("Please enter only numbers")
except ZeroDivisionError:   # not zero
    print("Number 2 should not be zero")
else:
    print("Great job!")
finally:    # at the end
    print("JOB OVER... GO GET SOME REST")
```

<img width="1147" height="362" alt="image" src="https://github.com/user-attachments/assets/96556ebe-bb21-4c11-ab1f-2d80be6d4325" />

