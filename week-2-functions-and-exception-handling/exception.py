def divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
        return None
    else:
        return result
    finally:
        print("Execution completed.")

print(divide(10, 2))
print(divide(10, 0))