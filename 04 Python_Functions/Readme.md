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
```




































