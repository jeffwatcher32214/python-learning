# Write a simple recursive function to calculate factorial of a number.
def factorial(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial(n-1)

# Write a recursive function to calculate the sum of numbers from 1 to N.
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n-1)

def main():
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Sum of 1-10: {sum_to_n(10)}")

if __name__ == "__main__":
    main()