# Define a simple function greet_user() that prints a greetin
def greet_user():
    print("Hello and Welcome to python World!")


# Create a function square_number(num) that returns square of a number.
number = 10
def square_number(number):
    return number * number

# Write a function sum_of_list(lst) that takes a list of numbers and returns their sum.
lst = [1, 2, 3, 4, 5]
def sum_of_lists(lst):
    sum = int(0)
    for i in lst:
        sum += int(i)
    return sum

# Write a function that takes two arguments and returns their product.
num1 = 4
num2 = 5
def product_of_two_numbers(num1, num2):
    return num1 * num2

# Write a function is_even(num) that returns True if number is even, False otherwise.
num = 10
def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False


def main():
    greet_user()
    print(f"Square of {number} is {square_number(number)}")
    print(f"Sum of {lst} is {sum_of_lists(lst)}")
    print(f"Product of {num1} and {num2} is {product_of_two_numbers(num1, num2)}")
    print (f"Is {num} Even? {is_even(num)}")


if __name__ == "__main__":
    main()