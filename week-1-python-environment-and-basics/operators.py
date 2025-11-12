x = 10
y = 3

# Arithmetic Operators
print("Arithmetic Operators:")
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Modulus: {x % y}")
print(f"Exponentiation: {x ** y}")
print(f"Floor Division: {x // y}")

# Comparison Operators
print()
print("Comparison Operators:")
print(f"Equal: {x == y}")
print(f"Not Equal: {x != y}")
print(f"Greater Than: {x > y}")
print(f"Less Than: {x < y}")
print(f"Greater Than or Equal To: {x >= y}")
print(f"Less Than or Equal To: {x <= y}")

# Identity Operators
print()
print(f"x is y: {x is y}")
print(f"x is not y: {x is not y}")

# Membership Operators
print(f"x in [10, 20, 30]: {x in [10, 20, 30]}")
print(f"x not in [10, 20, 30]: {x not in [10, 20, 30]}")

# Logical Operators
print()
print("Logical Operators:")
a = True
b = False
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")

# Assignment Operators
print()
print("Assignment Operators:")
z = 5
print(f"Initial z: {z}")
z += 2
print(f"After z += 2: {z}")
z -= 1
print(f"After z -= 1: {z}")
z *= 3
print(f"After z *= 3: {z}")
z /= 2
print(f"After z /= 2: {z}")
z %= 4
print(f"After z %= 4: {z}")
z **= 2
print(f"After z **= 2: {z}")
z //= 3
print(f"After z //= 3: {z}")

# Bitwise Operators
print()
print("Bitwise Operators:")
m = 6  # 110 in binary
n = 3  # 011 in binary
print(f"m & n: {m & n}")   # AND
print(f"m | n: {m | n}")   # OR
print(f"m ^ n: {m ^ n}")   # XOR
print(f"~m: {~m}")         # NOT
print(f"m << 1: {m << 1}") # Left Shift
print(f"m >> 1: {m >> 1}") # Right Shift