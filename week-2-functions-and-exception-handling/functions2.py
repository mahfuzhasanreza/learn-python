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