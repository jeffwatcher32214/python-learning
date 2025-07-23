FILENAME = "students_data.txt"

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    with open(FILENAME, "a") as f:
        f.write(f"{name},{marks}\n")
    print("Student added successfully.")

def delete_student():
    name = input("Enter student name to delete: ")
    lines = []
    found = False
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    with open(FILENAME, "w") as f:
        for line in lines:
            if not line.startswith(name + ","):
                f.write(line)
            else:
                found = True
    if found:
        print(f"🗑️ Student {name} deleted.")
    else:
        print("Student not found.")

def update_student():
    name = input("Enter student name to update: ")
    new_marks = input("Enter new marks: ")
    lines = []
    updated = False
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    with open(FILENAME, "w") as f:
        for line in lines:
            if line.startswith(name + ","):
                f.write(f"{name},{new_marks}\n")
                updated = True
            else:
                f.write(line)
    if updated:
        print("Student updated successfully.")
    else:
        print("Student not found.")

def view_students():
    try:
        with open(FILENAME, "r") as f:
            print("\n Student Records:")
            for line in f:
                name, marks = line.strip().split(",")
                print(f"Student: {name} | Marks: {marks}")
    except FileNotFoundError:
        print("No student file found. Please add students first.")

def main():
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Marks")
        print("4. View All Students")
        print("5. Exit")
        choice = input("Select an option (1–5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
