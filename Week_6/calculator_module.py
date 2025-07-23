# Create calculator_module.py
# Functions: add(), subtract(), multiply(), divide()
# Create calculator_module_test.py
# Import the module
# Take user input and perform the operation

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiple(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot Divide with 0!")
    return num1 / num2