# Use lambda to: Square a number.
square = lambda number: number * number

# Use lambda to: Check if a number is even.
is_even = lambda number: number%2 == 0

def main():
    number = 10
    print(f"Square of {number} is {is_even(number)}")
    print(f"Is {number} even? {is_even(number)}")

if __name__ == "__main__":
    main()