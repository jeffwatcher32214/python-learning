# Reopen students.txt in append mode.
# Add 2 more lines (e.g., new students or additional info).
def write_file():
    with open("students.txt", mode='w') as file:
        file.write("John,85\n")
        file.write("Emily,90\n")
        file.write("Olivia,78\n")
        file.write("William,82\n")
        file.write("Noah,79\n")

def read_file():
    total_marks = 0
    student_count = 0
    with open("students.txt", mode='r') as file:
        for line in file:
            line = line.strip()
            if line:
                name, marks = line.split(",")
                print(f"Student: {name} | Marks: {marks}")
                total_marks += int(marks)
                student_count += 1
    if student_count > 0:
        average = total_marks/student_count
        print(f"Total Students: {student_count}")
        print(f"Average Marks: {average}")
    else:
        print("No student record found!")


def main():
    write_file()
    read_file()

if __name__ == "__main__":
    main()