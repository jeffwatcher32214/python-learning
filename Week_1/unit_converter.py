# Mini Project Week 1 Unit Converter Program.
# Create a script unit_converter.py: Ask the user: Type of conversion: temperature, distance, time. Input value. Output the converted result.
print("Choose Conversion: \n1) Temperature \n2) Distance \n3) Time")
choice = int(input("Enter type (1-3): "))
match choice:
    case 1:
        celsius = float(input("Enter Temperature in Celsius: "))
        fahrenheit = ((celsius) * (9/5)) + 32
        print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")
    case 2:
        kilometers = float(input("Enter Distance in Kilometers: "))
        miles = kilometers / 1.609
        print(f"{kilometers} kilometers = {miles} miles")
    case 3:
        minutes = int(input("Enter Time in minutes: "))
        seconds = minutes * 60
        print(f"{minutes} minutes = {seconds} seconds")
    case _:
        print("Invalid Input!")