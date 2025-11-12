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