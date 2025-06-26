# Write a lambda function to square a number.
square = lambda number: number * number

# Write a lambda function to check if a number is even.
is_even = lambda number: number%2 == 0

# Use map() and lambda to square all elements in a list.
my_list = [1, 2, 3, 4, 5]

# Use filter() and lambda to filter only even numbers from a list.


def main():
    number = 10
    print(f"Square of {number} is {is_even(number)}")
    print(f"Is {number} even? {is_even(number)}")
    print(f"Square of list: {list(map(lambda n: n * 2, my_list))}")

if __name__ == "__main__":
    main()