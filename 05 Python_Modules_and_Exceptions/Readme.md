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
  __init__.py   <br>
  math_utils.py   <br>
  string_utils.py   <br>

**#Use the package:**   <br>
Syntax: **from** my_package **import** <package_name>
Example: **from** my_package **import** math__utils, string_utils

---

