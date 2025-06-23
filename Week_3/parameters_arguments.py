# Create a function that accepts a name and age and prints: "Hello John, you are 25 years old."
def function1(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Create a function calculate_area(length, width) to calculate area of rectangle.
def area_of_rectangle(length, width):
    area = length * width
    print(f"Area of Rectangle: {area} meter square")

# Create a function welcome(name="Guest") which prints greeting. Try calling with and without providing name.
def welcome(name="Guest"):
    print(f"Hello {name}")

# Create a function order(item, quantity) and call it using both positional and keyword arguments.
def order(item = "Breads", quantity = 10):
    print(f"You have ordered {quantity} {item}")


def main():
    function1("John", 25)
    area_of_rectangle(10,10)
    welcome()
    welcome("John")
    order()
    order("Cucumber", 5)

if __name__ == "__main__":
    main()