# Write a function that reverses a string using recursion.
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print("Reversed: ", reverse_string("python"))

# Write a recursive function that calculates Fibonacci numbers.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")

# Write a function that accepts any number of keyword arguments and prints them.
def print_keyword_arguments(**kwargs):
    if not kwargs:
        print("No keyword arguments were passed.")
    else:
        print("Keyword Arguments Received:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

print_keyword_arguments(name="Alice", age=30, country="USA")

print_keyword_arguments(language="Python", level="Intermediate")

print_keyword_arguments()