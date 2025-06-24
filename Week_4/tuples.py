# Create a tuple of 5 fruits.
fruits = ("apple", "banana", "orange", "kiwi", "mango")

# Try to change one element of the tuple and observe what happens.
# (Answer)If I try to change value it will show error


# Unpack a tuple into multiple variables.

def main():
    print(f"Tuple: {fruits}")
    first, second, third, forth, fifth = fruits
    print(f"{first} {second} {third} {forth} {fifth}")

if __name__ == "__main__":
    main()