# Mini Project: Simple Calculator: Build a console program where user can:
# Select operation (add, subtract, multiply, divide)
# Enter two numbers.
# Perform operation using functions.
# Show result.
# Keep running in loop until user exits.

def add(number1, number2):
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")

def subtract(number1, number2):
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")

def multiply(number1, number2):
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")

def divide(number1, number2):
    result = number1 / number2
    print(f"{number1} / {number2} = {result}")

def main():
    switch = True
    while switch == True:
        number1 = float(input("Num1: "))
        number2 = float(input("Num2: "))
        print("Enter + to Add")
        print("Enter - to Subtract")
        print("Enter * to Multiply")
        print("Enter / to Divide")
        choice = input("Your Choice: ")
        match choice:
            case '+':
                add(number1, number2)
            case '-':
                subtract(number1, number2)
            case '*':
                multiply(number1, number2)
            case '/':
                divide(number1, number2)
            case _:
                print("Invalid Operation!")
        control = input("Do you want to Exit: Enter Y or N: ")
        print(control)
        if(control == 'Y' or control == 'y'):
            switch = False

if __name__ == "__main__":
    main()