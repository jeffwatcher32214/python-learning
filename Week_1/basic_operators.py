#Basic Operators Programs
pi = 3.14
circle_radius = 10
circle_area = pi*circle_radius*circle_radius
circle_circumference = 2*pi*circle_radius
print(f"Area of Circle: {circle_area} meter square")
print(f"Circumference of Circle: {circle_circumference} meters")

rectangle_length = 10
rectangle_width = 10
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2*(rectangle_length+ rectangle_width)
print(f"Area of Rectangle: {rectangle_area} meter square")
print(f"Perimeter of Rectangle: {rectangle_perimeter} meters")

triangle_height = 10
triangle_base = 10
triangle_side1 = 10
triangle_side2 = 10
triangle_area = (triangle_height * triangle_base) / 2
triangle_perimeter = triangle_base + triangle_side1 + triangle_side2
print(f"Area of Triangle: {triangle_area} meter square")
print(f"Perimeter of Triangle: {triangle_perimeter} meters")

celsius = 100
fahrenheit = ((celsius) * (9/5)) + 32
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

kilometers = 100
miles = kilometers / 1.609
print(f"{kilometers} kilometers = {miles} miles")