# Add, subtract, multiply and divide two numbers
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print(f"Num1 + Num2 = {add}")
print(f"Num1 - Num2 = {sub}")
print(f"Num1 * Num2 = {mul}")
print(f"Num1 / Num2 = {div}")

#Calculate area and circumference of: Circle (use 3.14)
pi = 3.14
circle_radius = 10
circle_area = pi*circle_radius*circle_radius
circle_circumference = 2*pi*circle_radius
print(f"Area of Circle: {circle_area} meter square")
print(f"Circumference of Circle: {circle_circumference} meters")

# Calculate area and perimeter of: Rectangle
rectangle_length = 10
rectangle_width = 10
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2*(rectangle_length+ rectangle_width)
print(f"Area of Rectangle: {rectangle_area} meter square")
print(f"Perimeter of Rectangle: {rectangle_perimeter} meters")

# Calculate area and perimeter of: Triangle
triangle_height = 10
triangle_base = 10
triangle_side1 = 10
triangle_side2 = 10
triangle_area = (triangle_height * triangle_base) / 2
triangle_perimeter = triangle_base + triangle_side1 + triangle_side2
print(f"Area of Triangle: {triangle_area} meter square")
print(f"Perimeter of Triangle: {triangle_perimeter} meters")

# Convert: Celsius to Fahrenheit
celsius = 100
fahrenheit = ((celsius) * (9/5)) + 32
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

# Convert: KM to Miles
kilometers = 100
miles = kilometers / 1.609
print(f"{kilometers} kilometers = {miles} miles")