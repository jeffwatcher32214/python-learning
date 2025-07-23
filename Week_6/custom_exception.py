# Custom Exception:
# Define InvalidMarksError
# If marks > 100, raise this exception
# Handle the exception and show a friendly error message
class InvalidMarksError(Exception):
    def __init__(self, marks):
        super().__init__(f"Invalid marks: {marks}. Marks must be between 0 and 100.")

def register_student(name, marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError(marks)
    print(f"Student {name} registered successfully with {marks} marks.")
    return True

def main():
    success = False
    try:
        name = input("Enter student name: ")
        marks = float(input("Enter marks (0-100): "))
        success = register_student(name, marks)
    except InvalidMarksError as e:
        print(e)
    except ValueError:
        print("Error: Marks must be a number!")
    finally:
        if success:
            print("Student registration completed!")
        else:
            print("Student registration not completed!")

if __name__ == "__main__":
    main()
