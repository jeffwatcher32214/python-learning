# Create a function that takes:
#   Positional arguments (e.g. name, age)
#   Keyword arguments (e.g. name="John", age=30)
def person(name="John", age=30):
    print(f"You are {name} and your age is {age}")

# Create a function with default argument values.
def default_person(name, age=30):
    print(f"You are {name} and your age is {age}")

# Create a function that accepts a variable number of arguments using:
#   *args (multiple positional arguments)
def add_all(*args):
    total = 0
    for num in args:
        total += num
    print(f"The sum is: {total}")

#   **kwargs (multiple keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():
    person("James", 25)
    default_person("Tamara")
    add_all(5, 10, 15, 20)
    print_info(name="John", age=30, country="USA")

if __name__ == "__main__":
    main()