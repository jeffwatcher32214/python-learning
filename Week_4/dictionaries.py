# Create a dictionary of 5 students with names as keys and marks as values.
# Add a new student.
# Update marks of a student.
# Delete one student.
# Loop through dictionary to display all students and marks.

def main():
    my_dict = {"John": 78, "Alice": 82, "Bob": 92, "Nolan": 70, "Eva": 89}
    print(f"Dictionary: {my_dict}")
    my_dict.update({"James": 95})
    print(f"New Student: {my_dict}")
    my_dict["James"] = 98
    print(f"Update James Marks: {my_dict}")
    my_dict.pop("James")
    print(f"Student Deleted: {my_dict}")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()