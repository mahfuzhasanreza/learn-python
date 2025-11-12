# 🐍 Week 2: Functions and Exception Handling

## Functions

Syntax:
```python
def function_name(parameters):
    # Function body
    return value

def function_name(parameters) -> return_type:
    # Function body
    return value
```

Example:
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: float, b: float) -> float:
    return a + b

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    print(greet("Mahfuz"))
    print("3 + 4 =", add(3, 4))
    print("5! =", factorial(5))
```

## Function Arguments, default Values, *args, and **kwargs

Syntax:
```python
def function_name(param1: type1, param2: type2 = default_value) -> return_type:
    # Function body
    return value
```

Example:
```python
def robot_greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

print(robot_greet("Mahfuz"))            # Uses default greeting
print(robot_greet("Hasan", "Hi there"))  # Custom greeting

# *args and **kwargs
def func_with_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

    args_sum = sum(args)
    print("Sum of positional arguments:", args_sum)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

func_with_args(1, 2, 3, name="Mahfuz", age=25)
```

## Local vs Global Scope

Syntax:
```python
global_var = "global variable"
def my_function():
    local_var = "local variable"
```

Example:
```python
global_var = "global variable"

def my_function():
    local_var = "local variable"
    print(local_var)
    print(global_var)

my_function()
print(global_var)
# print(local_var)  # Error

# Changing global and local variables as same name
var = "global"
def change_var():
    var = "local"
    print("Inside function:", var)

def print_global_var():
    print("Inside function (global):", var)

change_var()
print_global_var()
print("Outside function:", var)
```

<br>

### _Get Connected with [Learn With Mahfuz](https://www.youtube.com/@learn-with-mahfuz)_
  - _Subscribe to my channel on [YouTube](https://www.youtube.com/@learn-with-mahfuz)_
  - _Follow me on [LinkedIn](https://www.linkedin.com/company/learn-with-mahfuz)_
  - _Follow me on [Facebook](https://www.facebook.com/learnwithmahfuzofficial)_
  - _Connect with me on [LinkedIn](https://www.linkedin.com/in/mahfuzhasanreza/)_