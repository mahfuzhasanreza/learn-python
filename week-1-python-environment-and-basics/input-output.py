first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello, {first_name} {last_name}!")

age = int(input("Enter your age: "))
next_year_age = age + 1
print(f"Next year, you will be {next_year_age} years old.")

height = float(input("Enter your height in meters: "))
print(f"You are {height} meters tall.")

print(first_name, last_name, sep=' ', end='\n')