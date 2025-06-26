# Build a simple menu-driven calculator where:
# User chooses operation: add, subtract, multiply, divide.
# You create separate functions for each operation.
# Use lambda functions where applicable.
# Handle invalid user input gracefull
add = lambda number1, number2: number1 + number2
sub = lambda number1, number2: number1 - number2
mul = lambda number1, number2: number1 * number2
div = lambda number1, number2: number1 / number2

def main():
    while True:
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = int(input("Your Choice: "))
        match choice:
            case 1:
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
                print(f"Result: {number1} + {number2} = {add(number1, number2)}")
            case 2:
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
                print(f"Result: {number1} - {number2} = {sub(number1, number2)}")
            case 3:
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
                print(f"Result: {number1} * {number2} = {mul(number1, number2)}")
            case 4:
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
                if number2 !=0:
                    print(f"Result: {number1} / {number2} = {div(number1, number2)}")
                else:
                    print("Cannot divide by zero!")
            case 5:
                print("Exiting the calculator. Goodbye!")
                exit()
            case _:
                print("Invalid Operation!")
        print('-' * 30)

if __name__ == "__main__":
    main()