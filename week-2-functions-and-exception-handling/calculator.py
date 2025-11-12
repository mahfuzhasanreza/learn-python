from utils import power
import sys

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "pow": power
}

def parse_number(s):
    try:
        return float(s)
    except ValueError as e:
        raise ValueError("Please enter a valid number.") from e

def main():
    print("Simple CLI Calculator. Type 'help' for commands, 'quit' to exit.")
    while True:
        try:
            line = input(">> ").strip()
            if not line:
                continue
            if line.lower() in ("quit", "exit"):
                print("Bye!")
                break
            if line.lower() == "help":
                print("Usage: <operation> <num1> <num2>")
                print("Operations: " + ", ".join(OPERATIONS.keys()))
                continue

            parts = line.split()
            op = parts[0].lower()
            if op not in OPERATIONS:
                print(f"Unknown operation '{op}'. Type 'help'.")
                continue
            if len(parts) < 3:
                print("Please provide two numbers. Example: add 3 4")
                continue

            a = parse_number(parts[1])
            b = parse_number(parts[2])
            result = OPERATIONS[op](a, b)
        except ZeroDivisionError as zde:
            print("Error:", zde)
        except ValueError as ve:
            print("Error:", ve)
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            sys.exit(0)
        except Exception as e:
            print("Unexpected error:", e)
        else:
            print("Result:", result)
        finally:
            pass

if __name__ == "__main__":
    main()
