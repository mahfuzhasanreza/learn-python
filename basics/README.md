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
