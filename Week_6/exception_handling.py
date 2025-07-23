# Write a division program
# Take two user inputs
# Catch ZeroDivisionError
# Catch invalid input (ValueError)
# Use a finally block to print "Program finished."
def main():
    try:
        number1 = int(input("Numerator: "))
        number2 = int(input("Denominator: "))
        result = number1 / number2
    except ZeroDivisionError:
        print("Denominator should never be Zero!")
    except ValueError:
        print("You must enter both integers")
    else:
        print(f"{number1}/{number2} = {result}")
    finally:
        print("Program Finished!")

if __name__ == "__main__":
    main()