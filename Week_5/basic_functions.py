# Define a function that greets the user by name.
def greeting(name):
    print(f"Welcome {name} to the Python world!")

# Define a function that takes two numbers and returns their sum.
def add(num1, num2):
    return num1 + num2

# Create a function to check if a number is even or odd.
def check_number(number):
    if number%2 == 0:
        print(f"{number} is Even!")
    else:
        print(f"{number} is Odd!")

def main():
    greeting("John")
    print(f"2 + 2 = {add(2,2)}")
    check_number(5)

if __name__ == "__main__":
    main()