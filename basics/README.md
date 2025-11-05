# 🐍 Python Basics

## Variables and Data Types

Syntax:
```python
variable_name = value
```

Example:
```python
name = "Mahfuz"        # string
age = 22               # integer
height = 5.9           # float
is_student = True      # boolean
```

## Data Types
- String: Text data, e.g., `"Hello, World!"`
- Integer: Whole numbers, e.g., `42`
- Float: Decimal numbers, e.g., `3.14`
- Boolean: True or False values, e.g., `True`, `False`

```python
name = "Mahfuz"        # string
age = 22               # integer
height = 5.9           # float
is_student = True      # boolean

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student))# <class 'bool'>
```

## Operators

### Arithmetic Operators

Syntax:
```python
# Arithmetic Operators
+  # Addition
-  # Subtraction
*  # Multiplication
/  # Division
%  # Modulus
** # Exponentiation
// # Floor Division
```

Example:
```python
x = 10
y = 3

print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Modulus: {x % y}")
print(f"Exponentiation: {x ** y}")
print(f"Floor Division: {x // y}")  
```

### Comparison Operators

Syntax:
```python
# Comparison Operators
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater than or equal to
<=  # Less than or equal to
```

Example:
```python
a = 5
b = 10
print(f"Equal: {a == b}")
print(f"Not Equal: {a != b}")
print(f"Greater Than: {a > b}")
print(f"Less Than: {a < b}")
print(f"Greater Than or Equal To: {a >= b}")
print(f"Less Than or Equal To: {a <= b}")
```

### Identity Operators

Syntax:
```python
# Identity Operators
is      # Returns True if both variables are the same object
is not  # Returns True if both variables are not the same object
```

Example:
```python
x = ["apple", "banana"]
y = x
z = ["apple", "banana"]
print(f"x is y: {x is y}")        # True
print(f"x is z: {x is z}")        # False
print(f"x is not z: {x is not z}")# True
```

### Membership Operators

Syntax:
```python
# Membership Operators
in        # Returns True if a sequence contains a value
not in    # Returns True if a sequence does not contain a value
```

Example:
```python
fruits = ["apple", "banana", "cherry"]
print(f"apple in fruits: {'apple' in fruits}")        # True
print(f"grape not in fruits: {'grape' not in fruits}")# True
```

### Logical Operators

Syntax:
```python
# Logical Operators
and  # Returns True if both statements are true
or   # Returns True if one of the statements is true
not  # Reverse the result, returns False if the result is true
```

Example:
```python
a = 5
b = 10
c = 15
print(f"(a < b) and (b < c): {(a < b) and (b < c)}")  # True
print(f"(a > b) or (b < c): {(a > b) or (b < c)}")    # True
print(f"not(a < b): {not(a < b)}")                  # False
```

### Assignment Operators
Syntax:
```python
# Assignment Operators
=    # Assignment
+=   # Add and assign
-=   # Subtract and assign
*=   # Multiply and assign
/=   # Divide and assign
%=   # Modulus and assign
**=  # Exponentiation and assign
//=  # Floor division and assign
```

Example:
```python
x = 5
x += 3  # x = x + 3
print(f"x after += 3: {x}")
x -= 2  # x = x - 2
print(f"x after -= 2: {x}")
x *= 4  # x = x * 4
print(f"x after *= 4: {x}")
x /= 2  # x = x / 2
print(f"x after /= 2: {x}")
x %= 3  # x = x % 3
print(f"x after %= 3: {x}")
x **= 2 # x = x ** 2
print(f"x after **= 2: {x}")
x //= 2 # x = x // 2
print(f"x after //= 2: {x}")
```

### Bitwise Operators
Syntax:
```python
# Bitwise Operators
&   # AND
|   # OR
^   # XOR
~   # NOT
<<  # Left Shift
>>  # Right Shift
```

Example:
```python
a = 5      # 0101 in binary
b = 3      # 0011 in binary
print(f"a & b: {a & b}")   # 0001 => 1
print(f"a | b: {a | b}")   # 0111 => 7
print(f"a ^ b: {a ^ b}")   # 0110 => 6
print(f"~a: {~a}")         # 1010 => -6
print(f"a << 1: {a << 1}") # 1010 => 10
print(f"a >> 1: {a >> 1}") # 0010 => 2
```

## Conditional Statements

Syntax:
```python
if condition:
    # code to execute if condition is true
elif another_condition:
    # code to execute if another_condition is true
else:
    # code to execute if all conditions are false
```

Example:
```python
mark = 85

if mark >= 90:
    print("Grade: A")
elif mark >= 80:
    print("Grade: B")
elif mark >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

## Loops

### For Loop

Syntax:
```python
for item in iterable:
    # code to execute for each item
```

Example:
```python
for i in range(5):
    print(f"Iteration {i}")
```

### While Loop

Syntax:
```python
while condition:
    # code to execute while condition is true
```

Example:
```python
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
```

## Input and Output

### Input

Syntax:
```python
input("Prompt message")
```

Example:
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

Example: (**With data type conversion:**)
```python
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```

### Output

Syntax:
```python
print(value1, value2, ..., sep=' ', end='\n')
```

Example:
```python
print("Python", "is", "fun", sep="-")
```

## Calculator Example

```python
print("==== My Calculator ====")

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation
if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid input! Please choose between 1–4.")
```

## Number Guessing Game Example

```python
import random

print("=== Number Guessing Game ===")

# Computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

# Allow user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Check guess
if guess == secret_number:
    print("Correct! You guessed the number!")
else:
    print(f"Wrong guess! The correct number was {secret_number}.")
```

## Collections

### Lists

Syntax:
```python
name = [item1, item2, item3, ...]
```

Example:
```python
name = ["Mahfuz", "Hasan", "Reza"]

print(name)
print(type(name))
print(name[0])  # Accessing first element
print(name[-1])  # Accessing last element
print(name[1:3])  # Slicing
name.append("MHR")  # Adding an element
print(name)
name[1] = "Learn"  # Modifying an element
print(name)
name.remove("Reza")  # Removing an element
print(name)

print(len(name))  # Length of the list
print(sum([1, 2, 3, 4, 5]))  # Sum of numbers in a list
print(sorted([3, 1, 4, 2, 5]))  # Sorted list
print(max([3, 1, 4, 2, 5]))  # Maximum value
print(min([3, 1, 4, 2, 5]))  # Minimum value

number_list = [5, 2, 9, 1, 5, 6]
number_list.sort()  # Sorting the list in place
print(number_list)
```

### Tuples

Syntax:
```python
name = (item1, item2, item3, ...)
```

Example:
```python
coordinates = (10.0, 20.0)
print(coordinates)

# coordinates[0] = 15.0  # This will raise an error since tuples are immutable
```

### Dictionaries

Syntax:
```python
name = {key1: value1, key2: value2, ...}
```

Example:
```python
student = {
    "name": "Mahfuz",
    "age": 22,
    "courses": ["Math", "Science"]
}
print(student)
print(student["name"])  # Accessing value by key
student["age"] = 23  # Modifying value
student["grade"] = "A"  # Adding new key-value pair
print(student)
del student["courses"]  # Removing key-value pair
print(student)
print(student.keys())  # Getting all keys
print(student.values())  # Getting all values
print(student.items())  # Getting all key-value pairs
```

### Sets

Syntax:
```python
name = {item1, item2, item3, ...}
```

Example:
```python
names_set = {"Mahfuz", "Hasan", "Reza"}
print(names_set)

names_set.add("MHR")  # Adding an element
print(names_set)
names_set.remove("Hasan")  # Removing an element
print(names_set)
print("Mahfuz" in names_set)  # Membership test
print(len(names_set))  # Length of the set

another_set = {"Reza", "Khan", "Ali"}
print(names_set.union(another_set))  # Union
print(names_set.intersection(another_set))  # Intersection
print(names_set.difference(another_set))  # Difference
print(names_set.symmetric_difference(another_set))  # Symmetric Difference
```

### Frozen Sets

Syntax:
```python
name = frozenset([item1, item2, item3, ...])
```

Example:
```python
frozen_names = frozenset(["Mahfuz", "Hasan", "Reza"])
print(frozen_names)
# frozen_names.add("MHR")  # This will raise an error since frozensets are immutable

print("Mahfuz" in frozen_names)  # Membership test
print(len(frozen_names))  # Length of the frozenset
print(frozen_names.union(another_set))  # Union
print(frozen_names.intersection(another_set))  # intersection
print(frozen_names.difference(another_set))  # Difference
print(frozen_names.symmetric_difference(another_set))  # Symmetric Difference
```


<br>


### _Get Connected with [Learn With Mahfuz](https://www.youtube.com/@learn-with-mahfuz)_
  - _Subscribe to my channel on [YouTube](https://www.youtube.com/@learn-with-mahfuz)_
  - _Follow me on [LinkedIn](https://www.linkedin.com/company/learn-with-mahfuz)_
  - _Follow me on [Facebook](https://www.facebook.com/learnwithmahfuzofficial)_
  - _Connect with me on [LinkedIn](https://www.linkedin.com/in/mahfuzhasanreza/)_