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