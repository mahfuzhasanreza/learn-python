# 🐍 Week 2: Functions and Exception Handling

## Functions

Syntax:
```python
def function_name(parameters):
    """Docstring explaining the function."""
    # Function body
    return value

def function_name(parameters) -> return_type:
    """Docstring explaining the function."""
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


<br>


### _Get Connected with [Learn With Mahfuz](https://www.youtube.com/@learn-with-mahfuz)_
  - _Subscribe to my channel on [YouTube](https://www.youtube.com/@learn-with-mahfuz)_
  - _Follow me on [LinkedIn](https://www.linkedin.com/company/learn-with-mahfuz)_
  - _Follow me on [Facebook](https://www.facebook.com/learnwithmahfuzofficial)_
  - _Connect with me on [LinkedIn](https://www.linkedin.com/in/mahfuzhasanreza/)_