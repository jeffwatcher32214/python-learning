# Create a function get_max(num1, num2) which returns the larger number.
number1 = 10
number2 = 20
def get_max(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

# Write a function that contains another function inside it. Example: Outer function asks for number; inner function squares it.
def outer_function():
    number = 10
    def inner_function():
        print(f"You have entered {number}")
    inner_function()

def main():
    print(f"The maximum number from {number1} and {number2} is {get_max(number1,number2)}")
    outer_function()

if __name__ == "__main__":
    main()