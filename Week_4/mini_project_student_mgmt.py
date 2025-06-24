# Build a simple program where:
# User can:
# Add student (name + marks)
# Delete student
# Update student marks
# View all students
# Use dictionary to store data.
# Run the system in a loop until user exits.t

def main():
    students = {
        "James": 85,
        "Emily": 92,
        "Michael": 78,
        "Olivia": 88,
        "William": 95,
        "Sophia": 81,
        "David": 90,
        "Isabella": 87,
        "John": 79,
        "Mia": 93
    }
    while True:
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. View all Students")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                name = input("Enter Student Name: ")
                marks = int(input("Enter Student Marks: "))
                students.update({name: marks})
                print("Student added successfully!")
            case 2:
                name = input("Enter Name to delete: ")
                students.pop(name)
                print(f"Student {name} deleted successfully!")
            case 3:
                name = input("Enter Student Name to Update: ")
                marks = int(input("Enter new Marks: "))
                students[name] = marks
                print("Student added successfully!")
            case 4:
                for key, value in students.items():
                    print(f"{key}: {value}")
            case 5:
                print("Exiting... Goodbye!")
                exit()

if __name__ == "__main__":
    main()