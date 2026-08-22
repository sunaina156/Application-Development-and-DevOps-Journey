## Topics Covered

- OOPs
  - Class
  - Object
  - Attributes
  - Methods
- Features of OOPs
  - Abstraction
  - Encapsulation
  - Inheritance
  - Polymorphism

    
---

# OOPs in Python

Two ways of programming in Python:  <br>
1. Procedural Programming
2. OOPs

**OOPs**  <br>
Object Oriented Programming  <br>
A way of organizing code by creating "blueprints" (called classes) to represent real-world things like a student, car, or house. <br>
These blueprints help you create objects  (individual examples of those things) and define their behaviour. <br>
<br>

**Class** <br>
A class is a blueprint or template for creating objects. <br>
It defines the properties (attributes) & actions/behaviours (methods) type will have. <br>
<br>

**Object**<br>
An object is a specific instance of a class.<br>
It has actual data based on the blueprint defined by the class. <br>

<br>
<br>

Class  <br>
(cast/mold)  <br>
  <br>
Attributes  <br>
(car properties: color)  <br>
  <br>
Methods  <br>
(car features: door open)  <br>
  <br>
Object  <br>
(car: product)  <br>


---

Without OOPs

```python
# OOPs in Python
# OOP - Object Oriented Programming

# student details
student_1 = ['Madhav', 10]    # Name, Grade
student_2 = ['Vishakha', 12]
student_3 = 'Keshav'

student_1.append('A')
print(student_1)

print(f'{student_1[0]} is in class {student_1[1]}')
print(f'{student_2[0]} is in class {student_2[1]}')
```

<br>

**Why OOPs?**
- Models Real-World Problems:   <br>
&nbsp;&nbsp; Mimics real-world entities for easier understanding. <br>
- Code Reusability:  <br>
&nbsp;&nbsp; Encourages reusable, modular, and organized code.
- Easier Maintenance:  <br>
&nbsp;&nbsp; OOP organizes code into small, manageable parts (classes and objects). Changes in one part don't impact others, making it easier to maintain. <br>
- Encapsulation:  <br>
&nbsp;&nbsp; Encapsulation protects data integrity and privacy by bundling data and methods. <br>
- Flexibility:  <br>
&nbsp;&nbsp; OOP makes it easier to add new features without affecting existing code. <br>

<br>

```python
# Using OOPs - Creating student records

# class - blueprint or template
# __init__ method - constructor value initialize  - this is fix
# self parameter - reference or connection build btw class and object - it is also fix
class Student:     # student class
    def __init__(self, name, grade): # method   
        self.name = name     # attribute
        self.grade = grade   # attribute

    def student_details(self):      # method
        print(f"{self.name} is in class {self.grade}")

# object - instance of class
student1 = Student('Madhav', 11)
# print(student1.name, student1.grade)

student2 = Student('Vishakha', 12)
# print(student2.name, student2.grade)


student1.student_details()
student2.student_details()
```

```python
# Using OOPs - Creating student records

# class - blueprint or template
# __init__ method - constructor value initialize  - this is fix
# self parameter - reference or connection build btw class and object - it is also fix
class Student:     # student class
    def __init__(self, name,grade, percentage): # method   
        self.name = name     # attribute
        self.grade = grade   # attribute
        self.percentage = percentage


    def student_details(self):      # method
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")

# object - instance of class
student1 = Student('Madhav', 11, 96)
# print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99)
# print(student2.name, student2.grade)


student1.student_details()
student2.student_details()

print(student1.__dict__)

```

```python
# Using OOPs - Creating student records

# class - blueprint or template
# __init__ method - constructor value initialize  - this is fix
# self parameter - reference or connection build btw class and object - it is also fix
class Student:     # student class
    def __init__(self, name,grade, percentage): # method   
        self.name = name     # attribute
        self.grade = grade   # attribute
        self.percentage = percentage


    def student_details(self):      # method
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")

# object - instance of class
student1 = Student('Madhav', 11, 96)
# print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99)
# print(student2.name, student2.grade)


# student1.student_details()
# student2.student_details()

# print(student1.__dict__)

#--------

# modify object property

print(student1.percentage)
student1.percentage = 98   # modify
print(student1.percentage)

#-------------

# delete object property
print(student1.__dict__)
del student1.percentage
print(student1.__dict__)

#---------------

# delete object
del student1
print(student1)
```

```python
# Using OOPs - Creating student records

# class - blueprint or template
# __init__ method - constructor value initialize  - this is fix
# self parameter - reference or connection build btw class and object - it is also fix
class Student:     # student class
    def __init__(self, name, grade, percentage, team): # method   
        self.name = name     # attribute
        self.grade = grade   # attribute
        self.percentage = percentage
        self.team = team


    def student_details(self):      # method
        print(f"{self.name} is in class {self.grade} with {self.percentage}%, is in team {self.team}")

team1 = 'A'
team2 = 'B'

# object - instance of class
student1 = Student('Madhav', 11, 96, team1)
# print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99, team2)
# print(student2.name, student2.grade)

# print(student1.team)
# print(student2.team)

student1.student_details()
student2.student_details()
```

---

## Features of OOPs

1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism
   <br>

### Abstraction

Hiding unnecessary details from users through class, methods <br>

```python
# Using OOPs - Creating student records

# class - blueprint or template
# __init__ method - constructor value initialize  - this is fix
# self parameter - reference or connection build btw class and object - it is also fix
class Student:     # student class
    def __init__(self, name, grade, percentage): # method   
        self.name = name     # attribute
        self.grade = grade   # attribute
        self.percentage = percentage

    def student_details(self):      # method - abstraction
        print(f"{self.name} is in class {self.grade} with {self.percentage+2}%")         # hidden from users

# object - instance of class
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)

student1.student_details()
student2.student_details()
```

### Encapsulation

Restrict access to certain attributes or methods to protect data and enforce controlled access. <br>

```python
# Using OOPs - Creating student records

# class - blueprint or template
# __init__ method - constructor value initialize  - this is fix
# self parameter - reference or connection build btw class and object - it is also fix
class Student:     # student class
    def __init__(self, name, grade, percentage): # method   
        self.name = name     # attribute
        self.grade = grade   # attribute
        self.__percentage = percentage    # double unscore limits access

    def get_percentage(self):
        return self.__percentage

    def student_details(self):      # method 
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")     

# object - instance of class
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)

# print(student1.__percentage)   #error without method to access this private
# print(student1.percentage)     #error

print(student1.get_percentage())
print(student2.get_percentage())
```

### Inheritance

Allows one class (child) to reuse the properties and methods of another class (parent). <br>

```python
# Using OOPs - Creating student records

# Parent class
# class - blueprint or template
# __init__ method - constructor value initialize  - this is fix
# self parameter - reference or connection build btw class and object - it is also fix
class Student:     # student class
    def __init__(self, name, grade, percentage): # method   
        self.name = name     # attribute
        self.grade = grade   # attribute
        self.percentage = percentage

    def student_details(self):      # method 
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")        

# object - instance of class
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)


# child class
class GraduateStudent(Student):   # Graduatestudent child class inherit properties and methods from Student Parent class
    def __init__(self, name, grade, percentage, stream):     # old parameters from parent class and new parameters in child class
        super().__init__(name, grade, percentage)    # call parent class initializer

        self.stream = stream   # new attribute in child class

    def student_details(self):
        super().student_details() # method inheritance from parent class
        print(f'Stream is {self.stream}')
 
# object
Grad_Student1 = GraduateStudent('Keshav', 12, 96, 'PCM')
print(Grad_Student1.stream)
print(student1.percentage)

Grad_Student1.student_details()
```

### Polymorphism

Allows methods in different classes to have same name but different behaviour depending on objects. <br>

```python
# Using OOPs - Creating student records

# Parent class
# class - blueprint or template
# __init__ method - constructor value initialize  - this is fix
# self parameter - reference or connection build btw class and object - it is also fix
class Student:     # student class
    def __init__(self, name, grade, percentage): # method   
        self.name = name     # attribute
        self.grade = grade   # attribute
        self.percentage = percentage

    def student_details(self):      # method 
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")        

# object - instance of class
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)


# child class
class GraduateStudent(Student):  
    def __init__(self, name, grade, percentage, stream):   
        super().__init__(name, grade, percentage)   

        self.stream = stream  

    def student_details(self):   # method
        # print(f'{self.name} is in class {self.grade}, with {self.percentage}% and from stream {self.stream}')
        print('same method with different output')
        
# object - Student class
student1 = Student('Madhav', 11, 96)

# object - GraduateStudent class
Grad_Student1 = GraduateStudent('Keshav', 12, 96, 'PCM')

student1.student_details()
Grad_Student1.student_details()
```
