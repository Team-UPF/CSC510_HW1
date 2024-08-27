def greet(name):
    print("Hello, " + name)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

greet("World")

result_add = add_numbers(5, 10)
print("The sum is:", result_add)

result_subtract = subtract_numbers(10, 5)
print("The difference is:", result_subtract)

# Intentional error: undefined variable
print("This will cause an error: " + undefined_variable)