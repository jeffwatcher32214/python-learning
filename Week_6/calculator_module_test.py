# calculator_module_test.py
import calculator_module

def main():
    print("Welcome to the Simple Calculator Module!")
    print("Options: add | subtract | multiply | divide")
    
    choice = input("Enter operation: ").strip().lower()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        match choice:
            case "add":
                result = calculator_module.add(num1, num2)
            case "subtract":
                result = calculator_module.subtract(num1, num2)
            case "multiply":
                result = calculator_module.multiply(num1, num2)
            case "divide":
                result = calculator_module.divide(num1, num2)
            case _:
                print("Invalid operation.")

        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()
