# Functions

A function is a block of code that performs a specific task. You can use it 
whenever you want by calling its name, which saves you from writing the same code multiple times.
<br>
Benefits of Using Functions:
- Increase code Readability & Reusability

**Basic Concepts:**
- **Create** function: Use the def keyword to define a function.
- **Call** function: Use the function's name followed by () to run it.
- **Parameter**: The variable listed inside parentheses in function definition.
- **Argument**: The actual value you pass to function when you call it.


--- 
## Types of Functions:
Below are the two types of functions in Python:

1. Built-in library function:
- These are Standard functions in Python that are available to us.
- Ex: print(), input(), type(), sum(), max(), etc
2. User-defined function:
- We can create our own functions based on our requirements.
- Ex: create your own function :)

<img width="1165" height="594" alt="image" src="https://github.com/user-attachments/assets/cb253fda-dc80-4820-a17b-7d69a8840c55" />

# **return result** is optional, Use if you want the function to give back a value

---

## Function without Parameters

Ex 1:
```python
# Create or Define Function
def greetings():
  print("Welcome to Python tutorial by Rishabh")

# Use or call this Function
greetings()

# output: Welcome to Python tutorial by Rishabh
```

Ex 2:

```python
# function to add two numbers & print result:
def add2numbers(a, b):
  result = a + b       #parameter (a, b)
  print("The sum is:", result)

# Calling this function with arguments
add2numbers(5, 3)       # arguments (5, 3)

# Output: The sum is: 8

add2numbers(a=10, b=100)
add2numbers(b=100, a=10)
```

```python
def add3numbers(a, b, c):
    result = a + b + c
    print("The sum is: ", result)

add3numbers(5, 3, 100)
```

---

## The return Statement
The return statement is used in a function to send a result back to the place where the function was called. <br>
When return is executed, the function **stops running** and immediately returns the specified value.  <br>

Ex:
```python
def add(a, b):
  return a + b   # This line sends back sum of a and b
result = add(3, 5)
print(result)                  # Output: 8
```
<br>
<br>

```python
# function with return statement
def add2num(a, b):
    return a + b
    # return a-b   after return statement ends

sum2num = add2num(10, 1)
print(sum2num)
```

<br>
<br>

```python
Ex: 3
# Function with a Return value

# function to conver Celsius to Fahrenheit:
def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Calling this function to return a value
temp_f = celsius_to_fahrenheit(25)
print("Temperature in Fahrenheit:", temp_f)
# Output: Temperature in Fahrenheit: 77

print("without return: ", type(temp_f)) 

```

<br>
<br>

```python

# Function without a Return value

# function to conver Celsius to Fahrenheit without return statement:
def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  print(fahrenheit)

# Calling this function to return a value
temp_f2 = celsius_to_fahrenheit(50)

print("without return: ", type(temp_f2)) 
```

---

## The pass Statement

The pass statement is a placeholder in a function or loop. <br>
It does nothing and is used when you need to write code that will be added latr or to define an empty function.
<br>
Ex: 

```python
def myfunction():
  pass    # This does nothing for now
```

---
---
---

# Function Arguments

## Arguments in Functions

Arguments are the values that are passed into a function when it's called. <br>
A function must be called with the right number of arguments.  <br>
If a function has 2 parameters, you must provide 2 arguments when calling it.     <br>

Ex:  <br>
function defined using one parameter (variable)

```python
def greetings(name):    # name is a parameter
  print("Hello, " + name + "!")

greetings("Madhav")    # Madhav as argument
# Output: Hello, Madhav!
```

---

## Types of Function Arguments

Python supports various types of arguments that can be passed at the time of the function call.

- Required arguments (Single/Multiple arguments)
- Default argument
- Keyword arguments (named arguments)
- Arbitrary arguments (variable-length arguments *args and **kwargs)

```python
# 1. Required Arguments (single/multiple arguments)

def greetings(name):                  # name is parameter
    print("Hello ", name, "!")

greetings("Madhav")    # Madhav is argument
# greetings()                  # required an argument to run code

#----

def intro(course_name, instructor_name):
    print("Welcome to ", course_name, "course by ", instructor_name)

intro("Python", "Rishabh")
```

<br>
<br>

### Default Arguments
You can assign default values to arguments in a function definition.  <br>
If a value isn't provided when the function is called, the default value is used.  <br>

Ex:   <br>
function defined using one parameter & default value

def greetings(name = "World"):               # default value   <br>
  print("Hello, " + name + "!")    <br>

greetings()      # No argument passed   <br> 
#Output: Hello, World!   <br>
<br>
greetings("Madhav")                        # Madhav as argument  <br>
#Output: Hello, Madhav!


```python
# 2. Default Arguments

def greetings(name = "World"):         # "World" is a default value    
    print("Hello ", name, "!")

greetings()      # runs without error using default value
greetings("Rishabh")
```

<br>
<br>

### Keyword Arguments (Named Arguments)

When calling a function, you can specify arguments by the parameter name.   <br>
These are called keyword arguments and can be given in any order. <br>

Ex: function defined using two parameters  <br>

```python
def divide(a, b):      # a, b are 2 parameters
    return a / b

result = divide(b=10, a=20)     # with keyword argument
print(result)     # Output: 2

result = divide(10, 20)    # positional argument
print(result)     # Output: 0.5
```

### Arbitrary Arguments

#### Arbitrary Positional Arguments (*args)

If you're unsure how many arguments will be passed, use *args to accept any number of positional arguments.  <br>
**Purpose:** Allow you to pass a variable number of positional arguments.    <br>
**Type:** The arguments are stored as a tuple.   <br>
**Usage:** Use when you want to pass multiple values that are accessed by position.    <br> 

Ex.1:   <br>

```python
def add_numbers(*args):
    return sum(args)

# ANy number of arguments
result = add_numbers(1, 2, 3, 4)
print(result)
```

**Note:** Here, *args collects all the passed arguments into a tuple, & sum() function adds them.










































