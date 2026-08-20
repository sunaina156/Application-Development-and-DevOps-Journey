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
