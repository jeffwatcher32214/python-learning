# Write a function that contains another function inside it.
# The inner function should process data received by the outer function.
# Example idea:
# Outer function receives a list of numbers, inner function returns the sum.
def outer_function(my_list):
    number = 10
    def inner_function(my_list):
        sum = 0
        for x in my_list:
            sum += x
        return sum
    print(f"Sum: {inner_function(my_list)}")

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    outer_function(numbers)

if __name__ == "__main__":
    main()